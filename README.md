# Task Manager

This is a simple task manager written in Python.  
It allows users to create, display, and delete tasks through a menu-driven interface.

## Features

### Add a new task

Users can enter a task name and description.

- Prevents empty input
- Prevents adding tasks with duplicate names

### Display all tasks

Shows a numbered list of all saved tasks along with their descriptions.

### Delete a task

Users can delete a task by selecting its number from the list.

- Validates index input
- Prevents deleting a non-existing task

### Simple user menu

The application runs inside an interactive loop until the user chooses to exit.

## How to Run

1. Make sure you have Python 3 installed.
2. Run the script from your terminal:  
   `python main.py`  
   The main menu will appear, allowing you to choose one of the following options:

```
1. Add a new task
2. Display all tasks
3. Delete a task
4. Exit the program
```

## Example Interaction

```
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu

Vyberte možnost(1-4): 1
Zadejte název úkolu: Nákup
Zadejte popis úkolu: Koupit mléko a chleba
Úkol 'Nákup' byl přidán.

1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu

Vyberte možnost(1-4): 2
Seznam úkolů:
1. Nákup - Koupit mléko a chleba

1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu
```

## Notes

Tasks are stored only in memory, not saved to a file.  
After restarting the program, the task list will reset.  
The program handles invalid inputs (empty strings, invalid menu choices, wrong indexes).
