from product_parser import ProductParser
from saver import Saver

from formatter import format_data_to_tuple

URL = 'https://zakup.sk.kz/eprocsearch/api/external/4dv3rts/filter?size=10&page=0&sort=lastModifiedDate,desc'
FILE_NAME = 'items.db'

parser = ProductParser(URL)
saver = Saver(FILE_NAME)

data_list = []
for item in parser.parse_items():
    data_list.append(format_data_to_tuple(item))

saver.save_to_database(data_list)


