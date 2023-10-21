from first_task.browser import Browser
from first_task.page_objects.components.base_component import BaseComponent
from first_task.utils import Utils


class TableComponent(BaseComponent):

    def __init__(self, browser: Browser, title):
        super().__init__(browser)
        self.table_title = title
        self.table_base_locator = f'//table[caption[contains(.,\'{self.table_title}\')]]'
        self.header_cells_locator = f'{self.table_base_locator}//thead//th'
        self.concrete_body_row_cells_locator = f'{self.table_base_locator}' + '//tbody//tr[%s]//td'
        self.all_body_rows_cells_locator = f'{self.table_base_locator}' + '//tbody//tr'

    def get_header_row_cells(self):
        return self.browser.find_elements(self.header_cells_locator)

    def get_body_row_cells(self, row_number):
        return self.browser.find_elements(self.concrete_body_row_cells_locator % row_number)

    def get_row_values_mapping(self, row_number):
        title_value_map = dict()
        header_elements = self.get_header_row_cells()
        row_elements = self.get_body_row_cells(row_number)

        for x in range(0, len(header_elements)):
            title_value_map[Utils.extract_text(header_elements[x])] = Utils.extract_text(row_elements[x])

        return title_value_map

    def get_all_rows_values_mapping(self):
        all_rows_values_list = list()
        number_of_rows = self.get_rows_quantity()
        for row_number in range(1, number_of_rows):
            all_rows_values_list.append(self.get_row_values_mapping(row_number))
        return all_rows_values_list

    def get_rows_quantity(self):
        return len(self.browser.find_elements(self.all_body_rows_cells_locator))
