import re
from datetime import datetime

from config import format_string


def format_data_to_dict(item: dict) -> dict:

    data = {
        'number': item['number'],
        'name': item['nameRu'],
    }

    if re.search(r'^CP', item['tenderType']):
        data['tender_type'] = "Запрос ценовых предложений"
    elif re.search(r'^OT', item['tenderType']):
        data['tender_type'] = "Открытый тендер"

    days_remain = datetime.strptime(item['acceptanceEndDateTime'], format_string) - datetime.strptime(
        item['acceptanceBeginDateTime'], format_string)

    data = {
        **data,
        'price': item['sumTruNoNds'],
        'days_remain': days_remain.days
    }

    return data


def format_data_to_tuple(item: dict) -> tuple:

    data = (
        item['number'],
        item['nameRu'],
    )

    if re.search(r'^CP', item['tenderType']):
        data += ("Запрос ценовых предложений",)
    elif re.search(r'^OT', item['tenderType']):
        data += ("Открытый тендер",)

    days_remain = datetime.strptime(item['acceptanceEndDateTime'], format_string) - datetime.strptime(
        item['acceptanceBeginDateTime'], format_string)

    data += (
        item['sumTruNoNds'],
        days_remain.days
    )

    return data
