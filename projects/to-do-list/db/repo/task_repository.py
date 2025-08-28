import sqlite3
from db.database import create_connection

class TaskRepository:
    
    def create_new_task(task_name, task_description, task_status, task_list_id):
        if task_name == "" or task_status == "" or task_list_id == "":
            print("vazio")
            return -1
        elif isinstance(task_name, str) == False or isinstance(task_status, str) == False or isinstance(task_list_id, int) == False or isinstance(task_description, str) == False:
            print("tipo")
            return -1
        elif task_name == None or task_status == None or task_list_id == None:
            print("none")
            return -1
        
        try:
            db_connection = create_connection()
            db_cursor = db_connection.cursor()

            db_cursor.execute("""
                INSERT INTO tasks (task_name, task_description, task_status, task_list_id)
                            VALUES(?, ?, ?, ?)
            """, (task_name, task_description, task_status, task_list_id,))

            db_connection.commit()

            new_task_id = db_cursor.lastrowid

            return new_task_id
        
        except sqlite3.Error as e:
            print("Error: ", e)
            return -1
        finally:
            if db_connection:
                db_connection.close()