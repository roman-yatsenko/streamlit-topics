import altair as alt
import pandas as pd
import seaborn as sns
import streamlit as st
import time 

st.title("Пінгвини Палмера")

penguins_file = st.file_uploader('Оберіть файл (або залиште за замовчуванням)')

@st.cache_data
def load_file(penguin_file):
    time.sleep(3)
    if penguins_file:
        penguins_df = pd.read_csv(penguins_file)
    else:
        # st.stop()
        penguins_df = pd.read_csv('penguins.csv')
    return penguins_df

# st.write(penguins_df.head())

penguins_df = load_file(penguins_file)
selected_gender = st.selectbox(
    'Яких пінгвінів обираєте для аналізу',
    ['усі', 'male', 'female']
)
selected_x_var = st.selectbox(
    'Вісь x',
    ['bill_length_mm', 'bill_depth_mm', 'body_mass_g', 'flipper_length_mm']
)
selected_y_var = st.selectbox(
    'Вісь y',
    ['bill_depth_mm', 'bill_length_mm', 'body_mass_g', 'flipper_length_mm']
)

if selected_gender == 'male':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']

alt_chart = (
    alt.Chart(penguins_df, title=f"Обрано: {selected_gender}")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color='species',
    )
    .interactive()
)
st.altair_chart(alt_chart, width='stretch')
