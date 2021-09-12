from flask import request, jsonify, abort
from model.db_connector import DBConnector
from model.content_manager import ContentManager

app = DBConnector().app
API_NAME = "/api/v1"


@app.route(f"{API_NAME}/pets", methods=["GET"])
def get_pets():
    """
    get_pets --> Get the list of all pets available
    Return:
        pets(dict): list of pets.
    """
    return jsonify(ContentManager.get_pets())


@app.route(f"{API_NAME}/pet", methods=["POST"])
def post_pet():
    """
    save_pet --> Save a given pet into a database.
    Return:
        pet(dict): The given pet that was saved.
    """
    result = ContentManager.save_pet(request.json)
    if result == {}:
        abort(400, "Invalid request. Check the data sent")
    return result


@app.route(f"{API_NAME}/pet/<pet_id>", methods=["GET"])
def get_pet_by_id(pet_id):
    """
    get_pet_by_id --> Get a pet given an id
    Args:
        pet_id(int): The pet id to look for
    Return:
        pet(dict): A pet
    """
    return jsonify(ContentManager.get_one_pet(pet_id))


@app.route(f"{API_NAME}/pets/filter", methods=["GET"])
def get_pets_with_args():
    """
    get_pet_with_args --> Get a collections of pets given a name, type or gender and type
    e.g: http://localhost:5000/api/v1/pets/filter?type=Cat
    Return:
        pets(dict): list of pets.
    """
    return jsonify(ContentManager.get_pets_with_args(request.args))


@app.route(f"{API_NAME}/pets", methods=["POST"])
def get_pets_with_filters():
    """
    get_pets_with_filters --> Get a collections of pets given criteria in the json request
    Return:
        pets(dict): list of pets.
    """
    return jsonify(ContentManager.get_one_using_filters(request.json))


@app.route(f"{API_NAME}/pet/<pet_id>", methods=["DELETE"])
def delete_pet(pet_id):
    """
    delete_pet --> Delete a pet given an id.
    Args:
        pet_id(integer): The pet id to delete.
    Return:
        result(dict): A dictionary that indicates if the pet was removed
    """
    if ContentManager.delete_pet(pet_id) != 1:
        return jsonify(Message=f"The given pet id <{pet_id}> was not found"), 404
