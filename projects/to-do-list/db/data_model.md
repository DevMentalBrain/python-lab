# Modelagem do Banco de Dados (to-do-list.db)

## Tabela: task_list
| Campo            | Tipo      | Restrição          |
|------------------|-----------|--------------------|
| task_list_id     | INTEGER  | PRIMARY KEY AUTOINCREMENT |
| task_list_name   | TEXT     | NOT NULL         |

## Tabela: task
| Campo            | Tipo      | Restrição          |
|------------------|-----------|--------------------|
| task_id          | INTEGER  | PRIMARY KEY AUTOINCREMENT |
| task_name        | TEXT     | NOT NULL         |
| task_description | TEXT     |                  |
| task_status      | TEXT     | NOT NULL  CHECK(task_status IN ('pendente', 'em andamento', 'concluido'))       |
| task_list_id     | INTEGER  | FOREIGN KEY REFERENCES task_list(task_list_id) |

## Link modelagem no Figma

- 🔗 https://www.figma.com/board/Wixc0El1HUAueEEo4vuzBs/to-do-list-db?node-id=0-1&t=lYG6sMwpkmmVjwQs-1