import os
from os import path
import re

import xlsxwriter

from tinydb import TinyDB, Query


try:
    from app_module import encrypt
    from app_module import tinydbaes as tae

except:
    import encrypt
    import tinyaes as tae
DB_EXTENSION = ".edb"


def open_database(path, key):
    paswd = key
    path_ = path
    db = TinyDB(encryption_key=paswd, path=path_,
                storage=tae.EncryptedJSONStorage)
    return db


def insert_data(password, server_name, database, paswd):

    server = Query()
    data_len = len(database.search(server.server == server_name))
    if data_len == 0:
        database.insert({'passwrd': encrypt.encrypt_txt(
            password, paswd), "server": server_name})
        return True
    else:
        return "found"


def fetch_data(database, passwrd, server_name):
    try:
        server = Query()
        data = database.search(server.server == server_name)[0]
        enc = data["passwrd"][0]
        iv = data["passwrd"][1]
        password = encrypt.decrypt_txt(enc, iv, passwrd)
        if password:
            return password
        else:
            return False
    except:
        return False


def update_data(database, server_name, password, paswd):
    server = Query()
    try:
        data_len = len(database.search(server.server == server_name))
        if data_len == 1:
            database.update({'passwrd': encrypt.encrypt_txt(
                password, paswd)}, server.server == server_name)
            return True
        else:

            return False
    except:
        return False


def remove_server(database, server_name):
    server = Query()
    try:
        database.remove(server.server == server_name)
        return True
    except:
        return False


def export_data(database_, password, file_name):
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()
    i = 1
    for item in database_:
        worksheet.write(f'A{i}', item["server"])
        worksheet.write(f'B{i}', fetch_data(
            database_, password, item["server"]))
        i += 1
    workbook.close()
    return True


def get_query(database, query):
    for item in database:
        if query in item["server"] or item["server"].startswith(query):
            yield item["server"]
