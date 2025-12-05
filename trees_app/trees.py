# from bokeh.plotting import figure
import altair as alt
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

st.write("San Francisco Trees")

trees_df = pd.read_csv('trees.csv')

st.subheader("Базові функції")
df_dbh_grouped = pd.DataFrame(
    trees_df.groupby(['dbh']).count()['tree_id']
).reset_index()
df_dbh_grouped.columns = ['dbh', 'tree_count']
st.line_chart(df_dbh_grouped, x='dbh', y='tree_count')
df_dbh_grouped['new_col'] = np.random.randn(len(df_dbh_grouped)) * 500
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)

trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n=1000)
st.map(trees_df)

st.subheader('Plotly')
fig = px.histogram(trees_df['dbh'])
st.plotly_chart(fig)

st.subheader('Seaborn')
trees_df['age'] = (
    pd.to_datetime('today') - 
    pd.to_datetime(trees_df['date'])
).dt.days
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df['age'])
plt.xlabel('Age (days)')
st.pyplot(fig_sb)

st.subheader('Matplotlib')
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df['age'])
plt.xlabel('Age (days)')
st.pyplot(fig_mpl)

# st.subheader('Bokeh')
# scatterplot = figure(title='Bokeh Scatterplot')
# scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
# scatterplot.xaxis.axis_label = 'dbh'
# scatterplot.yaxis.axis_label = 'site_order'
# st.bokeh_chart(scatterplot)

st.subheader('Altair')
# df_caretaker = pd.DataFrame(
#     trees_df.groupby(['caretaker']).count()['tree_id']
# ).reset_index()
# df_caretaker.columns = ['caretaker', 'tree_count']
# fig = alt.Chart(df_caretaker).mark_bar().encode(x='caretaker', y='tree_count')
fig = alt.Chart(trees_df).mark_bar().encode(
    x='caretaker',
    y='count(*):Q'
)
st.altair_chart(fig)
