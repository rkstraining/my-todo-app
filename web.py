import streamlit as st
import functions

todos = functions.get_todos()
def add_todos():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to increase productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="enter", label_visibility="hidden", placeholder="Add a new todo...",
              on_change=add_todos, key='new_todo')
