from typing import List, Optional

from App.exceptions.empty_text import EmptyTextException
from App.exceptions.invalid_id import InvalidTaskIdException
from App.exceptions.task_exists import TaskAlreadyExistsException
from App.exceptions.task_not_found import TaskNotFoundException
from App.iplanner import IPlanner
from App.models.task import Task


class Planner(IPlanner):
    """
    Класс для управления задачами

    Атрибуты:
        tasks (dict): Словарь задач: ключ - ID задачи, а значением — сама задача.
    """

    def __init__(self) -> None:
        """
        Конструктор класса Planner
        """
        self.tasks: dict[int, Task] = {}

    def add_task(self, task: Task) -> None:
        """
        Добавление задачи в планировщик.

        :param task: Объект Task(задача), которую необходимо добавить.
        :type task: Task
        :raises EmptyTextException: Если текст задачи пустой.
        :raises TaskAlreadyExistsException: Если задача с таким ID уже существует.
        """
        if not task.text:
            raise EmptyTextException("Текст задачи не должен быть пустым")
        if task.id in self.tasks:
            raise TaskAlreadyExistsException("Задача с заданным id уже существует")
        else:
            self.tasks[task.id] = task

    def mark_done(self, id: Optional[int]) -> None:
        """
        Изменеие статуса задачи на "done"(выполненная), после выполнения по id

        :param id: ID задачи, которую нужно отметить как выполненную.
        :type id: Optional[int]
        :raises InvalidTaskIdException: Если ID задачи некорректен.
        :raises TaskNotFoundException: Если задача с таким ID не найдена.
        """
        if id is None:
            raise InvalidTaskIdException("ID задачи не указан")
        if id in self.tasks:
            self.tasks[id].is_done = True
        else:
            raise TaskNotFoundException("Задача не найдена")

    def edit_task(self, id: Optional[int], new_text: str) -> None:
        """
        Редактирование задачи по её ID.

        :param id: ID задачи, которую нужно отредактировать.
        :type id: Optional[int]
        :param new_text: Новый текст задачи.
        :type new_text: str
        :raises InvalidTaskIdException: Если ID задачи некорректен.
        :raises EmptyTextException: Если новый текст задачи пустой.
        :raises TaskNotFoundException: Если задача с таким ID не найдена.
        """
        if id is None:
            raise InvalidTaskIdException("ID задачи не указан")
        if not new_text:
            raise EmptyTextException("Текст задачи не может быть пустым")
        if id in self.tasks:
            self.tasks[id].text = new_text
        else:
            raise TaskNotFoundException("Задача не найдена")

    def get_tasks(self) -> List[Task]:
        """
        Возвращение списка всех задач в планировщике.
        :rtype: List[Task]
        :return: Список объектов Task.
        """
        return list(self.tasks.values())

    def delete_task(self, id: int) -> None:
        """
        Удаление задачи из планировщика по ID.

        :param id: ID задачи, которую нужно удалить.
        :type id: int
        :raises InvalidTaskIdException: Если ID задачи некорректен.
        :raises TaskNotFoundException: Если задача с таким ID не найдена.
        """
        if not isinstance(id, int):
            raise InvalidTaskIdException("Не введен id задачи")
        if id in self.tasks:
            del self.tasks[id]
        else:
            raise TaskNotFoundException("Задача не найдена")

    def create_task(self, text: str) -> Task:
        return Task(text)
