# from .app import app_instance

# @app_instance.route("/home")
# def home():
#     return "This is home page."

from pymongo import MongoClient
from pprint import pprint


db = MongoClient()["pymongo_db"]
print(db.employee.find_one())

data = db.employee.find({})
for a in data:
    print(a["skill"])


result = db.employee.aggregate([{"$group":{"_id":"$dept","total": {"$sum":1}}},{"$project":{"_id":0}}])


for i in result:
    print(i)