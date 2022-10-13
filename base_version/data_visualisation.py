# %%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# !pip3 install seaborn
import seaborn as sns

# %%
df = pd.read_csv("/Users/tim/Downloads/subject_1664784097816.csv")

# df = pd.read_csv("/Users/tim/Downloads/subject_1664784097816.csv", keep_default_na=False
df = pd.read_csv("/Users/tim/Downloads/subject_1664784097816.csv")

# choose a readymade style sheet
plt.style.use('fivethirtyeight')

# %%
# Start by making appropriate filters for the rows of my dataframe.
# here I select only trials from the main task
filt_all_trials = df['task'] == 'main_task'

# select the complete trials from the main task (response was given)
filt_all_complete_trials = (df['task'] == 'main_task') & (df['response'].notnull())

# CHECKING RESULTS
# ACCURACY
overall_acc = df.loc[filt_all_complete_trials, 'correct']
print('the mean accuracy was {} %'.format(
    round((overall_acc.to_numpy().mean())*100)
    )
    )
# %%
# ACCURACY PER CONDITION
# declaring manipulations and average accuracy
manipulations = []
avg_acc = []
error = []
# checking accuracy per condition
for manipulation in np.unique(df.loc[filt_all_complete_trials, 'manipulation']):
    filt_manipulation = (df['manipulation'] == manipulation) # creating manipulation filters
    accuracy = df.loc[filt_all_complete_trials & filt_manipulation, 'correct']
    manipulations.append(manipulation)
    avg_acc.append((accuracy.to_numpy().mean())*100)
    error.append((accuracy.to_numpy().std()))
    print('the mean accuracy in the {} condition was {} %'.format(
        manipulation,
        round((accuracy.to_numpy().mean())*100)
    )
    )

# plotting results
fig, ax = plt.subplots()
bars = ax.bar(manipulations, np.round(avg_acc), yerr=error)
plt.title("Accuracy across conditions")
ax.set_ylabel('Accuracy')
ax.set_xlabel('Conditions')
ax.bar_label(bars)
plt.savefig('./figures/acc_cond.png')
plt.show()
# %%
# ACCURACY PER KEY
keystrokes = []
avg_acc = []
error = []
# checking accuracy per condition
for key in np.unique(df.loc[filt_all_complete_trials, 'correct_response']):
    filt_key = (df['correct_response'] == key) # creating manipulation filters
    accuracy = df.loc[filt_all_complete_trials & filt_key, 'correct']
    keystrokes.append(key)
    avg_acc.append((accuracy.to_numpy().mean())*100)
    error.append((accuracy.to_numpy().std()))
    print('the mean accuracy for the {} key was {} %'.format(
        key,
        round((accuracy.to_numpy().mean())*100)
    )
    )

# plotting results
fig, ax = plt.subplots()
bars = ax.bar(keystrokes, np.round(avg_acc), yerr=error)
plt.title("Accuracy across keys")
ax.set_ylabel('Accuracy')
ax.set_xlabel('Keys')
ax.bar_label(bars)
plt.savefig('./figures/acc_key.png')
plt.show()
# %%
# creating block numbers to add to the table
block = []
for i in df['trial_index']:
    block.append(round(i/173))

# adding a block number columns
df['block_nbr'] = block

# %%
# ACCURACY PER BLOCK
blocks = []
avg_acc = []
error = []
# checking accuracy per condition
for block in np.unique(df.loc[filt_all_complete_trials, 'block_nbr']):
    filt_block = (df['block_nbr'] == block) # creating manipulation filters
    accuracy = df.loc[filt_all_complete_trials & filt_block, 'correct']
    blocks.append(block)
    avg_acc.append((accuracy.to_numpy().mean())*100)
    error.append((accuracy.to_numpy().std()))
    print('the mean accuracy for block number {} was {} %'.format(
        block,
        round((accuracy.to_numpy().mean())*100)
    )
    )

