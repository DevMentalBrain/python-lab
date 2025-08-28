from db.repo.to_do_list_repository import ToDoListRepository
from models.to_do_list import TodoList
from models.display_to_do_lists import display_to_do_lists



while True:
    print("\nWelcome to the to do list system!\n\n(1)View all to do lists \n(2)Add new to do list \n(0)To leave. \n")
    user_selected_option = int(input("Select an option: ")) 
    match user_selected_option:
        case 1:
            display_to_do_lists()
        case 2:
            new_to_do_list_name = input("\nEnter the name of the to do list: ")
            if new_to_do_list_name == "":
                print("\nError: A name cannot be empty!")
            elif len(new_to_do_list_name) < 3:
                print("Error: A name cannot contain fewer than 3 characters!")
            elif len(new_to_do_list_name) > 50:
                print("Error: A name cannot contain more than 50 characters!")
            else:
                new_to_do_list = TodoList(new_to_do_list_name)
                task_list_created_id = ToDoListRepository.create_new_list(new_to_do_list.name)

                if(task_list_created_id == -1):
                    print("\n Error: Unfortunately, it was not possible to create your list. Please try again.")
                else:
                    print("\nTask list successfully created, with id: " + str(task_list_created_id))
        case 0:
            break
        case _:
            print("\nInvalid option!")