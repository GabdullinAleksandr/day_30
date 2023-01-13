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


# todo_list = []
# todo_list.append(Task('Сделать домашку'))
# todo_list.append(Task(''))
# todo_list.append(Task('Сделать домашку'))
# todo_list.append(Task(''))
# non_empty_tasks = [item for item in todo_list if item]
# len([item for item in todo_list if not item])
