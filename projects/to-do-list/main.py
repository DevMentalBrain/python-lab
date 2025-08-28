from db.repo.to_do_list_repository import ToDoListRepository
from db.repo.task_repository import TaskRepository
from models.to_do_list import TodoList
from models.display_to_do_lists import display_to_do_lists
from validators import task_validators
from models import task


while True:
    print("\nWelcome to the to do list system!\n\n(1)View all to do lists \n(2)Add new to do list \n(3)Add new task \n(0)To leave. \n")
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
        case 3:
            validator_info_new_task = False
            new_task_name = ""
            new_task_description = ""
            new_task_status = ""
            id_to_do_list_selected = None

            display_to_do_lists()

            while validator_info_new_task == False:
                name_to_list_selected = input("\nEnter the name of the list you want to add a task to: ")
                name_of_all_lists = ToDoListRepository.get_name_all_lists()
                validator_info_new_task = task_validators.to_do_list_selected_validator(name_to_list_selected, name_of_all_lists)[0]
                if validator_info_new_task == True:
                    id_to_do_list_selected = task_validators.to_do_list_selected_validator(name_to_list_selected, name_of_all_lists)[1]

            validator_info_new_task = False
            while validator_info_new_task == False:
                new_task_name = input("\nEnter the name of the task: ")
                validator_info_new_task = task_validators.task_name_validator(new_task_name)[0]
                if validator_info_new_task == False:
                    print(task_validators.task_name_validator(new_task_status)[1])

            validator_info_new_task = False
            while validator_info_new_task == False:
                new_task_description = input("\nEnter the description of the task: ")
                validator_info_new_task = task_validators.task_description_validator(new_task_description)[0]
                if validator_info_new_task == False:
                    print(task_validators.task_status_validator(new_task_status)[1])

            validator_info_new_task = False
            while validator_info_new_task == False:
                new_task_status = input("\nEnter the status of the task (Pendente, Em andamento, Conluida): ")
                validator_info_new_task = task_validators.task_status_validator(new_task_status)[0]
                if validator_info_new_task == False:
                    print(task_validators.task_status_validator(new_task_status)[1])

            new_task = task.Task(new_task_name, new_task_description, new_task_status, id_to_do_list_selected)
            task_created_id = TaskRepository.create_new_task(new_task_name, new_task_description, new_task_status, id_to_do_list_selected[0][0])

            if(task_created_id == -1):
                    print("\n Error: Unfortunately, it was not possible to create your list. Please try again.")
            else:
                    print("\nTask successfully created, with id: " + str(task_created_id))
        case 0:
            break
        case _:
            print("\nInvalid option!")