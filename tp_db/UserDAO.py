import sqlite3
from User import User
from dataclasses import astuple


class UserDAO:


    def __init__(self,db_file) -> None:
        self._con = sqlite3.connect(db_file)

    def save(self,user:User):
        cur = self._con.cursor()
#         sql = f"""INSERT INTO users_tbl(first_name,last_name,email,gender,ip_address)
# VALUES ('{user.first_name}','{user.last_name}','{user.email}','{user.gender}','{user.ip_address}')
# """
        sql = f"""INSERT INTO users_tbl(first_name,last_name,email,gender,ip_address)
VALUES (?,?,?,?,?)
"""
        cur.execute(sql,astuple(user)[1:])
        self._con.commit()

        

    def __del__(self):
        self._con.close()