from bson.code import Code
import pymongo as pm

if __name__ == '__main__':
    print('Testing access to MongoDB')

    client = pm.MongoClient()

    db = client['test']

    collection = db['restaurants']

    # cursor = collection \
    #     .find({"address.zipcode": "10460"}) \
    #     .sort([
    #         ("borough", pm.ASCENDING)
    #     ])

    # for record in cursor:
    #     print(record)

    cursor = collection \
        .aggregate([
            {
                "$group": {
                    "_id": "$borough",
                    "count": {"$sum": 1}
                }
            }
        ])

    for record in cursor['result']:
        print(record)


    mapper = Code("""
        function () {
            for(var grade in this.grades){
                emit({
                    _borough_id: this.borough,
                    _grade: this.grades[grade].grade
                }, 1)
            }
        }
    """)

    reducer = Code("""
        function (key, values) {
            var total = 0;
            for (var i = 0; i < values.length; i++) {
                total += values[i];
            }
            return total;
        }
    """)

    result = collection.map_reduce(mapper, reducer, 'myResults')

    for rec in result.find():
        print(rec)

# this.grades.forEach(function(z) {
#                 emit(z.grade, 1);
#             });


# from pymongo import MongoClient

# db = MongoClient().aggregation_example
# result = db.things.insert_many([
#     {"x": 1, "tags": ["dog", "cat"]},
#     {"x": 2, "tags": ["cat"]},
#     {"x": 2, "tags": ["mouse", "cat", "dog"]},
#     {"x": 3, "tags": []}
# ])

# from pymongo import MongoClient
# db = MongoClient().aggregation_example
# db.things.insert({"x": 1, "tags": ["dog", "cat"]})
# db.things.insert({"x": 2, "tags": ["cat"]})
# db.things.insert({"x": 2, "tags": ["mouse", "cat", "dog"]})
# db.things.insert({"x": 3, "tags": []})

# from bson.son import SON
# result = db.things.aggregate([
#     {"$unwind": "$tags"},
#     {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
#     {"$sort": SON([("count", -1), ("_id", -1)])}
# ])


# print(result)