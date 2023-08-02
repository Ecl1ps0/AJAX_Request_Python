from typing import Generator

import requests
import re

from config import cookies, headers, json_data


class ProductParser:
    def __init__(self, url: str):
        self.url = url

    def parse_items(self) -> Generator[dict, None, None]:
        current_page = 0
        current_url = self.url
        while True:
            try:
                response = requests.post(current_url, cookies=cookies, headers=headers, json=json_data,)
                data = response.json()
            except Exception as e:
                print(e)

            if isinstance(data, list) and not data:
                return

            for item in data:
                yield item

            current_page += 1
            print(current_url)

            current_url = re.sub(r'page=\d+', f'page={current_page}', current_url)
