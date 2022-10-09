#%%
import pandas as pd
from os.path import expanduser
import matplotlib.pyplot as plt
import datetime
from calendar import monthrange
import matplotlib.dates as mdates
import numpy as np

#%%


file_name = "../chart.xlsx"


df = pd.read_excel(io=file_name,sheet_name="modis",header=0)


# plt.plot(df["value"], marker='o')
# plt.figure(figsize=(20,4))


df.set_index('Date').plot()

x= plt.xticks(rotation=30, fontweight='light',  fontsize='x-small')
plt.xlabel("Date")
plt.ylabel("NDVI")
plt.title("Time series of NDVI")

L=plt.legend()
L.get_texts()[0].set_text('NDVI')

# plt.savefig('NDVI2.png', dpi = 300)
# my_dpi=96
# plt.figure(figsize=(1800/my_dpi, 800/my_dpi), dpi=my_dpi)

# plt.figure(figsize=(10,5), dpi = 0.06)

# df.set_index('Date').plot()
# plt.ylabel("NDVI")
# plt.title("Time series of NDVI for mashhad - Modis")
# L=plt.legend()
# L.get_texts()[0].set_text('NDVI')

# plt.xticks(df.year)
plt.show()
# %%
file_name = "../chart.xlsx"

df = pd.read_excel(io=file_name,sheet_name="modis",header=0)

df['yyyy'] = pd.to_datetime(df['Date']).dt.strftime('%Y')
df['mm'] = pd.to_datetime(df['Date']).dt.strftime('%m')
df['dd'] = pd.to_datetime(df['Date']).dt.strftime('%d')

# Group data first by year, then by month
# g = df.groupby(["yyyy", "mm"])
# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjOlKj0tOv5AhUqxQIHHTuIDD8QFnoECAkQAQ&url=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F29762546%2Fmonthly-averages-using-daily-data-using-python-pandas&usg=AOvVaw2im3RRUP7Nq4N3frqx7Eh9
# For each group, calculate the average of only the snow_depth column
# monthly_averages = g.aggregate({"value":np.mean})
# df.set_index('Date', inplace=True)
df.groupby(["yyyy", "mm"]).aggregate({"value":np.mean}).plot(legend=True)

# file_name = 'monthly_averages.xlsx'
# saving the excelsheet
# monthly_averages.to_excel(file_name)


# %%
# https://qa.icopy.site/questions/16139306/determine-season-given-timestamp-in-python-using-datetime
def season_of_date(date):
    year = str(date.year)
    seasons = {'spring': pd.date_range(start='21/03/'+year, end='20/06/'+year),
               'summer': pd.date_range(start='21/06/'+year, end='22/09/'+year),
               'autumn': pd.date_range(start='23/09/'+year, end='20/12/'+year)}
    if date in seasons['spring']:
        return f'{year}-spring'
    if date in seasons['summer']:
        return f'{year}-summer'
    if date in seasons['autumn']:
        return f'{year}-autumn'
    else:
        return f'{year}-winter'

df['Season'] = df['Date'].map(season_of_date)
seasonal_distribution = df.groupby(['Season'])['value'].mean().plot()

# file_name = 'season_averages.xlsx'
# saving the excelsheet
# seasonal_distribution.to_excel(file_name)
# %%
