from models.Model import Model

class Todo(Model):

    collection_name = 'todo'

    def __init__(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date

    def save(self):
        Model.collection_name = 'todo'
        Model.create({
            'title': self.title,
            'description': self.description,
            'date': self.date,
        })

    def __str__(self):
        return {
            'title': self.title,
            'description': self.description,
            'date': self.date
        }


    @staticmethod
    def all():
        Model.collection_name = 'todo'
        return Model.all()

