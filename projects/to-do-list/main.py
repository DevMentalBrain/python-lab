from db.repo.to_do_list_repository import ToDoListRepository
from models.to_do_list import TodoList
from models.display_task_lists import display_task_lists

# listaDeCompras = TodoList("Tarefas de Casa")
# task_list_created_id = ToDoListRepository.createNewList(listaDeCompras.name)

# if(task_list_created_id == -1):
#     print("\nInfelizmente ocorreu um erro! Tente novamente!")
# else:
#     print("\nLista criada com sucesso com id: " + str(task_list_created_id))


while True:
    print("\nWelcome to the task list system!\n\n(1)View all task lists \n(2)To leave \n")
    user_selected_option = int(input("Select an option: ")) 
    match user_selected_option:
        case 1:
            display_task_lists()
        case 2:
            break
        case _:
            print("Invalid option!") 