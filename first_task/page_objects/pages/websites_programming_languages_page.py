from first_task.data.website_data import Website
from first_task.page_objects.components.table_component import TableComponent
from first_task.page_objects.pages.base_page import BasePage


class WebsitesProgrammingLanguagesPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.table_component = TableComponent(self.browser, 'Programming languages used in most popular websites')
        self.url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'

    def open_page(self):
        self.browser.open(self.url)
        return self

    def get_website_by_row_number(self, row_number):
        fields_values = self.table_component.get_row_values_mapping(row_number)
        return Website.map_elements_to_website_dataclass(fields_values)

    def get_all_websites(self):
        all_rows_fields_values = self.table_component.get_all_rows_values_mapping()
        all_websites = list()
        for row in all_rows_fields_values:
            all_websites.append(Website.map_elements_to_website_dataclass(row))
        return all_websites
