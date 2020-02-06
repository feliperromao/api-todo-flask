from models.Todo import Todo

def get_all():
    return Todo.all()


def store(data):
    title = data['title']
    description = data['description']
    date = data['date']

    new_todo = Todo(title, description, date)
    return new_todo.save()


def update(id):
    pass


def delete(id):
    pass