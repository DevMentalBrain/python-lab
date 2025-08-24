import sqlite3

#importando conexão com banco de dados
from database import create_connection

#atribui o banco de dados a variavel
db_connection = create_connection()

#objeto que executa os comandos SQL
db_cursor = db_connection.cursor()

db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS task_list (
                  task_list_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  task_list_name TEXT NOT NULL
                  )
""")

db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
                  task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  task_name TEXT NOT NULL,
                  task_description TEXT,
                  task_status TEXT NOT NULL,
                  task_list_id INTEGER NOT NULL,
                  FOREIGN KEY (task_list_id) REFERENCES task_list (id)
                  )
""")


db_connection.commit()
db_connection.close()