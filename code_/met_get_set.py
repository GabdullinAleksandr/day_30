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

    def __bool__(self):
        return bool(self.content)

    def __repr__(self):
        return f'{self.content} (создано {self.date})'


class TodoList:
    def __init__(self):
        self.tasks = []

    def __setitem__(self, key, value):
        self.tasks.append(None)
        self.tasks[key] = value

    def __getitem__(self, item):
        return self.tasks[item]

    def __delitem__(self, key):
        del self.tasks[key]

    def __repr__(self):
        return str(self.tasks)


# todo_list = TodoList()
# todo_list[0] = Task('Сдать домашку')
# todo_list[1] = Task('Выпить кофе')
# todo_list[2] = Task('efbfegefbefb')
# todo_list[3] = Task('efaaaaaaaaaaafb')
# todo_list
# todo_list[1:3]
# del todo_list[0]
# todo_list
