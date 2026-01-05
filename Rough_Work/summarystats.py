# slightly random visualisations and then the first_routes bit is cleaning the route(s) column , then printing 15 most frequent
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

df_recent['route_codes'] = (
    df_recent['clean_routes']
    .map({
        's col-se ridge': 1,
        'n col-ne ridge': 2,
        'n face': 3,
        'sw face': 4,
        's pillar-se ridge': 5,
        'n col': 1,
    })
    .fillna(6)
)

df_recent['Result_clean'] = (
    df_recent['Result']
    .astype(str)                 # handle NaN safely
    .str.lower()                 # ignore capitalisation
    .str.replace(r'\(.*?\)', '', regex=True)  # remove parenthetical notes
    .str.replace(r'\s+', ' ', regex=True)   
    .str.strip()    # normalize spaces
)

df_recent['result_code'] = (
    df_recent['Result_clean']
    .map({
        'success': 1,
        'accident': 2,
        'route difficulty': 3,
        'illness, ams': 4,
        'lack of supplies': 5,
        'bad weather': 6,
        'bad conditions': 6,
        'other': 7,
        'lack of time': 8,
        'did not climb': 9,
        'unknown': 10
    })
    .fillna(11)                   
    .astype(int)
)

df_very_recent = df_recent[df_recent['Year'] >= 2010]

grouped_results = df_recent.groupby('Year')[['result_code']].mean().reset_index()

df_recent['mbr_hired_ratio'] = pd.to_numeric(df_recent['mbr_hired_ratio'], errors='coerce').fillna(0)
df_recent['mbr_hired_ratio'] = df_recent['mbr_hired_ratio'].where(df_recent['mbr_hired_ratio'] >= 0)
df_recent['OVERALL'] = pd.to_numeric(df_recent['OVERALL'], errors='coerce').fillna(0)

grouped_df3 = df_recent.groupby('Year')[['mbr_hired_ratio']].mean().reset_index()
grouped_df_DR = df_recent.groupby('Year')[['OVERALL']].mean().reset_index()

df_recent['Sucess_rate']= np.where(df_recent['Result_clean'] == 'success', 1, 0)
grouped_success = df_recent.groupby('Year')['Sucess_rate'].mean().reset_index()
yearly_popularity = df_recent.groupby('Year')['member_count'].sum().reset_index()

fig, ax = plt.subplots()
#ax.plot(grouped_df3['Year'], grouped_df3['mbr_hired_ratio'], label='Hired to Member Ratio', color='red')
#ax.plot(grouped_df_DR['Year'], grouped_df_DR['OVERALL'], label='Overall Death Rate', color='blue')
#ax.plot(grouped_success['Year'], grouped_success['Sucess_rate'], label='Success Rate', color='green')
#ax2 = ax.twinx()
#ax2.plot(yearly_popularity['Year'], yearly_popularity['member_count']/1000, label='Total Members (scaled)', color='orange')
ax.set_xlabel('Year')
ax.set_ylabel('Average Hired to Member Ratio')
#ax2.set_ylabel('Total Members (in thousands)')
ax.set_title('Average Hired to Member Ratio Over Years (1990 onwards)')

plt.grid()
#plt.show()

df2022 = df_recent[df_recent['Year'] == 2022]
df2021 = df_recent[df_recent['Year'] == 2021]
sns.countplot(data=df_recent[df_recent['Year'] == 2022], x='route_codes', order=sorted(df2022['route_codes'].unique()), color='blue')
sns.countplot(data=df_recent[df_recent['Year'] == 2021], x='route_codes', order=sorted(df2021['route_codes'].unique()), color='lightgreen', alpha=0.7)
plt.title('Expedition Route Codes in 2021 and 2022')
plt.xlabel('')
plt.xticks(ticks=[0,1,2,3,4,5],labels = ['S-Col/ SE Ridge', 'N-Col/ NE Ridge', 'N Face', 'SW Face', 'S Pillar/ SE Ridge', 'N Col'],rotation=30)
plt.ylabel('Number of Expeditions')
plt.legend(['2022','2021'])
#plt.show()



