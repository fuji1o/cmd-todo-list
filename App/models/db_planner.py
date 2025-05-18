from typing import List, Optional

from App.exceptions.empty_text import EmptyTextException
from App.exceptions.invalid_id import InvalidTaskIdException
from App.exceptions.task_exists import TaskAlreadyExistsException
from App.exceptions.task_not_found import TaskNotFoundException
from App.iplanner import IPlanner
from App.models.task_model import TaskModel


class DbPlanner(IPlanner):
    def __init__(self, session):
        self.session = session

    def add_task(self, task: TaskModel) -> None:
        if not task.text:
            raise EmptyTextException("Текст задачи не должен быть пустым")
        self.session.add(task)

    def mark_done(self, id: Optional[int]) -> None:
        if id is None:
            raise InvalidTaskIdException("ID задачи не указан")
        task = self.session.get(TaskModel, id)
        if task is None:
            raise TaskNotFoundException("Задача не найдена")
        task.is_done = True

    def edit_task(self, id, new_text):
        if id is None:
            raise InvalidTaskIdException("ID задачи не указан")
        if not new_text:
            raise EmptyTextException("Текст задачи не должен быть пустым")

        task = self.session.get(TaskModel, id)
        if task is None:
            raise TaskNotFoundException("Задача не найдена")
        task.text = new_text

    def get_tasks(self):
        return self.session.query(TaskModel).all()

    def delete_task(self, id):
        if not isinstance(id, int):
            raise InvalidTaskIdException("Не введен id задачи")
        task = self.session.get(TaskModel, id)
        if task is None:
            raise TaskNotFoundException("Задача не найдена")
        self.session.delete(task)

    def create_task(self, text: str) -> TaskModel:
        return TaskModel(text=text)
