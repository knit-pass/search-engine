import os
import json


class Writer:
    def write_json(dict, file_name):
        """
        It creates a directory called "data" if it doesn't exist, then it writes the dictionary to a file
        called "file_name.json" in the "data" directory.

        :param dict: The dictionary to write to the file
        :param file_name: The name of the file you want to save the data to
        """
        if not os.path.exists("data"):
            os.makedirs("data")
        with open(f"data/{file_name}.json", "w") as outfile:
            json.dump(dict, outfile, indent=2)
