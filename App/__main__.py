from App.models.task import Task
from App.exceptions.empty_text import EmptyTextException
from App.exceptions.task_not_found import TaskNotFoundException
from App.exceptions.task_exists import TaskAlreadyExistsException
from App.exceptions.invalid_id import InvalidTaskIdException
from typing import Optional
from App.models.planner import Planner
import logging

logging.basicConfig(level=logging.INFO, 
                    filename="py_log.log", 
                    filemode = "w", 
                    format="%(asctime)s %(levelname)s %(message)s",
                    encoding="utf-8")
logging.info("An INFO")



if __name__ == '__main__':
    
    planner: Planner = Planner()

    while True:
        print("Введите команду")
        line: list[str] = input().split()
        if not line:
            print("Пустая команда")
            continue

        command = line[0]

        try:
            if command == "add-task":
                text: str = " ".join(line[1:]).strip()
                planner.add_task(Task(text))

            elif command == "mark-done":
                task_id_mark_done: Optional[int] = int(line[1]) if len(line) > 1 else None
                planner.mark_done(task_id_mark_done)

            elif command == "delete-task":  
                task_id_delete_task: Optional[int] = int(line[1]) if len(line) > 1 else None
                planner.delete_task(task_id_delete_task)
                logging.info(f"Задача с ID {task.id} удалена")

            elif command == "edit-task":
                task_id_edit_task: Optional[int] = int(line[1]) if len(line) > 1 else None
                new_text: str = input("Отредактируйте задачу:\n").strip()
                planner.edit_task(task_id_edit_task, new_text)

            elif command == "get-tasks":
                for task in planner.get_tasks():
                    status: str = "done" if task.is_done else "in process"
                    print(f"{task.id} - {task.text} [{status}]")

            elif command == "exit":
                break

            else:
                print("Неизвестная команда")

        except ValueError:
            print("Ошибка: введите корректное число")

        except (TaskAlreadyExistsException, TaskNotFoundException, EmptyTextException, InvalidTaskIdException) as e:
            print(f"Ошибка: {e}")