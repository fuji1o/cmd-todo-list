class Task():
    next_id = 0
    
    def __init__(self, text):
        self.id = Task.next_id
        Task.next_id += 1
        self.text = text
        self.is_done = False


class Planner():
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, task):
        if task.id in self.tasks:
            print("Задача с данным id существует")
        else:
            self.tasks[task.id] = task 
            
    
    def mark_done(self, id):
        if id in self.tasks:
            self.tasks[id].is_done = True
        else:
            print("Задача не найдена")
    
    def edit_task(self, id):
        if id in self.tasks:
            self.tasks[id].text = new_text
        else:
            print("Задача не найдена")
    
    def get_tasks(self):
        return list(self.tasks.values())
    

    def delete_tasks(self, id):
        if id in self.tasks:
            del self.tasks[id]
            print("Задача удалена")
        else:
            print("Задача не найдена")
    
    
if __name__ == '__main__':
    planner = Planner()

    while True:
        print("Введите команду")
        line = input().split()
        if not line:
            print("Пустая команда")
            continue

        command = line[0]

        if command == "add-task":
            if len(line) < 2:
                print("Ошибка: введите задачу")
                continue
            text = " ".join(line[1:]).strip()
            if not text:
                print("Ошибка: текст задачи не должен быть пустым")
                continue
            planner.add_task(Task(text))
        
        elif command == "mark-done":
            if len(line) < 2:
                print("Ошибка: id не указан")
                continue
            try:
                id = int(line[1])
            except ValueError:
                print("Ошибка: введите число")
                continue
            planner.mark_done(id)
        
        elif command == "delete-task":
            if len(line) < 2:
                print("Ошибка: id не указан")
                continue
            try:
                id = int(line[1])
            except ValueError:
                print("Ошибка: введите число")
                continue
            planner.delete_tasks(id)

        elif command == "get-tasks":
            for task in planner.get_tasks():
                if task.is_done:
                    status = "done"
                else:
                    status = "in process"
                print(f"{task.id} - {task.text} [{status}]")

        elif command == "edit-task":
            text = " ".join(line[1:]).strip()
            if len(line) < 2:
                print("Ошибка: id не указан")
                continue
            try:
                id = int(line[1])
            except ValueError:
                print("Ошибка: введите число")
                continue
            if id in planner.tasks:
                new_text = input("Отредактируйте задачу\n")
                if not new_text:
                    print("Ошибка: текст задачи не может быть пустым")
                    continue
                planner.edit_task(id)
            else:
                print("Задача не найдена")

        elif command == "exit":
            break
        else: print("Неизвестная команда")
        
            
        


        
        


  
        

        


    

        

    


    
        
        



    






 