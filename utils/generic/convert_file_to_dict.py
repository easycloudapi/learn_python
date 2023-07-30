import os
import json


class ConvertFileToDict(object):
    def __init__(self, file_path: str) -> None:
        """
        <parameters>:
            file_path: (str) absolute path of the file
        """
        self.file_path = file_path

    def convertJsonToDict(self) -> dict:
        """
        Convert json file to dictionary
        """
        out_dict = dict()
        
        # file_extension = (self.file_path).split(".")[-1]
        filename, file_extension = os.path.splitext(self.file_path)

        with open(self.file_path) as json_file:
            dict_obj = json.load(json_file)

        out_dict["filename"] = filename + file_extension
        out_dict["file_extension"] = file_extension
        out_dict["dict_obj"] = dict_obj
        return out_dict
    

if __name__ == "__main__":
    file_path = "D:\\pythonProject\\learn_python\\tests\data\\example_1.json"
    obj = ConvertFileToDict(file_path=file_path)
    out = obj.convertJsonToDict()
    print(f"output: {out}")

    # python .\utils\generic\convert_file_to_dict.py
