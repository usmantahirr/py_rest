from flask import request
from flask_restful import Resource, reqparse, abort

users = [
    {
        "id": 1,
        "name": "Usman"
    },
    {
        "id": 2,
        "name": "Tahir"
    }
]


def get_item(id):
    user = None
    for u in users:
        if (u['id'] == id):
            user = u
    return user


class Auth(Resource):
    def get(self, user_id):
        user = get_item(user_id)
        if (user != None):
            return user
        else:
            abort(404, message='id Not valid')

    def post(self, user_id):
        # Define Body
        user_post_args = reqparse.RequestParser()
        user_post_args.add_argument("name", type=str, help="Name of Item", required=True)

        # Assign arguments to request
        args = user_post_args.parse_args()
        return {
            "data": "Posted",
            "name": user_id,
            "args": args
        }

    def put(self, id):
        print(request.form)
        return {
            "data": "Put"
        }
