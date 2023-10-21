from selenium.webdriver.remote.webelement import WebElement


class Utils:

    @staticmethod
    def extract_text(element: WebElement):
        def is_empty_or_null(text_exist):
            return not text_exist or len(text_exist) == 0

        result = ""

        element_text = element.text
        inner_text = element.get_attribute("innerText")
        value = element.get_attribute("value")

        if not is_empty_or_null(element_text):
            result = element_text
        elif not is_empty_or_null(inner_text):
            result = inner_text
        elif not is_empty_or_null(value):
            result = value

        return result

    @staticmethod
    def extract_field_value_from_dict(fields: dict, field_name):
        for field in fields.keys():
            if field_name in field:
                return fields[field]
        return ""
