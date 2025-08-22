import sqlite3

#cria (caso não exista) o banco de dados
def create_connection():
    return sqlite3.connect("to-do-list.db")