import pandas as pd 
import numpy as np
import plotly.express as px
import seaborn as sns
from sklearn.linear_model import LinearRegression

# load data and define helper function
df = pd.read_csv('/home/gchen22/Desktop/maggiechen615/Unicorn_Companies.csv')
import math
def split(v):
    return math.log(float(v.split('$')[1]))


# Display and plot top 20 unicorn companies
dff = df.sort_values(by = 'Valuation ($B)', ascending=False)[:20]
dff['Valuation_Log'] = dff['Valuation ($B)'].apply(split)
dff['Founded Year'] = dff['Founded Year'].astype(int)

scat1 = px.scatter(
    dff, 
    x = 'Founded Year',
    y = 'Valuation_Log',
    color = 'Country',
    size = 'Valuation_Log',
    hover_name = 'Company')

scat1.show()


# Deep dive into the emergence of unicorns over different time period
df = df.replace(to_replace='None', value=np.nan).dropna()
df['Founded Year'] = df['Founded Year'].astype(int)
df['Valuation_Log'] = df['Valuation ($B)'].apply(split)

fig = px.scatter(
    df, 
    x = 'Founded Year',
    y = 'Valuation_Log',
    color = 'Country',
    size = 'Valuation_Log',
    hover_name = 'Company')
    
fig.show()


# Plot countries with the most unicorns
country_unicorn = df.groupby('Country').size()
px.bar(country_unicorn)


# Add one more dimension of industry
fig = px.treemap(
    df, path = ['Industry', 'Country', 'Company'],
    values = 'Valuation_Log',
    color_discrete_sequence=px.colors.qualitative.Pastel)

fig.show()