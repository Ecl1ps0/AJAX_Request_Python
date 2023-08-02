import json
import os

from models import Item


class Saver:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.db = Item(file_path)

    def save_to_json(self, items: list[dict]) -> None:
        for item in items:
            if not os.path.exists(self.file_path):
                with open(self.file_path, 'w') as outfile:
                    json.dump([item], outfile, indent=6)
            else:
                with open(self.file_path, 'r') as outfile:
                    existed_data = json.load(outfile)

                existed_data.append(item)

                with open(self.file_path, 'w') as outfile:
                    json.dump(existed_data, outfile, indent=6)

    def save_to_database(self, items: list[tuple]) -> None:
        for item in items:
            self.db.insert(item)

        for item in self.db.get_all():
            print(item)
