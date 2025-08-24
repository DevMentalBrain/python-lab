import sqlite3
from db import create_connection

class ToDoListRepository:
    
    def createNewList(task_name):
        if(task_name == None):
            return False
        elif(isinstance(task_name, str) == False):
            return False
        
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
            return True
        
        except sqlite3.Error as e:
            print("Erro: ", e)
            return False
        finally:
            if(db_connection):  
                db_connection.close()