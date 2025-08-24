from models import TodoList, ToDoListRepository

#Primeiro teste criando tabela

listaDeCompras = TodoList("Compras para Casa")
task_list_created = ToDoListRepository.createNewList(listaDeCompras)

if(task_list_created == False):
    print("\nInfelizmente ocorreu um erro! Tente novamente!")
else:
    print("\nLista criada com sucesso!")