# plotting results
fig, ax = plt.subplots()
bars = ax.bar(blocks, np.round(avg_acc), yerr=error)
plt.title("Accuracy across blocks")
ax.set_ylabel('Accuracy')
ax.set_xlabel('Block number \n note that 0 is training')
ax.bar_label(bars)
plt.savefig("./figures/acc_block.png")
plt.show()
# %%
# %%
# REACTION TIME PER CONDITION
manipulations = []
avg_rt = []
error = []
# checking accuracy per condition
for manipulation in np.unique(df.loc[filt_all_complete_trials, 'manipulation']):
    filt_manipulation = (df['manipulation'] == manipulation) # creating manipulation filters
    reaction_time = df.loc[filt_all_complete_trials & filt_manipulation, 'rt']
    manipulations.append(manipulation)
    avg_rt.append(round(reaction_time.to_numpy().mean()))
    error.append((reaction_time.to_numpy().std()))
    print('the mean reaction time in the {} condition was {} %'.format(
        manipulation,
        round((round(reaction_time.to_numpy().mean())))
    )
    )

# plotting results
fig, ax = plt.subplots()
bars = ax.bar(manipulations, np.round(avg_rt), yerr=error)
plt.title("RT across conditions")
ax.set_ylabel('RT (ms)')
ax.set_xlabel('Conditions')
ax.bar_label(bars)
plt.savefig('./figures/rt_cond.png')
plt.show()
# %%
# REACTION TIME PER KEY
keystrokes = []
avg_rt = []
error = []
# checking accuracy per condition
for key in np.unique(df.loc[filt_all_complete_trials, 'correct_response']):
    filt_key = (df['correct_response'] == key) # creating manipulation filters
    reaction_time = df.loc[filt_all_complete_trials & filt_key, 'rt']
    keystrokes.append(key)
    avg_rt.append(round(reaction_time.to_numpy().mean()))
    error.append((reaction_time.to_numpy().std()))
    print('the mean reaction time for the {} key was {} %'.format(
        key,
        round((round(reaction_time.to_numpy().mean())))
    )
    )

# plotting results
fig, ax = plt.subplots()
bars = ax.bar(keystrokes, np.round(avg_rt), yerr=error)
plt.title("RT across keystrokes")
ax.set_ylabel('RT (ms)')
ax.set_xlabel('key')
ax.bar_label(bars)
plt.savefig('./figures/rt_key.png')
plt.show()
# %%
# REACTION TIME ACROSS BLOCKS
blocks = []
avg_rt = []
error = []
# checking accuracy per condition
for block in np.unique(df.loc[filt_all_complete_trials, 'block_nbr']):
    filt_block = (df['block_nbr'] == block) # creating manipulation filters
    reaction_time = df.loc[filt_all_complete_trials & filt_block, 'rt']
    blocks.append(block)
    avg_rt.append(round(reaction_time.to_numpy().mean()))
    error.append((reaction_time.to_numpy().std()))
    print('the mean reaction time for block number {} was {} %'.format(
        key,
        round((round(reaction_time.to_numpy().mean())))
    )
    )

# plotting results
fig, ax = plt.subplots()
bars = ax.bar(blocks, np.round(avg_rt), yerr=error)
plt.title("RT across blocks")
ax.set_ylabel('RT (ms)')
ax.set_xlabel('Block number \n (note block 0 is training)')
ax.bar_label(bars)
plt.savefig('./figures/rt_block.png')
plt.show()

# %%
# Trying new plot styles
sns.set_style("white")
sns.despine(top=True) # removes the borders
sns.barplot(x="manipulation", y="rt", data=df, capsize=.1, errorbar="sd")
sns.swarmplot(x="manipulation", y="rt", data=df, color="0", alpha=.35, size = 2)
plt.title("RT across conditions")
plt.xlabel('Conditions')
plt.ylabel('Reaction time (ms)')
sns.despine(bottom = True) # removes the borders
plt.bar_label(bars)

plt.show()
# %%
