import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(root_dir)

from utils.generic.convert_file_to_dict import ConvertFileToDict

def json_to_dict(file_path):
    obj = ConvertFileToDict(file_path=file_path)
    dict_obj = obj.convertJsonToDict()["dict_obj"]
    return dict_obj


if __name__ == "__main__":
    file_path = "D:\\pythonProject\\learn_python\\tests\data\\example_1.json"
    out = json_to_dict(file_path=file_path)
    print(f"out: {out}")
