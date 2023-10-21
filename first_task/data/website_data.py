import string
from dataclasses import dataclass

from first_task.utils import Utils
import re


@dataclass
class Website:
    name: string
    popularity: string
    frontend: string
    backend: string
    database: string
    notes: string

    @staticmethod
    def map_elements_to_website_dataclass(elements_and_values: dict):
        name = Utils.extract_field_value_from_dict(elements_and_values, "Websites")
        pattern = r'\[\d+\]'
        popularity = (Utils.extract_field_value_from_dict(elements_and_values, "Popularity")
                      .replace(",", "")).replace(".", "").split(" ")[0]
        popularity = re.sub(pattern, '', popularity)
        frontend = Utils.extract_field_value_from_dict(elements_and_values, "Front-end")
        backend = Utils.extract_field_value_from_dict(elements_and_values, "Back-end")
        database = Utils.extract_field_value_from_dict(elements_and_values, "Database")
        notes = Utils.extract_field_value_from_dict(elements_and_values, "Notes")
        return Website(name=name,
                       popularity=popularity,
                       frontend=frontend,
                       backend=backend,
                       database=database,
                       notes=notes)
