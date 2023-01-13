import datetime


class Task:
    def __init__(self, content):
        self.content = content
        self.date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def __keys(self):
        return self.content, self.date

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.content == other.content
        return NotImplemented

    def __hash__(self):
        return hash(self.content)

    def __repr__(self):
        return f'{self.content} (создано {self.date})'


todo_list = set()
todo_list.add(Task('Сделать домашку'))
todo_list.add(Task('Выпить кофе'))
todo_list.add(Task('Выйти на пробежку'))
todo_list.add(Task('Сделать домашку'))
todo_list.add(Task('Выйти на пробежку'))

for item in todo_list:
    print(item)
