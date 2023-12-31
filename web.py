import streamlit as st
import cli


todos = cli.read_todos()

st.set_page_config(layout="wide")


def add_todo():
	todo = st.session_state["todo"]
	if todo not in todos and todo != "":
		todos.append(todo + "\n")
		cli.write_todos(todos)
	else:
		st.error("Todo already exists")


st.title("My todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your <b>productivity</b>.", unsafe_allow_html=True)

for index, todo in enumerate(todos):
	checkbox = st.checkbox(todo, key=todo)
	if checkbox:
		todos.pop(index)
		cli.write_todos(todos)
		del st.session_state[todo]

st.text_input(
	label="",
	placeholder="Add a todo",
	on_change=add_todo,
	key="todo"
)
