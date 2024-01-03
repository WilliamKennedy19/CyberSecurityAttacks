from keras import layers
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
from IPython.display import display
import numpy as np

attack_data = pd.read_csv("cybersecurity_attacks.csv")

print(attack_data.head())

print(attack_data.describe())

print(len(attack_data))
attack_data.style

#Data preprocessing and Cleaning

columns = list(attack_data)
print(columns)
print(attack_data.isnull().sum())

malware_indicators = attack_data.get("Malware Indicators")
print(malware_indicators)
attack_data2 = attack_data.copy()
attack_data2["Malware Indicators"]