import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import os

def compute_silence_overtalk(conversation):
    silences, overtalks, turns = [], [], []
    for i in range(len(conversation) - 1):
        current, nxt = conversation[i], conversation[i + 1]
        silence = max(0, nxt['stime'] - current['etime'])
        overtalk = max(0, current['etime'] - nxt['stime'])
        silences.append(silence)
        overtalks.append(overtalk)
        turns.append(i + 1)
    return pd.DataFrame({'Turn': turns, 'Silence (s)': silences, 'Overtalk (s)': overtalks})

def plot_silence(df):
    plt.figure(figsize=(8, 4))
    plt.bar(df['Turn'], df['Silence (s)'], color='skyblue')
    plt.xlabel('Conversation Turn')
    plt.ylabel('Silence Duration (s)')
    plt.title('Silence Duration Between Turns')
    plt.tight_layout()
    os.makedirs('./output', exist_ok=True)
    plt.savefig('./output/silence_chart.png')
    st.pyplot(plt)

def plot_overtalk(df):
    plt.figure(figsize=(8, 4))
    plt.bar(df['Turn'], df['Overtalk (s)'], color='salmon')
    plt.xlabel('Conversation Turn')
    plt.ylabel('Overtalk Duration (s)')
    plt.title('Overtalk Duration Between Turns')
    plt.tight_layout()
    plt.savefig('./output/overtalk_chart.png')
    st.pyplot(plt)