import json
import os
import re
from datetime import datetime
from typing import Generator

from product_parser import ProductParser
from models import Item
from config import format_string


class Saver:
    def __init__(self, url: str, file_path: str):
        self.parser = ProductParser(url)
        self.file_path = file_path
        self.db = Item()

    def format_data_to_dict(self) -> Generator[dict, None, None]:
        for item in self.parser.parse_items():
            data = {
                'number': item['number'],
                'name': item['nameRu'],
            }

            if re.search(r'^CP', item['tenderType']):
                data['tender_type'] = "Запрос ценовых предложений"
            elif re.search(r'^OT', item['tenderType']):
                data['tender_type'] = "Открытый тендер"

            days_remain = datetime.strptime(item['acceptanceEndDateTime'], format_string) - datetime.strptime(item['acceptanceBeginDateTime'], format_string)

            data = {
                **data,
                'price': item['sumTruNoNds'],
                'days_remain': days_remain.days
            }

            yield data

    def format_data_to_tuple(self) -> Generator[tuple, None, None]:
        for item in self.parser.parse_items():
            data = (
                item['number'],
                item['nameRu'],
            )

            if re.search(r'^CP', item['tenderType']):
                data += ("Запрос ценовых предложений",)
            elif re.search(r'^OT', item['tenderType']):
                data += ("Открытый тендер",)

            days_remain = datetime.strptime(item['acceptanceEndDateTime'], format_string) - datetime.strptime(item['acceptanceBeginDateTime'], format_string)

            data += (
                item['sumTruNoNds'],
                days_remain.days
            )

            yield data

    def save_to_json(self) -> None:
        for item in self.format_data_to_dict():
            if not os.path.exists(self.file_path):
                with open(self.file_path, 'w') as outfile:
                    json.dump([item], outfile, indent=6)
            else:
                with open(self.file_path, 'r') as outfile:
                    existed_data = json.load(outfile)

                existed_data.append(item)

                with open(self.file_path, 'w') as outfile:
                    json.dump(existed_data, outfile, indent=6)

    def save_to_database(self) -> None:
        for item in self.format_data_to_tuple():
            self.db.insert(item)

        for item in self.db.get_all():
            print(item)
