from User import User
from UserDAO import UserDAO
import csv

import argparse
import configparser


def main():
    args = argparse.ArgumentParser()
    # args.add_argument('config_file',help="fichier de conf")
    args.add_argument('-c','--config',help="fichier de conf",default="./tp_db/config.ini")
    params = args.parse_args()

    config = configparser.ConfigParser()
    # config.read(params.config_file)
    config.read(params.config)

    db = UserDAO(config['DB']['db_file_name'])
    with open(config['DATA']['csv_file_name'], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user = User(**row)
            db.save(user)
            # print(user)

def main01():
    user = User(last_name="MARTIN",first_name="Jean",email="test@truc.com",gender="Male",ip_address="192.168.1.1")
    # db = UserDAO('./tp_db/users_db.db')
    # db.save(user) # create/update
    # db.getByName("DURAND") # read
    # db.delete("DURAND")# delete
    # db.delete(3)
    # CRUD
if __name__=='__main__':
    main()
