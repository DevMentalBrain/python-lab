import sqlite3
from db.database import create_connection

class ToDoListRepository:
    
    def create_new_to_do_list(to_do_list_name):
        if to_do_list_name == None:
            return -1
        if to_do_list_name == "":
            return -1
        elif isinstance(to_do_list_name, str) == False:
            return -1
        
        try: 
            db_connection = create_connection()
            db_cursor = db_connection.cursor()

            db_cursor.execute("""
            INSERT INTO task_list     (task_list_name)
                            VALUES  (?)
        """, (to_do_list_name,))
            
            db_connection.commit()
            new_list_id = db_cursor.lastrowid 
            
            return new_list_id
        
        except sqlite3.Error as e:
            print("Error: ", e)
            return -1
        finally:
            if db_connection:  
                db_connection.close()

    def get_name_all_lists():
        db_connection = create_connection()
        db_cursor = db_connection.cursor()

        db_cursor.execute("""
            SELECT * FROM task_list
        """)

        result = db_cursor.fetchall()
        
        registered_lists = []

        for i in range(len(result)):
            registered_lists.append(result[i - 1][1])

        return registered_lists

    def get_to_do_list_id(to_do_list_name):
        db_connection = create_connection()
        db_cursor = db_connection.cursor()

        db_cursor.execute("""
            SELECT task_list_id FROM task_list
                                WHERE task_list_name = ?   
        """, (to_do_list_name,))

        to_do_list_id = db_cursor.fetchall()

        return to_do_list_id