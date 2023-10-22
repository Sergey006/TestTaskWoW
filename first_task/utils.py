import re

from selenium.webdriver.remote.webelement import WebElement


def extract_text(element: WebElement):
    # сделаны отдельные return'ы, чтобы не обращаться к элементу повторно, если текст уже найден
    element_text = element.text
    if not is_empty_or_none(element_text):
        return element_text

    inner_text = element.get_attribute('innerText')
    if not is_empty_or_none(inner_text):
        return inner_text

    value = element.get_attribute('value')
    if not is_empty_or_none(value):
        return value

    return ''


def extract_field_value_from_dict(fields: dict, field_name):
    for field in fields.keys():
        if field_name in field:
            return remove_extra_symbols_from_text(fields[field])
    return ''


def remove_extra_symbols_from_text(text):
    pattern = r'\[.*?\]|\(.*?\)'
    result = re.sub(pattern, '', text)
    return result


def remove_extra_symbols_from_text_number(text_number):
    pattern = r'\[.*?\]|\(.*?\)|[.,]'
    result = re.sub(pattern, '', text_number)
    return int(result)


def is_empty_or_none(text):
    return not text or len(text) == 0
