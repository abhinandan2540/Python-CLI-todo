import os
import json
from argparse import ArgumentParser
from datetime import datetime

data = "todo.txt"
list = "list.txt"
if os.path.exists(data):
    with open(data, 'r')as file:
        todoSheet = json.load(file)
else:
    todoSheet = []


def save_data():
    with open(data, 'w') as file:
        json.dump(todoSheet, file, indent=4)


def time_now():
    date = datetime.now()
    date_modi = date.strftime("%m/%d/%Y")
    return date_modi


def add_data(todo_id, todo_descrip, todo_status):
    task = {
        "todo_id": todo_id,
        "todo_descrip": todo_descrip,
        "todo_status": todo_status,
        "todo_time": time_now()

    }

    todoSheet.append(task)
    save_data()
    print("data added sucessfully")


def view_data():
    if todoSheet:
        for task in todoSheet:
            print(
                f"todo_id :{task['todo_id']}, todo_description :{task['todo_descrip']}, todo_status :{task['todo_status']}, todo_time :{task['todo_time']}")

    else:
        print("no record was found")


def update_data():
    task_id = input("task id number :")
    for task in todoSheet:
        if task['task_id'] == task_id:
            task['todo_descrip'] = input("todo_description : ")
            task['todo_status'] = input("todo_status : ")
            task['todo_time'] = time_now()
            save_data()
        else:
            print(f"{task_id} is not found")


def delete_data():
    del_id = input("enter id num to delete : ")
    for task in todoSheet:
        if task['todo_id'] == del_id:
            todoSheet.remove(task)
            print(f"{del_id} deleted sucessfully")
            save_data()
        else:
            print(f"{del_id} not found for deletion")


# done undone underprocess data's

def list_data():
    todo_status = input(
        "choose between task_done/task_undone/task_underprocess :")
    for task in todoSheet:
        if task['todo_status'] == todo_status:
            with open(list, 'w') as file:
                json.dump(todoSheet, file, indent=4)


def main():
    parser = ArgumentParser()
    parser.add_argument("--add", action="store_true", help="adding the data")
    parser.add_argument("--view", action="store_true",
                        help="visualizing the data")
    parser.add_argument("--todo_id", type=str,
                        help="id of the task (string type)")
    parser.add_argument("--todo_descrip", type=str,
                        help="description about the task (string type)")
    parser.add_argument("--todo_status", type=str,
                        help="status of the task (string type)")
    parser.add_argument("--update", action='store_true',
                        help="updating the task")
    parser.add_argument("--delete", action="store_true",
                        help="deleting the data")
    parser.add_argument("--listing", action="store_true",
                        help="listing the task")

    args = parser.parse_args()

    if (args.add) and (args.todo_id) and (args.todo_descrip) and (args.todo_status):
        add_data(args.todo_id, args.todo_descrip, args.todo_status)
    elif (args.view):
        view_data()
    elif (args.update):
        update_data()
    elif (args.delete):
        delete_data()
    elif (args.listing):
        list_data()
    else:
        print(parser.print_help())


if __name__ == "__main__":
    main()
