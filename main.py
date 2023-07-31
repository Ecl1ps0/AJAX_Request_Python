from saver import Saver

URL = 'https://zakup.sk.kz/eprocsearch/api/external/4dv3rts/filter?size=10&page=0&sort=lastModifiedDate,desc'
FILE_PATH = 'items.json'

a = Saver(URL, FILE_PATH)
a.save_to_json()
