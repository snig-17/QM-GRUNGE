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

df = pd.read_csv('/Users/alicecaiger/Library/CloudStorage/OneDrive-UniversityCollegeLondon/Core BASc-alice’s MacBook Air/QM2/Everest/expeditions3.csv')

df['hired_DR'] = pd.to_numeric(df['hired_DR'], errors='coerce').fillna(0)
df['mbr_DR'] = pd.to_numeric(df['mbr_DR'], errors='coerce').fillna(0)

grouped_df = df.groupby('Year')[['hired_DR', 'mbr_DR']].mean().reset_index()
#plt.plot(grouped_df['Year'], grouped_df['hired_DR'], label='Hired Death Rate', marker='o')
#plt.plot(grouped_df['Year'], grouped_df['mbr_DR'], label='Member Death Rate', marker='o')
#plt.xlabel('Year')
#plt.ylabel('Average Death Rate')
#plt.title('Average Death Rates Over Years')
#plt.legend()
#plt.show()
#grouped_df2 = df.groupby('Year')['member_count'].sum().reset_index()
#slope, intercept = np.polyfit(grouped_df2['Year'], grouped_df2['member_count'], 1) 
#line = slope * grouped_df2['Year'] + intercept
#plt.plot(grouped_df2['Year'], line, color='red', linestyle='--', label='Trend Line')
#plt.plot(grouped_df2['Year'], grouped_df2['member_count'], 'o', marker='o')
#plt.xlabel('Year')
#plt.ylabel('Number of Climbers')
#plt.title('Number of Climbers Over Years')
#plt.show()
#print(df['Result'].unique())

#print(df['Route(s)'].value_counts().head(10))

import re

first_routes = (
    df['Route(s)']
    .dropna()
    .str.lower()
    .str.replace(r'\(.*?\)', '', regex=True)
    .str.replace(',', '/', regex=False)  
    .str.replace(';', '/', regex=False)        # normalize separators
    .str.split('/')                            # split routes
    .str[0]                                    # keep FIRST route only
    .str.replace(r'\s+', ' ', regex=True)      # normalize spaces
    .str.strip()
)
route_counts = first_routes.value_counts().head(15)
print(route_counts)



