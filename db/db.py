# ref: https://tinydb.readthedocs.io/en/latest/getting-started.html#basic-usage

from tinydb import TinyDB, Query


class Learn_Python_DB():
    learn_python_db = TinyDB("db\\learn_python_db.json")

    def _get_all(self):
        print(Learn_Python_DB.learn_python_db.all())

    def _db_truncate(self):
        Learn_Python_DB.learn_python_db.truncate()

    def _insert_record(self, topic, status):
        record = dict()
        record["topic"] = topic
        record["status"] = status

        Learn_Python_DB.learn_python_db.insert(record)



if __name__ == "__main__":
    lpdb = Learn_Python_DB()
    lpdb._db_truncate()
    lpdb._get_all()
    lpdb._insert_record("learn_unittest", "in-progress")
    lpdb._get_all()
    