class Task:
    """
    Класс задачи    .

    Атрибуты:
        id (int): Уникальный ID задачи.
        text (str): Текст задачи.
        is_done (bool): Статус выполнения задачи.
    """
    __next_id: int = 0

    def __init__(self, text: str) -> None:
        """
        Конструктор класса Task. 

        :param text: Текст задачи.
        :type text: str
        """
        self.id: int = Task.__next_id
        Task.__next_id += 1
        self.text: str = text
        self.is_done: bool = False