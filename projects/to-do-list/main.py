from models.to_do_list_repository import ToDoListRepository
from models.to_do_list import TodoList

#Primeiro teste criando tabela

# listaDeCompras = TodoList("Tarefas de Casa")
# task_list_created_id = ToDoListRepository.createNewList(listaDeCompras.name)

# if(task_list_created_id == -1):
#     print("\nInfelizmente ocorreu um erro! Tente novamente!")
# else:
#     print("\nLista criada com sucesso com id: " + str(task_list_created_id))

ToDoListRepository.getAllLists()