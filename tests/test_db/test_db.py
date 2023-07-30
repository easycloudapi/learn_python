import os
import sys
import unittest
import pytest
import json
from tinydb import TinyDB

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(root_dir)


# same fixture function name (lpdb), should pass same parameter to other test function
@pytest.fixture
def lpdb():
    db = TinyDB("db\\test_db.json")
    print("\n setup DB")
    yield db
    db.truncate()
    print("\n Teardown DB")


def test_insert_one(lpdb):
    lpdb.insert({"name": "indra"})
    assert len(lpdb.all()) == 1
    print("test_insert_one finished")


def test_insert_multiple(lpdb):
    lpdb.insert_multiple([{"name": "Indra"},
                 {"name": "Vikram"},
                 {"name": "Pravin"}])
    assert len(lpdb.all()) == 3
    print("test_insert_multiple finished")


if __name__ == "__main__":
    unittest.main()
