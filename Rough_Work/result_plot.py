from summarystats import df_recent
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
sns.set(font_scale=1)
sns.set_style("white")
plt.rcParams['figure.figsize'] = (8, 5)

newdf = pd.crosstab(df_recent['Year'], df_recent['result_code'])

import matplotlib.pyplot as plt

ax3 = newdf.plot(kind='bar', stacked=True)
ax3.set_xlabel('Year')
ax3.set_ylabel('Count of Expeditions')
ax3.set_title('Expedition Results by Year')
ax3.legend(['Success', 'Accident', 'Route Difficulty', 'Illness, AMS', 'Lack of Supplies', 'Bad Weather', 'Other', 'Lack of Time', 'Did Not Climb', 'Unknown'])
plt.show()