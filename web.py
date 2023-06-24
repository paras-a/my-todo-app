import streamlit as st
import cli


todos = cli.read_todos()


def add_todo():
	todo = st.session_state["todo"]
	if todo not in todos and todo != "":
		todos.append(todo + "\n")
		cli.write_todos(todos)
	else:
		st.error("Todo already exists")


st.title("My todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for todo in todos:
	st.checkbox(todo)

st.text_input(
	label="",
	placeholder="Add a todo",
	on_change=add_todo,
	key="todo"
)