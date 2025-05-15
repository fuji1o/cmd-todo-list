import logging
from typing import Optional

from App.database import Session
from App.exceptions.empty_text import EmptyTextException
from App.exceptions.invalid_id import InvalidTaskIdException
from App.exceptions.task_exists import TaskAlreadyExistsException
from App.exceptions.task_not_found import TaskNotFoundException
from App.models.console_planner import Planner
from App.models.db_planner import DbPlanner
from App.models.task import Task
from App.planner_context import PlannerContext

logging.basicConfig(
    level=logging.INFO,
    filename="py_log.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)
logging.info("An INFO")


if __name__ == "__main__":
    print("Режим работы:\n 1.Консольное приложение\n 2.С использованием БД")
    choice = input().strip()
    if choice == "1":
        context = PlannerContext(Planner())
    elif choice == "2":
        context = PlannerContext(DbPlanner(Session()))
    else:
        print("Неизвестная комманда")
        exit()

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
                task = context.create_task(text)
                context.add_task(task)

            elif command == "mark-done":
                task_id_mark_done: Optional[int] = int(line[1]) if len(line) > 1 else None
                context.mark_done(task_id_mark_done)

            elif command == "delete-task":
                task_id_delete_task: Optional[int] = int(line[1]) if len(line) > 1 else None
                context.delete_task(task_id_delete_task)
                logging.info(f"Задача с ID {task.id} удалена")

            elif command == "edit-task":
                task_id_edit_task: Optional[int] = int(line[1]) if len(line) > 1 else None
                new_text: str = input("Отредактируйте задачу:\n").strip()
                context.edit_task(task_id_edit_task, new_text)

            elif command == "get-tasks":
                for task in context.get_tasks():
                    status: str = "done" if task.is_done else "in process"
                    print(f"{task.id} - {task.text} [{status}]")

            elif command == "exit":
                break

            else:
                print("Неизвестная команда")

        except ValueError:
            print("Ошибка: введите корректное число")

        except (
            TaskAlreadyExistsException,
            TaskNotFoundException,
            EmptyTextException,
            InvalidTaskIdException,
        ) as e:
            print(f"Ошибка: {e}")
