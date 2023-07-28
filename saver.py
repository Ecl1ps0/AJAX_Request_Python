import json
import os
import re
import pandas as pd

from product_parser import ProductParser


class Saver:
    def __init__(self, url: str, file_path: str):
        self.parser = ProductParser(url)
        self.file_path = file_path

    def save_json(self) -> None:
        for item in self.parser.parse_items():
            data = {
                'number': item['number'],
                'name': item['nameRu'],
            }

            if re.search(r'^CP', item['tenderType']):
                data['tender_type'] = "Запрос ценовых предложений"
            elif re.search(r'^OT', item['tenderType']):
                data['tender_type'] = "Открытый тендер"

            days_remain = pd.to_datetime(item['acceptanceEndDateTime']) - pd.to_datetime(item['acceptanceBeginDateTime'])

            data = {
                **data,
                'price': item['sumTruNoNds'],
                'days_remain': str(days_remain.days)
            }

            if not os.path.exists(self.file_path):
                with open(self.file_path, 'w') as outfile:
                    json.dump([data], outfile, indent=6)
            else:
                with open(self.file_path, 'r') as outfile:
                    existed_data = json.load(outfile)

                existed_data.append(data)

                with open(self.file_path, 'w') as outfile:
                    json.dump(existed_data, outfile, indent=6)
