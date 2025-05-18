from abc import ABC, abstractmethod
from typing import List, Optional

from App.models.task import Task


class IPlanner(ABC):
    @abstractmethod
    def add_task(self, task: Task) -> None:
        """
        Добавление задачи в планировщик.

        :param task: Объект Task(задача), которую необходимо добавить.
        :type task: Task
        """
        pass

    @abstractmethod
    def mark_done(self, id: Optional[int]) -> None:
        """
        Изменеие статуса задачи на "done"(выполненная), после выполнения по id

        :param id: ID задачи, которую нужно отметить как выполненную.
        :type id: Optional[int]
        """
        pass

    @abstractmethod
    def edit_task(self, id: Optional[int], new_text: str) -> None:
        """
        Редактирование задачи по её ID.

        :param id: ID задачи, которую нужно отредактировать.
        :type id: Optional[int]
        :param new_text: Новый текст задачи.
        :type new_text: str
        """
        pass

    @abstractmethod
    def get_tasks(self) -> List[Task]:
        """
        Возвращение списка всех задач в планировщике.
        :rtype: List[Task]
        :return: Список объектов Task.
        """
        pass

    @abstractmethod
    def delete_task(self, id: int) -> None:
        """
        Удаление задачи из планировщика по ID.

        :param id: ID задачи, которую нужно удалить.
        :type id: int
        """
        pass

    @abstractmethod
    def create_task(self, text: str) -> Task:
        """
        Создает объект задачи из текста. Для разных реализаций (обычный Task или ORM TaskModel).
        """
        pass
