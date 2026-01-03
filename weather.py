import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly
import plotly.express as px
import warnings
from statsmodels.formula.api import ols
from statsmodels.iolib.summary2 import summary_col
warnings.filterwarnings('ignore')
sns.set(font_scale=1.5)
sns.set_style("white")
plt.rcParams['figure.figsize'] = (12, 8)

df = pd.read_csv('/Users/alicecaiger/Library/CloudStorage/OneDrive-UniversityCollegeLondon/Core BASc-alice’s MacBook Air/QM2/Everest/weather_southcol.csv')
df['date'] = pd.to_datetime(
    df['TIMESTAMP'],
    dayfirst=True,   # because format is DD/MM/YYYY
    errors='coerce'
)
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year


df = df.groupby('date')[['T_HMP','WS_AVG','RH']].mean().reset_index()
print(df.head())


df_a = pd.read_csv('/Users/alicecaiger/Library/CloudStorage/OneDrive-UniversityCollegeLondon/Core BASc-alice’s MacBook Air/QM2/Everest/ascents19_23.csv')
df_a['date'] = pd.to_datetime(
    df_a['Date'],
    dayfirst=True,   # because format is DD/MM/YYYY
    errors='coerce'
)
df_a['day'] = df_a['date'].dt.day
df_a['month'] = df_a['date'].dt.month
df_a['year'] = df_a['date'].dt.year
print(df_a.head())
df_merged = pd.merge(df_a, df, on=['date'], how='left')
print(df_merged.head())

