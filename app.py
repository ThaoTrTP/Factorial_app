import streamlit as st
from factorial import fact
import os

def load_users():
    """ Read users from user.txt"""
    try:
        if os.path.exists("user.txt"):
            with open("user.txt", "r", encoding="utf-8") as f:
                users = [line.strip() for line in f.readlines() if line.strip()]
                return users
        else:
            st.error(f"User.txt file doesn't exist")
            return []
    except Exception as e:
            st.error(f"Error when reading user.txt: {e}")
            return []
    st.write("loaded users:", users)
    
def login_page():
    """Login page"""
    st.title("log in")
    #Input username
    username = st.text_input("Enter username:").strip()

    if st.button("Log in"):
        if username:
            users = load_users()
            if username in users:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                # If user is invalid, greeting page will be displayed"
                st.session_state.show_greeting = True
                st.session_state.username = username
                st.rerun()
        else:
            st.warning ("Enter username, please!")

def factorial_calculator():
    """ Factorial calculation page"""
    st.title("Factorial calculator")

    # Display logged in information
    st.write(f"Hello, {st.session_state.username}")

    # Log out button
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
    st.divider()

    #calculate factorial function
    number = st.number_input("Enter an integer:", min_value = 0,
                             max_value = 900)
    
    if st.button("Calculate"):
        result = fact(number)
        st.write(f"Factorial of {number} is {result}")
def greeting_page():
    """Greeting page for invalid user"""
    st.title("Hello")
    st.write(f"Hello {st.session_state.username}")
    st.write("You don't have permission to access to factorial function.")

    if st.button("Back to log in"):
        st.session_state.show_greeting = False
        st.session_state.username = ""
        st.rerun()
    
def main():
    #Initialze session state

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'show_greeting' not in st.session_state:
        st.session_state.show_greeting = False
    
    #Cordinate page based on login status
    if st.session_state.logged_in:
        factorial_calculator()
    elif st.session_state.show_greeting:
        greeting_page()
    else:
        login_page()

if __name__ == "__main__":
    main()