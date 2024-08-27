import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

todos = functions.get_todos()

st.title("Wedam's Todo App")
st.subheader("Well, here we go again!")
st.write("It is what it is!")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"checkbox_{i}")
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        if f"checkbox_{i}" in st.session_state:
            del st.session_state[f"checkbox_{i}"]
            st.rerun()

st.text_input(" ",placeholder="Enter Your Todos", on_change= add_todo,
              key= "new_todo")