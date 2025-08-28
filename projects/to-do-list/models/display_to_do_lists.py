from db.repo.to_do_list_repository import ToDoListRepository

def display_to_do_lists():
    name_of_all_lists = ToDoListRepository.get_name_all_lists()

    print("\nExisting lists: \n")

    for qtd_lists in range(len(name_of_all_lists)):
        print(name_of_all_lists[qtd_lists] + "\n")