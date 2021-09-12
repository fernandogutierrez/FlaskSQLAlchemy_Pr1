from model.db_connector import DBConnector

db = DBConnector().db
ma = DBConnector().ma


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    date = db.Column(db.Date())

    def __init__(self, name, type, gender, date):
        self.name = name
        self.type = type
        self.gender = gender
        self.date = date


class PetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'type', 'gender', 'date')

    @staticmethod
    def dump_one(obj):
        return PetSchema().dump(obj)

    @staticmethod
    def dump_many(obj):
        return PetSchema(many=True).dump(obj)


if __name__ == '__main__':
    db.create_all()
