from model.db_connector import DBConnector
from model.pet import Pet, PetSchema
from utils import datetime

db = DBConnector().db


class ContentManager:
    @staticmethod
    def get_pets():
        pets = Pet.query.all()
        return PetSchema.dump_many(pets)

    @staticmethod
    def save_pet(pet):
        if "name" and "type" and "gender" and "date" not in pet or not datetime.validate(pet["date"]):
            return {}
        pet["date"] = datetime.cast(pet.get("date"), format='%d/%m/%Y')
        new_pet = Pet(**pet)
        db.session.add(new_pet)
        db.session.commit()
        return PetSchema.dump_one(new_pet)

    @staticmethod
    def delete_pet(pet_id):
        try:
            obj = Pet.query.filter_by(id=pet_id).one()
            return db.session.delete(obj)
        except:
            return {}

    @staticmethod
    def get_one_pet(pet_id):
        pet_query_result = Pet.query.filter_by(id=pet_id).first()
        return PetSchema.dump_one(pet_query_result)

    @staticmethod
    def get_one_using_filters(filters_criteria):
        results = Pet.query.filter_by(**filters_criteria).all()
        return PetSchema.dump_many(results)

    @staticmethod
    def get_pets_with_args(args):
        query_results = []
        if "name" in args:
            query_results = Pet.query.filter_by(name=args.get('name')).order_by(Pet.name).all()
        elif "type" and "gender" in args:
            query_results = Pet.query.filter_by(type=args.get('type'), gender=args.get('gender')).order_by(
                Pet.date).all()
        elif "type" in args:
            query_results = Pet.query.filter_by(type=args.get('type')).order_by(Pet.date).all()
        return PetSchema.dump_many(query_results)
