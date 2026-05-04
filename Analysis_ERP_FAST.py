# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 16:31:53 2025

@author: tvanneau
"""

import matplotlib as mpl

new_rc_params = {'text.usetex': False,
"svg.fonttype": 'none'
}
mpl.rcParams.update(new_rc_params)

#============================================
#     AVSRT Analysis - Visual Stimulation
#============================================

#loading needed toolboxes 
import mne
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy
import tkinter
import pandas as pd
from os.path import isfile
from tkinter import filedialog
import os
from pyprep.find_noisy_channels import NoisyChannels
from pyprep.prep_pipeline import PrepPipeline
import re

list_file = os.listdir('Z://Analysis/SFARI_Analysis/FAST/Theo/Epochs_EEG_Only/TD')
file_path = 'Z://Analysis/SFARI_Analysis/FAST/Theo/Epochs_EEG_Only/TD'

list_files_epochs = [s for s in list_file if '_EEG_epo' in s]
list_files_RT_TD = [s for s in list_file if '_RT_all' in s]
list_files_ET_TD = [s for s in list_file if '_ET_epo' in s]

# Initialize lists to store concatenated EEG epochs and RTs per participant
filtered_RT_lst_TD = []
filtered_epochs_lst_TD = []
percent_rejected_epochs = []

for i in range(len(list_files_epochs)):
    # Load EEG, ET, and RT files
    eeg_epochs = mne.read_epochs(file_path + "/" + list_files_epochs[i])
    et_epochs = mne.read_epochs(file_path + "/" + list_files_ET_TD[i])
    rt_data = pd.read_csv(file_path + "/" + list_files_RT_TD[i], sep='\t', encoding='utf-8')
    
    # Standardize channel names in ET epochs
    new_channel_names = {ch_name: re.sub(r'_(right|left)', '', ch_name) for ch_name in et_epochs.ch_names}
    et_epochs.rename_channels(new_channel_names)
    
    # Get gaze data and filter trials without blinks
    time_index = np.where(eeg_epochs.times == 0)[0][0]  # Index of t=0
    gaze_x_data = et_epochs.get_data(picks='xpos')
    gaze_y_data = et_epochs.get_data(picks='ypos')
    
    keep_indices = [j for j in range(gaze_x_data.shape[0]) 
                    if not np.isnan(gaze_x_data[j, 0, time_index]) 
                    and not np.isnan(gaze_y_data[j, 0, time_index])]
    
    filtered_epochs = eeg_epochs[keep_indices]
    filtered_rt = rt_data.iloc[keep_indices].reset_index(drop=True)
    
    percent_rejected_epochs.append(len(filtered_epochs)/len(eeg_epochs))
    
    filtered_RT_lst_TD.append(filtered_rt)
    filtered_epochs_lst_TD.append(filtered_epochs)
    
#%%

list_file = os.listdir('Z://Analysis/SFARI_Analysis/FAST/Theo/Epochs_EEG_Only/ASD')
file_path = 'Z://Analysis/SFARI_Analysis/FAST/Theo/Epochs_EEG_Only/ASD'

list_files_epochs_ASD = [s for s in list_file if '_EEG_epo' in s]
list_files_RT_ASD = [s for s in list_file if '_RT_all' in s]
list_files_ET_ASD = [s for s in list_file if '_ET_epo' in s]

# Initialize lists to store concatenated EEG epochs and RTs per participant
filtered_RT_lst_ASD = []
filtered_epochs_lst_ASD = []
percent_rejected_epochs_ASD = []

for i in range(len(list_files_epochs_ASD)):
    # Load EEG, ET, and RT files
    eeg_epochs = mne.read_epochs(file_path + "/" + list_files_epochs_ASD[i])
    et_epochs = mne.read_epochs(file_path + "/" + list_files_ET_ASD[i])
    rt_data = pd.read_csv(file_path + "/" + list_files_RT_ASD[i], sep='\t', encoding='utf-8')
    
    # Standardize channel names in ET epochs
    new_channel_names = {ch_name: re.sub(r'_(right|left)', '', ch_name) for ch_name in et_epochs.ch_names}
    et_epochs.rename_channels(new_channel_names)
    
    # Get gaze data and filter trials without blinks
    time_index = np.where(eeg_epochs.times == 0)[0][0]  # Index of t=0
    gaze_x_data = et_epochs.get_data(picks='xpos')
    gaze_y_data = et_epochs.get_data(picks='ypos')
    
    keep_indices = [j for j in range(gaze_x_data.shape[0]) 
                    if not np.isnan(gaze_x_data[j, 0, time_index]) 
                    and not np.isnan(gaze_y_data[j, 0, time_index])]
    
    filtered_epochs = eeg_epochs[keep_indices]
    filtered_rt = rt_data.iloc[keep_indices].reset_index(drop=True)
    
    percent_rejected_epochs_ASD.append(len(filtered_epochs)/len(eeg_epochs))
    
    filtered_RT_lst_ASD.append(filtered_rt)
    filtered_epochs_lst_ASD.append(filtered_epochs)
    
#%%

list_file = os.listdir('Z://Analysis/SFARI_Analysis/FAST/Theo/Epochs_EEG_Only/SIB')
file_path = 'Z://Analysis/SFARI_Analysis/FAST/Theo/Epochs_EEG_Only/SIB'

list_files_epochs_SIB = [s for s in list_file if '_EEG_epo' in s]
list_files_RT_SIB = [s for s in list_file if '_RT_all' in s]
list_files_ET_SIB = [s for s in list_file if '_ET_epo' in s]

# Initialize lists to store concatenated EEG epochs and RTs per participant
filtered_RT_lst_SIB = []
filtered_epochs_lst_SIB = []
percent_rejected_epochs_SIB = []

for i in range(len(list_files_epochs_SIB)):
    # Load EEG, ET, and RT files
    eeg_epochs = mne.read_epochs(file_path + "/" + list_files_epochs_SIB[i])
    et_epochs = mne.read_epochs(file_path + "/" + list_files_ET_SIB[i])
    rt_data = pd.read_csv(file_path + "/" + list_files_RT_SIB[i], sep='\t', encoding='utf-8')
    
    # Standardize channel names in ET epochs
    new_channel_names = {ch_name: re.sub(r'_(right|left)', '', ch_name) for ch_name in et_epochs.ch_names}
    et_epochs.rename_channels(new_channel_names)
    
    # Get gaze data and filter trials without blinks
    time_index = np.where(eeg_epochs.times == 0)[0][0]  # Index of t=0
    gaze_x_data = et_epochs.get_data(picks='xpos')
    gaze_y_data = et_epochs.get_data(picks='ypos')
    
    keep_indices = [j for j in range(gaze_x_data.shape[0]) 
                    if not np.isnan(gaze_x_data[j, 0, time_index]) 
                    and not np.isnan(gaze_y_data[j, 0, time_index])]
    
    filtered_epochs = eeg_epochs[keep_indices]
    filtered_rt = rt_data.iloc[keep_indices].reset_index(drop=True)
    
    percent_rejected_epochs_SIB.append(len(filtered_epochs)/len(eeg_epochs))
    
    filtered_RT_lst_SIB.append(filtered_rt)
    filtered_epochs_lst_SIB.append(filtered_epochs)
    
#%%
# Assuming you have 3 lists: filtered_RT_lst_ASD, filtered_RT_lst_TD, filtered_RT_lst_SIB

# For ASD group
for i, df in enumerate(filtered_RT_lst_ASD):
    df['Subject'] = list_files_RT_ASD[i][:5]  # Assign real subject number (first 5 characters) directly

# For TD group
for i, df in enumerate(filtered_RT_lst_TD):  # Continue numbering
    df['Subject'] = list_files_RT_TD[i][:5]  # Assign real subject number (first 5 characters)

# For SIB group
for i, df in enumerate(filtered_RT_lst_SIB):  # Continue numbering
    df['Subject'] = list_files_RT_SIB[i][:4]  # Assign real subject number (first 5 characters)

    
# Create a group label for each list
for df in filtered_RT_lst_ASD:
    df['Group'] = 'ASD'
for df in filtered_RT_lst_TD:
    df['Group'] = 'TD'
for df in filtered_RT_lst_SIB:
    df['Group'] = 'SIB'
    
#%%
# Concatenate all dataframes into one
df_combined = pd.concat([pd.concat(filtered_RT_lst_ASD),
                         pd.concat(filtered_RT_lst_TD),
                         pd.concat(filtered_RT_lst_SIB)])

# Check the combined dataframe
df_combined.head()

#%%

import pandas as pd
import numpy as np

# Step 1: Keep only RT-relevant trials
rt_event_ids = [121, 122, 131, 132]
df_rt_only = df_combined[df_combined['event_id'].isin(rt_event_ids)].copy()

# Step 2: Map each event_id to its corresponding RT column
event_to_rt_col = {
    121: 'face_shadow_RT',
    122: 'face_U_shadow_RT',
    131: 'obj_shadow_RT',
    132: 'obj_U_shadow_RT'
}

# Step 3: Create a new RT column by selecting the correct one for each row
def extract_rt(row):
    rt_col = event_to_rt_col.get(row['event_id'])
    return row[rt_col] if pd.notnull(rt_col) and pd.notnull(row[rt_col]) else np.nan

df_rt_only['RT'] = df_rt_only.apply(extract_rt, axis=1)

# Step 4: Group by Subject and event_id, and calculate mean RT
mean_rt = df_rt_only.groupby(['Subject', 'event_id'])['RT'].mean().reset_index()

# Step 5 (optional): Pivot for cleaner viewing
mean_rt_pivot = mean_rt.pivot(index='Subject', columns='event_id', values='RT')
mean_rt_pivot.columns = ['RT_121_face_shadow', 'RT_122_face_U_shadow', 'RT_131_obj_shadow', 'RT_132_obj_U_shadow']
mean_rt_pivot = mean_rt_pivot.reset_index()

# Display result
mean_rt_pivot

#%%

import pandas as pd
import numpy as np

# Step 1: Filter relevant event_ids
rt_event_ids = [121, 122, 131, 132]
df_rt_only = df_combined[df_combined['event_id'].isin(rt_event_ids)].copy()

# Step 2: Map each event_id to its corresponding RT column
event_to_rt_col = {
    121: 'face_shadow_RT',
    122: 'face_U_shadow_RT',
    131: 'obj_shadow_RT',
    132: 'obj_U_shadow_RT'
}

# Step 3: Extract correct RT value for each trial
def extract_rt(row):
    rt_col = event_to_rt_col.get(row['event_id'])
    return row[rt_col] if pd.notnull(rt_col) and pd.notnull(row[rt_col]) else np.nan

df_rt_only['RT'] = df_rt_only.apply(extract_rt, axis=1)

# Step 4: Group by Subject and event_id to get mean RT and count
agg_df = df_rt_only.groupby(['Subject', 'event_id'])['RT'].agg(['mean', 'count']).reset_index()

# Step 5: Pivot for wide-format dataframe
mean_rt_pivot = agg_df.pivot(index='Subject', columns='event_id', values='mean')
count_pivot = agg_df.pivot(index='Subject', columns='event_id', values='count')

# Step 6: Rename columns for clarity
mean_rt_pivot.columns = [f'MeanRT_{eid}' for eid in mean_rt_pivot.columns]
count_pivot.columns = [f'N_{eid}' for eid in count_pivot.columns]

# Step 7: Merge mean RT and count into a single dataframe
summary_df = pd.concat([mean_rt_pivot, count_pivot], axis=1).reset_index()

# Show result
summary_df

#%%
# Make sure Subject is a string so we can check its prefix
summary_df['Subject'] = summary_df['Subject'].astype(str)

# Define group based on prefix
def get_group(subject_id):
    if subject_id.startswith('10'):
        return 'TD'
    elif subject_id.startswith('11'):
        return 'ASD'
    elif subject_id.startswith('15'):
        return 'SIB'
    else:
        return 'Unknown'

# Apply the function to create 'Group' column
summary_df['Group'] = summary_df['Subject'].apply(get_group)

# Optional: move 'Group' column next to 'Subject'
cols = ['Subject', 'Group'] + [col for col in summary_df.columns if col not in ['Subject', 'Group']]
summary_df = summary_df[cols]

# Show result
summary_df

#%%

import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Melt the summary dataframe to long format
# Keep only RT columns
rt_cols = [col for col in summary_df.columns if col.startswith('MeanRT_')]
summary_long = summary_df.melt(
    id_vars=['Subject', 'Group'],
    value_vars=rt_cols,
    var_name='TrialType',
    value_name='RT'
)

# Step 2: Clean the 'TrialType' column for better labels
summary_long['TrialType'] = summary_long['TrialType'].str.replace('MeanRT_', '')
trial_type_labels = {
    '121': 'Face_Shadow',
    '122': 'Face_U_Shadow',
    '131': 'Obj_Shadow',
    '132': 'Obj_U_Shadow'
}
summary_long['TrialType'] = summary_long['TrialType'].map(trial_type_labels)

# Step 3: Plot grouped boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=summary_long, x='TrialType', y='RT', hue='Group')

plt.title('Reaction Times by Trial Type and Group')
plt.ylabel('Reaction Time (ms)')
plt.xlabel('Trial Type')
plt.legend(title='Group')
plt.tight_layout()
plt.show()

#%% Calculate ERP 

# Adjust the calculate_erp function to include the new baseline correction
def calculate_erp(filtered_epochs_lst, stim_type):
    erp_list = []
    number_stim = []

    # Loop through each subject's epochs
    for epochs in filtered_epochs_lst:
        # Select epochs based on stimulation type
        epochs.set_eeg_reference(ref_channels='average')
        epochs_stim = epochs[stim_type]
        
        # Calculate the ERP (mean across epochs)
        erp = epochs_stim.average()
        erp_list.append(erp)
        number_stim.append(len(epochs_stim))
    
    return erp_list, number_stim

# Calculate ERP for each group and stimulation type with the new baseline

# TD group
erp_face_TD, number_stim_face_TD = calculate_erp(filtered_epochs_lst_TD, 'face')
erp_face_ASD, number_stim_face_ASD = calculate_erp(filtered_epochs_lst_ASD, 'face')
erp_face_SIB, number_stim_face_SIB = calculate_erp(filtered_epochs_lst_SIB, 'face')

# erp_face_shadow_TD, number_stim_face_shadow_TD = calculate_erp(filtered_epochs_lst_TD, 'face_shadow')
# erp_face_shadow_ASD, number_stim_face_shadow_ASD = calculate_erp(filtered_epochs_lst_ASD, 'face_shadow')
# erp_face_shadow_SIB, number_stim_face_shadow_SIB = calculate_erp(filtered_epochs_lst_SIB, 'face_shadow')

erp_face_U_TD, number_stim_face_U_TD = calculate_erp(filtered_epochs_lst_TD, 'face_U')
erp_face_U_ASD, number_stim_face_U_ASD = calculate_erp(filtered_epochs_lst_ASD, 'face_U')
erp_face_U_SIB, number_stim_face_U_SIB = calculate_erp(filtered_epochs_lst_SIB, 'face_U')

# erp_face_U_shadow_TD, number_stim_face_U_shadow_TD = calculate_erp(filtered_epochs_lst_TD, 'face_U_shadow')
# erp_face_U_shadow_ASD, number_stim_face_U_shadow_ASD = calculate_erp(filtered_epochs_lst_ASD, 'face_U_shadow')
# erp_face_U_shadow_SIB, number_stim_face_U_shadow_SIB = calculate_erp(filtered_epochs_lst_SIB, 'face_U_shadow')

erp_obj_TD, number_stim_obj_TD = calculate_erp(filtered_epochs_lst_TD, 'obj')
erp_obj_ASD, number_stim_obj_ASD = calculate_erp(filtered_epochs_lst_ASD, 'obj')
erp_obj_SIB, number_stim_obj_SIB = calculate_erp(filtered_epochs_lst_SIB, 'obj')

# erp_obj_shadow_TD, number_stim_obj_shadow_TD = calculate_erp(filtered_epochs_lst_TD, 'obj_shadow')
# erp_obj_shadow_ASD, number_stim_obj_shadow_ASD = calculate_erp(filtered_epochs_lst_ASD, 'obj_shadow')
# erp_obj_shadow_SIB, number_stim_obj_shadow_SIB = calculate_erp(filtered_epochs_lst_SIB, 'obj_shadow')

erp_obj_U_TD, number_stim_obj_U_TD = calculate_erp(filtered_epochs_lst_TD, 'obj_U')
erp_obj_U_ASD, number_stim_obj_U_ASD = calculate_erp(filtered_epochs_lst_ASD, 'obj_U')
erp_obj_U_SIB, number_stim_obj_U_SIB = calculate_erp(filtered_epochs_lst_SIB, 'obj_U')

# erp_obj_U_shadow_TD, number_stim_obj_shadow_TD = calculate_erp(filtered_epochs_lst_TD, 'obj_U_shadow')
# erp_obj_U_shadow_ASD, number_stim_obj_shadow_ASD = calculate_erp(filtered_epochs_lst_ASD, 'obj_U_shadow')
# erp_obj_U_shadow_SIB, number_stim_obj_shadow_SIB = calculate_erp(filtered_epochs_lst_SIB, 'obj_U_shadow')

#%%

import pandas as pd

# Step 1: Combine counts for each group
# Make sure each list is of the same length (number of subjects in that group)

# TD group
df_TD = pd.DataFrame({
    'Group': 'TD',
    'N_121': number_stim_face_TD,
    'N_122': number_stim_face_U_TD,
    'N_131': number_stim_obj_TD,
    'N_132': number_stim_obj_U_TD
})

# ASD group
df_ASD = pd.DataFrame({
    'Group': 'ASD',
    'N_121': number_stim_face_ASD,
    'N_122': number_stim_face_U_ASD,
    'N_131': number_stim_obj_ASD,
    'N_132': number_stim_obj_U_ASD
})

# SIB group
df_SIB = pd.DataFrame({
    'Group': 'SIB',
    'N_121': number_stim_face_SIB,
    'N_122': number_stim_face_U_SIB,
    'N_131': number_stim_obj_SIB,
    'N_132': number_stim_obj_U_SIB
})

# Step 2: Concatenate all into one DataFrame
df_number_stim_all = pd.concat([df_TD, df_ASD, df_SIB], ignore_index=True)

# Display result
df_number_stim_all

#%% Plot topomap - face
Evoked_face_TD = mne.grand_average(erp_face_TD)
Evoked_face_ASD = mne.grand_average(erp_face_ASD)
Evoked_face_SIB = mne.grand_average(erp_face_SIB)

# Evoked_face_shadow_TD = mne.grand_average(erp_face_shadow_TD)
# Evoked_face_shadow_ASD = mne.grand_average(erp_face_shadow_ASD)
# Evoked_face_shadow_SIB = mne.grand_average(erp_face_shadow_SIB)

# times = [-0.05,0.12,0.170,0.250,0.31]  # Time in seconds

times = [-0.05,0.12]  # Time in seconds

Evoked_face_TD.plot_topomap(times=times, size=1, vlim=(0, 30), cmap='jet')
Evoked_face_ASD.plot_topomap(times=times, size=1, vlim=(5, 30), cmap='jet')
Evoked_face_SIB.plot_topomap(times=times, size=1, vlim=(5, 30), cmap='jet')

# Evoked_face_shadow_TD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
# Evoked_face_shadow_ASD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
# Evoked_face_shadow_SIB.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')

#%% save

plt.savefig('ERP_Topomap_Faces_SIB.svg')

#%% Plot ERP - between groups

import numpy as np
import matplotlib.pyplot as plt

# Function to average ERP over specific channels
def average_erp_channels(erp, channel_list):
    # Select the specified channels and average the ERP over these channels
    selected_channels = erp.copy().pick_channels(channel_list)
    avg_erp = np.mean(selected_channels.data, axis=0)  # Average over channels
    return avg_erp

tmin_epochs=-0.5
tmax_epochs=1.0

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate SEM (Standard Error of the Mean)
def calculate_sem(erp_list):
    erp_array = np.array([erp.data for erp in erp_list])  # Convert list of ERPs to a 2D array (n_subjects, n_timepoints)
    sem = np.std(erp_array, axis=0) / np.sqrt(erp_array.shape[0])  # SEM = std / sqrt(n_subjects)
    return sem

# Function to plot the average ERP with SEM for the three groups for a given stimulation type
def plot_avg_erp_with_sem(erp_TD, sem_TD, erp_ASD, sem_ASD, erp_SIB, sem_SIB, stim_type, channels, sfreq, plot_tmin=-0.1, plot_tmax=0.6):
    # Calculate time points based on the sampling frequency (sfreq)
    times = np.linspace(tmin_epochs, tmax_epochs, len(erp_TD))
    
    # Find the index range corresponding to the desired plot time window (-0.1 to 0.6 seconds)
    idx_min = np.searchsorted(times, plot_tmin)
    idx_max = np.searchsorted(times, plot_tmax)

    # Slice the ERP data, SEM, and time points for the plot time window
    times_plot = times[idx_min:idx_max]
    erp_TD_plot = erp_TD[idx_min:idx_max]
    sem_TD_plot = sem_TD[idx_min:idx_max]
    erp_ASD_plot = erp_ASD[idx_min:idx_max]
    sem_ASD_plot = sem_ASD[idx_min:idx_max]
    erp_SIB_plot = erp_SIB[idx_min:idx_max]
    sem_SIB_plot = sem_SIB[idx_min:idx_max]

    # Plotting the ERPs for the three groups with SEM shaded areas
    plt.figure(figsize=(10, 6))

    # TD group
    plt.plot(times_plot, erp_TD_plot, label='TD', color='blue')
    plt.fill_between(times_plot, erp_TD_plot - sem_TD_plot, erp_TD_plot + sem_TD_plot, color='blue', alpha=0.3)

    # ASD group
    plt.plot(times_plot, erp_ASD_plot, label='ASD', color='red')
    plt.fill_between(times_plot, erp_ASD_plot - sem_ASD_plot, erp_ASD_plot + sem_ASD_plot, color='red', alpha=0.3)

    # SIB group
    plt.plot(times_plot, erp_SIB_plot, label='SIB', color='green')
    plt.fill_between(times_plot, erp_SIB_plot - sem_SIB_plot, erp_SIB_plot + sem_SIB_plot, color='green', alpha=0.3)

    # Add title and labels
    plt.title(f'Average ERP with SEM for {stim_type} Stimulation ({", ".join(channels)})')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (µV)')
    plt.legend()
    plt.axvline(x=times_plot[12], color='black', linestyle='--')
    plt.ylim([-2e-6,22e-6])
    # plt.grid(True)
    plt.show()
    
#%% Plot ERP - within group

import numpy as np
import matplotlib.pyplot as plt

# Function to average ERP over specific channels
def average_erp_channels(erp, channel_list):
    # Select the specified channels and average the ERP over these channels
    selected_channels = erp.copy().pick_channels(channel_list)
    avg_erp = np.mean(selected_channels.data, axis=0)  # Average over channels
    return avg_erp

tmin_epochs=-0.5
tmax_epochs=1.0

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate SEM (Standard Error of the Mean)
def calculate_sem(erp_list):
    erp_array = np.array([erp.data for erp in erp_list])  # Convert list of ERPs to a 2D array (n_subjects, n_timepoints)
    sem = np.std(erp_array, axis=0) / np.sqrt(erp_array.shape[0])  # SEM = std / sqrt(n_subjects)
    return sem

# Function to plot the average ERP with SEM for the three groups for a given stimulation type
def plot_avg_erp_with_sem(erp_TD_face, sem_TD_face, erp_TD_U_face, sem_TD_U_face, 
                          erp_TD_obj, sem_TD_obj, erp_TD_U_obj, sem_TD_U_obj, group, channels, sfreq, plot_tmin=-0.1, plot_tmax=0.6):
    # Calculate time points based on the sampling frequency (sfreq)
    times = np.linspace(tmin_epochs, tmax_epochs, len(erp_TD_face))
    
    # Find the index range corresponding to the desired plot time window (-0.1 to 0.6 seconds)
    idx_min = np.searchsorted(times, plot_tmin)
    idx_max = np.searchsorted(times, plot_tmax)

    # Slice the ERP data, SEM, and time points for the plot time window
    times_plot = times[idx_min:idx_max]
    
    erp_TD_face_plot = erp_TD_face[idx_min:idx_max]
    sem_TD_face_plot = sem_TD_face[idx_min:idx_max]
    
    erp_TD_U_face_plot = erp_TD_U_face[idx_min:idx_max]
    sem_TD_U_face_plot = sem_TD_U_face[idx_min:idx_max]
    
    erp_TD_obj_plot = erp_TD_obj[idx_min:idx_max]
    sem_TD_obj_plot = sem_TD_obj[idx_min:idx_max]
    
    erp_TD_U_obj_plot = erp_TD_U_obj[idx_min:idx_max]
    sem_TD_U_obj_plot = sem_TD_U_obj[idx_min:idx_max]

    # Plotting the ERPs for the three groups with SEM shaded areas
    plt.figure(figsize=(10, 6))

    # TD group
    plt.plot(times_plot, erp_TD_face_plot, label='Faces', color='#b2182b')
    plt.fill_between(times_plot, erp_TD_face_plot - sem_TD_face_plot, erp_TD_face_plot + sem_TD_face_plot, color='#b2182b', alpha=0.3)

    # ASD group
    plt.plot(times_plot, erp_TD_U_face_plot, label='Inverted Faces', color='#ef8a62')
    plt.fill_between(times_plot, erp_TD_U_face_plot - sem_TD_U_face_plot, erp_TD_U_face_plot + sem_TD_U_face_plot, color='#ef8a62', alpha=0.3)

    # SIB group
    plt.plot(times_plot, erp_TD_obj_plot, label='Object', color='#2166ac')
    plt.fill_between(times_plot, erp_TD_obj_plot - sem_TD_obj_plot, erp_TD_obj_plot + sem_TD_obj_plot, color='#2166ac', alpha=0.3)
    
    # SIB group
    plt.plot(times_plot, erp_TD_U_obj_plot, label='Inverted Object', color='#67a9cf')
    plt.fill_between(times_plot, erp_TD_U_obj_plot - sem_TD_U_obj_plot, erp_TD_U_obj_plot + sem_TD_U_obj_plot, color='#67a9cf', alpha=0.3)

    # Add title and labels
    plt.title(f'Average ERP with SEM for {group} Stimulation ({", ".join(channels)})')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (µV)')
    plt.legend()
    plt.axvline(x=times_plot[12], color='black', linestyle='--')
    plt.ylim([-2e-6,30e-6])
    # plt.grid(True)
    # plt.xlim([0.05,0.175])
    plt.show()
    
#%% Plot ERP - within group with SHADOW ALL STIM TYPES

import numpy as np
import matplotlib.pyplot as plt

# Function to average ERP over specific channels
def average_erp_channels(erp, channel_list):
    # Select the specified channels and average the ERP over these channels
    selected_channels = erp.copy().pick_channels(channel_list)
    avg_erp = np.mean(selected_channels.data, axis=0)  # Average over channels
    return avg_erp

tmin_epochs=-0.5
tmax_epochs=1.0

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate SEM (Standard Error of the Mean)
def calculate_sem(erp_list):
    erp_array = np.array([erp.data for erp in erp_list])  # Convert list of ERPs to a 2D array (n_subjects, n_timepoints)
    sem = np.std(erp_array, axis=0) / np.sqrt(erp_array.shape[0])  # SEM = std / sqrt(n_subjects)
    return sem

# Function to plot the average ERP with SEM for the three groups for a given stimulation type
def plot_avg_erp_with_sem(erp_TD_face, sem_TD_face, 
                          erp_TD_shadow_face, sem_TD_shadow_face, 
                          erp_TD_U_face, sem_TD_U_face, 
                          erp_TD_shadow_U_face, sem_TD_shadow_U_face, 
                          erp_TD_obj, sem_TD_obj, 
                          erp_TD_shadow_obj, sem_TD_shadow_obj,
                          erp_TD_U_obj, sem_TD_U_obj, 
                          erp_TD_shadow_U_obj, sem_TD_shadow_U_obj, 
                          group, channels, sfreq, plot_tmin=-0.1, plot_tmax=0.6):
    # Calculate time points based on the sampling frequency (sfreq)
    times = np.linspace(tmin_epochs, tmax_epochs, len(erp_TD_face))
    
    # Find the index range corresponding to the desired plot time window (-0.1 to 0.6 seconds)
    idx_min = np.searchsorted(times, plot_tmin)
    idx_max = np.searchsorted(times, plot_tmax)

    # Slice the ERP data, SEM, and time points for the plot time window
    times_plot = times[idx_min:idx_max]
    
    erp_TD_face_plot = erp_TD_face[idx_min:idx_max]
    sem_TD_face_plot = sem_TD_face[idx_min:idx_max]
    
    erp_TD_face_shadow_plot = erp_TD_shadow_face[idx_min:idx_max]
    sem_TD_face_shadow_plot = sem_TD_shadow_face[idx_min:idx_max]
    
    erp_TD_U_face_plot = erp_TD_U_face[idx_min:idx_max]
    sem_TD_U_face_plot = sem_TD_U_face[idx_min:idx_max]
    
    erp_TD_shadow_U_face_plot = erp_TD_shadow_U_face[idx_min:idx_max]
    sem_TD_shadow_U_face_plot = sem_TD_shadow_U_face[idx_min:idx_max]
    
    erp_TD_obj_plot = erp_TD_obj[idx_min:idx_max]
    sem_TD_obj_plot = sem_TD_obj[idx_min:idx_max]
    
    erp_TD_shadow_obj_plot = erp_TD_shadow_obj[idx_min:idx_max]
    sem_TD_shadow_obj_plot = sem_TD_shadow_obj[idx_min:idx_max]
    
    erp_TD_U_obj_plot = erp_TD_U_obj[idx_min:idx_max]
    sem_TD_U_obj_plot = sem_TD_U_obj[idx_min:idx_max]
    
    erp_TD_shadow_U_obj_plot = erp_TD_shadow_U_obj[idx_min:idx_max]
    sem_TD_shadow_U_obj_plot = sem_TD_shadow_U_obj[idx_min:idx_max]

    # Plotting the ERPs for the three groups with SEM shaded areas
    plt.figure(figsize=(10, 6))

    # TD group
    plt.plot(times_plot, erp_TD_face_plot, label='Faces', color='#b2182b')
    plt.fill_between(times_plot, erp_TD_face_plot - sem_TD_face_plot, erp_TD_face_plot + sem_TD_face_plot, color='#b2182b', alpha=0.3)
    
    # TD group
    plt.plot(times_plot, erp_TD_face_shadow_plot, label='Shadow Faces', color='#b2182b',linestyle=':')
    plt.fill_between(times_plot, erp_TD_face_shadow_plot - sem_TD_face_shadow_plot, erp_TD_face_shadow_plot + sem_TD_face_shadow_plot, 
                     color='#b2182b', alpha=0.3)

    # ASD group
    plt.plot(times_plot, erp_TD_U_face_plot, label='Inverted face', color='#ef8a62')
    plt.fill_between(times_plot, erp_TD_U_face_plot - sem_TD_U_face_plot, erp_TD_U_face_plot + sem_TD_U_face_plot, color='#ef8a62', alpha=0.3)
    
    # ASD group
    plt.plot(times_plot, erp_TD_shadow_U_face_plot, label='Inverted face shadow', color='#ef8a62',linestyle=':')
    plt.fill_between(times_plot, erp_TD_shadow_U_face_plot - sem_TD_shadow_U_face_plot, erp_TD_shadow_U_face_plot + sem_TD_shadow_U_face_plot, 
                     color='#ef8a62', alpha=0.3)

    # SIB group
    plt.plot(times_plot, erp_TD_obj_plot, label='Object', color='#2166ac')
    plt.fill_between(times_plot, erp_TD_obj_plot - sem_TD_obj_plot, erp_TD_obj_plot + sem_TD_obj_plot, color='#2166ac', alpha=0.3)
    
    # SIB group
    plt.plot(times_plot, erp_TD_shadow_obj_plot, label='Shadow Object', color='#2166ac',linestyle=':')
    plt.fill_between(times_plot, erp_TD_shadow_obj_plot - sem_TD_shadow_obj_plot, erp_TD_shadow_obj_plot + sem_TD_shadow_obj_plot, 
                     color='#2166ac', alpha=0.3)
    
    # SIB group
    plt.plot(times_plot, erp_TD_shadow_U_obj_plot, label='Shadow Object', color='#67a9cf')
    plt.fill_between(times_plot, erp_TD_U_obj_plot - sem_TD_U_obj_plot, erp_TD_U_obj_plot + sem_TD_U_obj_plot, color='#67a9cf', alpha=0.3)
    
    # SIB group
    plt.plot(times_plot, erp_TD_shadow_U_obj_plot, label='Shadow Inverted Object', color='#67a9cf',linestyle=':')
    plt.fill_between(times_plot, erp_TD_shadow_U_obj_plot - sem_TD_shadow_U_obj_plot, erp_TD_shadow_U_obj_plot + sem_TD_shadow_U_obj_plot, 
                     color='#67a9cf', alpha=0.3)

    # Add title and labels
    plt.title(f'Average ERP with SEM for {group} Stimulation ({", ".join(channels)})')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (µV)')
    plt.legend()
    plt.axvline(x=times_plot[12], color='black', linestyle='--')
    plt.ylim([-2e-6,17e-6])
    # plt.grid(True)
    # plt.xlim([0.05,0.175])
    plt.show()
    
#%% Plot ERP - within group with SHADOW 

import numpy as np
import matplotlib.pyplot as plt

# Function to average ERP over specific channels
def average_erp_channels(erp, channel_list):
    # Select the specified channels and average the ERP over these channels
    selected_channels = erp.copy().pick_channels(channel_list)
    avg_erp = np.mean(selected_channels.data, axis=0)  # Average over channels
    return avg_erp

tmin_epochs=-0.5
tmax_epochs=1.0

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate SEM (Standard Error of the Mean)
def calculate_sem(erp_list):
    erp_array = np.array([erp.data for erp in erp_list])  # Convert list of ERPs to a 2D array (n_subjects, n_timepoints)
    sem = np.std(erp_array, axis=0) / np.sqrt(erp_array.shape[0])  # SEM = std / sqrt(n_subjects)
    return sem

# Function to plot the average ERP with SEM for the three groups for a given stimulation type
def plot_avg_erp_with_sem(erp_TD_face, sem_TD_face, erp_TD_U_face, sem_TD_U_face, 
                          erp_TD_obj, sem_TD_obj, erp_TD_U_obj, sem_TD_U_obj, group, channels, sfreq, plot_tmin=-0.1, plot_tmax=0.6):
    # Calculate time points based on the sampling frequency (sfreq)
    times = np.linspace(tmin_epochs, tmax_epochs, len(erp_TD_face))
    
    # Find the index range corresponding to the desired plot time window (-0.1 to 0.6 seconds)
    idx_min = np.searchsorted(times, plot_tmin)
    idx_max = np.searchsorted(times, plot_tmax)

    # Slice the ERP data, SEM, and time points for the plot time window
    times_plot = times[idx_min:idx_max]
    
    erp_TD_face_plot = erp_TD_face[idx_min:idx_max]
    sem_TD_face_plot = sem_TD_face[idx_min:idx_max]
    
    erp_TD_U_face_plot = erp_TD_U_face[idx_min:idx_max]
    sem_TD_U_face_plot = sem_TD_U_face[idx_min:idx_max]
    
    erp_TD_obj_plot = erp_TD_obj[idx_min:idx_max]
    sem_TD_obj_plot = sem_TD_obj[idx_min:idx_max]
    
    erp_TD_U_obj_plot = erp_TD_U_obj[idx_min:idx_max]
    sem_TD_U_obj_plot = sem_TD_U_obj[idx_min:idx_max]

    # Plotting the ERPs for the three groups with SEM shaded areas
    plt.figure(figsize=(10, 6))

    # TD group
    plt.plot(times_plot, erp_TD_face_plot, label='Faces', color='#b2182b')
    plt.fill_between(times_plot, erp_TD_face_plot - sem_TD_face_plot, erp_TD_face_plot + sem_TD_face_plot, color='#b2182b', alpha=0.3)

    # ASD group
    plt.plot(times_plot, erp_TD_U_face_plot, label='Shadow Faces', color='#ef8a62')
    plt.fill_between(times_plot, erp_TD_U_face_plot - sem_TD_U_face_plot, erp_TD_U_face_plot + sem_TD_U_face_plot, color='#ef8a62', alpha=0.3)

    # SIB group
    plt.plot(times_plot, erp_TD_obj_plot, label='Object', color='#2166ac')
    plt.fill_between(times_plot, erp_TD_obj_plot - sem_TD_obj_plot, erp_TD_obj_plot + sem_TD_obj_plot, color='#2166ac', alpha=0.3)
    
    # SIB group
    plt.plot(times_plot, erp_TD_U_obj_plot, label='Shadow Object', color='#67a9cf')
    plt.fill_between(times_plot, erp_TD_U_obj_plot - sem_TD_U_obj_plot, erp_TD_U_obj_plot + sem_TD_U_obj_plot, color='#67a9cf', alpha=0.3)

    # Add title and labels
    plt.title(f'Average ERP with SEM for {group} Stimulation ({", ".join(channels)})')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (µV)')
    plt.legend()
    plt.axvline(x=times_plot[12], color='black', linestyle='--')
    plt.ylim([-2e-6,17e-6])
    # plt.grid(True)
    # plt.xlim([0.05,0.175])
    plt.show()
    
#%% Plot ERP for TD

# visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# visual_channels = ['C1', 'Cz', 'C2', 'CP1', 'CPz', 'CP2']
# visual_channels = ['O1','O2']

visual_channels = ['P7','P8']

# visual_channels = ['Pz', 'CPz', 'P3', 'P4', 'POz']

# visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# visual_channels = ['O1',  'PO7', 'PO3']
# visual_channels = ['O2',  'PO8', 'PO4']
# visual_channels = ['F1',  'Fz', 'F2']

# visual_channels = ['FC1',  'FCz', 'FC2',
#                     'F1', 'Fz', 'F2']



# Visual ERP: Calculate and plot the average ERP with SEM for visual stimulation ('V')
avg_erp_face_TD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_TD], axis=0)
sem_erp_face_TD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_TD])

avg_erp_face_shadow_TD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_shadow_TD], axis=0)
sem_erp_face_shadow_TD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_shadow_TD])

avg_erp_U_face_TD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_U_TD], axis=0)
sem_erp_U_face_TD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_U_TD])

avg_erp_shadow_U_face_TD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_U_shadow_TD], axis=0)
sem_erp_shadow_U_face_TD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_U_shadow_TD])

avg_erp_obj_TD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_TD], axis=0)
sem_erp_obj_TD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_TD])

avg_erp_obj_shadow_TD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_shadow_TD], axis=0)
sem_erp_obj_shadow_TD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_shadow_TD])

avg_erp_U_obj_TD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_TD], axis=0)
sem_erp_U_obj_TD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_TD])

avg_erp_shadow_U_obj_TD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_shadow_TD], axis=0)
sem_erp_shadow_U_obj_TD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_shadow_TD])

# # Plot Visual ERP with SEM for -0.1 to 0.6 seconds
# plot_avg_erp_with_sem(avg_erp_face_TD, sem_erp_face_TD, avg_erp_U_face_TD, sem_erp_U_face_TD, 
#                       avg_erp_obj_TD, sem_erp_obj_TD, avg_erp_U_obj_TD, sem_erp_U_obj_TD, 'Faces',
#                       visual_channels, filtered_epochs_lst_TD[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)

# # Plot Visual ERP with SEM for -0.1 to 0.6 seconds
# plot_avg_erp_with_sem(avg_erp_face_TD, sem_erp_face_TD, avg_erp_face_shadow_TD, sem_erp_face_shadow_TD, 
#                       avg_erp_obj_TD, sem_erp_obj_TD, avg_erp_obj_shadow_TD, sem_erp_obj_shadow_TD, 'Faces',
#                       visual_channels, filtered_epochs_lst_TD[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)


plot_avg_erp_with_sem(avg_erp_face_TD, sem_erp_face_TD, 
                      avg_erp_face_shadow_TD, sem_erp_face_shadow_TD, 
                      avg_erp_U_face_TD, sem_erp_U_face_TD,
                      avg_erp_shadow_U_face_TD, sem_erp_shadow_U_face_TD,
                      avg_erp_obj_TD, sem_erp_obj_TD, 
                      avg_erp_obj_shadow_TD, sem_erp_obj_shadow_TD, 
                      avg_erp_U_obj_TD, sem_erp_U_obj_TD,
                      avg_erp_shadow_U_obj_TD, sem_erp_shadow_U_obj_TD,
                      'Faces',
                      visual_channels, filtered_epochs_lst_TD[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)

#%% Plot topomap - face
Evoked_face_TD = mne.grand_average(erp_face_TD)
Evoked_face_U_TD = mne.grand_average(erp_face_U_TD)

Evoked_obj_TD = mne.grand_average(erp_obj_TD)
Evoked_obj_U_TD = mne.grand_average(erp_obj_U_TD)

times = [-0.05,0.12,0.180,0.260,0.31,0.4,0.5]  # Time in seconds

Evoked_face_TD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
Evoked_face_U_TD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')

Evoked_obj_TD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
Evoked_obj_U_TD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')

#%%

from mne import combine_evoked

# Compute difference wave: Face - Inverted Face
# Evoked_diff_face = combine_evoked([Evoked_face_U_TD, Evoked_face_TD], weights=[1, -1])
Evoked_diff_face = combine_evoked([Evoked_face_TD, Evoked_obj_TD], weights=[1, -1])

# Define time points to plot
times = [-0.05, 0.135, 0.180, 0.240]  # seconds

# Plot topomap of the difference
Evoked_diff_face.plot_topomap(times=times, size=1, vlim=(-2, 2), cmap='RdBu_r')

#%%

from mne import combine_evoked

# Compute difference wave: Face - Inverted Face
# Evoked_diff_face_ASD = combine_evoked([Evoked_face_U_ASD, Evoked_face_ASD], weights=[1, -1])
Evoked_diff_face_ASD = combine_evoked([Evoked_face_ASD, Evoked_obj_ASD], weights=[1, -1])

# Define time points to plot
# times = [-0.05, 0.135, 0.180, 0.240]  # seconds
times = [-0.05, 0.100, 0.160, 0.220, 0.290]  # seconds

# Plot topomap of the difference
Evoked_diff_face_ASD.plot_topomap(times=times, size=1, vlim=(-4, 4), cmap='RdBu_r')

#%%

from mne import combine_evoked

# Compute difference wave: Face - Inverted Face
# Evoked_diff_face_SIB = combine_evoked([Evoked_face_U_SIB, Evoked_face_SIB], weights=[1, -1])
Evoked_diff_face_SIB = combine_evoked([Evoked_face_SIB, Evoked_obj_SIB], weights=[1, -1])

# Define time points to plot
# times = [-0.05, 0.135, 0.180, 0.240]  # seconds
times = [-0.05, 0.100, 0.160, 0.220, 0.290]  # seconds

# Plot topomap of the difference
Evoked_diff_face_SIB.plot_topomap(times=times, size=1, vlim=(-4, 4), cmap='RdBu_r')

#%%

from mne import combine_evoked

# Compute difference wave: Face - Inverted Face
Evoked_diff_face = combine_evoked([Evoked_face_TD, Evoked_obj_TD], weights=[1, -1])

# Define time points to plot
# times = [-0.05, 0.12, 0.180, 0.260, 0.31]  # seconds

times = [-0.05, 0.100, 0.160, 0.220, 0.290]  # seconds


# Plot topomap of the difference
Evoked_diff_face.plot_topomap(times=times, size=1, vlim=(-4, 4), cmap='RdBu_r')

#%% save

plt.savefig('ERP_Diff_Wave_F_minus_O_SIB.svg')

#%% Diff wave

visual_channels = ['P7']

# Compute difference wave per subject at the selected channels
# diff_erp_subjects = [
#     average_erp_channels(erp_u_face, visual_channels) - average_erp_channels(erp_face, visual_channels)
#     for erp_face, erp_u_face in zip(erp_face_TD, erp_face_U_TD)
# ]

# # Compute difference wave per subject at the selected channels
# diff_erp_subjects = [
#     average_erp_channels(erp_u_face, visual_channels) - average_erp_channels(erp_face, visual_channels)
#     for erp_face, erp_u_face in zip(erp_obj_TD, erp_face_TD)
# ]

# # Compute difference wave per subject at the selected channels
# diff_erp_subjects = [
#     average_erp_channels(erp_u_face, visual_channels) - average_erp_channels(erp_face, visual_channels)
#     for erp_face, erp_u_face in zip(erp_obj_TD, erp_obj_U_TD)
# ]

# Compute difference wave per subject at the selected channels
diff_erp_subjects = [
    average_erp_channels(erp_u_face, visual_channels) - average_erp_channels(erp_face, visual_channels)
    for erp_face, erp_u_face in zip(erp_face_SIB, erp_face_U_SIB)
]

import numpy as np

# Convert to array
diff_erp_subjects = np.array(diff_erp_subjects)

# Mean and SEM across subjects
avg_diff_erp = np.mean(diff_erp_subjects, axis=0)
sem_diff_erp = np.std(diff_erp_subjects, axis=0) / np.sqrt(len(diff_erp_subjects))

import matplotlib.pyplot as plt

# Time vector
sfreq = filtered_epochs_lst_TD[0].info['sfreq']
n_times = avg_diff_erp.shape[0]
# Extract time vector directly from ERP
times = erp_face_TD[0].times

# Plot
plt.figure(figsize=(10, 4))
plt.plot(times, avg_diff_erp, label='Inverted Face - Face', color='black')
plt.fill_between(times, avg_diff_erp - sem_diff_erp, avg_diff_erp + sem_diff_erp,
                 color='black', alpha=0.3)

plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.title(f'Difference ERP at {visual_channels}')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (µV)')
plt.legend()
plt.tight_layout()
plt.show()
plt.xlim([-0.1,0.6])
plt.ylim([-7.1e-6,4.5e-6])

#%%

# Define channels
chan_p8 = 'P8'
chan_p7 = 'P7'

# Define time window for N170 (in seconds)
n170_window = (0.170, 0.190)

# Find index of time window
tmin_idx = np.argmin(np.abs(times - n170_window[0]))
tmax_idx = np.argmin(np.abs(times - n170_window[1]))

# Initialize peak values per subject
n170_p8_peaks = []
n170_p7_peaks = []

for erp_face, erp_u_face in zip(erp_face_SIB, erp_face_U_SIB):
    # Get data for each channel (difference wave)
    diff_p8 = erp_u_face.copy().pick(chan_p8).data - erp_face.copy().pick(chan_p8).data
    diff_p7 = erp_u_face.copy().pick(chan_p7).data - erp_face.copy().pick(chan_p7).data
    
    # Extract min value (most negative) in the N170 time window
    min_p8 = np.min(diff_p8[0, tmin_idx:tmax_idx])
    min_p7 = np.min(diff_p7[0, tmin_idx:tmax_idx])
    
    # Append to lists
    n170_p8_peaks.append(min_p8)
    n170_p7_peaks.append(min_p7)
    
#%%

n170_p8_peaks = np.array(n170_p8_peaks)
n170_p7_peaks = np.array(n170_p7_peaks)

# Simple difference
li = n170_p8_peaks - n170_p7_peaks

li = li*1e6

#%% Cluster-based permutation test on the diff wave 

from mne.stats import permutation_cluster_1samp_test

times = erp_face_TD[0].times

plot_tmin = -0.1
plot_tmax = 0.6
# Find the index range corresponding to the desired plot time window
idx_min = np.searchsorted(times, plot_tmin)
idx_max = np.searchsorted(times, plot_tmax)

# Slice the ERP data, SEM, and time points for the plot time window
times_plot = times[idx_min:idx_max]

# Compute the difference per subject
X_diff = diff_erp_subjects[:,idx_min:idx_max]

# Run one-sample cluster permutation test (null: mean = 0)
T_obs, clusters, cluster_p_values, H0 = permutation_cluster_1samp_test(
    X_diff, n_permutations=1000, tail=0, threshold=None, out_type='mask', verbose=True
)

# Plot mean difference with significant clusters
plt.figure(figsize=(10, 5))
mean_diff = X_diff.mean(axis=0)
plt.plot(times_plot, mean_diff, label='P100 - P33', color='black')

# Highlight significant clusters
for i, cluster in enumerate(clusters):
    if cluster_p_values[i] < 0.05:
        cluster_inds = cluster
        plt.axvspan(times_plot[cluster_inds][0], times_plot[cluster_inds][-1],
                    color='gray', alpha=0.3)

plt.axhline(0, color='gray', linestyle='--')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Alpha Power Difference (a.u.)')
plt.title('Alpha Power: Difference P100 - P33 (Cluster Permutation, p < 0.05 shaded)')
plt.tight_layout()
plt.show()

#%% T-test permutation test 

from mne.stats import permutation_t_test
import numpy as np
import matplotlib.pyplot as plt

# Time window setup
times = erp_face_TD[0].times
plot_tmin = -0.1
plot_tmax = 0.6

idx_min = np.searchsorted(times, plot_tmin)
idx_max = np.searchsorted(times, plot_tmax)
times_plot = times[idx_min:idx_max]

# Data: shape (n_subjects, n_times)
X_diff = diff_erp_subjects[:, idx_min:idx_max]

# Run tmax permutation test (one-sample against 0)
p_values_tmax = permutation_t_test(
    X_diff, n_permutations=1000, tail=0, seed=42, n_jobs=1
)

# Plot
plt.figure(figsize=(10, 5))
mean_diff = X_diff.mean(axis=0)

plt.plot(times_plot, mean_diff, label='P100 - P33', color='black')

# Mark significant time points (p < 0.05)
significant_timepoints = p_values_tmax[1] < 0.05
plt.plot(times_plot[significant_timepoints], mean_diff[significant_timepoints],
         'o', color='red', label='p < 0.05 (tmax corrected)')

plt.axhline(0, color='gray', linestyle='--')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Alpha Power Difference (a.u.)')
plt.title('Alpha Power: Difference P100 - P33 (tmax Permutation Test)')
plt.tight_layout()
plt.show()

#%%

import numpy as np

# 150–250 ms window on your existing times_plot
win = (times_plot >= 0.150) & (times_plot <= 0.250)
if not np.any(win):
    raise ValueError("No samples found between 150–250 ms in times_plot.")

X_win = X_diff[:, win]           # (n_subjects, n_times_in_window)
t_win = times_plot[win]          # (n_times_in_window,)

# Per-subject minimum (peak) and latency
# Use nanargmin to tolerate NaNs; if an entire row is NaNs, handle separately
argmin_per_subj = np.nanargmin(X_win, axis=1)
peak_per_subj   = X_win[np.arange(X_win.shape[0]), argmin_per_subj] * 1e6
lat_per_subj    = t_win[argmin_per_subj]                    # seconds
lat_ms_per_subj = (lat_per_subj * 1000.0)                   # ms

# Optional: flag subjects with all-NaN in the window
all_nan_rows = np.isnan(X_win).all(axis=1)

# Group-mean minimum and latency (within 150–250 ms)
mean_trace = np.nanmean(X_win, axis=0)
idx_mean   = np.nanargmin(mean_trace)
group_peak = mean_trace[idx_mean]
group_lat  = t_win[idx_mean]         # seconds
group_lat_ms = group_lat * 1000.0    # ms

print(f"Group minimum: {group_peak:.4f} at {group_lat_ms:.1f} ms")
# peak_per_subj and lat_ms_per_subj hold per-subject values/latencies


#%% Spatio-temporal cluster test for the difference wave between inverted faces and face

import mne
import numpy as np
import matplotlib.pyplot as plt
from mne.stats import spatio_temporal_cluster_1samp_test

# Assuming you have lists of evoked data for each condition
evoked_audio_0 = erp_face_SIB  # Replace with your actual Evoked objects for condition 'Audio_0'
evoked_audio_1 = erp_obj_SIB  # Replace with your actual Evoked objects for condition 'Audio_1'

adjacency, ch_names = mne.channels.find_ch_adjacency(erp_face_TD[0].info, ch_type='eeg')

# Define the time window of interest
time_min = -0.1  # Start time
time_max = 0.6  # End time

# Find the indices corresponding to the time window of interest
time_indices = np.where((evoked_audio_0[0].times >= time_min) & (evoked_audio_0[0].times <= time_max))[0]

# Extract data for the specific time window
X_0 = np.array([evk.data[:, time_indices] for evk in evoked_audio_0])
X_1 = np.array([evk.data[:, time_indices] for evk in evoked_audio_1])

# Calculate the difference between the two conditions for each subject
difference = X_0 - X_1

difference = np.transpose(difference, (0, 2, 1))

# Perform the cluster-based permutation test on the difference from zero
# across both time and channel dimensions
T_obs, clusters, cluster_p_values, H0 = spatio_temporal_cluster_1samp_test(
    difference, adjacency=adjacency,n_permutations=1000, tail=0, threshold=None, out_type='mask'
)

T_plot = T_obs.T  # shape (n_channels, n_times)

# Get the channel names and times
ch_names = evoked_audio_0[0].info['ch_names']
times = evoked_audio_0[0].times[time_indices]  # Use the subset of times within the range
# times = evoked_audio_0[0].times
n_channels = len(ch_names)

# Create a mask for significant clusters (p < 0.05)
significant_mask = np.zeros(T_obs.shape, dtype=bool)
for i_clu, clu_p_value in enumerate(cluster_p_values):
    if clu_p_value < 0.01:
        significant_mask[clusters[i_clu]] = True

# # Plot the T-values with a mask for significant clusters
# fig, ax = plt.subplots(figsize=(12, 8))
# im = ax.imshow(T_plot, aspect='auto', origin='upper', cmap='RdBu_r', 
#                extent=[times[0], times[-1], 0, n_channels],
#                vmin=-np.max(np.abs(T_obs)), vmax=np.max(np.abs(T_obs)))
# plt.colorbar(im, ax=ax, label='T-value')

# Plot the T-values with a mask for significant clusters
fig, ax = plt.subplots(figsize=(12, 8))
im = ax.imshow(T_plot, aspect='auto', origin='upper', cmap='RdBu_r', 
               extent=[times[0], times[-1], 0, n_channels],
               vmin=-7, vmax=7)
plt.colorbar(im, ax=ax, label='T-value')
# Show actual channel names on the y-axis
ax.set_yticks(np.arange(len(ch_names)))
ax.set_yticklabels(ch_names[::-1])  # reverse the list

# Optional: make labels smaller if they overlap
ax.tick_params(axis='y', labelsize=5)

# Highlight significant clusters
ax.contour(significant_mask.T, levels=[0.5], colors='black', 
           linewidths=0.5, origin='upper', extent=[times[0], times[-1], 0, n_channels])

# Labeling the axes with 4 segments (adjusted to handle different channel counts)
num_segments = 4
segment_size = n_channels // num_segments
yticks = np.arange(segment_size // 2, n_channels, segment_size)

# Adjust yticklabels to match the actual number of yticks
yticklabels = [f'{start}-{min(end, n_channels)}' for start, end in 
               zip(range(0, n_channels, segment_size), 
                   range(segment_size, n_channels + segment_size, segment_size))]
yticklabels = yticklabels[:len(yticks)]  # Ensure matching lengths

# Apply yticks and yticklabels to the plot
ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Channels (Grouped)')
ax.set_title('Cluster Plot of T-values with Significant Clusters Highlighted')

plt.show()

# # Add topomaps
# for segment in range(num_segments):
#     start_idx = segment * segment_size
#     end_idx = (segment + 1) * segment_size
#     ax_topo = fig.add_axes([0.85, 0.1 + i * 0.2, 0.1, 0.2])  # now top-to-bottom aligns correctly
#     mask = np.zeros(n_channels, dtype=bool)
#     mask[start_idx:end_idx] = True
#     mask_params = dict(marker='o', markerfacecolor='r', markeredgecolor='r', linewidth=0)
#     mne.viz.plot_topomap(np.zeros(n_channels), evoked_audio_0[0].info, axes=ax_topo, show=False, mask=mask, mask_params=mask_params)
#     ax_topo.set_title(f'Channels {start_idx}-{end_idx}', fontsize=8)

# plt.show()

for i, segment in enumerate(reversed(range(num_segments))):
    start_idx = segment * segment_size
    end_idx = (segment + 1) * segment_size
    ax_topo = fig.add_axes([0.85, 0.1 + i * 0.2, 0.1, 0.2])  # now top-to-bottom aligns correctly
    
    mask = np.zeros(n_channels, dtype=bool)
    mask[start_idx:end_idx] = True
    mask_params = dict(marker='o', markerfacecolor='r', markeredgecolor='r', linewidth=0)
    
    mne.viz.plot_topomap(np.zeros(n_channels), evoked_audio_0[0].info, axes=ax_topo,
                         show=False, mask=mask, mask_params=mask_params)
    ax_topo.set_title(f'Channels {start_idx}-{end_idx}', fontsize=8)

#%% Plot ERP for ASD

# visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# visual_channels = ['C1', 'Cz', 'C2', 'CP1', 'CPz', 'CP2']
# visual_channels = ['O1','O2']
visual_channels = ['P7']

# visual_channels = ['Pz', 'CPz', 'P3', 'P4', 'POz']

# visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# visual_channels = ['O1',  'PO7', 'PO3']
# visual_channels = ['O2',  'PO8', 'PO4']
# visual_channels = ['F1',  'Fz', 'F2']


# Visual ERP: Calculate and plot the average ERP with SEM for visual stimulation ('V')
avg_erp_face_ASD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_ASD], axis=0)
sem_erp_face_ASD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_ASD])

# avg_erp_face_shadow_ASD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_shadow_ASD], axis=0)
# sem_erp_face_shadow_ASD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_shadow_ASD])

avg_erp_U_face_ASD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_U_ASD], axis=0)
sem_erp_U_face_ASD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_U_ASD])

avg_erp_shadow_U_face_ASD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_U_shadow_ASD], axis=0)
sem_erp_shadow_U_face_ASD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_U_shadow_ASD])

avg_erp_obj_ASD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_ASD], axis=0)
sem_erp_obj_ASD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_ASD])

avg_erp_obj_shadow_ASD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_shadow_ASD], axis=0)
sem_erp_obj_shadow_ASD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_shadow_ASD])

avg_erp_U_obj_ASD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_ASD], axis=0)
sem_erp_U_obj_ASD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_ASD])

avg_erp_shadow_U_obj_ASD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_shadow_ASD], axis=0)
sem_erp_shadow_U_obj_ASD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_shadow_ASD])

# # Plot Visual ERP with SEM for -0.1 to 0.6 seconds
# plot_avg_erp_with_sem(avg_erp_face_ASD, sem_erp_face_ASD, avg_erp_U_face_ASD, sem_erp_U_face_ASD, 
#                       avg_erp_obj_ASD, sem_erp_obj_ASD, avg_erp_U_obj_ASD, sem_erp_U_obj_ASD, 'Faces',
#                       visual_channels, filtered_epochs_lst_ASD[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)

# # Plot Visual ERP with SEM for -0.1 to 0.6 seconds
# plot_avg_erp_with_sem(avg_erp_face_ASD, sem_erp_face_ASD, avg_erp_face_shadow_ASD, sem_erp_face_shadow_ASD, 
#                       avg_erp_obj_ASD, sem_erp_obj_ASD, avg_erp_obj_shadow_ASD, sem_erp_obj_shadow_ASD, 'Faces',
#                       visual_channels, filtered_epochs_lst_ASD[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)


plot_avg_erp_with_sem(avg_erp_face_ASD, sem_erp_face_ASD, 
                      avg_erp_face_shadow_ASD, sem_erp_face_shadow_ASD, 
                      avg_erp_U_face_ASD, sem_erp_U_face_ASD,
                      avg_erp_shadow_U_face_ASD, sem_erp_shadow_U_face_ASD,
                      avg_erp_obj_ASD, sem_erp_obj_ASD, 
                      avg_erp_obj_shadow_ASD, sem_erp_obj_shadow_ASD, 
                      avg_erp_U_obj_ASD, sem_erp_U_obj_ASD,
                      avg_erp_shadow_U_obj_ASD, sem_erp_shadow_U_obj_ASD,
                      'Faces',
                      visual_channels, filtered_epochs_lst_ASD[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)

#%% Diff wave

# # Compute difference wave per subject at the selected channels
diff_erp_subjects = [
    average_erp_channels(erp_u_face, visual_channels) - average_erp_channels(erp_face, visual_channels)
    for erp_face, erp_u_face in zip(erp_face_ASD, erp_face_U_ASD)
]

# # Compute difference wave per subject at the selected channels
# diff_erp_subjects = [
#     average_erp_channels(erp_u_face, visual_channels) - average_erp_channels(erp_face, visual_channels)
#     for erp_face, erp_u_face in zip(erp_obj_ASD, erp_face_ASD)
# ]

# Compute difference wave per subject at the selected channels
# diff_erp_subjects = [
#     average_erp_channels(erp_u_face, visual_channels) - average_erp_channels(erp_face, visual_channels)
#     for erp_face, erp_u_face in zip(erp_obj_ASD, erp_obj_U_ASD)
# ]

import numpy as np

# Convert to array
diff_erp_subjects = np.array(diff_erp_subjects)

# Mean and SEM across subjects
avg_diff_erp = np.mean(diff_erp_subjects, axis=0)
sem_diff_erp = np.std(diff_erp_subjects, axis=0) / np.sqrt(len(diff_erp_subjects))

import matplotlib.pyplot as plt

# Time vector
sfreq = filtered_epochs_lst_TD[0].info['sfreq']
n_times = avg_diff_erp.shape[0]
# Extract time vector directly from ERP
times = erp_face_TD[0].times

# Plot
plt.figure(figsize=(10, 4))
plt.plot(times, avg_diff_erp, label='Inverted Face - Face', color='black')
plt.fill_between(times, avg_diff_erp - sem_diff_erp, avg_diff_erp + sem_diff_erp,
                 color='black', alpha=0.3)

plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.title(f'Difference ERP at {visual_channels}')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (µV)')
plt.legend()
plt.tight_layout()
plt.show()
plt.xlim([-0.1,0.6])
plt.ylim([-7.1e-6,4.5e-6])

#%% Plot topomap - face
Evoked_face_ASD = mne.grand_average(erp_face_ASD)
Evoked_face_U_ASD = mne.grand_average(erp_face_U_ASD)

Evoked_obj_ASD = mne.grand_average(erp_obj_ASD)
Evoked_obj_U_ASD = mne.grand_average(erp_obj_U_ASD)

times = [-0.05,0.12,0.180,0.260,0.31]  # Time in seconds

Evoked_face_ASD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
Evoked_face_U_ASD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')

Evoked_obj_ASD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
Evoked_obj_U_ASD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')

#%% save

plt.savefig('ERP_Topomap_Face_U_ASD.svg')


#%% Plot ERP for SIB

# visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# visual_channels = ['C1', 'Cz', 'C2', 'CP1', 'CPz', 'CP2']

visual_channels = ['P7','P8']
# visual_channels = ['P10']


# visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# visual_channels = ['O1',  'PO7', 'PO3']
# visual_channels = ['O2',  'PO8', 'PO4']
# visual_channels = ['F1',  'Fz', 'F2']


# Visual ERP: Calculate and plot the average ERP with SEM for visual stimulation ('V')
avg_erp_face_SIB = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_SIB], axis=0)
sem_erp_face_SIB = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_SIB])

avg_erp_face_shadow_SIB = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_shadow_SIB], axis=0)
sem_erp_face_shadow_SIB = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_shadow_SIB])

avg_erp_U_face_SIB = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_U_SIB], axis=0)
sem_erp_U_face_SIB = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_U_SIB])

avg_erp_shadow_U_face_SIB = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_U_shadow_SIB], axis=0)
sem_erp_shadow_U_face_SIB = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_U_shadow_SIB])

avg_erp_obj_SIB = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_SIB], axis=0)
sem_erp_obj_SIB = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_SIB])

avg_erp_obj_shadow_SIB = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_shadow_SIB], axis=0)
sem_erp_obj_shadow_SIB = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_shadow_SIB])

avg_erp_U_obj_SIB = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_SIB], axis=0)
sem_erp_U_obj_SIB = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_SIB])

avg_erp_shadow_U_obj_SIB = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_shadow_SIB], axis=0)
sem_erp_shadow_U_obj_SIB = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_shadow_SIB])

# # Plot Visual ERP with SEM for -0.1 to 0.6 seconds
# plot_avg_erp_with_sem(avg_erp_face_SIB, sem_erp_face_SIB, avg_erp_U_face_SIB, sem_erp_U_face_SIB, 
#                       avg_erp_obj_SIB, sem_erp_obj_SIB, avg_erp_U_obj_SIB, sem_erp_U_obj_SIB, 'Faces',
#                       visual_channels, filtered_epochs_lst_SIB[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)

# # Plot Visual ERP with SEM for -0.1 to 0.6 seconds
# plot_avg_erp_with_sem(avg_erp_face_SIB, sem_erp_face_SIB, avg_erp_face_shadow_SIB, sem_erp_face_shadow_SIB, 
#                       avg_erp_obj_SIB, sem_erp_obj_SIB, avg_erp_obj_shadow_SIB, sem_erp_obj_shadow_SIB, 'Faces',
#                       visual_channels, filtered_epochs_lst_SIB[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)


plot_avg_erp_with_sem(avg_erp_face_SIB, sem_erp_face_SIB, 
                      avg_erp_face_shadow_SIB, sem_erp_face_shadow_SIB, 
                      avg_erp_U_face_SIB, sem_erp_U_face_SIB,
                      avg_erp_shadow_U_face_SIB, sem_erp_shadow_U_face_SIB,
                      avg_erp_obj_SIB, sem_erp_obj_SIB, 
                      avg_erp_obj_shadow_SIB, sem_erp_obj_shadow_SIB, 
                      avg_erp_U_obj_SIB, sem_erp_U_obj_SIB,
                      avg_erp_shadow_U_obj_SIB, sem_erp_shadow_U_obj_SIB,
                      'Faces',
                      visual_channels, filtered_epochs_lst_SIB[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)

#%% Diff wave

# # Compute difference wave per subject at the selected channels
# diff_erp_subjects = [
#     average_erp_channels(erp_u_face, visual_channels) - average_erp_channels(erp_face, visual_channels)
#     for erp_face, erp_u_face in zip(erp_face_SIB, erp_face_U_SIB)
# ]

# # Compute difference wave per subject at the selected channels
# diff_erp_subjects = [
#     average_erp_channels(erp_u_face, visual_channels) - average_erp_channels(erp_face, visual_channels)
#     for erp_face, erp_u_face in zip(erp_obj_SIB, erp_face_SIB)
# ]

# Compute difference wave per subject at the selected channels
diff_erp_subjects = [
    average_erp_channels(erp_u_face, visual_channels) - average_erp_channels(erp_face, visual_channels)
    for erp_face, erp_u_face in zip(erp_obj_ASD, erp_obj_U_ASD)
]

import numpy as np

# Convert to array
diff_erp_subjects = np.array(diff_erp_subjects)

# Mean and SEM across subjects
avg_diff_erp = np.mean(diff_erp_subjects, axis=0)
sem_diff_erp = np.std(diff_erp_subjects, axis=0) / np.sqrt(len(diff_erp_subjects))

import matplotlib.pyplot as plt

# Time vector
sfreq = filtered_epochs_lst_TD[0].info['sfreq']
n_times = avg_diff_erp.shape[0]
# Extract time vector directly from ERP
times = erp_face_TD[0].times

# Plot
plt.figure(figsize=(10, 4))
plt.plot(times, avg_diff_erp, label='Inverted Face - Face', color='black')
plt.fill_between(times, avg_diff_erp - sem_diff_erp, avg_diff_erp + sem_diff_erp,
                 color='black', alpha=0.3)

plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.title(f'Difference ERP at {visual_channels}')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (µV)')
plt.legend()
plt.tight_layout()
plt.show()
plt.xlim([-0.1,0.6])
plt.ylim([-7.1e-6,4.5e-6])

#%% Plot topomap - face
Evoked_face_SIB = mne.grand_average(erp_face_SIB)
Evoked_face_U_SIB = mne.grand_average(erp_face_U_SIB)

Evoked_obj_SIB = mne.grand_average(erp_obj_SIB)
Evoked_obj_U_SIB = mne.grand_average(erp_obj_U_SIB)

times = [-0.05,0.12,0.180,0.260,0.31]  # Time in seconds

Evoked_face_SIB.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
Evoked_face_U_SIB.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')

Evoked_obj_SIB.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
Evoked_obj_U_SIB.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')

#%% save

plt.savefig('ERP_Topomap_Face_U_SIB.svg')

#%% Calculate P1 latency and amplitude for left cluster

def get_p1_peak(evoked_list, channel_names, tmin=0.07, tmax=0.20):
    latencies = []
    amplitudes = []

    for evoked in evoked_list:
        ch_indices = [evoked.ch_names.index(ch) for ch in channel_names]
        time_mask = (evoked.times >= tmin) & (evoked.times <= tmax)
        times = evoked.times[time_mask]
        data = evoked.data[ch_indices, :][:, time_mask]
        mean_data = data.mean(axis=0)

        if mean_data.size > 0:
            peak_idx = mean_data.argmax()
            latencies.append(times[peak_idx] * 1000)  # ms
            amplitudes.append(mean_data[peak_idx] * 1e6)  # µV
        else:
            latencies.append(np.nan)
            amplitudes.append(np.nan)

    return latencies, amplitudes

left_cluster = ['O1']
right_cluster = ['O2']


# For amplitude
# # TD Group
amp_face_TD_L = get_p1_peak(erp_face_TD, left_cluster)[1]
amp_face_TD_R = get_p1_peak(erp_face_TD, right_cluster)[1]
amp_face_U_TD_L = get_p1_peak(erp_face_U_TD, left_cluster)[1]
amp_face_U_TD_R = get_p1_peak(erp_face_U_TD, right_cluster)[1]
amp_obj_TD_L = get_p1_peak(erp_obj_TD, left_cluster)[1]
amp_obj_TD_R = get_p1_peak(erp_obj_TD, right_cluster)[1]
amp_obj_U_TD_L = get_p1_peak(erp_obj_U_TD, left_cluster)[1]
amp_obj_U_TD_R = get_p1_peak(erp_obj_U_TD, right_cluster)[1]

# ASD Group
amp_face_ASD_L = get_p1_peak(erp_face_ASD, left_cluster)[1]
amp_face_ASD_R = get_p1_peak(erp_face_ASD, right_cluster)[1]
amp_face_U_ASD_L = get_p1_peak(erp_face_U_ASD, left_cluster)[1]
amp_face_U_ASD_R = get_p1_peak(erp_face_U_ASD, right_cluster)[1]
amp_obj_ASD_L = get_p1_peak(erp_obj_ASD, left_cluster)[1]
amp_obj_ASD_R = get_p1_peak(erp_obj_ASD, right_cluster)[1]
amp_obj_U_ASD_L = get_p1_peak(erp_obj_U_ASD, left_cluster)[1]
amp_obj_U_ASD_R = get_p1_peak(erp_obj_U_ASD, right_cluster)[1]

# SIB Group
amp_face_SIB_L = get_p1_peak(erp_face_SIB, left_cluster)[1]
amp_face_SIB_R = get_p1_peak(erp_face_SIB, right_cluster)[1]
amp_face_U_SIB_L = get_p1_peak(erp_face_U_SIB, left_cluster)[1]
amp_face_U_SIB_R = get_p1_peak(erp_face_U_SIB, right_cluster)[1]
amp_obj_SIB_L = get_p1_peak(erp_obj_SIB, left_cluster)[1]
amp_obj_SIB_R = get_p1_peak(erp_obj_SIB, right_cluster)[1]
amp_obj_U_SIB_L = get_p1_peak(erp_obj_U_SIB, left_cluster)[1]
amp_obj_U_SIB_R = get_p1_peak(erp_obj_U_SIB, right_cluster)[1]

# For latency
# TD Group
amp_face_TD_L = get_p1_peak(erp_face_TD, left_cluster)[0]
amp_face_TD_R = get_p1_peak(erp_face_TD, right_cluster)[0]
amp_face_U_TD_L = get_p1_peak(erp_face_U_TD, left_cluster)[0]
amp_face_U_TD_R = get_p1_peak(erp_face_U_TD, right_cluster)[0]
amp_obj_TD_L = get_p1_peak(erp_obj_TD, left_cluster)[0]
amp_obj_TD_R = get_p1_peak(erp_obj_TD, right_cluster)[0]
amp_obj_U_TD_L = get_p1_peak(erp_obj_U_TD, left_cluster)[0]
amp_obj_U_TD_R = get_p1_peak(erp_obj_U_TD, right_cluster)[0]

# ASD Group
amp_face_ASD_L = get_p1_peak(erp_face_ASD, left_cluster)[0]
amp_face_ASD_R = get_p1_peak(erp_face_ASD, right_cluster)[0]
amp_face_U_ASD_L = get_p1_peak(erp_face_U_ASD, left_cluster)[0]
amp_face_U_ASD_R = get_p1_peak(erp_face_U_ASD, right_cluster)[0]
amp_obj_ASD_L = get_p1_peak(erp_obj_ASD, left_cluster)[0]
amp_obj_ASD_R = get_p1_peak(erp_obj_ASD, right_cluster)[0]
amp_obj_U_ASD_L = get_p1_peak(erp_obj_U_ASD, left_cluster)[0]
amp_obj_U_ASD_R = get_p1_peak(erp_obj_U_ASD, right_cluster)[0]

# SIB Group
amp_face_SIB_L = get_p1_peak(erp_face_SIB, left_cluster)[0]
amp_face_SIB_R = get_p1_peak(erp_face_SIB, right_cluster)[0]
amp_face_U_SIB_L = get_p1_peak(erp_face_U_SIB, left_cluster)[0]
amp_face_U_SIB_R = get_p1_peak(erp_face_U_SIB, right_cluster)[0]
amp_obj_SIB_L = get_p1_peak(erp_obj_SIB, left_cluster)[0]
amp_obj_SIB_R = get_p1_peak(erp_obj_SIB, right_cluster)[0]
amp_obj_U_SIB_L = get_p1_peak(erp_obj_U_SIB, left_cluster)[0]
amp_obj_U_SIB_R = get_p1_peak(erp_obj_U_SIB, right_cluster)[0]


def make_df(amplitudes, condition, cluster, group):
    return pd.DataFrame({
        'Amplitude (µV)': amplitudes,
        'Condition': condition,
        'Cluster': cluster,
        'Group': group
    })

# Concatenate all into one dataframe
df_all = pd.concat([
    # TD
    make_df(amp_face_TD_L, 'Face', 'Left', 'TD'),
    make_df(amp_face_TD_R, 'Face', 'Right', 'TD'),
    make_df(amp_face_U_TD_L, 'Inverted Face', 'Left', 'TD'),
    make_df(amp_face_U_TD_R, 'Inverted Face', 'Right', 'TD'),
    make_df(amp_obj_TD_L, 'Object', 'Left', 'TD'),
    make_df(amp_obj_TD_R, 'Object', 'Right', 'TD'),
    make_df(amp_obj_U_TD_L, 'Inverted Object', 'Left', 'TD'),
    make_df(amp_obj_U_TD_R, 'Inverted Object', 'Right', 'TD'),

    # ASD
    make_df(amp_face_ASD_L, 'Face', 'Left', 'ASD'),
    make_df(amp_face_ASD_R, 'Face', 'Right', 'ASD'),
    make_df(amp_face_U_ASD_L, 'Inverted Face', 'Left', 'ASD'),
    make_df(amp_face_U_ASD_R, 'Inverted Face', 'Right', 'ASD'),
    make_df(amp_obj_ASD_L, 'Object', 'Left', 'ASD'),
    make_df(amp_obj_ASD_R, 'Object', 'Right', 'ASD'),
    make_df(amp_obj_U_ASD_L, 'Inverted Object', 'Left', 'ASD'),
    make_df(amp_obj_U_ASD_R, 'Inverted Object', 'Right', 'ASD'),

    # SIB
    make_df(amp_face_SIB_L, 'Face', 'Left', 'SIB'),
    make_df(amp_face_SIB_R, 'Face', 'Right', 'SIB'),
    make_df(amp_face_U_SIB_L, 'Inverted Face', 'Left', 'SIB'),
    make_df(amp_face_U_SIB_R, 'Inverted Face', 'Right', 'SIB'),
    make_df(amp_obj_SIB_L, 'Object', 'Left', 'SIB'),
    make_df(amp_obj_SIB_R, 'Object', 'Right', 'SIB'),
    make_df(amp_obj_U_SIB_L, 'Inverted Object', 'Left', 'SIB'),
    make_df(amp_obj_U_SIB_R, 'Inverted Object', 'Right', 'SIB'),
], ignore_index=True)

#%% 

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 6))
sns.boxplot(x='Condition', y='Amplitude (µV)', hue='Group', data=df_all, palette='Set2')
sns.despine()
plt.title('P1 Amplitudes by Condition, Hemisphere, and Group')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#%%

g = sns.catplot(
    data=df_all,
    x='Condition',
    y='Amplitude (µV)',
    hue='Group',
    col='Cluster',
    kind='box',
    height=5,
    aspect=1.2,
    palette='Set2'
)
g.fig.suptitle('P1 Latency by Condition, Cluster, and Group', y=1.05)
g.set_xticklabels(rotation=45)
plt.tight_layout()

#%%

Stats = np.concatenate([amp_face_TD_L , amp_face_ASD_L, amp_face_SIB_L,
                        amp_face_U_TD_L , amp_face_U_ASD_L, amp_face_U_SIB_L,
                        amp_obj_TD_L , amp_obj_ASD_L, amp_obj_SIB_L,
                        amp_obj_U_TD_L , amp_obj_U_ASD_L, amp_obj_U_SIB_L,
                        amp_face_TD_R , amp_face_ASD_R, amp_face_SIB_R,
                        amp_face_U_TD_R , amp_face_U_ASD_R, amp_face_U_SIB_R,
                        amp_obj_TD_R , amp_obj_ASD_R, amp_obj_SIB_R,
                        amp_obj_U_TD_R , amp_obj_U_ASD_R, amp_obj_U_SIB_R])

#%% Plot one boxplot per group

import matplotlib.pyplot as plt

# Data (example for TD group)
data = [lat_face_TD, lat_face_U_TD, lat_obj_TD, lat_obj_U_TD]
labels = ['Faces', 'Inverted Faces', 'Object', 'Inverted Object']
colors = ['#b2182b', '#ef8a62', '#2166ac', '#67a9cf']

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 4))

# Plot each box manually to apply colors
for i, (y, label, color) in enumerate(zip(data, labels, colors), start=1):
    bp = ax.boxplot(y, positions=[i], patch_artist=True, widths=0.6,
                    boxprops=dict(facecolor=color, color=color),
                    capprops=dict(color=color),
                    whiskerprops=dict(color=color),
                    flierprops=dict(markerfacecolor=color, marker='o', markersize=4, linestyle='none'),
                    medianprops=dict(color='black'))
    
# Set x-axis labels and other formatting
ax.set_xticks(range(1, 5))
ax.set_xticklabels(labels)
ax.set_ylabel('P1 Latency at P8 (ms)')
ax.set_title('P1 Latency in TD Group')
plt.tight_layout()
plt.show()

#%% Plot one boxplot for all groups

import matplotlib.pyplot as plt

# --- Organize data: 6 for faces, 6 for objects ---
data = [
    lat_face_TD, lat_face_ASD, lat_face_SIB,                # Faces
    lat_face_U_TD, lat_face_U_ASD, lat_face_U_SIB,          # Inverted Faces
    lat_obj_TD, lat_obj_ASD, lat_obj_SIB,                   # Objects
    lat_obj_U_TD, lat_obj_U_ASD, lat_obj_U_SIB              # Inverted Objects
]

# Corresponding group + condition labels
x_labels = [
    'Faces\nTD', 'Faces\nASD', 'Faces\nSIB',
    'Inv. Faces\nTD', 'Inv. Faces\nASD', 'Inv. Faces\nSIB',
    'Object\nTD', 'Object\nASD', 'Object\nSIB',
    'Inv. Object\nTD', 'Inv. Object\nASD', 'Inv. Object\nSIB'
]

# Matching colors (same color per condition across groups)
colors = [
    '#b2182b', '#b2182b', '#b2182b',       # Faces
    '#ef8a62', '#ef8a62', '#ef8a62',       # Inverted Faces
    '#2166ac', '#2166ac', '#2166ac',       # Object
    '#67a9cf', '#67a9cf', '#67a9cf'        # Inverted Object
]

# --- Plotting ---
fig, ax = plt.subplots(figsize=(12, 5))

for i, (y, label, color) in enumerate(zip(data, x_labels, colors), start=1):
    ax.boxplot(y, positions=[i], patch_artist=True, widths=0.6,
               boxprops=dict(facecolor=color, color=color),
               capprops=dict(color=color),
               whiskerprops=dict(color=color),
               flierprops=dict(markerfacecolor=color, marker='o', markersize=4, linestyle='none'),
               medianprops=dict(color='black'))

# Add group labels and vertical separators
ax.set_xticks(range(1, 13))
ax.set_xticklabels(x_labels, rotation=45, ha='right')

ax.set_ylabel('P1 Latency at P8 (ms)')
ax.set_title('P1 Latency Across Conditions and Groups')
ax.axvline(6.5, color='gray', linestyle='--', lw=1)  # Separator between face and object
ax.text(3.5, ax.get_ylim()[1], 'Faces', ha='center', va='bottom', fontsize=10, weight='bold')
ax.text(9.5, ax.get_ylim()[1], 'Objects', ha='center', va='bottom', fontsize=10, weight='bold')

ax.grid(axis='y')
plt.tight_layout()
plt.show()

#%% Calculate the amplitude of the N170 


# With Peak-to-peak amplitude
# def get_n170_latency_and_ptp(evoked_list, channel_names=['P7', 'PO7', 'O1'], 
#                              p1_window=(0.05, 0.18), n170_window=(0.13, 0.26)):
#     n170_latencies = []
#     ptp_amplitudes = []

#     for evoked in evoked_list:
#         ch_indices = [evoked.ch_names.index(ch) for ch in channel_names]
#         times = evoked.times

#         # --- P1 ---
#         p1_mask = (times >= p1_window[0]) & (times <= p1_window[1])
#         p1_data = evoked.data[ch_indices][:, p1_mask].mean(axis=0)
#         p1_times = times[p1_mask]

#         # --- N170 ---
#         n170_mask = (times >= n170_window[0]) & (times <= n170_window[1])
#         n170_data = evoked.data[ch_indices][:, n170_mask].mean(axis=0)
#         n170_times = times[n170_mask]

#         if p1_data.size > 0 and n170_data.size > 0:
#             p1_idx = p1_data.argmax()
#             n170_idx = n170_data.argmin()

#             p1_amp = p1_data[p1_idx] * 1e6  # µV
#             n170_amp = n170_data[n170_idx] * 1e6  # µV
#             n170_latency = n170_times[n170_idx] * 1000  # ms

#             ptp_amp = p1_amp - n170_amp  # µV

#             n170_latencies.append(n170_latency)
#             ptp_amplitudes.append(ptp_amp)
#         else:
#             n170_latencies.append(np.nan)
#             ptp_amplitudes.append(np.nan)

#     return n170_latencies, ptp_amplitudes


# Direct calcul of N170 amplitude

def get_n170_latency_and_ptp(evoked_list, channel_names=['P7', 'PO7', 'O1'], n170_window=(0.17, 0.23)):
    n170_latencies = []
    n170_amplitudes = []

    for evoked in evoked_list:
        ch_indices = [evoked.ch_names.index(ch) for ch in channel_names]
        times = evoked.times

        # --- N170 ---
        n170_mask = (times >= n170_window[0]) & (times <= n170_window[1])
        n170_data = evoked.data[ch_indices][:, n170_mask].mean(axis=0)
        n170_times = times[n170_mask]

        if n170_data.size > 0:
            n170_idx = n170_data.argmin()
            n170_amp = n170_data[n170_idx] * 1e6  # µV
            n170_latency = n170_times[n170_idx] * 1000  # ms

            n170_amplitudes.append(n170_amp)
            n170_latencies.append(n170_latency)
        else:
            n170_amplitudes.append(np.nan)
            n170_latencies.append(np.nan)

    return n170_latencies, n170_amplitudes



# Define clusters
left_cluster = ['P7']
right_cluster = ['P8']

# TD Group
n170_face_TD_L, ptp_face_TD_L = get_n170_latency_and_ptp(erp_face_TD, left_cluster)
n170_face_TD_R, ptp_face_TD_R = get_n170_latency_and_ptp(erp_face_TD, right_cluster)
n170_face_U_TD_L, ptp_face_U_TD_L = get_n170_latency_and_ptp(erp_face_U_TD, left_cluster)
n170_face_U_TD_R, ptp_face_U_TD_R = get_n170_latency_and_ptp(erp_face_U_TD, right_cluster)
n170_obj_TD_L, ptp_obj_TD_L = get_n170_latency_and_ptp(erp_obj_TD, left_cluster)
n170_obj_TD_R, ptp_obj_TD_R = get_n170_latency_and_ptp(erp_obj_TD, right_cluster)
n170_obj_U_TD_L, ptp_obj_U_TD_L = get_n170_latency_and_ptp(erp_obj_U_TD, left_cluster)
n170_obj_U_TD_R, ptp_obj_U_TD_R = get_n170_latency_and_ptp(erp_obj_U_TD, right_cluster)

# ASD Group
n170_face_ASD_L, ptp_face_ASD_L = get_n170_latency_and_ptp(erp_face_ASD, left_cluster)
n170_face_ASD_R, ptp_face_ASD_R = get_n170_latency_and_ptp(erp_face_ASD, right_cluster)
n170_face_U_ASD_L, ptp_face_U_ASD_L = get_n170_latency_and_ptp(erp_face_U_ASD, left_cluster)
n170_face_U_ASD_R, ptp_face_U_ASD_R = get_n170_latency_and_ptp(erp_face_U_ASD, right_cluster)
n170_obj_ASD_L, ptp_obj_ASD_L = get_n170_latency_and_ptp(erp_obj_ASD, left_cluster)
n170_obj_ASD_R, ptp_obj_ASD_R = get_n170_latency_and_ptp(erp_obj_ASD, right_cluster)
n170_obj_U_ASD_L, ptp_obj_U_ASD_L = get_n170_latency_and_ptp(erp_obj_U_ASD, left_cluster)
n170_obj_U_ASD_R, ptp_obj_U_ASD_R = get_n170_latency_and_ptp(erp_obj_U_ASD, right_cluster)

# SIB Group
n170_face_SIB_L, ptp_face_SIB_L = get_n170_latency_and_ptp(erp_face_SIB, left_cluster)
n170_face_SIB_R, ptp_face_SIB_R = get_n170_latency_and_ptp(erp_face_SIB, right_cluster)
n170_face_U_SIB_L, ptp_face_U_SIB_L = get_n170_latency_and_ptp(erp_face_U_SIB, left_cluster)
n170_face_U_SIB_R, ptp_face_U_SIB_R = get_n170_latency_and_ptp(erp_face_U_SIB, right_cluster)
n170_obj_SIB_L, ptp_obj_SIB_L = get_n170_latency_and_ptp(erp_obj_SIB, left_cluster)
n170_obj_SIB_R, ptp_obj_SIB_R = get_n170_latency_and_ptp(erp_obj_SIB, right_cluster)
n170_obj_U_SIB_L, ptp_obj_U_SIB_L = get_n170_latency_and_ptp(erp_obj_U_SIB, left_cluster)
n170_obj_U_SIB_R, ptp_obj_U_SIB_R = get_n170_latency_and_ptp(erp_obj_U_SIB, right_cluster)

#%% N170 Amplitude with shadow stimulus for right and left cortex

import numpy as np
import pandas as pd

# -------------------------------
# Function to extract N170 latency & amplitude
# -------------------------------
def get_n170_latency_and_amp(evoked_list, channel, n170_window=(0.170, 0.230)):
    latencies = []
    amplitudes = []

    for evoked in evoked_list:
        times = evoked.times
        ch_idx = evoked.ch_names.index(channel)

        # Time mask for N170 window
        mask = (times >= n170_window[0]) & (times <= n170_window[1])
        if not np.any(mask):
            latencies.append(np.nan)
            amplitudes.append(np.nan)
            continue

        data = evoked.data[ch_idx, mask]
        t_window = times[mask]

        # Minimum (most negative) value in the window
        min_idx = np.argmin(data)
        min_val = data[min_idx] * 1e6  # Convert to µV
        min_time = t_window[min_idx] * 1000  # Convert to ms

        latencies.append(min_time)
        amplitudes.append(min_val)

    return latencies, amplitudes

# -------------------------------
# N170 settings
# -------------------------------
left_chan = 'P7'
right_chan = 'P8'
n170_window = (0.170, 0.230)

# -------------------------------
# Results dictionary
# -------------------------------
results = {}

def process_condition(group, stim_type, erp_list):
    condition_name = f"{stim_type}"
    results[(group, condition_name)] = {
        'Left_Latency': None,
        'Left_Amplitude': None,
        'Right_Latency': None,
        'Right_Amplitude': None
    }
    lat_L, amp_L = get_n170_latency_and_amp(erp_list, left_chan, n170_window)
    lat_R, amp_R = get_n170_latency_and_amp(erp_list, right_chan, n170_window)
    results[(group, condition_name)]['Left_Latency'] = lat_L
    results[(group, condition_name)]['Left_Amplitude'] = amp_L
    results[(group, condition_name)]['Right_Latency'] = lat_R
    results[(group, condition_name)]['Right_Amplitude'] = amp_R

# -------------------------------
# Process all groups & conditions
# -------------------------------

stim_conditions = [
    ('face', erp_face_TD, erp_face_ASD, erp_face_SIB),
    ('face_shadow', erp_face_shadow_TD, erp_face_shadow_ASD, erp_face_shadow_SIB),
    ('face_U', erp_face_U_TD, erp_face_U_ASD, erp_face_U_SIB),
    ('face_U_shadow', erp_face_U_shadow_TD, erp_face_U_shadow_ASD, erp_face_U_shadow_SIB),
    ('obj', erp_obj_TD, erp_obj_ASD, erp_obj_SIB),
    ('obj_shadow', erp_obj_shadow_TD, erp_obj_shadow_ASD, erp_obj_shadow_SIB),
    ('obj_U', erp_obj_U_TD, erp_obj_U_ASD, erp_obj_U_SIB),
    ('obj_U_shadow', erp_obj_U_shadow_TD, erp_obj_U_shadow_ASD, erp_obj_U_shadow_SIB)
]

groups = ['TD', 'ASD', 'SIB']

for stim_type, td_list, asd_list, sib_list in stim_conditions:
    process_condition('TD', stim_type, td_list)
    process_condition('ASD', stim_type, asd_list)
    process_condition('SIB', stim_type, sib_list)

# -------------------------------
# Convert results to DataFrame
# -------------------------------
df_rows = []
for (group, condition), vals in results.items():
    n = len(vals['Left_Latency'])
    for i in range(n):
        df_rows.append({
            'Group': group,
            'Condition': condition,
            'Subject': i + 1,
            'Left_Latency_ms': vals['Left_Latency'][i],
            'Left_Amplitude_uV': vals['Left_Amplitude'][i],
            'Right_Latency_ms': vals['Right_Latency'][i],
            'Right_Amplitude_uV': vals['Right_Amplitude'][i]
        })

df_n170 = pd.DataFrame(df_rows)

# ✅ Save to Excel
df_n170.to_excel('N170_amplitude_latency_all_conditions.xlsx', index=False)
print(df_n170.head())

#%% N170 amplitude for a cluster of channel 

import numpy as np
import pandas as pd

# -------------------------------
# Function to extract N170 latency & amplitude for a cluster
# -------------------------------
def get_n170_latency_and_amp(evoked_list, channels, n170_window=(0.170, 0.230)):
    latencies = []
    amplitudes = []

    for evoked in evoked_list:
        times = evoked.times

        # Get indices for the cluster channels
        ch_indices = [evoked.ch_names.index(ch) for ch in channels]

        # Time mask for N170 window
        mask = (times >= n170_window[0]) & (times <= n170_window[1])
        if not np.any(mask):
            latencies.append(np.nan)
            amplitudes.append(np.nan)
            continue

        # Average signal across cluster channels
        data = evoked.data[ch_indices, :][:, mask].mean(axis=0)
        t_window = times[mask]

        # Minimum (most negative) value in the window
        min_idx = np.argmin(data)
        min_val = data[min_idx] * 1e6  # Convert to µV
        min_time = t_window[min_idx] * 1000  # Convert to ms

        latencies.append(min_time)
        amplitudes.append(min_val)

    return latencies, amplitudes

# -------------------------------
# N170 settings
# -------------------------------
cluster_channels = ['P7', 'P8']  # Cluster of interest
n170_window = (0.170, 0.230)

# -------------------------------
# Results dictionary
# -------------------------------
results = {}

def process_condition(group, stim_type, erp_list):
    condition_name = f"{stim_type}"
    results[(group, condition_name)] = {
        'Latency': None,
        'Amplitude': None
    }
    lat, amp = get_n170_latency_and_amp(erp_list, cluster_channels, n170_window)
    results[(group, condition_name)]['Latency'] = lat
    results[(group, condition_name)]['Amplitude'] = amp

# -------------------------------
# Process all groups & conditions
# -------------------------------
stim_conditions = [
    ('face', erp_face_TD, erp_face_ASD, erp_face_SIB),
    ('face_shadow', erp_face_shadow_TD, erp_face_shadow_ASD, erp_face_shadow_SIB),
    ('face_U', erp_face_U_TD, erp_face_U_ASD, erp_face_U_SIB),
    ('face_U_shadow', erp_face_U_shadow_TD, erp_face_U_shadow_ASD, erp_face_U_shadow_SIB),
    ('obj', erp_obj_TD, erp_obj_ASD, erp_obj_SIB),
    ('obj_shadow', erp_obj_shadow_TD, erp_obj_shadow_ASD, erp_obj_shadow_SIB),
    ('obj_U', erp_obj_U_TD, erp_obj_U_ASD, erp_obj_U_SIB),
    ('obj_U_shadow', erp_obj_U_shadow_TD, erp_obj_U_shadow_ASD, erp_obj_U_shadow_SIB)
]

groups = ['TD', 'ASD', 'SIB']

for stim_type, td_list, asd_list, sib_list in stim_conditions:
    process_condition('TD', stim_type, td_list)
    process_condition('ASD', stim_type, asd_list)
    process_condition('SIB', stim_type, sib_list)

# -------------------------------
# Convert results to DataFrame
# -------------------------------
df_rows = []
for (group, condition), vals in results.items():
    n = len(vals['Latency'])
    for i in range(n):
        df_rows.append({
            'Group': group,
            'Condition': condition,
            'Subject': i + 1,
            'Cluster': 'P7-P8',
            'Latency_ms': vals['Latency'][i],
            'Amplitude_uV': vals['Amplitude'][i]
        })

df_n170 = pd.DataFrame(df_rows)

# ✅ Save to Excel
df_n170.to_excel('N170_amplitude_latency_cluster_P7P8.xlsx', index=False)
print(df_n170.head())

#%% Boxplot of the result for all the conditions

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataframe (or use df_n170 from previous step)
df = df_n170

# Set up the figure
plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")

# Create a boxplot
sns.boxplot(x='Condition', y='Amplitude_uV', hue='Group', data=df, palette='Set2')

# Add swarmplot for individual points (optional)
sns.stripplot(x='Condition', y='Amplitude_uV', hue='Group', data=df, 
              dodge=True, color='k', alpha=0.4)

# Titles and labels
plt.title('N170 Amplitude (µV) across Conditions and Groups', fontsize=14)
plt.ylabel('Amplitude (µV)', fontsize=12)
plt.xlabel('Condition', fontsize=12)

# Adjust legend
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[:3], labels[:3], title='Group', loc='upper right')

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

#%% Boxplot to highlight the face effect for both clear and shadow stimuli

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataframe
df = df_n170

# ✅ Filter the conditions of interest
selected_conditions = ['obj', 'face', 'obj_shadow', 'face_shadow']
df_filtered = df[df['Condition'].isin(selected_conditions)].copy()

# ✅ Reorder conditions for plotting
condition_order = ['obj', 'face', 'obj_shadow', 'face_shadow']
df_filtered['Condition'] = pd.Categorical(df_filtered['Condition'], categories=condition_order, ordered=True)

# ✅ Create a boxplot
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

sns.boxplot(x='Condition', y='Amplitude_uV', hue='Group', data=df_filtered, palette='Set2')

# Add individual data points for visibility
sns.stripplot(x='Condition', y='Amplitude_uV', hue='Group', data=df_filtered, 
              dodge=True, color='k', alpha=0.4)

# ✅ Adjust legend (remove duplicates)
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[:3], labels[:3], title='Group', loc='upper right')

# ✅ Titles and labels
plt.title('N170 Amplitude (µV): Faces vs Objects (+ Shadows)', fontsize=14)
plt.ylabel('Amplitude (µV)', fontsize=12)
plt.xlabel('Condition', fontsize=12)
plt.xticks(rotation=0)

# ✅ Add space between object/face and shadow conditions
# Insert a vertical line between face and obj_shadow for visual grouping
plt.axvline(1.5, color='gray', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()


#%% Difference wave between clear and shadow stimuli - SOCIAL

import numpy as np
import matplotlib.pyplot as plt
import mne

# --- Helper functions ---
def combine_evokeds(list1, list2):
    """Average two lists of Evoked objects element-wise."""
    return [mne.combine_evoked([ev1, ev2], weights='equal') for ev1, ev2 in zip(list1, list2)]

def compute_diff(clear_list, shadow_list):
    """Compute difference wave (clear - shadow) for a list of subjects."""
    return [mne.combine_evoked([clear, shadow], weights=[1, -1]) for clear, shadow in zip(clear_list, shadow_list)]

def extract_data(evokeds, channels):
    """Extract channel data from list of Evokeds into array (n_subjects, n_channels, n_times)."""
    n_subj = len(evokeds)
    n_ch = len(channels)
    n_times = len(evokeds[0].times)
    data = np.zeros((n_subj, n_ch, n_times))
    for i, ev in enumerate(evokeds):
        data[i] = ev.copy().pick(channels).data
    return data

# --- Combine conditions for each group ---
erp_clear_TD = combine_evokeds(erp_face_TD, erp_face_U_TD)
erp_shadow_TD = combine_evokeds(erp_face_shadow_TD, erp_face_U_shadow_TD)
erp_clear_ASD = combine_evokeds(erp_face_ASD, erp_face_U_ASD)
erp_shadow_ASD = combine_evokeds(erp_face_shadow_ASD, erp_face_U_shadow_ASD)
erp_clear_SIB = combine_evokeds(erp_face_SIB, erp_face_U_SIB)
erp_shadow_SIB = combine_evokeds(erp_face_shadow_SIB, erp_face_U_shadow_SIB)

# Compute difference waves per subject
erp_diff_TD = compute_diff(erp_clear_TD, erp_shadow_TD)
erp_diff_ASD = compute_diff(erp_clear_ASD, erp_shadow_ASD)
erp_diff_SIB = compute_diff(erp_clear_SIB, erp_shadow_SIB)

# Channels of interest
channels = ['O1','PO7', 'O2','PO8']
times = erp_diff_TD[0].times * 1000  # ms

# Extract data
data_TD = extract_data(erp_diff_TD, channels) * 1e6  # Convert to µV
data_ASD = extract_data(erp_diff_ASD, channels) * 1e6
data_SIB = extract_data(erp_diff_SIB, channels) * 1e6

# Compute mean and SEM
mean_TD = data_TD.mean(axis=0)
sem_TD = data_TD.std(axis=0) / np.sqrt(data_TD.shape[0])
mean_ASD = data_ASD.mean(axis=0)
sem_ASD = data_ASD.std(axis=0) / np.sqrt(data_ASD.shape[0])
mean_SIB = data_SIB.mean(axis=0)
sem_SIB = data_SIB.std(axis=0) / np.sqrt(data_SIB.shape[0])

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {'TD': 'blue', 'ASD': 'red', 'SIB': 'green'}

for idx, ch in enumerate(channels):
    plt.subplot(2, 1, idx + 1)

    # TD
    plt.plot(times, mean_TD[idx], color=colors['TD'], label='TD')
    plt.fill_between(times, mean_TD[idx]-sem_TD[idx], mean_TD[idx]+sem_TD[idx], color=colors['TD'], alpha=0.3)

    # ASD
    plt.plot(times, mean_ASD[idx], color=colors['ASD'], label='ASD')
    plt.fill_between(times, mean_ASD[idx]-sem_ASD[idx], mean_ASD[idx]+sem_ASD[idx], color=colors['ASD'], alpha=0.3)

    # SIB
    plt.plot(times, mean_SIB[idx], color=colors['SIB'], label='SIB')
    plt.fill_between(times, mean_SIB[idx]-sem_SIB[idx], mean_SIB[idx]+sem_SIB[idx], color=colors['SIB'], alpha=0.3)

    plt.axvline(0, color='k', linestyle='--')
    plt.axhline(0, color='k', linewidth=0.5)
    plt.title(f'Difference Wave (Clear - Shadow) at {ch}')
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude (µV)')
    plt.xlim([-100,600])
    if idx == 0:
        plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()

#%% difference wave for a cluster of channel

import numpy as np
import matplotlib.pyplot as plt
import mne

# --- Helper functions ---
def combine_evokeds(list1, list2):
    """Average two lists of Evoked objects element-wise."""
    return [mne.combine_evoked([ev1, ev2], weights='equal') for ev1, ev2 in zip(list1, list2)]

def compute_diff(clear_list, shadow_list):
    """Compute difference wave (clear - shadow) for a list of subjects."""
    return [mne.combine_evoked([clear, shadow], weights=[1, -1]) for clear, shadow in zip(clear_list, shadow_list)]

def extract_data(evokeds, channels):
    """Extract channel data from list of Evokeds into array (n_subjects, n_times), averaged across channels."""
    n_subj = len(evokeds)
    n_times = len(evokeds[0].times)
    data = np.zeros((n_subj, n_times))
    for i, ev in enumerate(evokeds):
        data[i] = ev.copy().pick(channels).data.mean(axis=0)
    return data

# --- Combine conditions for each group ---
erp_clear_TD = combine_evokeds(erp_face_TD, erp_face_U_TD)
erp_shadow_TD = combine_evokeds(erp_face_shadow_TD, erp_face_U_shadow_TD)
erp_clear_ASD = combine_evokeds(erp_face_ASD, erp_face_U_ASD)
erp_shadow_ASD = combine_evokeds(erp_face_shadow_ASD, erp_face_U_shadow_ASD)
erp_clear_SIB = combine_evokeds(erp_face_SIB, erp_face_U_SIB)
erp_shadow_SIB = combine_evokeds(erp_face_shadow_SIB, erp_face_U_shadow_SIB)

# Compute difference waves per subject
erp_diff_TD = compute_diff(erp_clear_TD, erp_shadow_TD)
erp_diff_ASD = compute_diff(erp_clear_ASD, erp_shadow_ASD)
erp_diff_SIB = compute_diff(erp_clear_SIB, erp_shadow_SIB)

# Channels of interest
channels = ['O1', 'PO7', 'O2', 'PO8']
times = erp_diff_TD[0].times * 1000  # ms

# Extract data averaged across channels
data_TD = extract_data(erp_diff_TD, channels) * 1e6  # µV
data_ASD = extract_data(erp_diff_ASD, channels) * 1e6
data_SIB = extract_data(erp_diff_SIB, channels) * 1e6

# Compute mean and SEM across subjects
mean_TD = data_TD.mean(axis=0)
sem_TD = data_TD.std(axis=0) / np.sqrt(data_TD.shape[0])
mean_ASD = data_ASD.mean(axis=0)
sem_ASD = data_ASD.std(axis=0) / np.sqrt(data_ASD.shape[0])
mean_SIB = data_SIB.mean(axis=0)
sem_SIB = data_SIB.std(axis=0) / np.sqrt(data_SIB.shape[0])

# --- Plot grand average difference wave with SEM ---
plt.figure(figsize=(10, 6))
colors = {'TD': 'blue', 'ASD': 'red', 'SIB': 'green'}

# TD
plt.plot(times, mean_TD, color=colors['TD'], label='TD')
plt.fill_between(times, mean_TD - sem_TD, mean_TD + sem_TD, color=colors['TD'], alpha=0.3)

# ASD
plt.plot(times, mean_ASD, color=colors['ASD'], label='ASD')
plt.fill_between(times, mean_ASD - sem_ASD, mean_ASD + sem_ASD, color=colors['ASD'], alpha=0.3)

# SIB
plt.plot(times, mean_SIB, color=colors['SIB'], label='SIB')
plt.fill_between(times, mean_SIB - sem_SIB, mean_SIB + sem_SIB, color=colors['SIB'], alpha=0.3)

# Reference lines
plt.axvline(0, color='k', linestyle='--')
plt.axhline(0, color='k', linewidth=0.5)
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude (µV)')
plt.title('Difference Wave (Clear - Shadow), Averaged Across Channels')
plt.xlim([-100, 600])
plt.legend()
# plt.grid(True)
plt.tight_layout()
plt.show()


#%%

import numpy as np
import matplotlib.pyplot as plt
import mne

# Times of interest in ms
times_of_interest = [-50, 110, 150, 240, 350]  # ms

# Compute grand-average difference wave for each group
grand_diff_TD = mne.grand_average(erp_diff_TD)
grand_diff_ASD = mne.grand_average(erp_diff_ASD)
grand_diff_SIB = mne.grand_average(erp_diff_SIB)

# Create a figure for each group
groups = {'TD': grand_diff_TD, 'ASD': grand_diff_ASD, 'SIB': grand_diff_SIB}

for group_name, evoked in groups.items():
    fig = evoked.plot_topomap(
        times=np.array(times_of_interest) / 1000.0,  # Convert ms to s
        scalings=1e6,  # Convert to µV
        units='µV',
        time_unit='s',
        cmap='RdBu_r',  # Red/Blue colormap
        outlines='head',
        size=3,
        vlim = (-6,6)
    )
    plt.show()

#%% save

plt.savefig('Topomap_Diff_wave_Clear_Shadow_SIB_nonsocial.svg')

#%% Difference wave between clear and shadow stimuli - NON-SOCIAL

import numpy as np
import matplotlib.pyplot as plt
import mne

# --- Combine conditions for each group ---
erp_clear_TD = combine_evokeds(erp_obj_TD, erp_obj_U_TD)
erp_shadow_TD = combine_evokeds(erp_obj_shadow_TD, erp_obj_U_shadow_TD)
erp_clear_ASD = combine_evokeds(erp_obj_ASD, erp_obj_U_ASD)
erp_shadow_ASD = combine_evokeds(erp_obj_shadow_ASD, erp_obj_U_shadow_ASD)
erp_clear_SIB = combine_evokeds(erp_obj_SIB, erp_obj_U_SIB)
erp_shadow_SIB = combine_evokeds(erp_obj_shadow_SIB, erp_obj_U_shadow_SIB)

# Compute difference waves per subject
erp_diff_TD = compute_diff(erp_clear_TD, erp_shadow_TD)
erp_diff_ASD = compute_diff(erp_clear_ASD, erp_shadow_ASD)
erp_diff_SIB = compute_diff(erp_clear_SIB, erp_shadow_SIB)

# Channels of interest
channels = ['P7', 'P8']
times = erp_diff_TD[0].times * 1000  # ms

# Extract data
data_TD = extract_data(erp_diff_TD, channels) * 1e6  # Convert to µV
data_ASD = extract_data(erp_diff_ASD, channels) * 1e6
data_SIB = extract_data(erp_diff_SIB, channels) * 1e6

# Compute mean and SEM
mean_TD = data_TD.mean(axis=0)
sem_TD = data_TD.std(axis=0) / np.sqrt(data_TD.shape[0])
mean_ASD = data_ASD.mean(axis=0)
sem_ASD = data_ASD.std(axis=0) / np.sqrt(data_ASD.shape[0])
mean_SIB = data_SIB.mean(axis=0)
sem_SIB = data_SIB.std(axis=0) / np.sqrt(data_SIB.shape[0])

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {'TD': 'blue', 'ASD': 'red', 'SIB': 'green'}

for idx, ch in enumerate(channels):
    plt.subplot(2, 1, idx + 1)

    # TD
    plt.plot(times, mean_TD[idx], color=colors['TD'], label='TD')
    plt.fill_between(times, mean_TD[idx]-sem_TD[idx], mean_TD[idx]+sem_TD[idx], color=colors['TD'], alpha=0.3)

    # ASD
    plt.plot(times, mean_ASD[idx], color=colors['ASD'], label='ASD')
    plt.fill_between(times, mean_ASD[idx]-sem_ASD[idx], mean_ASD[idx]+sem_ASD[idx], color=colors['ASD'], alpha=0.3)

    # SIB
    plt.plot(times, mean_SIB[idx], color=colors['SIB'], label='SIB')
    plt.fill_between(times, mean_SIB[idx]-sem_SIB[idx], mean_SIB[idx]+sem_SIB[idx], color=colors['SIB'], alpha=0.3)

    plt.axvline(0, color='k', linestyle='--')
    plt.axhline(0, color='k', linewidth=0.5)
    plt.title(f'Difference Wave (Clear - Shadow) at {ch}')
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude (µV)')
    if idx == 0:
        plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()

#%% difference wave for a cluster of channel

import numpy as np
import matplotlib.pyplot as plt
import mne

# --- Helper functions ---
def combine_evokeds(list1, list2):
    """Average two lists of Evoked objects element-wise."""
    return [mne.combine_evoked([ev1, ev2], weights='equal') for ev1, ev2 in zip(list1, list2)]

def compute_diff(clear_list, shadow_list):
    """Compute difference wave (clear - shadow) for a list of subjects."""
    return [mne.combine_evoked([clear, shadow], weights=[1, -1]) for clear, shadow in zip(clear_list, shadow_list)]

def extract_data(evokeds, channels):
    """Extract channel data from list of Evokeds into array (n_subjects, n_times), averaged across channels."""
    n_subj = len(evokeds)
    n_times = len(evokeds[0].times)
    data = np.zeros((n_subj, n_times))
    for i, ev in enumerate(evokeds):
        data[i] = ev.copy().pick(channels).data.mean(axis=0)
    return data

# --- Combine conditions for each group ---
erp_clear_TD = combine_evokeds(erp_obj_TD, erp_obj_U_TD)
erp_shadow_TD = combine_evokeds(erp_obj_shadow_TD, erp_obj_U_shadow_TD)
erp_clear_ASD = combine_evokeds(erp_obj_ASD, erp_obj_U_ASD)
erp_shadow_ASD = combine_evokeds(erp_obj_shadow_ASD, erp_obj_U_shadow_ASD)
erp_clear_SIB = combine_evokeds(erp_obj_SIB, erp_obj_U_SIB)
erp_shadow_SIB = combine_evokeds(erp_obj_shadow_SIB, erp_obj_U_shadow_SIB)

# Compute difference waves per subject
erp_diff_TD = compute_diff(erp_clear_TD, erp_shadow_TD)
erp_diff_ASD = compute_diff(erp_clear_ASD, erp_shadow_ASD)
erp_diff_SIB = compute_diff(erp_clear_SIB, erp_shadow_SIB)

# Channels of interest
channels = ['O1', 'PO7', 'O2', 'PO8']
times = erp_diff_TD[0].times * 1000  # ms

# Extract data averaged across channels
data_TD = extract_data(erp_diff_TD, channels) * 1e6  # µV
data_ASD = extract_data(erp_diff_ASD, channels) * 1e6
data_SIB = extract_data(erp_diff_SIB, channels) * 1e6

# Compute mean and SEM across subjects
mean_TD = data_TD.mean(axis=0)
sem_TD = data_TD.std(axis=0) / np.sqrt(data_TD.shape[0])
mean_ASD = data_ASD.mean(axis=0)
sem_ASD = data_ASD.std(axis=0) / np.sqrt(data_ASD.shape[0])
mean_SIB = data_SIB.mean(axis=0)
sem_SIB = data_SIB.std(axis=0) / np.sqrt(data_SIB.shape[0])

# --- Plot grand average difference wave with SEM ---
plt.figure(figsize=(10, 6))
colors = {'TD': 'blue', 'ASD': 'red', 'SIB': 'green'}

# TD
plt.plot(times, mean_TD, color=colors['TD'], label='TD')
plt.fill_between(times, mean_TD - sem_TD, mean_TD + sem_TD, color=colors['TD'], alpha=0.3)

# ASD
plt.plot(times, mean_ASD, color=colors['ASD'], label='ASD')
plt.fill_between(times, mean_ASD - sem_ASD, mean_ASD + sem_ASD, color=colors['ASD'], alpha=0.3)

# SIB
plt.plot(times, mean_SIB, color=colors['SIB'], label='SIB')
plt.fill_between(times, mean_SIB - sem_SIB, mean_SIB + sem_SIB, color=colors['SIB'], alpha=0.3)

# Reference lines
plt.axvline(0, color='k', linestyle='--')
plt.axhline(0, color='k', linewidth=0.5)
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude (µV)')
plt.title('Difference Wave (Clear - Shadow), Averaged Across Channels')
plt.xlim([-100, 600])
plt.legend()
# plt.grid(True)
plt.tight_layout()
plt.show()

#%%

def make_df(values, measure, condition, cluster, group):
    return pd.DataFrame({
        'Value': values,
        'Measure': measure,
        'Condition': condition,
        'Cluster': cluster,
        'Group': group
    })

# Combine both latency and peak-to-peak amplitude
df_n170 = pd.concat([
    # TD
    make_df(n170_face_TD_L, 'Latency (ms)', 'Face', 'Left', 'TD'),
    make_df(n170_face_TD_R, 'Latency (ms)', 'Face', 'Right', 'TD'),
    make_df(n170_face_U_TD_L, 'Latency (ms)', 'Inverted Face', 'Left', 'TD'),
    make_df(n170_face_U_TD_R, 'Latency (ms)', 'Inverted Face', 'Right', 'TD'),
    make_df(n170_obj_TD_L, 'Latency (ms)', 'Object', 'Left', 'TD'),
    make_df(n170_obj_TD_R, 'Latency (ms)', 'Object', 'Right', 'TD'),
    make_df(n170_obj_U_TD_L, 'Latency (ms)', 'Inverted Object', 'Left', 'TD'),
    make_df(n170_obj_U_TD_R, 'Latency (ms)', 'Inverted Object', 'Right', 'TD'),
    
    # ASD
    make_df(n170_face_ASD_L, 'Latency (ms)', 'Face', 'Left', 'ASD'),
    make_df(n170_face_ASD_R, 'Latency (ms)', 'Face', 'Right', 'ASD'),
    make_df(n170_face_U_ASD_L, 'Latency (ms)', 'Inverted Face', 'Left', 'ASD'),
    make_df(n170_face_U_ASD_R, 'Latency (ms)', 'Inverted Face', 'Right', 'ASD'),
    make_df(n170_obj_ASD_L, 'Latency (ms)', 'Object', 'Left', 'ASD'),
    make_df(n170_obj_ASD_R, 'Latency (ms)', 'Object', 'Right', 'ASD'),
    make_df(n170_obj_U_ASD_L, 'Latency (ms)', 'Inverted Object', 'Left', 'ASD'),
    make_df(n170_obj_U_ASD_R, 'Latency (ms)', 'Inverted Object', 'Right', 'ASD'),
    
    # SIB
    make_df(n170_face_SIB_L, 'Latency (ms)', 'Face', 'Left', 'SIB'),
    make_df(n170_face_SIB_R, 'Latency (ms)', 'Face', 'Right', 'SIB'),
    make_df(n170_face_U_SIB_L, 'Latency (ms)', 'Inverted Face', 'Left', 'SIB'),
    make_df(n170_face_U_SIB_R, 'Latency (ms)', 'Inverted Face', 'Right', 'SIB'),
    make_df(n170_obj_SIB_L, 'Latency (ms)', 'Object', 'Left', 'SIB'),
    make_df(n170_obj_SIB_R, 'Latency (ms)', 'Object', 'Right', 'SIB'),
    make_df(n170_obj_U_SIB_L, 'Latency (ms)', 'Inverted Object', 'Left', 'SIB'),
    make_df(n170_obj_U_SIB_R, 'Latency (ms)', 'Inverted Object', 'Right', 'SIB')])

#%%

g = sns.catplot(
    data=df_n170,
    x='Condition',
    y='Value',
    hue='Group',
    col='Cluster',
    kind='box',
    height=5,
    aspect=1.2,
    palette='Set2'
)
g.fig.suptitle('P1 Amplitudes by Condition, Cluster, and Group', y=1.05)
g.set_xticklabels(rotation=45)
plt.tight_layout()

#%%

def make_df(values, measure, condition, cluster, group):
    return pd.DataFrame({
        'Value': values,
        'Measure': measure,
        'Condition': condition,
        'Cluster': cluster,
        'Group': group
    })

# Combine both latency and peak-to-peak amplitude
df_n170 = pd.concat([
    # TD
    make_df(ptp_face_TD_L, 'Latency (ms)', 'Face', 'Left', 'TD'),
    make_df(ptp_face_TD_R, 'Latency (ms)', 'Face', 'Right', 'TD'),
    make_df(ptp_face_U_TD_L, 'Latency (ms)', 'Inverted Face', 'Left', 'TD'),
    make_df(ptp_face_U_TD_R, 'Latency (ms)', 'Inverted Face', 'Right', 'TD'),
    make_df(ptp_obj_TD_L, 'Latency (ms)', 'Object', 'Left', 'TD'),
    make_df(ptp_obj_TD_R, 'Latency (ms)', 'Object', 'Right', 'TD'),
    make_df(ptp_obj_U_TD_L, 'Latency (ms)', 'Inverted Object', 'Left', 'TD'),
    make_df(ptp_obj_U_TD_R, 'Latency (ms)', 'Inverted Object', 'Right', 'TD'),
    
    # ASD
    make_df(ptp_face_ASD_L, 'Latency (ms)', 'Face', 'Left', 'ASD'),
    make_df(ptp_face_ASD_R, 'Latency (ms)', 'Face', 'Right', 'ASD'),
    make_df(ptp_face_U_ASD_L, 'Latency (ms)', 'Inverted Face', 'Left', 'ASD'),
    make_df(ptp_face_U_ASD_R, 'Latency (ms)', 'Inverted Face', 'Right', 'ASD'),
    make_df(ptp_obj_ASD_L, 'Latency (ms)', 'Object', 'Left', 'ASD'),
    make_df(ptp_obj_ASD_R, 'Latency (ms)', 'Object', 'Right', 'ASD'),
    make_df(ptp_obj_U_ASD_L, 'Latency (ms)', 'Inverted Object', 'Left', 'ASD'),
    make_df(ptp_obj_U_ASD_R, 'Latency (ms)', 'Inverted Object', 'Right', 'ASD'),
    
    # SIB
    make_df(ptp_face_SIB_L, 'Latency (ms)', 'Face', 'Left', 'SIB'),
    make_df(ptp_face_SIB_R, 'Latency (ms)', 'Face', 'Right', 'SIB'),
    make_df(ptp_face_U_SIB_L, 'Latency (ms)', 'Inverted Face', 'Left', 'SIB'),
    make_df(ptp_face_U_SIB_R, 'Latency (ms)', 'Inverted Face', 'Right', 'SIB'),
    make_df(ptp_obj_SIB_L, 'Latency (ms)', 'Object', 'Left', 'SIB'),
    make_df(ptp_obj_SIB_R, 'Latency (ms)', 'Object', 'Right', 'SIB'),
    make_df(ptp_obj_U_SIB_L, 'Latency (ms)', 'Inverted Object', 'Left', 'SIB'),
    make_df(ptp_obj_U_SIB_R, 'Latency (ms)', 'Inverted Object', 'Right', 'SIB')])

#%%

g = sns.catplot(
    data=df_n170,
    x='Condition',
    y='Value',
    hue='Group',
    col='Cluster',
    kind='box',
    height=5,
    aspect=1.2,
    palette='Set2'
)
g.fig.suptitle('P1 Amplitudes by Condition, Cluster, and Group', y=1.05)
g.set_xticklabels(rotation=45)
plt.tight_layout()

#%%

Stats = np.concatenate([n170_face_TD_L , n170_face_ASD_L, n170_face_SIB_L,
                        n170_face_U_TD_L , n170_face_U_ASD_L, n170_face_U_SIB_L,
                        n170_obj_TD_L , n170_obj_ASD_L, n170_obj_SIB_L,
                        n170_obj_U_TD_L , n170_obj_U_ASD_L, n170_obj_U_SIB_L,
                        n170_face_TD_R , n170_face_ASD_R, n170_face_SIB_R,
                        n170_face_U_TD_R , n170_face_U_ASD_R, n170_face_U_SIB_R,
                        n170_obj_TD_R , n170_obj_ASD_R, n170_obj_SIB_R,
                        n170_obj_U_TD_R , n170_obj_U_ASD_R, n170_obj_U_SIB_R])

#%%

Stats = np.concatenate([ptp_face_TD_L , ptp_face_ASD_L, ptp_face_SIB_L,
                        ptp_face_U_TD_L , ptp_face_U_ASD_L, ptp_face_U_SIB_L,
                        ptp_obj_TD_L , ptp_obj_ASD_L, ptp_obj_SIB_L,
                        ptp_obj_U_TD_L , ptp_obj_U_ASD_L, ptp_obj_U_SIB_L,
                        ptp_face_TD_R , ptp_face_ASD_R, ptp_face_SIB_R,
                        ptp_face_U_TD_R , ptp_face_U_ASD_R, ptp_face_U_SIB_R,
                        ptp_obj_TD_R , ptp_obj_ASD_R, ptp_obj_SIB_R,
                        ptp_obj_U_TD_R , ptp_obj_U_ASD_R, ptp_obj_U_SIB_R])

#%%

from mne import EvokedArray
import numpy as np
import matplotlib.pyplot as plt

def compute_gfp(evoked):
    """Compute GFP: standard deviation across channels at each time point."""
    return evoked.data.std(axis=0) * 1e6  # Convert to µV

gfp_face = compute_gfp(evoked_face_TD)
gfp_face_U = compute_gfp(evoked_face_U_TD)
gfp_obj = compute_gfp(evoked_obj_TD)
gfp_obj_U = compute_gfp(evoked_obj_U_TD)

times = evoked_face_TD.times * 1000  # convert to ms

plt.figure(figsize=(10, 5))
plt.plot(times, gfp_face, label='Face')
plt.plot(times, gfp_face_U, label='Inverted Face')
plt.plot(times, gfp_obj, label='Object')
plt.plot(times, gfp_obj_U, label='Inverted Object')
plt.axvline(0, color='k', linestyle='--')
plt.xlabel('Time (ms)')
plt.ylabel('GFP (µV)')
plt.title('Global Field Power (TD Group)')
plt.legend()
plt.tight_layout()
plt.show()


#%%

]

x_labels = [
    'Faces\nTD', 'Faces\nASD', 'Faces\nSIB',
    'Inv. Faces\nTD', 'Inv. Faces\nASD', 'Inv. Faces\nSIB',
    'Object\nTD', 'Object\nASD', 'Object\nSIB',
    'Inv. Object\nTD', 'Inv. Object\nASD', 'Inv. Object\nSIB'
]

colors = [
    '#b2182b', '#b2182b', '#b2182b',
    '#ef8a62', '#ef8a62', '#ef8a62',
    '#2166ac', '#2166ac', '#2166ac',
    '#67a9cf', '#67a9cf', '#67a9cf'
]

fig, ax = plt.subplots(figsize=(12, 5))

for i, (y, label, color) in enumerate(zip(data_amplitudes, x_labels, colors), start=1):
    ax.boxplot(y, positions=[i], patch_artist=True, widths=0.6,
               boxprops=dict(facecolor=color, color=color),
               capprops=dict(color=color),
               whiskerprops=dict(color=color),
               flierprops=dict(markerfacecolor=color, marker='o', markersize=4, linestyle='none'),
               medianprops=dict(color='black'))

ax.set_xticks(range(1, 13))
ax.set_xticklabels(x_labels, rotation=45, ha='right')
ax.set_ylabel('N170 Peak-to-Peak Amplitude (µV)')
ax.set_title('P1-N170 Amplitude Across Conditions and Groups')
ax.axvline(6.5, color='gray', linestyle='--', lw=1)
ax.text(3.5, ax.get_ylim()[1], 'Faces', ha='center', va='bottom', fontsize=10, weight='bold')
ax.text(9.5, ax.get_ylim()[1], 'Objects', ha='center', va='bottom', fontsize=10, weight='bold')
ax.grid(axis='y')
plt.tight_layout()
plt.show()


#%% Plot ERP for face

visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# visual_channels = ['C1', 'Cz', 'C2', 'CP1', 'CPz', 'CP2']

# visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# visual_channels = ['O1',  'PO7', 'PO3']
# visual_channels = ['O2',  'PO8', 'PO4']
# visual_channels = ['F1',  'Fz', 'F2']


# Visual ERP: Calculate and plot the average ERP with SEM for visual stimulation ('V')
avg_erp_v_TD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_TD], axis=0)
sem_erp_v_TD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_TD])

avg_erp_v_ASD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_ASD], axis=0)
sem_erp_v_ASD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_ASD])

avg_erp_v_SIB = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_SIB], axis=0)
sem_erp_v_SIB = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_SIB])

# Plot Visual ERP with SEM for -0.1 to 0.6 seconds
plot_avg_erp_with_sem(avg_erp_v_TD, sem_erp_v_TD, avg_erp_v_ASD, sem_erp_v_ASD, avg_erp_v_SIB, sem_erp_v_SIB, 'Faces',
                      visual_channels, filtered_epochs_lst_TD[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)

#%% Plot ERP for inverted faces

visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# visual_channels = ['C1', 'Cz', 'C2', 'CP1', 'CPz', 'CP2']

# visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# visual_channels = ['O1',  'PO7', 'PO3']
# visual_channels = ['O2',  'PO8', 'PO4']
# visual_channels = ['F1',  'Fz', 'F2']


# Visual ERP: Calculate and plot the average ERP with SEM for visual stimulation ('V')
avg_erp_v_TD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_U_TD], axis=0)
sem_erp_v_TD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_U_TD])

avg_erp_v_ASD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_U_ASD], axis=0)
sem_erp_v_ASD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_U_ASD])

avg_erp_v_SIB = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_face_U_SIB], axis=0)
sem_erp_v_SIB = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_face_U_SIB])

# Plot Visual ERP with SEM for -0.1 to 0.6 seconds
plot_avg_erp_with_sem(avg_erp_v_TD, sem_erp_v_TD, avg_erp_v_ASD, sem_erp_v_ASD, avg_erp_v_SIB, sem_erp_v_SIB, 'Inverted Faces',
                      visual_channels, filtered_epochs_lst_TD[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)

#%% Plot topomap - face
Evoked_face_TD = mne.grand_average(erp_face_U_TD)
Evoked_face_ASD = mne.grand_average(erp_face_U_ASD)
Evoked_face_SIB = mne.grand_average(erp_face_U_SIB)

times = [-0.05,0.12,0.170,0.250,0.31]  # Time in seconds

Evoked_face_TD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
Evoked_face_ASD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
Evoked_face_SIB.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')

#%% save

plt.savefig('ERP_Topomap_Inverted_Faces_SIB.svg')

#%% plot ERP for objects

visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# visual_channels = ['C1', 'Cz', 'C2', 'CP1', 'CPz', 'CP2']

# visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# visual_channels = ['O1',  'PO7', 'PO3']
# visual_channels = ['O2',  'PO8', 'PO4']
# visual_channels = ['F1',  'Fz', 'F2']


# Visual ERP: Calculate and plot the average ERP with SEM for visual stimulation ('V')
avg_erp_v_TD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_TD], axis=0)
sem_erp_v_TD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_TD])

avg_erp_v_ASD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_ASD], axis=0)
sem_erp_v_ASD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_ASD])

avg_erp_v_SIB = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_SIB], axis=0)
sem_erp_v_SIB = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_SIB])

# Plot Visual ERP with SEM for -0.1 to 0.6 seconds
plot_avg_erp_with_sem(avg_erp_v_TD, sem_erp_v_TD, avg_erp_v_ASD, sem_erp_v_ASD, avg_erp_v_SIB, sem_erp_v_SIB, 'Objects',
                      visual_channels, filtered_epochs_lst_TD[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)

#%% Plot topomap - face
Evoked_face_TD = mne.grand_average(erp_obj_TD)
Evoked_face_ASD = mne.grand_average(erp_obj_ASD)
Evoked_face_SIB = mne.grand_average(erp_obj_SIB)

times = [-0.05,0.12,0.170,0.250,0.31]  # Time in seconds

Evoked_face_TD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
Evoked_face_ASD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
Evoked_face_SIB.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')

#%% save

plt.savefig('ERP_Topomap_Object_SIB.svg')

#%% Plot ERP for inverted objects

visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# visual_channels = ['C1', 'Cz', 'C2', 'CP1', 'CPz', 'CP2']

# visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# visual_channels = ['O1',  'PO7', 'PO3']
# visual_channels = ['O2',  'PO8', 'PO4']
# visual_channels = ['F1',  'Fz', 'F2']


# Visual ERP: Calculate and plot the average ERP with SEM for visual stimulation ('V')
avg_erp_v_TD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_TD], axis=0)
sem_erp_v_TD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_TD])

avg_erp_v_ASD = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_ASD], axis=0)
sem_erp_v_ASD = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_ASD])

avg_erp_v_SIB = np.mean([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_SIB], axis=0)
sem_erp_v_SIB = calculate_sem([average_erp_channels(erp, visual_channels) for erp in erp_obj_U_SIB])

# Plot Visual ERP with SEM for -0.1 to 0.6 seconds
plot_avg_erp_with_sem(avg_erp_v_TD, sem_erp_v_TD, avg_erp_v_ASD, sem_erp_v_ASD, avg_erp_v_SIB, sem_erp_v_SIB, 'Inverted Objects',
                      visual_channels, filtered_epochs_lst_TD[0].info['sfreq'], plot_tmin=-0.1, plot_tmax=0.6)

#%% Plot topomap - face
Evoked_face_TD = mne.grand_average(erp_obj_U_TD)
Evoked_face_ASD = mne.grand_average(erp_obj_U_ASD)
Evoked_face_SIB = mne.grand_average(erp_obj_U_SIB)

times = [-0.05,0.12,0.170,0.250,0.31]  # Time in seconds

Evoked_face_TD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
Evoked_face_ASD.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')
Evoked_face_SIB.plot_topomap(times=times, size=1, vlim=(-20, 20), cmap='jet')

#%% save

plt.savefig('ERP_Topomap_Inverted_Object_SIB.svg')

#%% Plot the difference wave: inverted face - face

# Step 1: Difference waves for each subject (TD)
erp_diff_TD = [
    average_erp_channels(face, visual_channels) - average_erp_channels(obj, visual_channels)
    for face, obj in zip(erp_face_TD, erp_obj_TD)
]

# ASD group
erp_diff_ASD = [
    average_erp_channels(face, visual_channels) - average_erp_channels(obj, visual_channels)
    for face, obj in zip(erp_face_ASD, erp_obj_ASD)
]

# SIB group
erp_diff_SIB = [
    average_erp_channels(face, visual_channels) - average_erp_channels(obj, visual_channels)
    for face, obj in zip(erp_face_SIB, erp_obj_SIB)
]

# Step 2: Compute group average and SEM
avg_erp_diff_TD = np.mean(erp_diff_TD, axis=0)
sem_erp_diff_TD = calculate_sem(erp_diff_TD)

avg_erp_diff_ASD = np.mean(erp_diff_ASD, axis=0)
sem_erp_diff_ASD = calculate_sem(erp_diff_ASD)

avg_erp_diff_SIB = np.mean(erp_diff_SIB, axis=0)
sem_erp_diff_SIB = calculate_sem(erp_diff_SIB)

# Step 3: Plot the difference waves
plot_avg_erp_with_sem(
    avg_erp_diff_TD, sem_erp_diff_TD,
    avg_erp_diff_ASD, sem_erp_diff_ASD,
    avg_erp_diff_SIB, sem_erp_diff_SIB,
    'Face – Object ERP',
    visual_channels,
    filtered_epochs_lst_TD[0].info['sfreq'],
    plot_tmin=-0.1,
    plot_tmax=0.6
)

plt.ylim(-8e-6,4e-6)

#%% Plot the difference wave: face - object ERP

# Step 1: Difference waves for each subject (TD)
erp_diff_TD = [
    average_erp_channels(face_U, visual_channels) - average_erp_channels(face, visual_channels)
    for face_U, face in zip(erp_face_U_TD, erp_face_TD)
]

# ASD group
erp_diff_ASD = [
    average_erp_channels(face_U, visual_channels) - average_erp_channels(face, visual_channels)
    for face_U, face in zip(erp_face_U_ASD, erp_face_ASD)
]

# SIB group
erp_diff_SIB = [
    average_erp_channels(face_U, visual_channels) - average_erp_channels(face, visual_channels)
    for face_U, face in zip(erp_face_U_SIB, erp_face_SIB)
]

# Step 2: Compute group average and SEM
avg_erp_diff_TD = np.mean(erp_diff_TD, axis=0)
sem_erp_diff_TD = calculate_sem(erp_diff_TD)

avg_erp_diff_ASD = np.mean(erp_diff_ASD, axis=0)
sem_erp_diff_ASD = calculate_sem(erp_diff_ASD)

avg_erp_diff_SIB = np.mean(erp_diff_SIB, axis=0)
sem_erp_diff_SIB = calculate_sem(erp_diff_SIB)

# Step 3: Plot the difference waves
plot_avg_erp_with_sem(
    avg_erp_diff_TD, sem_erp_diff_TD,
    avg_erp_diff_ASD, sem_erp_diff_ASD,
    avg_erp_diff_SIB, sem_erp_diff_SIB,
    'Face – Object ERP',
    visual_channels,
    filtered_epochs_lst_TD[0].info['sfreq'],
    plot_tmin=-0.1,
    plot_tmax=0.6
)

plt.ylim(-4e-6,4e-6)

#%% Plot ERP NO PREP

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

#%% Calculate GFP 

import numpy as np

def compute_gfp_per_subject(evoked_list):
    """Return array of shape (n_subjects, n_times) with GFP for each subject."""
    gfp_all = []
    for evoked in evoked_list:
        gfp = evoked.data.std(axis=0) * 1e6  # µV
        gfp_all.append(gfp)
    return np.array(gfp_all)  # shape: (n_subjects, n_times)

# Compute GFP for each condition
gfp_face_TD = compute_gfp_per_subject(erp_face_TD)
gfp_face_U_TD = compute_gfp_per_subject(erp_face_U_TD)
gfp_obj_TD = compute_gfp_per_subject(erp_obj_TD)
gfp_obj_U_TD = compute_gfp_per_subject(erp_obj_U_TD)

def mean_and_sem(gfp_array):
    mean = gfp_array.mean(axis=0)
    sem = gfp_array.std(axis=0) / np.sqrt(gfp_array.shape[0])
    return mean, sem

mean_face, sem_face = mean_and_sem(gfp_face_TD)
mean_face_U, sem_face_U = mean_and_sem(gfp_face_U_TD)
mean_obj, sem_obj = mean_and_sem(gfp_obj_TD)
mean_obj_U, sem_obj_U = mean_and_sem(gfp_obj_U_TD)

times = erp_face_TD[0].times * 1000  # convert to ms

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

# Plot mean ± SEM
def plot_gfp(mean, sem, label, color):
    plt.plot(times, mean, label=label, color=color)
    plt.fill_between(times, mean - sem, mean + sem, alpha=0.3, color=color)

plot_gfp(mean_face, sem_face, 'Face', 'tab:blue')
plot_gfp(mean_face_U, sem_face_U, 'Inverted Face', 'tab:orange')
plot_gfp(mean_obj, sem_obj, 'Object', 'tab:green')
plot_gfp(mean_obj_U, sem_obj_U, 'Inverted Object', 'tab:red')

plt.axvline(0, color='k', linestyle='--')
plt.xlabel('Time (ms)')
plt.ylabel('GFP (µV)')
plt.title('GFP in TD Group (Mean ± SEM)')
plt.legend()
plt.tight_layout()
plt.show()


#%% Calculate GFP 

import numpy as np

def compute_gfp_per_subject(evoked_list):
    """Return array of shape (n_subjects, n_times) with GFP for each subject."""
    gfp_all = []
    for evoked in evoked_list:
        gfp = evoked.data.std(axis=0) * 1e6  # µV
        gfp_all.append(gfp)
    return np.array(gfp_all)  # shape: (n_subjects, n_times)

# Compute GFP for each condition
gfp_face_ASD = compute_gfp_per_subject(erp_face_ASD)
gfp_face_U_ASD = compute_gfp_per_subject(erp_face_U_ASD)
gfp_obj_ASD = compute_gfp_per_subject(erp_obj_ASD)
gfp_obj_U_ASD = compute_gfp_per_subject(erp_obj_U_ASD)

def mean_and_sem(gfp_array):
    mean = gfp_array.mean(axis=0)
    sem = gfp_array.std(axis=0) / np.sqrt(gfp_array.shape[0])
    return mean, sem

mean_face, sem_face = mean_and_sem(gfp_face_ASD)
mean_face_U, sem_face_U = mean_and_sem(gfp_face_U_ASD)
mean_obj, sem_obj = mean_and_sem(gfp_obj_ASD)
mean_obj_U, sem_obj_U = mean_and_sem(gfp_obj_U_ASD)

times = erp_face_ASD[0].times * 1000  # convert to ms

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

# Plot mean ± SEM
def plot_gfp(mean, sem, label, color):
    plt.plot(times, mean, label=label, color=color)
    plt.fill_between(times, mean - sem, mean + sem, alpha=0.3, color=color)

plot_gfp(mean_face, sem_face, 'Face', 'tab:blue')
plot_gfp(mean_face_U, sem_face_U, 'Inverted Face', 'tab:orange')
plot_gfp(mean_obj, sem_obj, 'Object', 'tab:green')
plot_gfp(mean_obj_U, sem_obj_U, 'Inverted Object', 'tab:red')

plt.axvline(0, color='k', linestyle='--')
plt.xlabel('Time (ms)')
plt.ylabel('GFP (µV)')
plt.title('GFP in ASD Group (Mean ± SEM)')
plt.legend()
plt.tight_layout()
plt.show()

#%%

# Compute difference wave per subject at the selected channels
diff_erp_subjects = [
    average_erp_channels(erp_u_face, visual_channels) - average_erp_channels(erp_face, visual_channels)
    for erp_face, erp_u_face in zip(erp_face_TD, erp_face_U_TD)
]

import numpy as np

# Convert to array
diff_erp_subjects = np.array(diff_erp_subjects)

# Mean and SEM across subjects
avg_diff_erp = np.mean(diff_erp_subjects, axis=0)
sem_diff_erp = np.std(diff_erp_subjects, axis=0) / np.sqrt(len(diff_erp_subjects))

import matplotlib.pyplot as plt

# Time vector
sfreq = filtered_epochs_lst_TD[0].info['sfreq']
n_times = avg_diff_erp.shape[0]
# Extract time vector directly from ERP
times = erp_face_TD[0].times

# Plot
plt.figure(figsize=(10, 4))
plt.plot(times, avg_diff_erp, label='Inverted Face - Face', color='black')
plt.fill_between(times, avg_diff_erp - sem_diff_erp, avg_diff_erp + sem_diff_erp,
                 color='black', alpha=0.3)

plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.title(f'Difference ERP at {visual_channels}')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (µV)')
plt.legend()
plt.tight_layout()
plt.show()
plt.xlim([-0.1,0.6])

#%% Plot individual ERP for peak detection illustration

import matplotlib.pyplot as plt

def plot_peaks_per_subject(evoked_list, channel_names, p1_window=(0.07, 0.17), n170_window=(0.14, 0.23), group_name='TD', condition='Face'):
    for i, evoked in enumerate(evoked_list):
        ch_indices = [evoked.ch_names.index(ch) for ch in channel_names]
        times = evoked.times
        signal = evoked.data[ch_indices].mean(axis=0) * 1e6  # µV

        # Extract windowed data
        p1_mask = (times >= p1_window[0]) & (times <= p1_window[1])
        n170_mask = (times >= n170_window[0]) & (times <= n170_window[1])

        # P1
        p1_data = signal[p1_mask]
        p1_times = times[p1_mask]
        p1_idx = p1_data.argmax()
        p1_time = p1_times[p1_idx] * 1000
        p1_amp = p1_data[p1_idx]

        # N170
        n170_data = signal[n170_mask]
        n170_times = times[n170_mask]
        n170_idx = n170_data.argmin()
        n170_time = n170_times[n170_idx] * 1000
        n170_amp = n170_data[n170_idx]

        # Plot
        plt.figure(figsize=(8, 4))
        plt.plot(times * 1000, signal, label='ERP')
        plt.axvline(p1_time, color='blue', linestyle='--', label='P1 peak')
        plt.axvline(n170_time, color='red', linestyle='--', label='N170 peak')
        plt.plot(p1_time, p1_amp, 'bo')
        plt.plot(n170_time, n170_amp, 'ro')
        plt.title(f'{group_name} - {condition} - Subject {i+1}')
        plt.xlabel('Time (ms)')
        plt.ylabel('Amplitude (µV)')
        plt.axvline(0, color='k', linestyle='--')
        plt.legend()
        plt.tight_layout()
        plt.show()

# Define clusters
left_cluster = ['P7']

# Plot ERP and detected peaks for TD group, face condition
plot_peaks_per_subject(erp_face_ASD, left_cluster, group_name='TD', condition='Face')

#%% Difference wave between face TD and face ASD

import numpy as np
import matplotlib.pyplot as plt
import mne

# --- Helper functions ---
def extract_data(evokeds, channels):
    """Extract channel data from list of Evokeds into array (n_subjects, n_times), averaged across channels."""
    n_subj = len(evokeds)
    n_times = len(evokeds[0].times)
    data = np.zeros((n_subj, n_times))
    for i, ev in enumerate(evokeds):
        data[i] = ev.copy().pick(channels).data.mean(axis=0)
    return data

# ================================
# FACE stimuli only: TD vs ASD
# ================================
channels = ['O1', 'PO7', 'O2', 'PO8']  # Parieto-occipital cluster
times = erp_face_TD[0].times * 1000  # ms

# Extract ERP data averaged across channels
data_TD = extract_data(erp_face_TD, channels) * 1e6  # µV
data_ASD = extract_data(erp_face_ASD, channels) * 1e6

# Extract ERP data averaged across channels
# data_TD = extract_data(erp_obj_TD, channels) * 1e6  # µV
# data_ASD = extract_data(erp_obj_ASD, channels) * 1e6

# Compute group means and SEM
mean_TD = data_TD.mean(axis=0)
sem_TD = data_TD.std(axis=0) / np.sqrt(data_TD.shape[0])

mean_ASD = data_ASD.mean(axis=0)
sem_ASD = data_ASD.std(axis=0) / np.sqrt(data_ASD.shape[0])

# Difference wave TD - ASD
diff_wave = mean_TD - mean_ASD

# ================================
# Plot waveform with SEM shading
# ================================
plt.figure(figsize=(10, 6))
plt.plot(times, diff_wave, color='black', label='TD - ASD')

plt.axvline(0, color='k', linestyle='--')
plt.axhline(0, color='k', linewidth=0.5)
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude Difference (µV)')
plt.title('TD - ASD Difference Wave (Faces) - Parieto-Occipital Cluster')
plt.xlim([-100, 600])
plt.ylim([-2.2,2])
plt.grid(False)
plt.legend()
plt.tight_layout()
plt.show()

# ================================
# Compute Evoked difference for topomap
# ================================
# Compute grand average per group for face condition
grand_TD_face = mne.grand_average(erp_face_TD)
grand_ASD_face = mne.grand_average(erp_face_ASD)

# Difference Evoked (TD - ASD)
diff_evoked = mne.combine_evoked([grand_TD_face, grand_ASD_face], weights=[1, -1])

# ================================
# Plot topomaps at selected times
# ================================
times_of_interest = [-0.05, 0.11, 0.15, 0.24, 0.35]  # in seconds
diff_evoked.plot_topomap(times=times_of_interest, ch_type='eeg', scalings=1,
                          time_unit='s', cmap='RdBu_r', vmin=-3, vmax=3,
                          title='TD - ASD Difference (Faces)')
