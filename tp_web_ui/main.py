import streamlit as st
from UserDAO import UserDAO
def main():
    title = st.text_input('Movie title', '')
    st.write('The current movie title is', title)
    dao = UserDAO('users_db.db')
    users = dao.findAll()
    st.table(users)


if __name__=='__main__':
    main()


