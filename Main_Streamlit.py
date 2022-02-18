import streamlit as st
from UsersDAO import UsersDAO
from DbService import DbService
import streamlit_authenticator as stauth
from HomePage import Home_Page
from SideLog import Sign
import schedule
from UpdateClientTable import UpdateClientTable
import time

update_t = UpdateClientTable()


def main():
    Dbs = DbService()
    nick = Sign(Dbs)
    if nick is not None:
        api = UsersDAO(nick_name=nick).get_Api_of_usr()
        Home_Page(api_key=api[0][0], api_secret=api[0][1])
    else:
        Home_Page()


schedule.every().day.at("00:00").do(update_t.update_all_table())

try:
    main()
    while True:
        schedule.run_pending()
        time.sleep(1)
except:
    print("Errore")
