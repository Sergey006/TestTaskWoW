import pytest

from first_task.page_objects.pages.websites_programming_languages_page import WebsitesProgrammingLanguagesPage
from first_task.tests.test_base import TestBase


class TestProgrammingLanguagesBase(TestBase):

    @pytest.mark.parametrize("expected_popularity_value", [10 ** 7,
                                                           1.5 * (10 ** 7),
                                                           5 * (10 ** 7),
                                                           10 ** 8,
                                                           5 * (10 ** 8),
                                                           10 ** 9,
                                                           1.5 * (10 ** 9)])
    def test_popularity_should_be_more_than_concrete_value(self, expected_popularity_value):
        # act
        websites = (WebsitesProgrammingLanguagesPage(self.browser)
                    .open_page()
                    .get_all_websites())
        # assert
        assert all(float(website.popularity) > expected_popularity_value for website in websites)
