# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 17:28:46 2025

@author: tvanneau
"""

#%% For faces

# Load pickle file with corresponding power data 
import os
import pickle
import mne
import matplotlib.pyplot as plt

# with open('Power_face_TD.pkl', 'rb') as f:
#     [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)
with open('Power_face_TD_Gamma.pkl', 'rb') as f:
    [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)

# with open('Power_face_all_TD.pkl', 'rb') as f:
#     [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)
# with open('Power_face_ASD.pkl', 'rb') as f:
#     [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)
# with open('Power_face_ASD_Gamma.pkl', 'rb') as f:
#     [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)

# with open('Power_face_SIB.pkl', 'rb') as f:
#     [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)
# with open('Power_face_SIB_Gamma.pkl', 'rb') as f:
#     [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_face_TD)):
    Power_NPL_face_TD[i].apply_baseline(baseline=baseline, mode='percent')
# Apply baseline correction to each subject's power
for i in range(len(Power_face_TD)):
    Power_face_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_TD = mne.grand_average(Power_NPL_face_TD)

# with open('Power_face_U_TD.pkl', 'rb') as f:
#     [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
# with open('Power_face_shadow_TD.pkl', 'rb') as f:
#     [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
with open('Power_face_U_TD_Gamma.pkl', 'rb') as f:
    [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)

# with open('Power_face_U_all_TD.pkl', 'rb') as f:
#     [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
# with open('Power_face_U_ASD.pkl', 'rb') as f:
#     [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
# with open('Power_face_U_ASD_Gamma.pkl', 'rb') as f:
#     [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)

# with open('Power_face_U_SIB.pkl', 'rb') as f:
#     [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
# with open('Power_face_U_SIB_Gamma.pkl', 'rb') as f:
#     [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_face_U_TD)):
    Power_NPL_face_U_TD[i].apply_baseline(baseline=baseline, mode='percent')
# Apply baseline correction to each subject's power
for i in range(len(Power_face_U_TD)):
    Power_face_U_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_U_TD = mne.grand_average(Power_NPL_face_U_TD)

# with open('Power_obj_TD.pkl', 'rb') as f:
#     [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)
# with open('Power_obj_TD_Gamma.pkl', 'rb') as f:
#     [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)

# with open('Power_obj_all_TD.pkl', 'rb') as f:
#     [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)
# with open('Power_obj_ASD.pkl', 'rb') as f:
#     [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)
# with open('Power_obj_ASD_Gamma.pkl', 'rb') as f:
#     [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)

# with open('Power_obj_SIB.pkl', 'rb') as f:
#     [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)
# with open('Power_obj_SIB_Gamma.pkl', 'rb') as f:
#     [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_obj_TD)):
    Power_NPL_obj_TD[i].apply_baseline(baseline=baseline, mode='percent')
# Apply baseline correction to each subject's power
for i in range(len(Power_obj_TD)):
    Power_obj_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_TD = mne.grand_average(Power_NPL_obj_TD)

# with open('Power_obj_U_TD.pkl', 'rb') as f:
#     [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)
# with open('Power_obj_U_TD_Gamma.pkl', 'rb') as f:
#     [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)

# with open('Power_obj_U_all_TD.pkl', 'rb') as f:
#     [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)
# with open('Power_obj_U_ASD.pkl', 'rb') as f:
#     [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)
# with open('Power_obj_U_ASD_Gamma.pkl', 'rb') as f:
#     [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)

# with open('Power_obj_U_SIB.pkl', 'rb') as f:
#     [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)
# with open('Power_obj_U_SIB_Gamma.pkl', 'rb') as f:
#     [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.15, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_obj_U_TD)):
    Power_NPL_obj_U_TD[i].apply_baseline(baseline=baseline, mode='percent')
for i in range(len(Power_NPL_obj_U_TD)):
    Power_obj_U_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_U_TD = mne.grand_average(Power_NPL_obj_U_TD)

#%%

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(4, 1, figsize=(10, 8))

fmin=25
fmax=40

tmin1 = 0.05
tmax1 = 0.13

#Audiovisual scale
vlim1 = -0.15
vlim2= 0.15

M_Power_NPL_face_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
M_Power_NPL_face_U_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
M_Power_NPL_obj_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
M_Power_NPL_obj_U_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)


# M_Power_NPL_face_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
# M_Power_NPL_face_U_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
# M_Power_NPL_obj_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
# M_Power_NPL_obj_U_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)


# M_Power_NPL_face_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
# M_Power_NPL_face_U_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
# M_Power_NPL_obj_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
# M_Power_NPL_obj_U_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)


# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%%

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(4, 1, figsize=(10, 8))

fmin=4
fmax=7

tmin1 = 0.2
tmax1 = 0.4

#Audiovisual scale
vlim1 = -0.7
vlim2= 0.6

M_Power_NPL_face_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
M_Power_NPL_face_U_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
M_Power_NPL_obj_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
M_Power_NPL_obj_U_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%%

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(4, 1, figsize=(10, 8))

fmin=13
fmax=25

tmin1 = 0.05
tmax1 = 0.15

#Audiovisual scale
vlim1 = -0.1
vlim2= 0.1

M_Power_NPL_face_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
M_Power_NPL_face_U_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
M_Power_NPL_obj_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
M_Power_NPL_obj_U_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%% Time-frequency maps

# Centro-frontal - Auditory stimulation

# Occipital - Visual stimulation
# Electrodes = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']

# Electrodes = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz']

# Electrodes = ['O2', 'PO4', 'PO8' ]

Electrodes = ['Iz', 'Oz', 'POz', 'O1', 'O2' ]

# Electrodes = ['O1', 'PO3', 'PO7' ]

# Electrodes = ['Cz','C1','C2','FC1','FCz','FC2']

# Alpha scale for visual and audiovisual
M_Power_NPL_face_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vlim=(-0.2,0.2),fmin=2,fmax=40)
M_Power_NPL_face_U_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vlim=(-0.2,0.2),fmin=2,fmax=40)
M_Power_NPL_obj_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vlim=(-0.2,0.2),fmin=2,fmax=40)
M_Power_NPL_obj_U_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vlim=(-0.2,0.2),fmin=2,fmax=40)

# # Alpha scale for visual and audiovisual
# M_Power_NPL_face_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vmin=-0.2,vmax=0.2,fmin=25,fmax=40)
# M_Power_NPL_face_U_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vmin=-0.2,vmax=0.2,fmin=25,fmax=40)
# M_Power_NPL_obj_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vmin=-0.2,vmax=0.2,fmin=25,fmax=40)
# M_Power_NPL_obj_U_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vmin=-0.2,vmax=0.2,fmin=25,fmax=40)

#%% Alpha suppression for Induced power for TD
import numpy as np

freqs = np.linspace(*np.array([4, 40]), num=100) #num = step / bin allows a precision of the frequency resolution
# freqs = np.linspace(*np.array([4, 20]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz']

# channels = ['O2', 'PO4', 'PO8' ]

# channels = ['O1', 'PO3', 'PO7' ]
# channels = ['Iz', 'Oz', 'POz', 'O1', 'O2' ]

channels = ['C5', 'C3',
            'C4', 'C6']


# channels = ['O1', 'O2', 'POz', 'Oz']

# channels = ['P8']

tmin = -0.2
tmax = 0.6

# Alpha_min = 19 # 13Hz
# Alpha_max = 56 # 25Hz

# Alpha_min = 9 # 13Hz
# Alpha_max = 24 # 25Hz

# Alpha_min = 25 # 13Hz
# Alpha_max = 58 # 25Hz

Alpha_min = 59 # 13Hz
Alpha_max = 99 # 25Hz

Alpha_suppression_face_TD = []
Alpha_suppression_U_face_TD = []

Alpha_suppression_obj_TD = []
Alpha_suppression_U_obj_TD = []

for i in range(0,len(Power_NPL_face_TD),1):
    Aph_TD = Power_NPL_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_face_TD.append(Fa_TD)

for i in range(0,len(Power_NPL_face_U_TD),1):
    Aph_TD = Power_NPL_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_face_TD.append(Fa_TD)
    
for i in range(0,len(Power_NPL_obj_TD),1):
    Aph_TD = Power_NPL_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_obj_TD.append(Fa_TD)
    
for i in range(0,len(Power_NPL_obj_U_TD),1):
    Aph_TD = Power_NPL_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_obj_TD.append(Fa_TD)
    
# # For total power
# for i in range(0,len(Power_face_TD),1):
#     Aph_TD = Power_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_face_TD.append(Fa_TD)

# for i in range(0,len(Power_face_U_TD),1):
#     Aph_TD = Power_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_U_face_TD.append(Fa_TD)
    
# for i in range(0,len(Power_obj_TD),1):
#     Aph_TD = Power_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_obj_TD.append(Fa_TD)
    
# for i in range(0,len(Power_obj_U_TD),1):
#     Aph_TD = Power_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_U_obj_TD.append(Fa_TD)
    
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
ax.set_ylim(-0.15,0.3)
ax.legend()

#%% Alpha suppression for Induced power for ASD
import numpy as np

freqs = np.linspace(*np.array([4, 20]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz']

# channels = ['O1', 'O2', 'POz', 'Oz']

# channels = ['P8']

tmin = -0.2
tmax = 0.6

Alpha_min = 19 # 7Hz
Alpha_max = 56 # 13Hz

Alpha_suppression_face_ASD = []
Alpha_suppression_U_face_ASD = []

Alpha_suppression_obj_ASD= []
Alpha_suppression_U_obj_ASD = []

for i in range(0,len(Power_NPL_face_TD),1):
    Aph_TD = Power_NPL_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_face_ASD.append(Fa_TD)

for i in range(0,len(Power_NPL_face_U_TD),1):
    Aph_TD = Power_NPL_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_face_ASD.append(Fa_TD)
    
for i in range(0,len(Power_NPL_obj_TD),1):
    Aph_TD = Power_NPL_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_obj_ASD.append(Fa_TD)
    
for i in range(0,len(Power_NPL_obj_U_TD),1):
    Aph_TD = Power_NPL_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
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
ax.set_ylim(-0.50,0.07)
ax.legend()

#%% Alpha suppression for Induced power for SIB
import numpy as np

freqs = np.linspace(*np.array([4, 20]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz']

# channels = ['O1', 'O2', 'POz', 'Oz']

# channels = ['P8']

tmin = -0.2
tmax = 0.6

Alpha_min = 19 # 7Hz
Alpha_max = 56 # 13Hz

Alpha_suppression_face_SIB = []
Alpha_suppression_U_face_SIB = []

Alpha_suppression_obj_SIB= []
Alpha_suppression_U_obj_SIB = []

for i in range(0,len(Power_NPL_face_TD),1):
    Aph_TD = Power_NPL_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_face_SIB.append(Fa_TD)

for i in range(0,len(Power_NPL_face_U_TD),1):
    Aph_TD = Power_NPL_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_face_SIB.append(Fa_TD)
    
for i in range(0,len(Power_NPL_obj_TD),1):
    Aph_TD = Power_NPL_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_obj_SIB.append(Fa_TD)
    
for i in range(0,len(Power_NPL_obj_U_TD),1):
    Aph_TD = Power_NPL_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
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
ax.set_ylim(-0.50,0.07)
ax.legend()


#%%

import matplotlib.pyplot as plt
import numpy as np

# Time vector (assumes 104 time points from -0.2 to 0.6s)
x = np.linspace(-0.2, 0.6, 104)

# 🧠 Detect latency of max alpha suppression (most negative point)
def get_min_latency(erd_list):
    return [x[np.argmin(subject)] * 1000 for subject in erd_list]  # convert to ms

def get_min_value(erd_list):
    return [np.min(subject) for subject in erd_list]  # directly get the ERD value


# --- Apply to each list ---
latencies = [
    get_min_latency(Alpha_suppression_face_TD),
    get_min_latency(Alpha_suppression_face_ASD),
    get_min_latency(Alpha_suppression_face_SIB),
    
    get_min_latency(Alpha_suppression_U_face_TD),
    get_min_latency(Alpha_suppression_U_face_ASD),
    get_min_latency(Alpha_suppression_U_face_SIB),
    
    get_min_latency(Alpha_suppression_obj_TD),
    get_min_latency(Alpha_suppression_obj_ASD),
    get_min_latency(Alpha_suppression_obj_SIB),
    
    get_min_latency(Alpha_suppression_U_obj_TD),
    get_min_latency(Alpha_suppression_U_obj_ASD),
    get_min_latency(Alpha_suppression_U_obj_SIB),
]

# --- Apply to each list ---
latencies = [
    get_min_value(Alpha_suppression_face_TD),
    get_min_value(Alpha_suppression_face_ASD),
    get_min_value(Alpha_suppression_face_SIB),
    
    get_min_value(Alpha_suppression_U_face_TD),
    get_min_value(Alpha_suppression_U_face_ASD),
    get_min_value(Alpha_suppression_U_face_SIB),
    
    get_min_value(Alpha_suppression_obj_TD),
    get_min_value(Alpha_suppression_obj_ASD),
    get_min_value(Alpha_suppression_obj_SIB),
    
    get_min_value(Alpha_suppression_U_obj_TD),
    get_min_value(Alpha_suppression_U_obj_ASD),
    get_min_value(Alpha_suppression_U_obj_SIB),
]

# Labels and colors
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

# --- Plot ---
fig, ax = plt.subplots(figsize=(12, 5))

for i, (data, label, color) in enumerate(zip(latencies, x_labels, colors), start=1):
    ax.boxplot(data, positions=[i], patch_artist=True, widths=0.6,
               boxprops=dict(facecolor=color, color=color),
               capprops=dict(color=color),
               whiskerprops=dict(color=color),
               flierprops=dict(markerfacecolor=color, marker='o', markersize=4, linestyle='none'),
               medianprops=dict(color='black'))

ax.set_xticks(range(1, 13))
ax.set_xticklabels(x_labels, rotation=45, ha='right')
ax.set_ylabel('Latency of Max Alpha Suppression (ms)')
ax.set_title('Latency of Alpha ERD Minimum Across Groups & Conditions')
ax.axvline(6.5, color='gray', linestyle='--', lw=1)
ax.text(3.5, ax.get_ylim()[1], 'Faces', ha='center', va='bottom', fontsize=10, weight='bold')
ax.text(9.5, ax.get_ylim()[1], 'Objects', ha='center', va='bottom', fontsize=10, weight='bold')
ax.grid(axis='y')
plt.tight_layout()
plt.show()

#%%

def get_mean_alpha_ERD(erd_list, x, tmin=0.2, tmax=0.5):
    """
    Extract average alpha ERD in a time window for a list of ERD time series (1 per subject)
    """
    idx_start = np.argmin(np.abs(x - tmin))
    idx_end = np.argmin(np.abs(x - tmax)) + 1  # +1 to include the end point

    return [np.mean(subject[idx_start:idx_end]) for subject in erd_list]


# Time vector
x = np.linspace(-0.2, 0.6, 104)

# Apply to each list of ERD
erd_avg_0_150 = [
    get_mean_alpha_ERD(Alpha_suppression_face_TD, x),
    get_mean_alpha_ERD(Alpha_suppression_face_ASD, x),
    get_mean_alpha_ERD(Alpha_suppression_face_SIB, x),

    get_mean_alpha_ERD(Alpha_suppression_U_face_TD, x),
    get_mean_alpha_ERD(Alpha_suppression_U_face_ASD, x),
    get_mean_alpha_ERD(Alpha_suppression_U_face_SIB, x),

    get_mean_alpha_ERD(Alpha_suppression_obj_TD, x),
    get_mean_alpha_ERD(Alpha_suppression_obj_ASD, x),
    get_mean_alpha_ERD(Alpha_suppression_obj_SIB, x),

    get_mean_alpha_ERD(Alpha_suppression_U_obj_TD, x),
    get_mean_alpha_ERD(Alpha_suppression_U_obj_ASD, x),
    get_mean_alpha_ERD(Alpha_suppression_U_obj_SIB, x),
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

for i, (y, label, color) in enumerate(zip(erd_avg_0_150, x_labels, colors), start=1):
    ax.boxplot(y, positions=[i], patch_artist=True, widths=0.6,
               boxprops=dict(facecolor=color, color=color),
               capprops=dict(color=color),
               whiskerprops=dict(color=color),
               flierprops=dict(markerfacecolor=color, marker='o', markersize=4, linestyle='none'),
               medianprops=dict(color='black'))

ax.set_xticks(range(1, 13))
ax.set_xticklabels(x_labels, rotation=45, ha='right')
ax.set_ylabel('Avg Alpha ERD (0–150 ms, µV²)')
ax.set_title('Mean Early Alpha Suppression Across Groups & Conditions')
ax.axvline(6.5, color='gray', linestyle='--', lw=1)
ax.text(3.5, ax.get_ylim()[1], 'Faces', ha='center', va='bottom', fontsize=10, weight='bold')
ax.text(9.5, ax.get_ylim()[1], 'Objects', ha='center', va='bottom', fontsize=10, weight='bold')
ax.grid(axis='y')
plt.tight_layout()
plt.show()



#%% Theta synchronisation for Induced power for TD
import numpy as np

freqs = np.linspace(*np.array([4, 20]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz']

# channels = ['O1', 'O2', 'POz', 'Oz']

channels = ['Cz','C1','C2','FC1','FCz','FC2']

tmin = -0.2
tmax = 0.6

Alpha_min = 0 # 7Hz
Alpha_max = 18 # 13Hz

Alpha_suppression_face_TD = []
Alpha_suppression_U_face_TD = []

Alpha_suppression_obj_TD = []
Alpha_suppression_U_obj_TD = []

for i in range(0,len(Power_NPL_face_TD),1):
    Aph_TD = Power_NPL_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_face_TD.append(Fa_TD)

for i in range(0,len(Power_NPL_face_U_TD),1):
    Aph_TD = Power_NPL_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_face_TD.append(Fa_TD)
    
for i in range(0,len(Power_NPL_obj_TD),1):
    Aph_TD = Power_NPL_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_obj_TD.append(Fa_TD)
    
for i in range(0,len(Power_NPL_obj_U_TD),1):
    Aph_TD = Power_NPL_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
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
ax.set_ylim(-0.05,0.59)
ax.legend()

#%% Theta synchronisation for Induced power for ASD
import numpy as np

freqs = np.linspace(*np.array([4, 20]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz']

# channels = ['O1', 'O2', 'POz', 'Oz']

channels = ['Cz','C1','C2','FC1','FCz','FC2']

tmin = -0.2
tmax = 0.6

Alpha_min = 0 # 7Hz
Alpha_max = 18 # 13Hz

Alpha_suppression_face_ASD = []
Alpha_suppression_U_face_ASD = []

Alpha_suppression_obj_ASD= []
Alpha_suppression_U_obj_ASD = []

for i in range(0,len(Power_NPL_face_TD),1):
    Aph_TD = Power_NPL_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_face_ASD.append(Fa_TD)

for i in range(0,len(Power_NPL_face_U_TD),1):
    Aph_TD = Power_NPL_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_face_ASD.append(Fa_TD)
    
for i in range(0,len(Power_NPL_obj_TD),1):
    Aph_TD = Power_NPL_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_obj_ASD.append(Fa_TD)
    
for i in range(0,len(Power_NPL_obj_U_TD),1):
    Aph_TD = Power_NPL_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
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
ax.set_ylim(-0.05,0.59)
ax.legend()

#%% Alpha suppression for Induced power for SIB
import numpy as np

freqs = np.linspace(*np.array([4, 20]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz']

# channels = ['O1', 'O2', 'POz', 'Oz']

# channels = ['P8']

channels = ['Cz','C1','C2','FC1','FCz','FC2']

tmin = -0.2
tmax = 0.6

Alpha_min = 0 # 7Hz
Alpha_max = 18 # 13Hz

Alpha_suppression_face_SIB = []
Alpha_suppression_U_face_SIB = []

Alpha_suppression_obj_SIB= []
Alpha_suppression_U_obj_SIB = []

for i in range(0,len(Power_NPL_face_TD),1):
    Aph_TD = Power_NPL_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_face_SIB.append(Fa_TD)

for i in range(0,len(Power_NPL_face_U_TD),1):
    Aph_TD = Power_NPL_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_face_SIB.append(Fa_TD)
    
for i in range(0,len(Power_NPL_obj_TD),1):
    Aph_TD = Power_NPL_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_obj_SIB.append(Fa_TD)
    
for i in range(0,len(Power_NPL_obj_U_TD),1):
    Aph_TD = Power_NPL_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
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
ax.set_ylim(-0.05,0.59)
ax.legend()


#%%

def get_mean_alpha_ERD(erd_list, x, tmin=0.0, tmax=0.150):
    """
    Extract average alpha ERD in a time window for a list of ERD time series (1 per subject)
    """
    idx_start = np.argmin(np.abs(x - tmin))
    idx_end = np.argmin(np.abs(x - tmax)) + 1  # +1 to include the end point

    return [np.mean(subject[idx_start:idx_end]) for subject in erd_list]


# Time vector
x = np.linspace(-0.2, 0.6, 104)

# Apply to each list of ERD
erd_avg_0_150 = [
    get_mean_alpha_ERD(Alpha_suppression_face_TD, x),
    get_mean_alpha_ERD(Alpha_suppression_face_ASD, x),
    get_mean_alpha_ERD(Alpha_suppression_face_SIB, x),

    get_mean_alpha_ERD(Alpha_suppression_U_face_TD, x),
    get_mean_alpha_ERD(Alpha_suppression_U_face_ASD, x),
    get_mean_alpha_ERD(Alpha_suppression_U_face_SIB, x),

    get_mean_alpha_ERD(Alpha_suppression_obj_TD, x),
    get_mean_alpha_ERD(Alpha_suppression_obj_ASD, x),
    get_mean_alpha_ERD(Alpha_suppression_obj_SIB, x),

    get_mean_alpha_ERD(Alpha_suppression_U_obj_TD, x),
    get_mean_alpha_ERD(Alpha_suppression_U_obj_ASD, x),
    get_mean_alpha_ERD(Alpha_suppression_U_obj_SIB, x),
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

for i, (y, label, color) in enumerate(zip(erd_avg_0_150, x_labels, colors), start=1):
    ax.boxplot(y, positions=[i], patch_artist=True, widths=0.6,
               boxprops=dict(facecolor=color, color=color),
               capprops=dict(color=color),
               whiskerprops=dict(color=color),
               flierprops=dict(markerfacecolor=color, marker='o', markersize=4, linestyle='none'),
               medianprops=dict(color='black'))

ax.set_xticks(range(1, 13))
ax.set_xticklabels(x_labels, rotation=45, ha='right')
ax.set_ylabel('Avg Alpha ERD (0–150 ms, µV²)')
ax.set_title('Mean Early Alpha Suppression Across Groups & Conditions')
ax.axvline(6.5, color='gray', linestyle='--', lw=1)
ax.text(3.5, ax.get_ylim()[1], 'Faces', ha='center', va='bottom', fontsize=10, weight='bold')
ax.text(9.5, ax.get_ylim()[1], 'Objects', ha='center', va='bottom', fontsize=10, weight='bold')
ax.grid(axis='y')
plt.tight_layout()
plt.show()

#%% For max peak detection - amplitude and latency

import matplotlib.pyplot as plt
import numpy as np

# Time vector (assumes 104 time points from -0.2 to 0.6s)
x = np.linspace(-0.2, 0.6, 104)

# 🧠 Detect latency of max alpha suppression (most negative point)
def get_min_latency(erd_list):
    return [x[np.argmax(subject)] * 1000 for subject in erd_list]  # convert to ms

def get_min_value(erd_list):
    return [np.max(subject) for subject in erd_list]  # directly get the ERD value


# # --- Apply to each list ---
# latencies = [
#     get_min_latency(Alpha_suppression_face_TD),
#     get_min_latency(Alpha_suppression_face_ASD),
#     get_min_latency(Alpha_suppression_face_SIB),
    
#     get_min_latency(Alpha_suppression_U_face_TD),
#     get_min_latency(Alpha_suppression_U_face_ASD),
#     get_min_latency(Alpha_suppression_U_face_SIB),
    
#     get_min_latency(Alpha_suppression_obj_TD),
#     get_min_latency(Alpha_suppression_obj_ASD),
#     get_min_latency(Alpha_suppression_obj_SIB),
    
#     get_min_latency(Alpha_suppression_U_obj_TD),
#     get_min_latency(Alpha_suppression_U_obj_ASD),
#     get_min_latency(Alpha_suppression_U_obj_SIB),
# ]

# --- Apply to each list ---
latencies = [
    get_min_value(Alpha_suppression_face_TD),
    get_min_value(Alpha_suppression_face_ASD),
    get_min_value(Alpha_suppression_face_SIB),
    
    get_min_value(Alpha_suppression_U_face_TD),
    get_min_value(Alpha_suppression_U_face_ASD),
    get_min_value(Alpha_suppression_U_face_SIB),
    
    get_min_value(Alpha_suppression_obj_TD),
    get_min_value(Alpha_suppression_obj_ASD),
    get_min_value(Alpha_suppression_obj_SIB),
    
    get_min_value(Alpha_suppression_U_obj_TD),
    get_min_value(Alpha_suppression_U_obj_ASD),
    get_min_value(Alpha_suppression_U_obj_SIB),
]

# Labels and colors
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

# --- Plot ---
fig, ax = plt.subplots(figsize=(12, 5))

for i, (data, label, color) in enumerate(zip(latencies, x_labels, colors), start=1):
    ax.boxplot(data, positions=[i], patch_artist=True, widths=0.6,
               boxprops=dict(facecolor=color, color=color),
               capprops=dict(color=color),
               whiskerprops=dict(color=color),
               flierprops=dict(markerfacecolor=color, marker='o', markersize=4, linestyle='none'),
               medianprops=dict(color='black'))

ax.set_xticks(range(1, 13))
ax.set_xticklabels(x_labels, rotation=45, ha='right')
ax.set_ylabel('Latency of Max Alpha Suppression (ms)')
ax.set_title('Latency of Alpha ERD Minimum Across Groups & Conditions')
ax.axvline(6.5, color='gray', linestyle='--', lw=1)
ax.text(3.5, ax.get_ylim()[1], 'Faces', ha='center', va='bottom', fontsize=10, weight='bold')
ax.text(9.5, ax.get_ylim()[1], 'Objects', ha='center', va='bottom', fontsize=10, weight='bold')
ax.grid(axis='y')
plt.tight_layout()
plt.show()

#%%

import matplotlib.pyplot as plt
import numpy as np

# Time vector (assumes 104 time points from -0.2 to 0.6 s)
x = np.linspace(-0.2, 0.6, 104)

# ---- Helper: get peak VALUE and LATENCY within a time window ----
def get_peak_in_window(erd_list, tvec, win_ms=(50, 150), kind='max'):
    """
    erd_list: list of 1D arrays (subjects), each length == len(tvec)
    tvec: time vector in seconds
    win_ms: (start_ms, end_ms)
    kind: 'max' (peak) or 'min' (trough)
    Returns: (list_of_peak_values, list_of_peak_latencies_ms)
    """
    tmin, tmax = [w / 1000.0 for w in win_ms]
    mask = (tvec >= tmin) & (tvec <= tmax)

    peak_vals, peak_lats = []
    peak_lats = []
    peak_vals = []
    for subj in erd_list:
        seg = subj[mask]
        if seg.size == 0:
            peak_vals.append(np.nan)
            peak_lats.append(np.nan)
            continue
        idx = np.argmax(seg) if kind == 'max' else np.argmin(seg)
        peak_vals.append(seg[idx])
        peak_lats.append(tvec[mask][idx] * 1000.0)  # ms
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
    vals, lats = get_peak_in_window(G, x, win_ms=(50, 150), kind='max')
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


#%% For ITPC - TD

# Load pickle file with corresponding power data 
import os
import pickle
import mne
import matplotlib.pyplot as plt

with open('Power_face_TD.pkl', 'rb') as f:
    [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.25, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_face_TD)):
    Power_NPL_face_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_TD = mne.grand_average(Power_NPL_face_TD)
# M_Power_NPL_face_TD = mne.grand_average(ITPC_face_TD)


with open('Power_face_U_TD.pkl', 'rb') as f:
    [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
    
# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_face_U_TD)):
    Power_NPL_face_U_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_U_TD = mne.grand_average(Power_NPL_face_U_TD)

# M_Power_NPL_face_U_TD = mne.grand_average(ITPC_face_U_TD)


with open('Power_obj_TD.pkl', 'rb') as f:
    [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)
    
# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_obj_TD)):
    Power_NPL_obj_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_TD = mne.grand_average(Power_NPL_obj_TD)

# M_Power_NPL_obj_TD = mne.grand_average(ITPC_obj_TD)


with open('Power_obj_U_TD.pkl', 'rb') as f:
    [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)
    

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_obj_U_TD)):
    Power_NPL_obj_U_TD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_U_TD = mne.grand_average(Power_NPL_obj_U_TD)

# M_Power_NPL_obj_U_TD = mne.grand_average(ITPC_obj_U_TD)

#%% For ITPC - TD GAMMA

# Load pickle file with corresponding power data 
import os
import pickle
import mne
import matplotlib.pyplot as plt

# with open('Power_face_all_ASD.pkl', 'rb') as f:
#     [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)
with open('Power_face_TD_Gamma.pkl', 'rb') as f:
    [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)

M_Power_NPL_face_TD = mne.grand_average(ITPC_face_TD)

# with open('Power_face_U_all_ASD.pkl', 'rb') as f:
#     [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
with open('Power_face_U_TD_Gamma.pkl', 'rb') as f:
    [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)

M_Power_NPL_face_U_TD = mne.grand_average(ITPC_face_U_TD)


# with open('Power_obj_all_ASD.pkl', 'rb') as f:
#     [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)
with open('Power_obj_TD_Gamma.pkl', 'rb') as f:
    [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)

M_Power_NPL_obj_TD = mne.grand_average(ITPC_obj_TD)


# with open('Power_obj_U_all_ASD.pkl', 'rb') as f:
#     [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)
with open('Power_obj_U_TD_Gamma.pkl', 'rb') as f:
    [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)

M_Power_NPL_obj_U_TD = mne.grand_average(ITPC_obj_U_TD)

#%% For ITPC - TD GAMMA

# Load pickle file with corresponding power data 
import os
import pickle
import mne
import matplotlib.pyplot as plt

# with open('Power_face_all_ASD.pkl', 'rb') as f:
#     [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)
with open('Power_face_ASD_Gamma.pkl', 'rb') as f:
    [Power_face_TD,Power_NPL_face_TD,ITPC_face_ASD] = pickle.load(f)

M_Power_NPL_face_TD = mne.grand_average(ITPC_face_TD)

# with open('Power_face_U_all_ASD.pkl', 'rb') as f:
#     [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
with open('Power_face_U_ASD_Gamma.pkl', 'rb') as f:
    [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_ASD] = pickle.load(f)

M_Power_NPL_face_U_TD = mne.grand_average(ITPC_face_U_TD)


# with open('Power_obj_all_ASD.pkl', 'rb') as f:
#     [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)
with open('Power_obj_ASD_Gamma.pkl', 'rb') as f:
    [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_ASD] = pickle.load(f)

M_Power_NPL_obj_TD = mne.grand_average(ITPC_obj_TD)


# with open('Power_obj_U_all_ASD.pkl', 'rb') as f:
#     [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)
with open('Power_obj_U_ASD_Gamma.pkl', 'rb') as f:
    [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_ASD] = pickle.load(f)

M_Power_NPL_obj_U_TD = mne.grand_average(ITPC_obj_U_TD)

#%% For ITPC - TD GAMMA

# Load pickle file with corresponding power data 
import os
import pickle
import mne
import matplotlib.pyplot as plt

# with open('Power_face_all_ASD.pkl', 'rb') as f:
#     [Power_face_TD,Power_NPL_face_TD,ITPC_face_TD] = pickle.load(f)
with open('Power_face_SIB_Gamma.pkl', 'rb') as f:
    [Power_face_TD,Power_NPL_face_TD,ITPC_face_SIB] = pickle.load(f)

M_Power_NPL_face_TD = mne.grand_average(ITPC_face_TD)

# with open('Power_face_U_all_ASD.pkl', 'rb') as f:
#     [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_TD] = pickle.load(f)
with open('Power_face_U_SIB_Gamma.pkl', 'rb') as f:
    [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_SIB] = pickle.load(f)

M_Power_NPL_face_U_TD = mne.grand_average(ITPC_face_U_TD)


# with open('Power_obj_all_ASD.pkl', 'rb') as f:
#     [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_TD] = pickle.load(f)
with open('Power_obj_SIB_Gamma.pkl', 'rb') as f:
    [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_SIB] = pickle.load(f)

M_Power_NPL_obj_TD = mne.grand_average(ITPC_obj_TD)


# with open('Power_obj_U_all_ASD.pkl', 'rb') as f:
#     [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_TD] = pickle.load(f)
with open('Power_obj_U_SIB_Gamma.pkl', 'rb') as f:
    [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_SIB] = pickle.load(f)

M_Power_NPL_obj_U_TD = mne.grand_average(ITPC_obj_U_TD)

#%% For ITPC - ASD

# Load pickle file with corresponding power data 
import os
import pickle
import mne
import matplotlib.pyplot as plt

with open('Power_face_ASD.pkl', 'rb') as f:
    [Power_face_ASD,Power_NPL_face_ASD,ITPC_face_ASD] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.25, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_face_ASD)):
    Power_NPL_face_ASD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_ASD = mne.grand_average(Power_NPL_face_ASD)
# M_Power_NPL_face_ASD = mne.grand_average(ITPC_face_ASD)


with open('Power_face_U_ASD.pkl', 'rb') as f:
    [Power_face_U_ASD,Power_NPL_face_U_ASD,ITPC_face_U_ASD] = pickle.load(f)
    
# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_face_U_ASD)):
    Power_NPL_face_U_ASD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_U_ASD = mne.grand_average(Power_NPL_face_U_ASD)

# M_Power_NPL_face_U_ASD = mne.grand_average(ITPC_face_U_ASD)


with open('Power_obj_ASD.pkl', 'rb') as f:
    [Power_obj_ASD,Power_NPL_obj_ASD,ITPC_obj_ASD] = pickle.load(f)
    
# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_obj_ASD)):
    Power_NPL_obj_ASD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_ASD = mne.grand_average(Power_NPL_obj_ASD)

# M_Power_NPL_obj_ASD = mne.grand_average(ITPC_obj_ASD)


with open('Power_obj_U_ASD.pkl', 'rb') as f:
    [Power_obj_U_ASD,Power_NPL_obj_U_ASD,ITPC_obj_U_ASD] = pickle.load(f)
    

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_obj_U_ASD)):
    Power_NPL_obj_U_ASD[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_U_ASD = mne.grand_average(Power_NPL_obj_U_ASD)

# M_Power_NPL_obj_U_ASD = mne.grand_average(ITPC_obj_U_ASD)

#%% ASD - GAMMA

with open('Power_face_ASD_Gamma.pkl', 'rb') as f:
    [Power_face_TD,Power_NPL_face_TD,ITPC_face_ASD] = pickle.load(f)
    
M_Power_NPL_face_ASD = mne.grand_average(ITPC_face_ASD)

with open('Power_face_U_ASD_Gamma.pkl', 'rb') as f:
    [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_ASD] = pickle.load(f)

M_Power_NPL_face_U_ASD = mne.grand_average(ITPC_face_U_ASD)

with open('Power_obj_ASD_Gamma.pkl', 'rb') as f:
    [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_ASD] = pickle.load(f)
    
M_Power_NPL_obj_ASD = mne.grand_average(ITPC_obj_ASD)

with open('Power_obj_U_ASD_Gamma.pkl', 'rb') as f:
    [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_ASD] = pickle.load(f)

M_Power_NPL_obj_U_ASD = mne.grand_average(ITPC_obj_U_ASD)

#%% For ITPC - SIB

# Load pickle file with corresponding power data 
import os
import pickle
import mne
import matplotlib.pyplot as plt

with open('Power_face_SIB.pkl', 'rb') as f:
    [Power_face_SIB,Power_NPL_face_SIB,ITPC_face_SIB] = pickle.load(f)
    
# Define baseline range (in seconds)
baseline = (-0.25, 0.0)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_face_SIB)):
    Power_NPL_face_SIB[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_SIB = mne.grand_average(Power_NPL_face_SIB)
# M_Power_NPL_face_SIB = mne.grand_average(ITPC_face_SIB)


with open('Power_face_U_SIB.pkl', 'rb') as f:
    [Power_face_U_SIB,Power_NPL_face_U_SIB,ITPC_face_U_SIB] = pickle.load(f)
    
# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_face_U_SIB)):
    Power_NPL_face_U_SIB[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_face_U_SIB = mne.grand_average(Power_NPL_face_U_SIB)

# M_Power_NPL_face_U_SIB = mne.grand_average(ITPC_face_U_SIB)


with open('Power_obj_SIB.pkl', 'rb') as f:
    [Power_obj_SIB,Power_NPL_obj_SIB,ITPC_obj_SIB] = pickle.load(f)
    
# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_obj_SIB)):
    Power_NPL_obj_SIB[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_SIB = mne.grand_average(Power_NPL_obj_SIB)

# M_Power_NPL_obj_SIB = mne.grand_average(ITPC_obj_SIB)


with open('Power_obj_U_SIB.pkl', 'rb') as f:
    [Power_obj_U_SIB,Power_NPL_obj_U_SIB,ITPC_obj_U_SIB] = pickle.load(f)
    

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_obj_U_SIB)):
    Power_NPL_obj_U_SIB[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_obj_U_SIB = mne.grand_average(Power_NPL_obj_U_SIB)

# M_Power_NPL_obj_U_SIB = mne.grand_average(ITPC_obj_U_SIB)

#%% SIB - GAMMA

with open('Power_face_SIB_Gamma.pkl', 'rb') as f:
    [Power_face_TD,Power_NPL_face_TD,ITPC_face_SIB] = pickle.load(f)
    
M_Power_NPL_face_SIB = mne.grand_average(ITPC_face_SIB)

with open('Power_face_U_SIB_Gamma.pkl', 'rb') as f:
    [Power_face_U_TD,Power_NPL_face_U_TD,ITPC_face_U_SIB] = pickle.load(f)

M_Power_NPL_face_U_SIB = mne.grand_average(ITPC_face_U_SIB)

with open('Power_obj_SIB_Gamma.pkl', 'rb') as f:
    [Power_obj_TD,Power_NPL_obj_TD,ITPC_obj_SIB] = pickle.load(f)
    
M_Power_NPL_obj_SIB = mne.grand_average(ITPC_obj_SIB)

with open('Power_obj_U_SIB_Gamma.pkl', 'rb') as f:
    [Power_obj_U_TD,Power_NPL_obj_U_TD,ITPC_obj_U_SIB] = pickle.load(f)

M_Power_NPL_obj_U_SIB = mne.grand_average(ITPC_obj_U_SIB)

#%%

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(4, 1, figsize=(10, 8))

fmin=25
fmax=40

tmin1 = 0.0
tmax1 = 0.2

#Audiovisual scale
vlim1 = 0.07
vlim2= 0.2

M_Power_NPL_face_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
M_Power_NPL_face_U_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
M_Power_NPL_obj_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
M_Power_NPL_obj_U_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%%

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(4, 1, figsize=(10, 8))

fmin=25
fmax=40

tmin1 = 0.0
tmax1 = 0.2

#Audiovisual scale
vlim1 = 0.07
vlim2= 0.2

M_Power_NPL_face_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
M_Power_NPL_face_U_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
M_Power_NPL_obj_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
M_Power_NPL_obj_U_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%%

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(4, 1, figsize=(10, 8))

fmin=25
fmax=40

tmin1 = 0.0
tmax1 = 0.2

#Audiovisual scale
vlim1 = 0.07
vlim2= 0.2

M_Power_NPL_face_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
M_Power_NPL_face_U_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
M_Power_NPL_obj_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
M_Power_NPL_obj_U_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%%

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(4, 1, figsize=(10, 8))

fmin=4
fmax=7

tmin1 = 0.2
tmax1 = 0.5

#Audiovisual scale
vlim1 = -0.3
vlim2= 0.3

M_Power_NPL_face_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
M_Power_NPL_face_U_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
M_Power_NPL_obj_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
M_Power_NPL_obj_U_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%%

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(4, 1, figsize=(10, 8))

fmin=4
fmax=7

tmin1 = 0.0
tmax1 = 0.2

#Audiovisual scale
vlim1 = -0.6
vlim2= 0.6

M_Power_NPL_face_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
M_Power_NPL_face_U_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
M_Power_NPL_obj_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
M_Power_NPL_obj_U_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%%

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(4, 1, figsize=(10, 8))

fmin=7
fmax=13

tmin1 = 0.1
tmax1 = 0.3

#Audiovisual scale
vlim1 = -0.5
vlim2= 0.5

M_Power_NPL_face_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
M_Power_NPL_face_U_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
M_Power_NPL_obj_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
M_Power_NPL_obj_U_TD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%%

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(4, 1, figsize=(10, 8))

fmin=7
fmax=13

tmin1 = 0.1
tmax1 = 0.3

#Audiovisual scale
vlim1 = -0.5
vlim2= 0.5

M_Power_NPL_face_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
M_Power_NPL_face_U_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
M_Power_NPL_obj_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
M_Power_NPL_obj_U_ASD.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%%

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(4, 1, figsize=(10, 8))

fmin=7
fmax=13

tmin1 = 0.1
tmax1 = 0.3

#Audiovisual scale
vlim1 = -0.5
vlim2= 0.5

M_Power_NPL_face_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0], show=False)
M_Power_NPL_face_U_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1], show=False)
M_Power_NPL_obj_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2], show=False)
M_Power_NPL_obj_U_SIB.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[3], show=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%% Time-frequency maps

# Centro-frontal - Auditory stimulation

# Occipital - Visual stimulation
Electrodes = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']

# Electrodes = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz']

# Electrodes = ['Cz','C1','C2','FC1','FCz','FC2']


# Alpha scale for visual and audiovisual
M_Power_NPL_face_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vmin=0,vmax=0.4,fmin=4,fmax=40)
M_Power_NPL_face_U_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vmin=0,vmax=0.4,fmin=4,fmax=40)
M_Power_NPL_obj_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vmin=0,vmax=0.4,fmin=4,fmax=40)
M_Power_NPL_obj_U_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vmin=0,vmax=0.4,fmin=4,fmax=40)

# Alpha scale for visual and audiovisual
# M_Power_NPL_face_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vmin=-0.2,vmax=0.2,fmin=25,fmax=40)
# M_Power_NPL_face_U_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vmin=-0.2,vmax=0.2,fmin=25,fmax=40)
# M_Power_NPL_obj_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vmin=-0.2,vmax=0.2,fmin=25,fmax=40)
# M_Power_NPL_obj_U_TD.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=0.6,vmin=-0.2,vmax=0.2,fmin=25,fmax=40)

#%% Alpha suppression for Induced power for TD
import numpy as np

# freqs = np.linspace(*np.array([4, 40]), num=100) #num = step / bin allows a precision of the frequency resolution
freqs = np.linspace(*np.array([25, 40]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz', 'Iz']

# channels = ['O1', 'O2', 'Oz','Iz']

# channels = ['Cz','C1','C2','FC1','FCz','FC2']

# channels = ['O1', 'O2', 'POz', 'Oz']

# channels = ['P8']

tmin = -0.2
tmax = 0.6

# Alpha_min = 0 # 13Hz
# Alpha_max = 8 # 25Hz

# Alpha_min = 9 # 13Hz
# Alpha_max = 24 # 25Hz

# Alpha_min = 25 # 13Hz
# Alpha_max = 58 # 25Hz

# Alpha_min = 59 # 13Hz
# Alpha_max = 99 # 25Hz

Alpha_min = 33 # 13Hz
Alpha_max = 99 # 25Hz

Alpha_suppression_face_TD = []
Alpha_suppression_U_face_TD = []

Alpha_suppression_obj_TD = []
Alpha_suppression_U_obj_TD = []

# For ITPC
for i in range(0,len(ITPC_face_TD),1):
    Aph_TD = ITPC_face_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_face_TD.append(Fa_TD)

for i in range(0,len(ITPC_face_U_TD),1):
    Aph_TD = ITPC_face_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_face_TD.append(Fa_TD)
    
for i in range(0,len(ITPC_obj_TD),1):
    Aph_TD = ITPC_obj_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_obj_TD.append(Fa_TD)
    
for i in range(0,len(ITPC_obj_U_TD),1):
    Aph_TD = ITPC_obj_U_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_obj_TD.append(Fa_TD)
    
# # For NPL Power
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
ax.set_ylim(0.07,0.25)
# ax.set_ylim(0.07,0.25)

ax.legend()

#%% Alpha suppression for Induced power for ASD
import numpy as np

freqs = np.linspace(*np.array([25, 40]), num=100) #num = step / bin allows a precision of the frequency resolution
# freqs = np.linspace(*np.array([25, 40]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz', 'Iz']

# channels = ['O1', 'O2', 'Oz','Iz']

# channels = ['Cz','C1','C2','FC1','FCz','FC2']

# channels = ['O1', 'O2', 'POz', 'Oz']

# channels = ['P8']

tmin = -0.2
tmax = 0.6

Alpha_min = 33 # 25Hz
Alpha_max = 99 # 40Hz

# Alpha_min = 25 # 25Hz
# Alpha_max = 58 # 40Hz

Alpha_suppression_face_ASD = []
Alpha_suppression_U_face_ASD = []

Alpha_suppression_obj_ASD = []
Alpha_suppression_U_obj_ASD = []

# For ITPC
for i in range(0,len(ITPC_face_ASD),1):
    Aph_TD = ITPC_face_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_face_ASD.append(Fa_TD)

for i in range(0,len(ITPC_face_U_ASD),1):
    Aph_TD = ITPC_face_U_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_face_ASD.append(Fa_TD)
    
for i in range(0,len(ITPC_obj_ASD),1):
    Aph_TD = ITPC_obj_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_obj_ASD.append(Fa_TD)
    
for i in range(0,len(ITPC_obj_U_ASD),1):
    Aph_TD = ITPC_obj_U_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_obj_ASD.append(Fa_TD)
    
# # For NPL Power
# for i in range(0,len(Power_NPL_face_ASD),1):
#     Aph_TD = Power_NPL_face_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_face_ASD.append(Fa_TD)

# for i in range(0,len(Power_NPL_face_U_ASD),1):
#     Aph_TD = Power_NPL_face_U_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_U_face_ASD.append(Fa_TD)
    
# for i in range(0,len(Power_NPL_obj_ASD),1):
#     Aph_TD = Power_NPL_obj_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_obj_ASD.append(Fa_TD)
    
# for i in range(0,len(Power_NPL_obj_U_ASD),1):
#     Aph_TD = Power_NPL_obj_U_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_U_obj_ASD.append(Fa_TD)

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
ax.set_ylim(0.07,0.25)
# ax.set_ylim(0.07,0.25)

ax.legend()

#%% Alpha suppression for Induced power for SIB
import numpy as np

freqs = np.linspace(*np.array([25, 40]), num=100) #num = step / bin allows a precision of the frequency resolution
# freqs = np.linspace(*np.array([25, 40]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8', 'POz', 'Oz', 'Iz']

# channels = ['O1', 'O2', 'Oz','Iz']

# channels = ['Cz','C1','C2','FC1','FCz','FC2']

# channels = ['O1', 'O2', 'POz', 'Oz']

# channels = ['P8']

tmin = -0.2
tmax = 0.6

Alpha_min = 33 # 25Hz
Alpha_max = 99 # 40Hz

# Alpha_min = 0 # 25Hz
# Alpha_max = 18 # 40Hz

Alpha_suppression_face_SIB = []
Alpha_suppression_U_face_SIB = []

Alpha_suppression_obj_SIB = []
Alpha_suppression_U_obj_SIB = []

# For ITPC
for i in range(0,len(ITPC_face_SIB),1):
    Aph_TD = ITPC_face_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_face_SIB.append(Fa_TD)

for i in range(0,len(ITPC_face_U_SIB),1):
    Aph_TD = ITPC_face_U_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_face_SIB.append(Fa_TD)
    
for i in range(0,len(ITPC_obj_SIB),1):
    Aph_TD = ITPC_obj_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_obj_SIB.append(Fa_TD)
    
for i in range(0,len(ITPC_obj_U_SIB),1):
    Aph_TD = ITPC_obj_U_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppression_U_obj_SIB.append(Fa_TD)
    
# # For NPL Power
# for i in range(0,len(Power_NPL_face_SIB),1):
#     Aph_TD = Power_NPL_face_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_face_SIB.append(Fa_TD)

# for i in range(0,len(Power_NPL_face_U_SIB),1):
#     Aph_TD = Power_NPL_face_U_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_U_face_SIB.append(Fa_TD)
    
# for i in range(0,len(Power_NPL_obj_SIB),1):
#     Aph_TD = Power_NPL_obj_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_obj_SIB.append(Fa_TD)
    
# for i in range(0,len(Power_NPL_obj_U_SIB),1):
#     Aph_TD = Power_NPL_obj_U_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     Alpha_suppression_U_obj_SIB.append(Fa_TD)
    

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
ax.set_ylim(0.07,0.25)
# ax.set_ylim(0.07,0.25)

ax.legend()


#%% Permutation test between averaged ERP curves

import numpy as np
import matplotlib.pyplot as plt
import mne
from scipy.stats import t
from mne.stats import permutation_cluster_test, ttest_ind_no_p

alpha_suppression_td = np.array(Alpha_suppression_face_TD)
alpha_suppression_asd = np.array(Alpha_suppression_face_ASD)

# Determine the cluster-forming threshold based on a critical t-value
n_participants = 38  # Assume equal sample size for simplicity
alpha_level = 0.05  # Desired significance level for the threshold
df = n_participants - 1  # Degrees of freedom for each group
t_threshold = abs(t.ppf(alpha_level / 2, df))  # Two-tailed t-value for alpha level

# Run the cluster-based permutation test with the t-test function
n_permutations = 2000
data = [alpha_suppression_td, alpha_suppression_asd]
T_obs, clusters, cluster_p_values, _ = permutation_cluster_test(
    data, n_permutations=n_permutations, threshold=t_threshold, tail=0, n_jobs=1, stat_fun=ttest_ind_no_p
)

# Identify significant clusters (p < 0.05)
significant_clusters = np.where(cluster_p_values < 0.05)[0]

# Calculate the mean and SEM for plotting
mean_alpha_td = np.mean(alpha_suppression_td, axis=0)
mean_alpha_asd = np.mean(alpha_suppression_asd, axis=0)
sem_td = np.std(alpha_suppression_td, axis=0) / np.sqrt(len(alpha_suppression_td))
sem_asd = np.std(alpha_suppression_asd, axis=0) / np.sqrt(len(alpha_suppression_asd))

# Define time vector (adjust if needed)

# Plot the results
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, mean_alpha_td, label='TD', color='blue')
ax.fill_between(x, mean_alpha_td - sem_td, mean_alpha_td + sem_td, color='blue', alpha=0.2)
ax.plot(x, mean_alpha_asd, label='ASD', color='orange')
ax.fill_between(x, mean_alpha_asd - sem_asd, mean_alpha_asd + sem_asd, color='orange', alpha=0.2)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Alpha Suppression')
ax.legend()
ax.set_title('Alpha Suppression with Significant Clusters Highlighted')

# Highlight significant clusters
for cluster_idx in significant_clusters:
    cluster_times = clusters[cluster_idx][0]  # Boolean array for this cluster
    cluster_start = x[cluster_times[0]]  # Start time of cluster
    cluster_end = x[cluster_times[-1]]   # End time of cluster
    ax.axvspan(cluster_start, cluster_end, color='red', alpha=0.3)

plt.tight_layout()
plt.show()

#%%

from mne.stats import permutation_t_test
from scipy.stats import ttest_ind
import numpy as np
import matplotlib.pyplot as plt

# Prepare your data (n_subjects x n_times)
data1 = np.array(Alpha_suppression_U_face_SIB)  # shape: (n_subjects, n_times)
data2 = np.array(Alpha_suppression_obj_SIB)

# Perform tmax-corrected permutation test
n_permutations = 5000
p_values_corrected = permutation_t_test(
    data1 - data2,  # use paired if desired, or subtract before
    n_permutations=n_permutations,
    tail=0,  # two-sided
    n_jobs=1,
    seed=42,
)

# Plot mean and SEM
x = np.linspace(-0.2, 0.8, data1.shape[1])  # Adjust to match your time vector
mean1 = np.mean(data1, axis=0)
mean2 = np.mean(data2, axis=0)
sem1 = np.std(data1, axis=0) / np.sqrt(data1.shape[0])
sem2 = np.std(data2, axis=0) / np.sqrt(data2.shape[0])

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, mean1, label='TD', color='blue')
ax.fill_between(x, mean1 - sem1, mean1 + sem1, alpha=0.2, color='blue')
ax.plot(x, mean2, label='ASD', color='orange')
ax.fill_between(x, mean2 - sem2, mean2 + sem2, alpha=0.2, color='orange')

# Highlight significant time points after tmax correction
significant_timepoints = p_values_corrected[1] < 0.05
ax.plot(x[significant_timepoints], mean1[significant_timepoints], 'o', color='red', label='p < 0.05 (tmax corrected)')

ax.set_xlabel("Time (s)")
ax.set_ylabel("Alpha Suppression")
ax.set_title("Alpha Suppression - tmax Corrected Permutation Test")
ax.legend()
plt.tight_layout()
plt.show()

#%% Extract peak from ITPC vectors 

# Define your time vector
x = np.linspace(-0.2, 0.6, 104)

# Define the time window of interest
time_window_mask = (x >= 0.0) & (x <= 0.2)

# Function to get peak value and latency
def extract_peak_and_latency(data_list, time_vector, mask):
    peaks = []
    latencies = []
    for data in data_list:
        data_window = np.array(data)[mask]
        peak_idx = np.argmax(data_window)
        peaks.append(data_window[peak_idx])
        latencies.append(time_vector[mask][peak_idx])
    return peaks, latencies

# Extract for each condition for TD group
peak_face_TD, latency_face_TD = extract_peak_and_latency(Alpha_suppression_face_TD, x, time_window_mask)
peak_face_U_TD, latency_face_U_TD = extract_peak_and_latency(Alpha_suppression_U_face_TD, x, time_window_mask)
peak_obj_TD, latency_obj_TD = extract_peak_and_latency(Alpha_suppression_obj_TD, x, time_window_mask)
peak_obj_U_TD, latency_obj_U_TD = extract_peak_and_latency(Alpha_suppression_U_obj_TD, x, time_window_mask)

# Extract for each condition for ASD group
peak_face_ASD, latency_face_ASD = extract_peak_and_latency(Alpha_suppression_face_ASD, x, time_window_mask)
peak_face_U_ASD, latency_face_U_ASD = extract_peak_and_latency(Alpha_suppression_U_face_ASD, x, time_window_mask)
peak_obj_ASD, latency_obj_ASD = extract_peak_and_latency(Alpha_suppression_obj_ASD, x, time_window_mask)
peak_obj_U_ASD, latency_obj_U_ASD = extract_peak_and_latency(Alpha_suppression_U_obj_ASD, x, time_window_mask)

# Extract for each condition for SIB group
peak_face_SIB, latency_face_SIB = extract_peak_and_latency(Alpha_suppression_face_SIB, x, time_window_mask)
peak_face_U_SIB, latency_face_U_SIB = extract_peak_and_latency(Alpha_suppression_U_face_SIB, x, time_window_mask)
peak_obj_SIB, latency_obj_SIB = extract_peak_and_latency(Alpha_suppression_obj_SIB, x, time_window_mask)
peak_obj_U_SIB, latency_obj_U_SIB = extract_peak_and_latency(Alpha_suppression_U_obj_SIB, x, time_window_mask)

#%%

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# # Combine all peak values into a single list
peak_values = (
    peak_face_TD + peak_face_U_TD + peak_obj_TD + peak_obj_U_TD +
    peak_face_ASD + peak_face_U_ASD + peak_obj_ASD + peak_obj_U_ASD +
    peak_face_SIB + peak_face_U_SIB + peak_obj_SIB + peak_obj_U_SIB
)

# peak_values = (
#     latency_face_TD + latency_face_U_TD + latency_obj_TD + latency_obj_U_TD +
#     latency_face_ASD + latency_face_U_ASD + latency_obj_ASD + latency_obj_U_ASD +
#     latency_face_SIB + latency_face_U_SIB + latency_obj_SIB + latency_obj_U_SIB
# )

# Create corresponding condition labels
conditions = (
    ['Face'] * len(peak_face_TD) + ['Face (Inv)'] * len(peak_face_U_TD) + ['Object'] * len(peak_obj_TD) + ['Object (Inv)'] * len(peak_obj_U_TD) +
    ['Face'] * len(peak_face_ASD) + ['Face (Inv)'] * len(peak_face_U_ASD) + ['Object'] * len(peak_obj_ASD) + ['Object (Inv)'] * len(peak_obj_U_ASD) +
    ['Face'] * len(peak_face_SIB) + ['Face (Inv)'] * len(peak_face_U_SIB) + ['Object'] * len(peak_obj_SIB) + ['Object (Inv)'] * len(peak_obj_U_SIB)
)

# Create corresponding group labels
groups = (
    ['TD'] * (len(peak_face_TD) + len(peak_face_U_TD) + len(peak_obj_TD) + len(peak_obj_U_TD)) +
    ['ASD'] * (len(peak_face_ASD) + len(peak_face_U_ASD) + len(peak_obj_ASD) + len(peak_obj_U_ASD)) +
    ['SIB'] * (len(peak_face_SIB) + len(peak_face_U_SIB) + len(peak_obj_SIB) + len(peak_obj_U_SIB))
)

# Create a DataFrame for plotting
df_plot = pd.DataFrame({
    'Peak ITPC': peak_values,
    'Condition': conditions,
    'Group': groups
})

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_plot, x='Condition', y='Peak ITPC', hue='Group', palette='Set2')
sns.stripplot(data=df_plot, x='Condition', y='Peak ITPC', hue='Group', 
              dodge=True, jitter=True, alpha=0.5, linewidth=0.5, color='k')
plt.title('Peak Gamma ITPC (0–200 ms)')
plt.ylabel('Peak ITPC')
plt.xlabel('Condition')
plt.legend(title='Group', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
