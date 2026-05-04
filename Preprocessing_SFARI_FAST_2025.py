# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:57:38 2024

@author: theov
@modified: mdarrell
@modified: cbrittenha
"""

#============================================
#               FAST experiment
#============================================

#loading needed toolboxes 
import mne
import numpy as np
import copy
import tkinter as tk
import pandas as pd
from tkinter import filedialog
import logging
import os
from matplotlib import pyplot as plt

#%% Reading BDF files 

Subjects = os.listdir('Z://Data_new/SFARI_DATA_2024/F.A.S.T._Response_task')

#%% load files

Subject = Subjects[133] # To do # S = 1:43 TD group; S = 44:106 ASD group; S = 107:133 SIB group
file_path = 'Z://Data_new/SFARI_DATA_2024/F.A.S.T._Response_task/' + Subject
subject_path = f'Z://Data_new/SFARI_DATA_2024/F.A.S.T._Response_task/{Subject}'

# List all files in the directory for the specific subject
EEG_files = os.listdir(subject_path)

# Filter out only the .bdf files
bdf_files = [file for file in EEG_files if file.endswith('.bdf') and 'fast' in file]
# bdf_files = [file for file in EEG_files if file.endswith('.bdf')]
ET_files = [file for file in EEG_files if file.endswith('.asc')]

import re

# Function to extract the numeric part of the block
def extract_block_number(filename):
    match = re.search(r'_(\d+)\.asc$', filename)
    return int(match.group(1)) if match else float('inf')  # Return inf for non-matching filenames

# Sort the list by the extracted block number
ET_files = sorted(ET_files, key=extract_block_number)
# bdf_files = [file for file in EEG_files if file.endswith('.bdf')]

# Print the .bdf files
print(bdf_files)

preprocessing_info = {
    'Subject_ID': Subject,  # The subject ID
    'Bad_Channels_Detected': [],  # List of bad channels detected
    'Interpolated_Channels': [],  # List of channels that were interpolated
    'ICA_Components_Removed': [],  # List of ICA components removed
    'Bad_Epochs_Rejected': 0,
    'bad_face_rejected': 0,
    'bad_face_U_rejected': 0,
    'bad_obj_rejected': 0,
    'bad_face_U_rejected': 0,
    'bad_face_shadow_rejected': 0,
    'bad_face_U_shadow_rejected': 0,
    'bad_obj_shadow_rejected': 0,
    'bad_obj_U_shadow_rejected': 0,
    'Total_Number_good_epochs': 0,
    'good_face': 0,
    'good_face_U': 0,
    'good_obj': 0,
    'good_obj_U': 0,
    'good_face_shadow': 0,
    'good_face_U_shadow': 0,
    'good_obj_shadow': 0,
    'good_obj_U_shadow': 0,
    'F1_score': 0,
    'FA_rate':0,
    'Misses':0,
    'Precision':0,
    'Recall':0
}

#%% function to linearly interpolate

def interpolate_nan(data):
    """Linearly interpolate over NaN values in a 1D array."""
    valid_idx = np.where(~np.isnan(data))[0]  # Indices of valid (non-NaN) data
    if len(valid_idx) > 1:  # Ensure there is enough data to interpolate
        return np.interp(np.arange(len(data)), xp=valid_idx, fp=data[valid_idx])
    else:
        print("Not enough valid data for interpolation.")
        return data  # Return original if interpolation isn't possible

#%% Load ET
raw_et = []
annotations = []  
for i in range(0, len(ET_files),1):
    et = mne.io.read_raw_eyelink(file_path + "/" + ET_files[i])
    annotations.append(et.annotations)
    # Rename channels by removing '_right' and '_left'
    new_channel_names = {}
    for ch_name in et.ch_names:
        # Remove '_right' and '_left' from xpos, ypos, and pupil channels
        new_name = re.sub(r'_(right|left)', '', ch_name)
        new_channel_names[ch_name] = new_name

    # Apply the new names
    et.rename_channels(new_channel_names)
    
    # Append the processed raw ET data
    raw_et.append(et)

raw_ET = mne.concatenate_raws(raw_et, preload=True)

# For comparison 
raw_ET_copy = copy.deepcopy(raw_ET)

# Step 3: Extract events based on annotations (instead of using find_events)
# Annotations can be used to create events
annotations = raw_ET.annotations
print(annotations)  # Print to check the available annotations


# Create a list to store events
events_list = []
# Step 2: Loop through annotations and identify trial start annotations
for i, description in enumerate(annotations.description):
    # Use regex to match 'TRIALID trial start X' and extract trial number and type
    match = re.match(r'TRIALID (\d+)', description)
    print(match)
    if match:
        
        trial_num = int(match.group(1))  # Extract trial number (though it's repeating)

        # Get the onset time of this event
        onset_time = annotations.onset[i]
        
        # Append the event (MNE format requires [onset, 0, event_type])
        events_list.append([int(onset_time * raw_ET.info['sfreq']), 0, trial_num])

# Step 3: Convert the list to a numpy array in the MNE format
events_array = np.array(events_list)

# Step 4: Now `events_array` is in the correct format and can be used to create epochs
print(events_array)

# Step 5: You can now use this events_array to create epochs in MNE

#%% load EEG

raw_EEG = []
Events = []
for i in range(0, len(bdf_files),1):
    raw_tmp = mne.io.read_raw_bdf(file_path + "/" + bdf_files[i], eog=None, misc = None, stim_channel='auto',
                        exclude = (), infer_types = True, preload= True)
    
    events_tmp = mne.find_events(raw_tmp, stim_channel="Status", shortest_event = 1)
    
    raw_EEG.append(raw_tmp)
    Events.append(events_tmp)
    
raw, events= mne.concatenate_raws(raw_EEG, preload=True, 
                                    events_list=Events)
    
print("Number of channels:", len(raw.ch_names))

montage = mne.channels.make_standard_montage('biosemi64')
raw.set_montage(montage, on_missing='ignore')

raw.set_channel_types({"EXG1":"emg"})
raw.set_channel_types({"EXG2":"emg"})
raw.set_channel_types({"EXG3":"emg"})
raw.set_channel_types({"EXG4":"emg"})
raw.set_channel_types({"EXG5":"emg"})
raw.set_channel_types({"EXG6":"emg"})
raw.set_channel_types({"EXG7":"emg"})
raw.set_channel_types({"EXG8":"emg"})

# For subject 10708 FAST recorded at the end of the IC bdf
# events = np.delete(events, np.s_[0:537], axis=0) 

# For subject 10769 half of the block 12 recorded two times
# events = np.delete(events, np.s_[866:906], axis=0) 

# For subject 10787 block 4 not recorded in the ET
# events = np.delete(events, np.s_[235:313], axis=0) 

# For subject 10959 beginning of block 8 recorded two times
# events = np.delete(events, np.s_[627:662], axis=0) 

# For subject 11055 beginning of block 12 recorded two times
# events = np.delete(events, np.s_[871:908], axis=0) 

# For subject 11055 beginning of block 3 recorded two times
# events = np.delete(events, np.s_[163:183], axis=0) 

# For subject 11831 beginning of block 3 recorded two times
# events = np.delete(events, np.s_[150:161], axis=0) 

# For subject 1584 beginning of block 3 recorded two times
# events = np.delete(events, np.s_[158:217], axis=0) 


#%% Check if subject is over-responding or not

# Define event IDs for different stimuli and responses
event_dict = {'face': 21, 'face_U': 22,
              'obj': 31, 'obj_U': 32,
              'face_shadow': 121, 'face_U_shadow': 122,
            'obj_shadow': 131, 'obj_U_shadow': 132,
            'response':1}

# Get the indices of each stimulus type and responses
face = events[events[:, 2] == event_dict['face']]
face_U = events[events[:, 2] == event_dict['face_U']]
obj = events[events[:, 2] == event_dict['obj']]
obj_U = events[events[:, 2] == event_dict['obj_U']]
face_shadow = events[events[:, 2] == event_dict['face_shadow']]
face_U_shadow = events[events[:, 2] == event_dict['face_U_shadow']]
obj_shadow = events[events[:, 2] == event_dict['obj_shadow']]
obj_U_shadow = events[events[:, 2] == event_dict['obj_U_shadow']]
responses = events[events[:, 2] == event_dict['response']]

# Combine all stimuli (V, A, and AV) into a single array
every_stim = np.vstack([face, face_U, obj,obj_U,face_shadow,face_U_shadow,obj_shadow,obj_U_shadow])
all_stim = np.vstack([face_shadow,face_U_shadow,obj_shadow,obj_U_shadow])

# Calculate the total number of stimuli and total number of responses
total_stimuli = len(all_stim)
total_responses = len(responses)

print('The total number of stimuli is:',total_stimuli)
print('The total number of responses is:',total_responses)

# Check if the total number of responses is more than twice the number of stimuli
if total_responses >= 2 * total_stimuli:
    print(f"Warning: The total number of responses ({total_responses}) is more than twice the number of stimuli ({total_stimuli}).")
    print("Consider rejecting this subject as they may be randomly pressing the response button.")

#%%  F-score calculation

# Define the response window in samples (100 ms to 1500 ms)
sampling_rate = 512  # EEG sampling rate in Hz
lower_bound_samples = int(100 * sampling_rate / 1000)  # 100 ms in samples
upper_bound_samples = int(1500 * sampling_rate / 1000)  # 1500 ms in samples

# Function to calculate TP, FP, FN for all stimuli combined
def calculate_tp_fp_fn(all_stim_events, response_events, lower_bound, upper_bound):
    TP = 0  # True Positives
    FN = 0  # False Negatives
    FP = 0  # False Positives

    # Track responses that have been used (matched to a stimulus)
    used_responses = []

    # Loop over each stimulus in the combined set
    for stim in all_stim_events:
        # Find responses in the valid time window (100-1500 ms) after stimulus onset
        valid_responses = [resp for resp in response_events
                           if (stim[0] + lower_bound <= resp[0] <= stim[0] + upper_bound) 
                           and resp[0] not in used_responses]

        if valid_responses:
            TP += 1  # Correct response within the defined window
            used_responses.append(valid_responses[0][0])  # Mark the response as used
        else:
            FN += 1  # Stimulus presented but no correct response in the window

    # False positives: Responses that do not match any stimulus within the valid window
    for resp in response_events:
        stim_nearby = np.any((all_stim_events[:, 0] + lower_bound <= resp[0]) & 
                             (resp[0] <= all_stim_events[:, 0] + upper_bound))
        if not stim_nearby and resp[0] not in used_responses:
            FP += 1  # Response without a corresponding stimulus

    return TP, FP, FN

# Calculate TP, FP, FN for all stimuli combined
TP, FP, FN = calculate_tp_fp_fn(all_stim, responses, lower_bound_samples, upper_bound_samples)

# Calculate total stimuli and total responses
total_stimuli = len(all_stim)
total_responses = len(responses)

# Function to calculate precision, recall, and F1-score
def calculate_f1_score(TP, FP, FN):
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    if precision + recall > 0:
        f1_score = 2 * (precision * recall) / (precision + recall)
    else:
        f1_score = 0
    return precision, recall, f1_score

# Calculate F1-score for all stimuli combined
precision, recall, f1 = calculate_f1_score(TP, FP, FN)

# Calculate False Alarm Rate and Miss Rate
false_alarm_rate = (FP / total_responses) * 100 if total_responses > 0 else 0
miss_rate = (FN / total_stimuli) * 100 if total_stimuli > 0 else 0

# Print results
print(f'Global Precision: {precision}, Recall: {recall}, F1-Score: {f1}')
print(f'Percent of False Alarms: {false_alarm_rate:.2f}%')
print(f'Percent of Misses: {miss_rate:.2f}%')

#%% Test pyprep - Noisy Channels to detect bad channels in raw object

from pyprep.find_noisy_channels import NoisyChannels

nd = NoisyChannels(raw, random_state=None) 

nd.find_all_bads(ransac = True, channel_wise = True) # Call all the functions to detect bad channels

# Functions = 
# # # NOTE: Bad-by-NaN/flat is already run during init, no need to re-run here
#         self.find_bad_by_deviation()
#         self.find_bad_by_hfnoise()
#         self.find_bad_by_correlation()
#         self.find_bad_by_SNR()
#         if ransac:
#             self.find_bad_by_ransac(
#                 channel_wise=channel_wise, max_chunk_size=max_chunk_size
#             )

# Get the list of bad channels
bad_channels = nd.get_bads()

# Calculate the percentage of bad channels
total_channels = 64  # Since you're working with 64 channels
bad_channel_count = len(bad_channels)
bad_channel_percentage = (bad_channel_count / total_channels) * 100

print('Bad channels detected:',nd.get_bads())
print('Percent of bad channels detected:',bad_channel_percentage)

#%% interpolate bad channels

# Check if the percentage of bad channels exceeds 15%
if bad_channel_percentage > 15:
    print(f"Subject should be removed: {bad_channel_count} bad channels detected ({bad_channel_percentage:.2f}% of total channels).")
else:
    # If less than 15%, proceed to interpolate bad channels
    raw.info["bads"] = bad_channels
    raw = raw.interpolate_bads()
    # Fill the interpolated channels (which are the same as detected bad channels in this case)
    
    print(f"Interpolation performed: {bad_channel_count} bad channels detected ({bad_channel_percentage:.2f}% of total channels).")

#%% Filtration

lowpass_epochs = 40
highpass_epochs = 0.01

raw.filter(l_freq=highpass_epochs, h_freq=lowpass_epochs)

#%% Event filtration and selection 

import numpy as np
import mne

# Assume your events are already loaded in the `events` array
# Copy the events as per your initial step
events_news = events.copy()

events_base_EEG = events_news[np.where((events_news[:, 2] == 21) | 
                                   (events_news[:, 2] == 22) | 
                                   (events_news[:, 2] == 31) | 
                                   (events_news[:, 2] == 32) | 
                                   (events_news[:, 2] == 121) | 
                                   (events_news[:, 2] == 122) | 
                                   (events_news[:, 2] == 131) | 
                                   (events_news[:, 2] == 132))]

# # Define the sampling frequency
# sfreq = 512  # Hz

# # Extract event onset times (assumes event times are stored in the first column)
# event_times = events_base_EEG[:, 0]  # Extract event onset times in samples

# # Compute ISI in seconds
# ISI = np.diff(event_times) / sfreq  # Convert from samples to seconds

# # Display results
# print("Inter-Stimulus Intervals (ISI) in seconds:", ISI)

# # # Define the sampling frequency
# sfreq_et = 500  # Hz

# # Extract event onset times (assumes event times are stored in the first column)
# event_times_et = events_array[:, 0]  # Extract event onset times in samples

# # Compute ISI in seconds
# ISI_et = np.diff(event_times_et) / sfreq_et  # Convert from samples to seconds


#%% Compare if not same length

event_code_eeg = events_base_EEG[:,2]
event_code_et = events_array[:,2]

if len(event_code_eeg) == len(event_code_et):
    print("WOOOHOOOOO they match! Continue.")
else:
    print("Yikes you're cooked. The events don't line up. :( Good luck figuring that out.")
    
#%% If they are the same length then extract the triggers code from the EEG to code the trials type in the eye-tracking

events_array[:,2] = events_base_EEG[:,2]

# Delete trials EEG

# For Subject 10400 delete trial 300 and 301 because block 4 restarted
# events_news = np.delete(events_news, np.s_[608:611], axis=0) # Becareful, need to drop them also in RT file

#  Delete trials in ET

# # For Subject 10182 first 13 trials not recorded with the EEG => deleted in the ET to match
# # Delete rows 0 to 12 (inclusive)
# events_array = np.delete(events_array, np.s_[0:13], axis=0)

# # For Subject 10314 
# events_array = np.delete(events_array, np.s_[128], axis=0)

# For Subject 11038: 2 trials not recorded in the EEG but present in the EEG flagged based on the ISI
# events_array = np.delete(events_array, np.s_[503], axis=0)
# events_array = np.delete(events_array, np.s_[543], axis=0)

# # For Subject 11161
# events_array = np.delete(events_array, np.s_[116], axis=0)

# # For Subject 11235
# events_array = np.delete(events_array, np.s_[57], axis=0)
# events_array = np.delete(events_array, np.s_[517], axis=0)

# # For Subject 11386
# events_array = np.delete(events_array, np.s_[209], axis=0)

# # For Subject 11638
# events_array = np.delete(events_array, np.s_[446], axis=0) # and remove block 1 in ET files

# # For Subject 11777
# events_array = np.delete(events_array, np.s_[637:660], axis=0) # and remove block 1 in ET files


#%% Calculate dataframe that index the reaction time for target stimuli for further selection

events_base_EEG_responses = events_news[np.where((events_news[:, 2] == 21) | 
                                   (events_news[:, 2] == 22) | 
                                   (events_news[:, 2] == 31) | 
                                   (events_news[:, 2] == 32) | 
                                   (events_news[:, 2] == 121) | 
                                   (events_news[:, 2] == 122) | 
                                   (events_news[:, 2] == 131) | 
                                   (events_news[:, 2] == 132) | 
                                   (events_news[:,2] == 1))]

#%% Epoching EEG data with all trials after PREP

event_dict = {'face': 21,
 'face_U': 22,
 'obj': 31,
 'obj_U': 32,
 'face_shadow': 121,
 'face_U_shadow': 122,
 'obj_shadow': 131,
 'obj_U_shadow': 132}

tmin_epochs = -0.5
tmax_epochs = 1

epochs_all = mne.Epochs(raw, events_base_EEG, tmin=tmin_epochs, tmax=tmax_epochs, reject=None, 
                        event_id=event_dict, baseline=None, detrend=1, preload=True, decim=4)

#%% Step 1: Epoch the raw ET data without interpolating blinks
# Epoch uncorrected ET data (raw data without blink interpolation or offscreen cleaning)
# Need to have reject_by_annotations set to "false" to avoid rejecting by bad blink

# Uncleaned ET epochs:
epochs_uncorrected_ET = mne.Epochs(raw_ET, events_array, tmin=tmin_epochs, tmax=tmax_epochs, reject=None, flat=None, 
                        event_id=event_dict, baseline=None, preload=True, decim=1, reject_by_annotation=False)

#%% Compare drop_log for EEG and ET epochs

dropped_epochs_all = [n for n, dl in enumerate(epochs_all.drop_log) if len(dl)]  # result is a list

print('Epochs dropped for the EEG:',dropped_epochs_all)

dropped_epochs_ET = [n for n, dl in enumerate(epochs_uncorrected_ET.drop_log) if len(dl)]  # result is a list

print('Epochs dropped for the eye-tracking:',dropped_epochs_ET)

#%% CARE - Manual step checking 

# Select only the common valid epochs
epochs_uncorrected_ET = epochs_uncorrected_ET.drop(dropped_epochs_all) # If the epoch 719 has been dropped in the EEG and not in the ET

# Need also to drop corresponding events from the events_base_EEG_responses file before calculating RT to have a synchronized file
events_base_EEG_responses = np.delete(events_base_EEG_responses,0,axis=0) # To delete the first event, check that is not a target event 
events_base_EEG_responses = np.delete(events_base_EEG_responses,len(events_base_EEG_responses)-1,axis=0) # To delete the very last event

# Need also to drop corresponding events from the ET events file for later to have a synchronized file
events_array = np.delete(events_array,0,axis=0) # To delete the first event, check that is not a target event 
events_array = np.delete(events_array,len(events_array)-1,axis=0) # To delete the very last event

# # Need also to drop corresponding events from the events_base_EEG_responses file before calculating RT to have a synchronized file
# events_base_EEG_responses = np.delete(events_base_EEG_responses,dropped_epochs_all,axis=0) # To delete the first event, check that is not a target event 

# # Need also to drop corresponding events from the ET events file for later to have a synchronized file
# events_array = np.delete(events_array,dropped_epochs_all,axis=0) # To delete the first event, check that is not a target event 


#%% Calculating reaction time for each target trial

import pandas as pd
import numpy as np

# Define event codes
event_dict = {
    'face_shadow': 121,
    'face_U_shadow': 122,
    'obj_shadow': 131,
    'obj_U_shadow': 132
}
response_code = 1  # Mouse button press

# Convert events to a Pandas DataFrame
df_events = pd.DataFrame(events_base_EEG_responses, columns=["time", "unknown", "event_id"])

# Initialize RT columns for each target type
for target in event_dict.keys():
    df_events[target + "_RT"] = np.nan  # Create separate RT columns

# Extract response trials (do not include them in df_events)
df_responses = df_events[df_events["event_id"] == response_code].copy()

# Define RT validity range in ms
valid_RT_min, valid_RT_max = 150, 1000  

# Compute RT for each target trial while keeping all trials
for target, event_code in event_dict.items():
    df_targets = df_events[df_events["event_id"] == event_code].copy()
    
    for i, row in df_targets.iterrows():
        target_time = row["time"]
        
        # Find the first response occurring after the stimulus
        response_times = df_responses["time"][df_responses["time"] > target_time]
        
        if not response_times.empty:
            RT = (response_times.values[0] - target_time) / raw.info["sfreq"] * 1000  # Convert to ms
            
            # Check if RT is within valid range
            if valid_RT_min <= RT <= valid_RT_max:
                df_events.loc[df_events["time"] == target_time, target + "_RT"] = RT  # Store valid RT
            else:
                df_events.loc[df_events["time"] == target_time, target + "_RT"] = -1  # No valid response
        else:
            df_events.loc[df_events["time"] == target_time, target + "_RT"] = -1  # No response at all

# Remove response events from the DataFrame (but keep all other trials)
df_RT = df_events[df_events["event_id"] != response_code]

# Keep only relevant columns (time, event_id, and RTs)
df_RT = df_RT[["time", "event_id"] + [target + "_RT" for target in event_dict.keys()]]
df_RT = df_RT.reset_index(drop=True)

# Example to select one type of target trial responses: rt_data = df_RT["face_shadow_RT"].dropna()

# Extract RT data for face_shadow trials, excluding NaN and -1 values
rt_data_face = df_RT["face_shadow_RT"].dropna()  # Remove NaN values first
rt_data_face = rt_data_face[rt_data_face != -1]  # Exclude missed responses (-1)

# Extract RT data for face_shadow trials, excluding NaN and -1 values
rt_data_U_face = df_RT["face_U_shadow_RT"].dropna()  # Remove NaN values first
rt_data_U_face = rt_data_U_face[rt_data_U_face != -1]  # Exclude missed responses (-1)

# Extract RT data for face_shadow trials, excluding NaN and -1 values
rt_data_object = df_RT["obj_shadow_RT"].dropna()  # Remove NaN values first
rt_data_object = rt_data_object[rt_data_object != -1]  # Exclude missed responses (-1)

# Extract RT data for face_shadow trials, excluding NaN and -1 values
rt_data_U_object = df_RT["obj_U_shadow_RT"].dropna()  # Remove NaN values first
rt_data_U_object = rt_data_U_object[rt_data_U_object != -1]  # Exclude missed responses (-1)

# Compute the average RT
average_rt_face = rt_data_face.mean()
average_rt_U_face = rt_data_U_face.mean()
average_rt_object = rt_data_object.mean()
average_rt_U_object = rt_data_U_object.mean()

# Print result
print(f"Average RT for face_shadow trials (excluding misses): {average_rt_face:.2f} ms")
print(f"Average RT for inverted_face_shadow trials (excluding misses): {average_rt_U_face:.2f} ms")
print(f"Average RT for object_shadow trials (excluding misses): {average_rt_object:.2f} ms")
print(f"Average RT for inverted_object_shadow trials (excluding misses): {average_rt_U_object:.2f} ms")

#%%#INDEPENDENT COMPONENTS ANALYSIS (ICA) for PREP epochs files

# epochs_ica = raw_tmp.filter(l_freq=1., h_freq=None)

epochs_ica = epochs_all.filter(l_freq=1., h_freq=None)
# epochs_ica.set_eeg_reference('average')
#ICA est sensible aux dérives basse fréquence donc 1Hz + charge données

#Parameters ICA
n_components = None #0.99 # % de vraiance expliquée ou alors le nombre d'électrodes
max_pca_components = 63 # disparaitra dans une future version de MNE, nombre de PCA a faire avant ICA
random_state = 42 #* pour que l'ICA donne la même chose sur les mêmes données
method = 'fastica' # méthode de l'ICA (si 'picard' nécessite pip install python-picard)
fit_params = None # fastica_it=5 paramètre lié à la methode picard
max_iter = 1000 # nombre d'iterations de l'ICA

ica = mne.preprocessing.ICA(n_components=n_components, method = method, max_iter = max_iter, fit_params= fit_params, random_state=random_state)

ica.fit(epochs_ica)
ica.plot_sources(epochs_all)
ica.plot_components()

#%% APPLICATION ICA COMMUN AVERAGE REFERENCE
ica.apply(epochs_all)

# Baseline correction after ICA
baseline = (-0.2,-0.05)
epochs_all.apply_baseline(baseline=baseline)

# Use of autoreject package after ICA to remove bads epochs for no PREP epochs
import autoreject

ar = autoreject.AutoReject(n_interpolate= [1, 2, 4],
                           thresh_method='bayesian_optimization',
                           n_jobs = 1,
                           verbose = True)

ar.fit(epochs_all)
epochs_ar_all, reject_log_all = ar.transform(epochs_all, return_log=True)

#%% Visualisation tools all no PREP

# All
# Visualize the dropped epochs
epochs_all[reject_log_all.bad_epochs].plot(scalings=dict(eeg=100e-6))

# Visualize the rejected log
reject_log_all.plot('horizontal')

#%% Drop epochs into the RT dataframe and save clean EEG epochs and associated RT file 

# Save the number of rejected epochs
rejected_epochs_count = len(np.where(reject_log_all.bad_epochs)[0])

epochs_uncorrected_ET.drop(np.where(reject_log_all.bad_epochs)[0])

# Remove the corresponding reaction time entries
df_RT = df_RT.copy().drop(np.where(reject_log_all.bad_epochs)[0])
# Reset the index to keep it continuous
df_RT = df_RT.reset_index(drop=True)

events_array = np.delete(events_array, np.where(reject_log_all.bad_epochs)[0], axis=0)

# Print the updated Reaction Time file length for verification
print('Updated number of reaction time trials:', len(df_RT))
print('Number of EEG epochs:', len(epochs_ar_all))
print('Number of ET epochs:', len(epochs_uncorrected_ET))
#%% Plot ERP NO PREP

# Step 1: Set EEG reference
epochs_ar_all.set_eeg_reference(ref_channels='average')  # Common Average Reference

# Step 2: Compute ERP for each stimulus type
ERP_face = epochs_ar_all['face'].average()
ERP_face_U = epochs_ar_all['face_U'].average()
ERP_obj = epochs_ar_all['obj'].average()
ERP_obj_U = epochs_ar_all['obj_U'].average()

# Step 3: Select cluster of occipital-parietal channels
channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
picks = [ERP_face.ch_names.index(ch) for ch in channels if ch in ERP_face.ch_names]

# Step 4: Extract ERP data for selected channels and average across them
times = ERP_face.times  # Time vector (same for all ERPs)
erp_face_data = ERP_face.data[picks, :].mean(axis=0)
erp_face_U_data = ERP_face_U.data[picks, :].mean(axis=0)
erp_obj_data = ERP_obj.data[picks, :].mean(axis=0)
erp_obj_U_data = ERP_obj_U.data[picks, :].mean(axis=0)

# Step 5: Plot ERPs
plt.figure(figsize=(10, 5))

plt.plot(times, erp_face_data * 1e6, label="Face", color="blue")  # Convert V to µV
plt.plot(times, erp_face_U_data * 1e6, label="Face_U", color="cyan")
plt.plot(times, erp_obj_data * 1e6, label="Object", color="red")
plt.plot(times, erp_obj_U_data * 1e6, label="Object_U", color="orange")

# Step 6: Formatting
plt.axvline(x=0, color='k', linestyle='--', label="Stimulus Onset")  # Mark stimulus onset
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (µV)")
plt.title("ERP over Occipital-Parietal Channels")
plt.legend()
plt.grid(True)
plt.show()

#%% Save pre-processing information and EEG-only epochs file + RT dataframe

import json

# Total number of good epochs
total_good_epochs_face = len(epochs_ar_all['face'])
total_good_epochs_face_U = len(epochs_ar_all['face_U'])

total_good_epochs_obj = len(epochs_ar_all['obj'])
total_good_epochs_obj_U = len(epochs_ar_all['obj_U'])

total_good_epochs_face_shadow = len(epochs_ar_all['face_shadow'])
total_good_epochs_face_U_shadow = len(epochs_ar_all['face_U_shadow'])

total_good_epochs_obj_shadow = len(epochs_ar_all['obj_shadow'])
total_good_epochs_obj_U_shadow = len(epochs_ar_all['obj_U_shadow'])

# Update preprocessing_info dictionary with the values
preprocessing_info = {
    'Subject_ID': Subject,  # The subject ID
    'Bad_Channels_Detected': nd.get_bads(),  # List of bad channels detected
    'Interpolated_Channels': bad_channels,  # List of channels that were interpolated
    'ICA_Components_Removed': ica.exclude,  # List of ICA components removed
    'Bad_Epochs_Rejected_Autoreject': len(np.where(reject_log_all.bad_epochs)[0]),
    'Total_Number_good_epochs_face': total_good_epochs_face,
    'Total_Number_good_epochs_face_U': total_good_epochs_face_U,
    'Total_Number_good_epochs_obj': total_good_epochs_obj,
    'Total_Number_good_epochs_obj_U': total_good_epochs_obj_U,
    'Total_Number_good_epochs_face_shadow': total_good_epochs_face_shadow,
    'Total_Number_good_epochs_face_U_shadow': total_good_epochs_face_U_shadow,
    'Total_Number_good_epochs_obj_shadow': total_good_epochs_obj_shadow,
    'Total_Number_good_epochs_obj_U_shadow': total_good_epochs_obj_U_shadow,
    'F1_score': f1,
    'FA_rate':false_alarm_rate,
    'Misses':miss_rate,
    'Precision':precision,
    'Recall':recall,
    'RT_face':average_rt_face,
    'RT_face_U':average_rt_U_face,
    'RT_obj':average_rt_object,
    'RT_obj_U':average_rt_U_object
}

# Print the updated preprocessing information
print(preprocessing_info)

file_path = 'Z://Analysis/SFARI_Analysis/FAST/Theo/Epochs_EEG_Only/SIB'

# Ensure the file path exists, if not, create it
if not os.path.exists(file_path):
    os.makedirs(file_path)

# Epochs file: Save epochs as a .fif file
saving_file_all = file_path + '/' + Subject + '_EEG_epo.fif'
epochs_ar_all.save(saving_file_all)

saving_file_epo_ET = file_path + '/' + Subject + '_ET_epo.fif'
epochs_uncorrected_ET.save(saving_file_epo_ET)

# Reaction time file: Save RT DataFrame as a .csv file
csv_path_RT = file_path + "/" + Subject + "_RT_all.csv"
df_RT.to_csv(csv_path_RT, sep='\t', encoding='utf-8')

# Function to convert NumPy data types to native Python types
def convert_to_serializable(d):
    for key, value in d.items():
        if isinstance(value, np.integer):
            d[key] = int(value)
        elif isinstance(value, np.floating):
            d[key] = float(value)
        elif isinstance(value, np.ndarray):
            d[key] = value.tolist()  # Convert arrays to lists if any
    return d

# Convert preprocessing_info dictionary to JSON serializable format
preprocessing_info_serializable = convert_to_serializable(preprocessing_info)

# Save the preprocessing information as a JSON file
json_file_path = file_path + '/' + Subject + '_preprocessing_info.json'
with open(json_file_path, 'w') as json_file:
    json.dump(preprocessing_info_serializable, json_file, indent=4)

print(f"Preprocessing info saved to {json_file_path}")

print("Files saved successfully:")
print(f"Epochs file: {saving_file_all}")
print(f"Reaction time file: {csv_path_RT}")
print(f"Preprocessing info file: {json_file_path}")

#%% save excel sheet for all

import pandas as pd
import os

# File path where the Excel will be saved
excel_file_path = 'Z://Analysis/SFARI_Analysis/FAST/Theo/Epochs_EEG_Only/SIB/preprocessing_info.xlsx'

# Convert preprocessing info into a DataFrame for the current subject
preprocessing_df = pd.DataFrame([preprocessing_info], index=[Subject])

# If the file exists, load it and append the new data
if os.path.exists(excel_file_path):
    existing_df = pd.read_excel(excel_file_path, index_col=0)
    # Append the new subject's data to the existing DataFrame
    updated_df = pd.concat([existing_df, preprocessing_df])
else:
    # If the file doesn't exist, create a new DataFrame
    updated_df = preprocessing_df

# Save (or overwrite) the Excel file with the updated DataFrame
updated_df.to_excel(excel_file_path)

print(f"Preprocessing information for subject {Subject} saved successfully.")

#%% Step 1: Epoch the raw ET data without interpolating blinks
# Epoch uncorrected ET data (raw data without blink interpolation or offscreen cleaning)
# Need to have reject_by_annotations set to "false" to avoid rejecting by bad blink

event_dict = {'face': 21,
 'face_U': 22,
 'obj': 31,
 'obj_U': 32,
 'face_shadow': 121,
 'face_U_shadow': 122,
 'obj_shadow': 131,
 'obj_U_shadow': 132}

# Define screen bounds
screen_width = 1920
screen_height = 1080

# Get channel indices for xpos and ypos and pupil
xpos_index = raw_ET.ch_names.index("xpos")  # X position
ypos_index = raw_ET.ch_names.index("ypos")  # Y position
pupil_index = raw_ET.ch_names.index("pupil")  # Pupil channel

#  Step 2: Identify blink (0 values) and offscreen data in each epoch
blink_positions_per_epoch = {}
offscreen_positions_per_epoch = {}
blink_proportions = []
offscreen_proportions = []

for epoch_id, epoch_data in enumerate(epochs_uncorrected_ET.get_data()):
    pupil_data_epoch = epoch_data[pupil_index, :]  # Pupil data for this epoch
    xpos_data_epoch = epoch_data[xpos_index, :]  # X position
    ypos_data_epoch = epoch_data[ypos_index, :]  # Y position

    # Identify blink positions (0 values)
    blink_positions = np.where(pupil_data_epoch == 0)[0]
    blink_positions_per_epoch[epoch_id] = blink_positions
    num_blink_samples = len(blink_positions)  # Count the number of samples
    
    
    # Calculate proportion of blink counts
    epoch_length = epochs_uncorrected_ET.get_data().shape[2]  # Number of samples in an epoch
    blink_proportion = num_blink_samples/ epoch_length
    blink_proportions.append(blink_proportion)  # Save the proportion
    
    # Identify offscreen positions
    offscreen_mask = (xpos_data_epoch <= 0) | (xpos_data_epoch > screen_width) | \
                     (ypos_data_epoch <= 0) | (ypos_data_epoch > screen_height)
    offscreen_positions = np.where(offscreen_mask)[0]
    offscreen_positions_per_epoch[epoch_id] = offscreen_positions
    num_offscreen_samples =len(offscreen_positions)
    
    # Calculate the proportion of offscreen counts
    offscreen_proportion = num_offscreen_samples/ epoch_length
    offscreen_proportions.append(offscreen_proportion) 
    
# Calculate averages for preprocessing log
avg_blink_proportions = sum(blink_proportions)/len(blink_proportions)
avg_offscreen_proportions = sum(offscreen_proportions)/len(offscreen_proportions)

print("Average blink proportions:", avg_blink_proportions)
print("Average offscreen proportions:", avg_offscreen_proportions)

#%% Step 2: Epoch the raw data AFTER interpolating blinks and cleaning offscreen data

# Interpolate blinks and clean offscreen data in the raw data
xpos_data = raw_ET._data[xpos_index, :]
ypos_data = raw_ET._data[ypos_index, :]
pupil_data = raw_ET._data[pupil_index, :]

# Create offscreen mask for raw data
offscreen_mask = (xpos_data < 0) | (xpos_data > screen_width) | \
                 (ypos_data < 0) | (ypos_data > screen_height)

# Mark offscreen points as NaN in the pupil channel
pupil_data[offscreen_mask] = np.nan

# Interpolate blink data in raw data
raw_ET_cleaned = raw_ET.copy()  # Create a copy for cleaned data
raw_ET_cleaned = mne.preprocessing.eyetracking.interpolate_blinks(
    raw_ET_cleaned, match="BAD_blink", buffer=(0.05, 0.2)
)

# Epoch the cleaned raw data
epochs_cleaned_ET = mne.Epochs(raw_ET_cleaned, events_array, tmin=tmin_epochs, tmax=tmax_epochs, 
                            reject=None, flat= None, event_id=event_dict, baseline=None, preload=True, 
                            decim=1, reject_by_annotation=False )

#%% Step 3: Compare indicies of blinks and offscreen data (all missing data) for each epoch
total_interpolated_counts = {}
epochs_to_drop = []
epochs_drop_critical_window = [] # for informational purposes only
sfreq = epochs_cleaned_ET.info['sfreq']

interpolated_proportions = []

for epoch_id in range(len(epochs_cleaned_ET)):
    # Get blink and offscreen positions for this epoch from uncorrected data
    blink_positions = blink_positions_per_epoch.get(epoch_id, [])
    offscreen_positions = offscreen_positions_per_epoch.get(epoch_id, [])

    # Calculate overlap and unique points
    overlap = set(blink_positions).intersection(offscreen_positions)
    unique = set(blink_positions).union(offscreen_positions)
    total_interpolated_counts[epoch_id] = len(unique) - len(overlap)
    
    critical_window=(0, 0.2) # 0-200 ms, the stimulus in on the screen
    # Adjusting for epoch start time (-0.5 sec)
    time_samples = (int((critical_window[0] + .5) * sfreq), int((critical_window[1] + .5) * sfreq))  
    
    # Calculate proportion of interpolated counts
    epoch_length = epochs_cleaned_ET.get_data().shape[2]  # Number of samples in an epoch
    interpolated_proportion = total_interpolated_counts[epoch_id] / epoch_length
    interpolated_proportions.append(interpolated_proportion)  # Save the proportion
    
    # Check if any blink or offscreen index falls within the 500-700 ms window (0-200 ms; critical
    # stimulus display window)
    if any(time_samples[0] <= idx < time_samples[1] for idx in blink_positions) or \
       any(time_samples[0] <= idx < time_samples[1] for idx in offscreen_positions):
        epochs_to_drop.append(epoch_id)
        epochs_drop_critical_window.append(epoch_id)
     # Determine if this epoch should be dropped
    elif interpolated_proportion > 0.5:
        epochs_to_drop.append(epoch_id)
        
print(f"Marked {len(epochs_drop_critical_window)} epochs for removal due to blinks or offscreen data in the critical window (0-200 ms).")
        
# After the loop, interpolated_proportions will contain the proportions for all epochs
#print("Interpolated proportions for each epoch:", interpolated_proportions)

avg_interpolated_proportion = sum(interpolated_proportions)/len(epochs_cleaned_ET)

print("Average interpolated proportions:", avg_interpolated_proportion)

#%% Need to drop the identified epochs: epochs_to_drop from EEG, ET and RT file

# Drop identified epochs for the cleaned ET
epochs_cleaned_ET.drop(epochs_to_drop)

# Same for the EEG
epochs_ar_all.drop(epochs_to_drop)

# Same for the RT file
df_RT = df_RT.copy().drop(np.where(epochs_to_drop)[0])
# Reset the index to keep it continuous
df_RT = df_RT.reset_index(drop=True)

#%% Step 4: Identify and remove outliers

# Get the data for all epochs
epochs_ID_outliers = epochs_cleaned_ET.get_data()  # Shape: (n_epochs, n_channels, n_times)

# Initialize a dictionary to store the count of outliers for each epoch
outliers_per_epoch = {}

outlier_proportions = []

# Loop through each epoch and clean outliers
for epoch_id in range(len(epochs_ID_outliers)):
    pupil_data = epochs_ID_outliers[epoch_id, pupil_index, :]  # Extract pupil data for the epoch

    # Calculate IQR
    Q1 = np.percentile(pupil_data, 25)
    Q3 = np.percentile(pupil_data, 75)
    IQR = Q3 - Q1

    # Define outlier thresholds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Identify outliers
    outlier_mask = (pupil_data < lower_bound) | (pupil_data > upper_bound)
    
    # Count the number of outliers
    num_outliers = np.sum(outlier_mask)
    outliers_per_epoch[epoch_id] = num_outliers
    
    # Calculate the proportion of outliers
    outlier_proportion = num_outliers/epoch_length
    outlier_proportions.append(outlier_proportion)
    
    #Calculate averages for preprocessing log
    avg_outlier_proportions = sum(outlier_proportions)/len(outlier_proportions)
    
    
    # Remove outliers by setting them to NaN
    pupil_data[outlier_mask] = np.nan
    
    # Replace the cleaned data back into the epoch
    epochs_ID_outliers[epoch_id, pupil_index, :] = pupil_data
    
# Update the epochs with the cleaned data
epochs_cleaned_ET._data = epochs_ID_outliers

# Print the number of outliers removed per epoch
print("Number of outliers removed per epoch:")
for epoch_id, count in outliers_per_epoch.items():
    print(f"Epoch {epoch_id}: {count} outliers")

#%% Step 7: Interpolate the remaining epochs

interpolated_epochs_data = epochs_cleaned_ET.get_data()  # Shape: (n_epochs, n_channels, n_times)

for i in range(len(interpolated_epochs_data)):
    # Extract pupil data for the current epoch
    pupil_data_epoch = interpolated_epochs_data[i, pupil_index, :]
    
    # Interpolate NaN values
    pupil_data_epoch_interpolated = interpolate_nan(pupil_data_epoch)
    
    # Replace the data back into the epoch
    interpolated_epochs_data[i, pupil_index, :] = pupil_data_epoch_interpolated
    
# Update the epochs data with the interpolated and smoothed pupil data
epochs_cleaned_ET._data = interpolated_epochs_data

#%% Save epoch for ET only and preprocessing info
import json

# Update preprocessing_info dictionary with the values
preprocessing_info_ET = {'Subject_ID': Subject, # The subject ID
    'Percent_interpolated_per_block': interpolated_proportions,
    'Average_Percent_Interpolated': avg_interpolated_proportion, # average proportion of missing data (blinks, offscreen, or outliers)
    'Percent_blinks_per_block':blink_proportions,
    'Average_Percent_Blinks': avg_blink_proportions, # average proportion removed due to blinks
    'Percent_outliers_per_block': outlier_proportions,
    'Average_Percent_Outliers': avg_outlier_proportions,  # average proportion removed due to outliers
    'Percent_offscreen_per_block': offscreen_proportions,
    'Average_Percent_Offscreen': avg_offscreen_proportions, # average proportion removed due to offscreen
    'Bad_Epochs': epochs_to_drop # Number of bad epochs detected and dropped
    }

# Print the updated preprocessing information
print(preprocessing_info_ET)

file_path = 'Z://Analysis/SFARI_Analysis/FAST/Theo/Epochs_ET_EEG_Synch/SIB'

# Ensure the file path exists, if not, create it
if not os.path.exists(file_path):
    os.makedirs(file_path)

# Epochs file: Save epochs as a .fif file
saving_file_epo_ET = file_path + '/' + Subject + '_Cleaned_FAST_ET_Only_epo.fif'
epochs_cleaned_ET.save(saving_file_epo_ET)

saving_file_all = file_path + '/' + Subject + '_EEG_epo.fif'
epochs_ar_all.save(saving_file_all)

# Reaction time file: Save RT DataFrame as a .csv file
csv_path_RT = file_path + "/" + Subject + "_RT_all.csv"
df_RT.to_csv(csv_path_RT, sep='\t', encoding='utf-8')

# Function to convert NumPy data types to native Python types
def convert_to_serializable(d):
    for key, value in d.items():
        if isinstance(value, np.integer):
            d[key] = int(value)
        elif isinstance(value, np.floating):
            d[key] = float(value)
        elif isinstance(value, np.ndarray):
            d[key] = value.tolist()  # Convert arrays to lists if any
    return d

# Convert preprocessing_info dictionary to JSON serializable format
preprocessing_info_serializable = convert_to_serializable(preprocessing_info_ET)

# Save the preprocessing information as a JSON file
json_file_path = file_path + '/' + Subject + '_preprocessing_info.json'
with open(json_file_path, 'w') as json_file:
    json.dump(preprocessing_info_serializable, json_file, indent=4)
    
print(f"Preprocessing info saved to {json_file_path}")

print("Files saved successfully:")
print(f"Epochs file: {saving_file_all}")

# File path where the Excel will be saved
excel_file_path = 'Z://Analysis/SFARI_Analysis/FAST/Theo/Epochs_ET_EEG_Synch/SIB/preprocessing_info.xlsx'

# Convert preprocessing info into a DataFrame for the current subject
preprocessing_df = pd.DataFrame([preprocessing_info_ET], index=[Subject])

# If the file exists, load it and append the new data
if os.path.exists(excel_file_path):
    existing_df = pd.read_excel(excel_file_path, index_col=0)
    # Append the new subject's data to the existing DataFrame
    updated_df = pd.concat([existing_df, preprocessing_df])
else:
    # If the file doesn't exist, create a new DataFrame
    updated_df = preprocessing_df

# Save (or overwrite) the Excel file with the updated DataFrame
updated_df.to_excel(excel_file_path)

print(f"Preprocessing information for subject {Subject} saved successfully.")

# Filtration for ET

# import numpy as np
# import pandas as pd

# # Define screen bounds
# screen_width = 1920
# screen_height = 1080

# # Get channel indices for xpos and ypos
# xpos_index = raw_ET.ch_names.index("xpos")  # X position
# ypos_index = raw_ET.ch_names.index("ypos")  # Y position

# # Define the time window (0 to 200ms)
# sfreq = epochs_uncorrected_ET.info["sfreq"]
# tmin, tmax = 0, 0.2  # Time in seconds
# time_mask = (epochs_uncorrected_ET.times >= tmin) & (epochs_uncorrected_ET.times <= tmax)

# # List to track epochs to reject
# epochs_to_reject = []

# # Step 2: Identify blink (0 values) and offscreen gaze during stimulus presentation (0-200ms)
# for epoch_id, epoch_data in enumerate(epochs_uncorrected_ET.get_data()):
#     xpos_data_epoch = epoch_data[xpos_index, time_mask]  # X position (0-200ms)
#     ypos_data_epoch = epoch_data[ypos_index, time_mask]  # Y position (0-200ms)

#     # Identify offscreen positions (out of screen bounds)
#     offscreen_mask = (xpos_data_epoch <= 0) | (xpos_data_epoch > screen_width) | \
#                      (ypos_data_epoch <= 0) | (ypos_data_epoch > screen_height)

#     # If any sample in 0-200ms is offscreen, mark this epoch for rejection
#     if np.any(offscreen_mask):
#         epochs_to_reject.append(epoch_id)

# # Convert to numpy array for indexing
# epochs_to_reject = np.array(epochs_to_reject)

# # Step 3: Remove flagged epochs from both EEG and ET epoch objects
# epochs_filtered_EEG = epochs_all.drop(epochs_to_reject, reason="Offscreen Gaze")
# epochs_filtered_ET = epochs_uncorrected_ET.drop(epochs_to_reject, reason="Offscreen Gaze")

# # Step 4: Remove rejected epochs from the RT DataFrame
# df_RT_filtered = df_RT.drop(epochs_to_reject).reset_index(drop=True)

# # Display how many epochs were removed
# print(f"Removed {len(epochs_to_reject)} epochs due to offscreen gaze behavior.")

# # Display updated EEG, ET, and RT epoch counts
# print(f"Remaining EEG epochs: {len(epochs_filtered_EEG)}")
# print(f"Remaining ET epochs: {len(epochs_filtered_ET)}")
# print(f"Remaining RT entries: {len(df_RT_filtered)}")

# # Display the filtered RT DataFrame
# import ace_tools as tools
# tools.display_dataframe_to_user(name="Filtered Reaction Time Data", dataframe=df_RT_filtered)