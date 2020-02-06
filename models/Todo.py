from models.Model import Model

class Todo(Model):

    collection_name = 'todo'

    def __init__(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date


    @staticmethod
    def all():
        Model.collection_name = 'todo'
        return Model.all()

