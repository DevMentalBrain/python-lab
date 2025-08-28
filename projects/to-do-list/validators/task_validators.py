from db.repo.to_do_list_repository import ToDoListRepository

def task_status_validator(task_status):
    if task_status == None:
        return (False, "\nError: Status is null!")
    if task_status == "":
        return (False, "\nError: Status is empty!")
    if task_status.upper() != "PENDENTE" and task_status.upper() != "EM ANDAMENTO" and task_status.upper() != "CONCLUIDA":
        return (False, "\nError: Status is not (Pendente, Em andamento, Concluida)!")
    
    return (True, "")

def task_name_validator(task_name):
    if task_name == None:
        return (False, "\nError: Name is null!")
    if task_name == "":
        return (False, "\nError: Name is empty!")
    if len(task_name) > 50:
        return (False, "\nError: A name cannot contain more than 50 characters!")
    if len(task_name) < 3:
        return (False, "\nError: A name cannot contain fewer than 3 characters!")
    
    return (True, "")

def task_description_validator(task_description):
    if len(task_description) > 100:
        return (False, "\nError: A name cannot contain more than 100 characters!")
    
    return (True, "")

def to_do_list_selected_validator(to_do_list_name, name_of_all_lists):
    for i in range(len(name_of_all_lists)):
        if to_do_list_name == name_of_all_lists[i]:
            to_do_list_id = ToDoListRepository.get_to_do_list_id(to_do_list_name)
            return (True, to_do_list_id)
    return (False, None)