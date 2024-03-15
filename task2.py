from pymongo import MongoClient


client = MongoClient(
    "mongodb://root:example@127.0.0.1:27017/mongo?authSource=admin",
)

db = client.animals

# result_one = db.cats.insert_one(
#     {
#         "name": "barsik",
#         "age": 3,
#         "features": ["ходить в капці", "дає себе гладити", "рудий"],
#     }
# )

# print(result_one.inserted_id)


# result_many = db.cats.insert_many(
#     [
#         {
#             "name": "Lama",
#             "age": 2,
#             "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
#         },
#         {
#             "name": "Liza",
#             "age": 4,
#             "features": ["ходить в лоток", "дає себе гладити", "білий"],
#         },
#     ]
# )
# print(result_many.inserted_ids)


def get_all():
    res = list(db.cats.find())
    print(res)


def get_by_name(name):
    res = db.cats.find_one({"name": name})
    print(res)


def update_age(name, age):
    res = db.cats.update_one({"name": name}, {"$set": {"age": age}})
    get_by_name(name)


def add_new_feature(name, feature):
    res = db.cats.update_one({"name": name}, {"$addToSet": {"features": feature}})
    get_by_name(name)


def delete_by_name(name):
    db.cats.delete_one({"name": name})
    get_all()


def delete_all():
    db.cats.delete_many({})
    get_all()


# get_by_name("barsik")
# update_age("barsik", 5)
# add_new_feature("barsik", "test1")
# delete_by_name("barsik")
# delete_all()
# get_by_name("test")
# update_age("test", 5)
# delete_by_name("test")
