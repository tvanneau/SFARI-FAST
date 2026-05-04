# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 09:29:47 2025

@author: tvanneau
"""

#%% For faces

# Load pickle file with corresponding power data 
import os
import pickle
import mne
import matplotlib.pyplot as plt


with open('Power_face_TD_Gamma.pkl', 'rb') as f:
    [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_face_TD)):
    Power_NPL_face_TD[i].apply_baseline(baseline=baseline, mode='percent')
# Apply baseline correction to each subject's power
for i in range(len(Power_face_TD)):
    Power_face_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_TD = mne.grand_average(Power_face_TD)


with open('Power_face_U_TD_Gamma.pkl', 'rb') as f:
    [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_face_U_TD)):
    Power_NPL_face_U_TD[i].apply_baseline(baseline=baseline, mode='percent')
# Apply baseline correction to each subject's power
for i in range(len(Power_face_U_TD)):
    Power_face_U_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_U_TD = mne.grand_average(Power_face_U_TD)


with open('Power_obj_TD_Gamma.pkl', 'rb') as f:
    [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_obj_TD)):
    Power_NPL_obj_TD[i].apply_baseline(baseline=baseline, mode='percent')
# Apply baseline correction to each subject's power
for i in range(len(Power_obj_TD)):
    Power_obj_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_TD = mne.grand_average(Power_obj_TD)


with open('Power_obj_U_TD_Gamma.pkl', 'rb') as f:
    [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_obj_U_TD)):
    Power_NPL_obj_U_TD[i].apply_baseline(baseline=baseline, mode='percent')
for i in range(len(Power_NPL_obj_U_TD)):
    Power_obj_U_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_U_TD = mne.grand_average(Power_obj_U_TD)

#%% Alpha suppression for Induced power for TD
import numpy as np

freqs = np.linspace(*np.array([25, 40]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz']

# channels = ['O2', 'PO4', 'PO8' ]

# channels = ['O1', 'PO3', 'PO7' ]
channels = ['Iz', 'Oz', 'POz', 'O1', 'O2' ]


# channels = ['O1', 'O2', 'POz', 'Oz']

# channels = ['P8']

tmin = -0.2
tmax = 0.6

Alpha_min = 0 # 7Hz
Alpha_max = 100 # 13Hz

Alpha_suppression_face_TD = []
Alpha_suppression_U_face_TD = []

Alpha_suppression_obj_TD = []
Alpha_suppression_U_obj_TD = []

# for i in range(0,len(Power_NPL_face_TD),1):
#     Aph_TD = Power_NPL_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_face_TD.append(Fa_TD)

# for i in range(0,len(Power_NPL_face_U_TD),1):
#     Aph_TD = Power_NPL_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_U_face_TD.append(Fa_TD)
    
# for i in range(0,len(Power_NPL_obj_TD),1):
#     Aph_TD = Power_NPL_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_obj_TD.append(Fa_TD)
    
# for i in range(0,len(Power_NPL_obj_U_TD),1):
#     Aph_TD = Power_NPL_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_U_obj_TD.append(Fa_TD)
    
# For total power
for i in range(0,len(Power_face_TD),1):
    Aph_TD = Power_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_face_TD.append(Fa_TD)

for i in range(0,len(Power_face_U_TD),1):
    Aph_TD = Power_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_face_TD.append(Fa_TD)
    
for i in range(0,len(Power_obj_TD),1):
    Aph_TD = Power_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_obj_TD.append(Fa_TD)
    
for i in range(0,len(Power_obj_U_TD),1):
    Aph_TD = Power_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_obj_TD.append(Fa_TD)
    

fig, ax = plt.subplots()

Mean_face = np.mean(np.array( Alpha_suppression_face_TD),axis=0)
Mean_face_U = np.mean(np.array( Alpha_suppression_U_face_TD),axis=0)
Mean_obj = np.mean(np.array( Alpha_suppression_obj_TD),axis=0)
Mean_obj_U = np.mean(np.array( Alpha_suppression_U_obj_TD),axis=0)

SEM_face = np.std(np.array(Alpha_suppression_face_TD), axis=0) / np.sqrt(len(Alpha_suppression_face_TD))
SEM_face_U = np.std(np.array(Alpha_suppression_U_face_TD), axis=0) / np.sqrt(len(Alpha_suppression_U_face_TD))
SEM_obj = np.std(np.array(Alpha_suppression_obj_TD), axis=0) / np.sqrt(len(Alpha_suppression_obj_TD))
SEM_obj_U = np.std(np.array(Alpha_suppression_U_obj_TD), axis=0) / np.sqrt(len(Alpha_suppression_U_obj_TD))

x = np.linspace(-0.2,0.6,104)

ax.plot(x, Mean_face, label = 'Faces', color = '#b2182b')
ax.fill_between(x, Mean_face - SEM_face, Mean_face + SEM_face, alpha=0.2, color = '#b2182b')

ax.plot(x, Mean_face_U, label = 'Inverted faces', color = '#ef8a62')
ax.fill_between(x, Mean_face_U - SEM_face_U, Mean_face_U + SEM_face_U, alpha=0.2, color = '#ef8a62')

ax.plot(x, Mean_obj, label = 'Object', color = '#2166ac')
ax.fill_between(x, Mean_obj - SEM_obj, Mean_obj + SEM_obj, alpha=0.2, color = '#2166ac')

ax.plot(x, Mean_obj_U, label = 'Inverted object', color= '#67a9cf')
ax.fill_between(x, Mean_obj_U - SEM_obj_U, Mean_obj_U + SEM_obj_U, alpha=0.2, color= '#67a9cf')


# ax.set_ylim(-0.02,0.18) # For theta power
ax.set_ylim(-0.15,0.37)
ax.legend()

#%% For faces

# Load pickle file with corresponding power data 
import os
import pickle
import mne
import matplotlib.pyplot as plt


with open('Power_face_SIB_Gamma.pkl', 'rb') as f:
    [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_face_TD)):
    Power_NPL_face_TD[i].apply_baseline(baseline=baseline, mode='percent')
# Apply baseline correction to each subject's power
for i in range(len(Power_face_TD)):
    Power_face_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_SIB = mne.grand_average(Power_face_TD)


with open('Power_face_U_SIB_Gamma.pkl', 'rb') as f:
    [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_face_U_TD)):
    Power_NPL_face_U_TD[i].apply_baseline(baseline=baseline, mode='percent')
# Apply baseline correction to each subject's power
for i in range(len(Power_face_U_TD)):
    Power_face_U_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_U_SIB = mne.grand_average(Power_face_U_TD)


with open('Power_obj_SIB_Gamma.pkl', 'rb') as f:
    [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_obj_TD)):
    Power_NPL_obj_TD[i].apply_baseline(baseline=baseline, mode='percent')
# Apply baseline correction to each subject's power
for i in range(len(Power_obj_TD)):
    Power_obj_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_SIB = mne.grand_average(Power_obj_TD)


with open('Power_obj_U_SIB_Gamma.pkl', 'rb') as f:
    [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_obj_U_TD)):
    Power_NPL_obj_U_TD[i].apply_baseline(baseline=baseline, mode='percent')
for i in range(len(Power_NPL_obj_U_TD)):
    Power_obj_U_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_U_SIB = mne.grand_average(Power_obj_U_TD)

#%% Alpha suppression for Induced power for TD
import numpy as np

freqs = np.linspace(*np.array([25, 40]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz']

# channels = ['O2', 'PO4', 'PO8' ]

# channels = ['O1', 'PO3', 'PO7' ]
channels = ['Iz', 'Oz', 'POz', 'O1', 'O2' ]


# channels = ['O1', 'O2', 'POz', 'Oz']

# channels = ['P8']

tmin = -0.2
tmax = 0.6

Alpha_min = 0 # 7Hz
Alpha_max = 100 # 13Hz

Alpha_suppression_face_SIB = []
Alpha_suppression_U_face_SIB = []

Alpha_suppression_obj_SIB = []
Alpha_suppression_U_obj_SIB = []

# for i in range(0,len(Power_NPL_face_TD),1):
#     Aph_TD = Power_NPL_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_face_SIB.append(Fa_TD)

# for i in range(0,len(Power_NPL_face_U_TD),1):
#     Aph_TD = Power_NPL_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_U_face_SIB.append(Fa_TD)
    
# for i in range(0,len(Power_NPL_obj_TD),1):
#     Aph_TD = Power_NPL_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_obj_SIB.append(Fa_TD)
    
# for i in range(0,len(Power_NPL_obj_U_TD),1):
#     Aph_TD = Power_NPL_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_U_obj_SIB.append(Fa_TD)
    
# For total power
for i in range(0,len(Power_face_TD),1):
    Aph_TD = Power_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_face_SIB.append(Fa_TD)

for i in range(0,len(Power_face_U_TD),1):
    Aph_TD = Power_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_face_SIB.append(Fa_TD)
    
for i in range(0,len(Power_obj_TD),1):
    Aph_TD = Power_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_obj_SIB.append(Fa_TD)
    
for i in range(0,len(Power_obj_U_TD),1):
    Aph_TD = Power_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_obj_SIB.append(Fa_TD)
    

fig, ax = plt.subplots()

Mean_face = np.mean(np.array( Alpha_suppression_face_SIB),axis=0)
Mean_face_U = np.mean(np.array( Alpha_suppression_U_face_SIB),axis=0)
Mean_obj = np.mean(np.array( Alpha_suppression_obj_SIB),axis=0)
Mean_obj_U = np.mean(np.array( Alpha_suppression_U_obj_SIB),axis=0)

SEM_face = np.std(np.array(Alpha_suppression_face_SIB), axis=0) / np.sqrt(len(Alpha_suppression_face_SIB))
SEM_face_U = np.std(np.array(Alpha_suppression_U_face_SIB), axis=0) / np.sqrt(len(Alpha_suppression_U_face_SIB))
SEM_obj = np.std(np.array(Alpha_suppression_obj_SIB), axis=0) / np.sqrt(len(Alpha_suppression_obj_SIB))
SEM_obj_U = np.std(np.array(Alpha_suppression_U_obj_SIB), axis=0) / np.sqrt(len(Alpha_suppression_U_obj_SIB))

x = np.linspace(-0.2,0.6,104)

ax.plot(x, Mean_face, label = 'Faces', color = '#b2182b')
ax.fill_between(x, Mean_face - SEM_face, Mean_face + SEM_face, alpha=0.2, color = '#b2182b')

ax.plot(x, Mean_face_U, label = 'Inverted faces', color = '#ef8a62')
ax.fill_between(x, Mean_face_U - SEM_face_U, Mean_face_U + SEM_face_U, alpha=0.2, color = '#ef8a62')

ax.plot(x, Mean_obj, label = 'Object', color = '#2166ac')
ax.fill_between(x, Mean_obj - SEM_obj, Mean_obj + SEM_obj, alpha=0.2, color = '#2166ac')

ax.plot(x, Mean_obj_U, label = 'Inverted object', color= '#67a9cf')
ax.fill_between(x, Mean_obj_U - SEM_obj_U, Mean_obj_U + SEM_obj_U, alpha=0.2, color= '#67a9cf')


# ax.set_ylim(-0.02,0.18) # For theta power
ax.set_ylim(-0.15,0.37)
ax.legend()

#%% For faces

# Load pickle file with corresponding power data 
import os
import pickle
import mne
import matplotlib.pyplot as plt


with open('Power_face_ASD_Gamma.pkl', 'rb') as f:
    [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_face_TD)):
    Power_NPL_face_TD[i].apply_baseline(baseline=baseline, mode='percent')
# Apply baseline correction to each subject's power
for i in range(len(Power_face_TD)):
    Power_face_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_ASD = mne.grand_average(Power_face_TD)


with open('Power_face_U_ASD_Gamma.pkl', 'rb') as f:
    [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_face_U_TD)):
    Power_NPL_face_U_TD[i].apply_baseline(baseline=baseline, mode='percent')
# Apply baseline correction to each subject's power
for i in range(len(Power_face_U_TD)):
    Power_face_U_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_U_ASD = mne.grand_average(Power_face_U_TD)


with open('Power_obj_ASD_Gamma.pkl', 'rb') as f:
    [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_obj_TD)):
    Power_NPL_obj_TD[i].apply_baseline(baseline=baseline, mode='percent')
# Apply baseline correction to each subject's power
for i in range(len(Power_obj_TD)):
    Power_obj_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_ASD = mne.grand_average(Power_obj_TD)


with open('Power_obj_U_ASD_Gamma.pkl', 'rb') as f:
    [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_obj_U_TD)):
    Power_NPL_obj_U_TD[i].apply_baseline(baseline=baseline, mode='percent')
for i in range(len(Power_NPL_obj_U_TD)):
    Power_obj_U_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_U_ASD = mne.grand_average(Power_obj_U_TD)

#%% Alpha suppression for Induced power for TD
import numpy as np

freqs = np.linspace(*np.array([25, 40]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz']

# channels = ['O2', 'PO4', 'PO8' ]

# channels = ['O1', 'PO3', 'PO7' ]
channels = ['Iz', 'Oz', 'POz', 'O1', 'O2' ]


# channels = ['O1', 'O2', 'POz', 'Oz']

# channels = ['P8']

tmin = -0.2
tmax = 0.6

Alpha_min = 0 # 7Hz
Alpha_max = 100 # 13Hz

Alpha_suppression_face_ASD = []
Alpha_suppression_U_face_ASD = []

Alpha_suppression_obj_ASD = []
Alpha_suppression_U_obj_ASD = []

# for i in range(0,len(Power_NPL_face_TD),1):
#     Aph_TD = Power_NPL_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_face_SIB.append(Fa_TD)

# for i in range(0,len(Power_NPL_face_U_TD),1):
#     Aph_TD = Power_NPL_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_U_face_SIB.append(Fa_TD)
    
# for i in range(0,len(Power_NPL_obj_TD),1):
#     Aph_TD = Power_NPL_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_obj_SIB.append(Fa_TD)
    
# for i in range(0,len(Power_NPL_obj_U_TD),1):
#     Aph_TD = Power_NPL_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_U_obj_SIB.append(Fa_TD)
    
# For total power
for i in range(0,len(Power_face_TD),1):
    Aph_TD = Power_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_face_ASD.append(Fa_TD)

for i in range(0,len(Power_face_U_TD),1):
    Aph_TD = Power_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_face_ASD.append(Fa_TD)
    
for i in range(0,len(Power_obj_TD),1):
    Aph_TD = Power_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_obj_ASD.append(Fa_TD)
    
for i in range(0,len(Power_obj_U_TD),1):
    Aph_TD = Power_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_obj_ASD.append(Fa_TD)
    

fig, ax = plt.subplots()

Mean_face = np.mean(np.array( Alpha_suppression_face_ASD),axis=0)
Mean_face_U = np.mean(np.array( Alpha_suppression_U_face_ASD),axis=0)
Mean_obj = np.mean(np.array( Alpha_suppression_obj_ASD),axis=0)
Mean_obj_U = np.mean(np.array( Alpha_suppression_U_obj_ASD),axis=0)

SEM_face = np.std(np.array(Alpha_suppression_face_ASD), axis=0) / np.sqrt(len(Alpha_suppression_face_ASD))
SEM_face_U = np.std(np.array(Alpha_suppression_U_face_ASD), axis=0) / np.sqrt(len(Alpha_suppression_U_face_ASD))
SEM_obj = np.std(np.array(Alpha_suppression_obj_ASD), axis=0) / np.sqrt(len(Alpha_suppression_obj_ASD))
SEM_obj_U = np.std(np.array(Alpha_suppression_U_obj_ASD), axis=0) / np.sqrt(len(Alpha_suppression_U_obj_ASD))

x = np.linspace(-0.2,0.6,104)

ax.plot(x, Mean_face, label = 'Faces', color = '#b2182b')
ax.fill_between(x, Mean_face - SEM_face, Mean_face + SEM_face, alpha=0.2, color = '#b2182b')

ax.plot(x, Mean_face_U, label = 'Inverted faces', color = '#ef8a62')
ax.fill_between(x, Mean_face_U - SEM_face_U, Mean_face_U + SEM_face_U, alpha=0.2, color = '#ef8a62')

ax.plot(x, Mean_obj, label = 'Object', color = '#2166ac')
ax.fill_between(x, Mean_obj - SEM_obj, Mean_obj + SEM_obj, alpha=0.2, color = '#2166ac')

ax.plot(x, Mean_obj_U, label = 'Inverted object', color= '#67a9cf')
ax.fill_between(x, Mean_obj_U - SEM_obj_U, Mean_obj_U + SEM_obj_U, alpha=0.2, color= '#67a9cf')


# ax.set_ylim(-0.02,0.18) # For theta power
ax.set_ylim(-0.15,0.37)
ax.legend()

#%% Peak detection within a time-window

import matplotlib.pyplot as plt
import numpy as np

# Time vector (assumes 104 time points from -0.2 to 0.6 s)
x = np.linspace(-0.2, 0.6, 104)

# ---- Helper: get peak VALUE and LATENCY within a time window ----
def get_peak_in_window(erd_list, tvec, win_ms=(50, 150), kind='max'):
    """
    erd_list: iterable of 1D arrays (one per subject), len == len(tvec)
    tvec: time vector in seconds
    win_ms: (start_ms, end_ms)
    kind: 'max' for peak, 'min' for trough
    Returns: (list_of_peak_values, list_of_peak_latencies_ms)
    """
    tmin, tmax = (win_ms[0] / 1000.0, win_ms[1] / 1000.0)
    mask = (tvec >= tmin) & (tvec <= tmax)

    peak_vals = []
    peak_lats = []
    # Precompute the time subvector for the window
    t_sub = tvec[mask]

    for subj in erd_list:
        # Guard: subject length must match tvec
        if len(subj) != len(tvec) or t_sub.size == 0:
            peak_vals.append(np.nan)
            peak_lats.append(np.nan)
            continue

        seg = subj[mask]

        # If all NaN in the segment, return NaNs
        if np.all(np.isnan(seg)):
            peak_vals.append(np.nan)
            peak_lats.append(np.nan)
            continue

        # Use nanargmax/nanargmin to ignore NaNs
        if kind == 'max':
            idx = np.nanargmax(seg)
        elif kind == 'min':
            idx = np.nanargmin(seg)
        else:
            raise ValueError("kind must be 'max' or 'min'")

        peak_vals.append(seg[idx])
        peak_lats.append(t_sub[idx] * 1000.0)  # ms

    return peak_vals, peak_lats


# ---- Apply to each list: get MAX peak in 50–150 ms ----
groups = [
    Alpha_suppression_face_TD,
    Alpha_suppression_face_ASD,
    Alpha_suppression_face_SIB,

    Alpha_suppression_U_face_TD,
    Alpha_suppression_U_face_ASD,
    Alpha_suppression_U_face_SIB,

    Alpha_suppression_obj_TD,
    Alpha_suppression_obj_ASD,
    Alpha_suppression_obj_SIB,

    Alpha_suppression_U_obj_TD,
    Alpha_suppression_U_obj_ASD,
    Alpha_suppression_U_obj_SIB,
]

peak_values = []
peak_latencies = []
for G in groups:
    vals, lats = get_peak_in_window(G, x, win_ms=(50, 110), kind='max')
    peak_values.append(vals)
    peak_latencies.append(lats)

# ---- Plot: boxplots of MAX peak VALUES in 50–150 ms ----
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
for i, (data, label, color) in enumerate(zip(peak_values, x_labels, colors), start=1):
    ax.boxplot(data, positions=[i], patch_artist=True, widths=0.6,
               boxprops=dict(facecolor=color, color=color),
               capprops=dict(color=color),
               whiskerprops=dict(color=color),
               flierprops=dict(markerfacecolor=color, marker='o', markersize=4, linestyle='none'),
               medianprops=dict(color='black'))

ax.set_xticks(range(1, 13))
ax.set_xticklabels(x_labels, rotation=45, ha='right')
ax.set_ylabel('Max Alpha Power (50–150 ms window, a.u.)')
ax.set_title('Peak Alpha (50–150 ms) Across Groups & Conditions')
ax.axvline(6.5, color='gray', linestyle='--', lw=1)
ax.text(3.5, ax.get_ylim()[1], 'Faces', ha='center', va='bottom', fontsize=10, weight='bold')
ax.text(9.5, ax.get_ylim()[1], 'Objects', ha='center', va='bottom', fontsize=10, weight='bold')
ax.grid(axis='y')
plt.tight_layout()
plt.show()

#%% Average amplitude within a time-window

import matplotlib.pyplot as plt
import numpy as np

# Time vector (assumes 104 time points from -0.2 to 0.6 s)
x = np.linspace(-0.2, 0.6, 104)

# ---- Helper: mean VALUE within a time window ----
def get_mean_in_window(erd_list, tvec, win_ms=(150, 230)):
    """
    erd_list: iterable of 1D arrays (one per subject), len == len(tvec)
    tvec: time vector in seconds
    win_ms: (start_ms, end_ms)
    Returns: list_of_window_means (NaN-safe)
    """
    tmin, tmax = (win_ms[0] / 1000.0, win_ms[1] / 1000.0)
    mask = (tvec >= tmin) & (tvec <= tmax)
    t_sub = tvec[mask]

    means = []
    for subj in erd_list:
        if len(subj) != len(tvec) or t_sub.size == 0:
            means.append(np.nan)
            continue
        seg = subj[mask]
        # NaN-safe mean
        if np.all(np.isnan(seg)):
            means.append(np.nan)
        else:
            means.append(np.nanmean(seg))
    return means

# ---- Apply to each list: mean in 50–150 ms ----
groups = [
    Alpha_suppression_face_TD,
    Alpha_suppression_face_ASD,
    Alpha_suppression_face_SIB,

    Alpha_suppression_U_face_TD,
    Alpha_suppression_U_face_ASD,
    Alpha_suppression_U_face_SIB,

    Alpha_suppression_obj_TD,
    Alpha_suppression_obj_ASD,
    Alpha_suppression_obj_SIB,

    Alpha_suppression_U_obj_TD,
    Alpha_suppression_U_obj_ASD,
    Alpha_suppression_U_obj_SIB,
]

mean_values = [get_mean_in_window(G, x, win_ms=(50, 110)) for G in groups]

# ---- Plot: boxplots of MEAN values in 50–150 ms ----
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
for i, (data, label, color) in enumerate(zip(mean_values, x_labels, colors), start=1):
    ax.boxplot(data, positions=[i], patch_artist=True, widths=0.6,
               boxprops=dict(facecolor=color, color=color),
               capprops=dict(color=color),
               whiskerprops=dict(color=color),
               flierprops=dict(markerfacecolor=color, marker='o', markersize=4, linestyle='none'),
               medianprops=dict(color='black'))

ax.set_xticks(range(1, 13))
ax.set_xticklabels(x_labels, rotation=45, ha='right')
ax.set_ylabel('Mean Alpha (50–150 ms window, a.u.)')
ax.set_title('Mean Alpha (50–150 ms) Across Groups & Conditions')
ax.axvline(6.5, color='gray', linestyle='--', lw=1)
ax.text(3.5, ax.get_ylim()[1], 'Faces', ha='center', va='bottom', fontsize=10, weight='bold')
ax.text(9.5, ax.get_ylim()[1], 'Objects', ha='center', va='bottom', fontsize=10, weight='bold')
ax.grid(axis='y')
plt.tight_layout()
plt.show()


#%%

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(4, 1, figsize=(10, 8))

fmin=29
fmax=40

tmin1 = 0.05
tmax1 = 0.13

#Audiovisual scale
vlim1 = -0.15
vlim2= 0.15

# M_Power_NPL_face_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
# M_Power_NPL_face_U_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
# M_Power_NPL_obj_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
# M_Power_NPL_obj_U_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)


# M_Power_NPL_face_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
# M_Power_NPL_face_U_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
# M_Power_NPL_obj_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
# M_Power_NPL_obj_U_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)


M_Power_NPL_face_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
M_Power_NPL_face_U_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
M_Power_NPL_obj_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
M_Power_NPL_obj_U_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)


# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()