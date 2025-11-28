import streamlit as st

st.title("ToDo Streamlit App")

if 'my_todo_list' not in st.session_state:
    st.session_state.my_todo_list = [
        "Випити кави",
        "Опанувати Streamlit",
        "Виконати інд. завдання"
    ]

new_todo = st.text_input("Нове завдання:")
if st.button("Додати"):
    st.write("Додавання нового завдання до списку")
    st.session_state.my_todo_list.append(new_todo)
st.write("Оновлений список завдань:", st.session_state.my_todo_list)
