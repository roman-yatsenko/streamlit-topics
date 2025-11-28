import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Демонстрація центральної граничної теореми")
st.subheader("СТАД-Python")
st.write("Застосунок імітує підкидування монети (1000) і візуалізує імітацію")

perc_heads = st.number_input(label="Вірогідність що випаде орел",
                             min_value=0.0, max_value=1.0, value=0.5)
graph_title = st.text_input(label="Назва графіку")

binom_dist = np.random.binomial(1, perc_heads, 1000)
list_of_means = []

for i in range(1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())

fig, ax = plt.subplots()
ax = plt.hist(list_of_means)
plt.hist([1, 1, 1, 1])
plt.title(graph_title)
st.pyplot(fig)
