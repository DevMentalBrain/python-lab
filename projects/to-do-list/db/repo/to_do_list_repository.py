import sqlite3
from db.database import create_connection

class ToDoListRepository:
    
    def create_new_list(task_name):
        if(task_name == None):
            return -1
        elif(isinstance(task_name, str) == False):
            return -1
        
        try: 
            #atribui o banco de dados a variavel
            db_connection = create_connection()
            #objeto que executa os comandos SQL
            db_cursor = db_connection.cursor()

            db_cursor.execute("""
            INSERT INTO task_list     (task_list_name)
                            VALUES  (?)
        """, (task_name,))
            
            db_connection.commit()
            new_list_id = db_cursor.lastrowid 
            return new_list_id
        
        except sqlite3.Error as e:
            print("Erro: ", e)
            return -1
        finally:
            if(db_connection):  
                db_connection.close()

    def get_name_all_lists():
        #atribui o banco de dados a variavel
        db_connection = create_connection()
        #objeto que executa os comandos SQL
        db_cursor = db_connection.cursor()

        db_cursor.execute("""
            SELECT * FROM task_list
        """)

        result = db_cursor.fetchall()
        
        registered_lists = []

        for i in range(len(result)):
            registered_lists.append(result[i - 1][1])

        return registered_lists