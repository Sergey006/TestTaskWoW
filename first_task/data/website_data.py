import string
from dataclasses import dataclass

from first_task.utils import extract_field_value_from_dict, remove_extra_symbols_from_text_number


@dataclass
class Website:
    name: string
    popularity: int
    frontend: string
    backend: string
    database: string
    notes: string

    @staticmethod
    def map_elements_to_website_dataclass(elements_and_values: dict):
        name = extract_field_value_from_dict(elements_and_values, 'Websites')
        popularity = remove_extra_symbols_from_text_number(
            extract_field_value_from_dict(elements_and_values, 'Popularity'))
        frontend = extract_field_value_from_dict(elements_and_values, 'Front-end')
        backend = extract_field_value_from_dict(elements_and_values, 'Back-end')
        database = extract_field_value_from_dict(elements_and_values, 'Database')
        notes = extract_field_value_from_dict(elements_and_values, 'Notes')
        return Website(name=name,
                       popularity=popularity,
                       frontend=frontend,
                       backend=backend,
                       database=database,
                       notes=notes)
