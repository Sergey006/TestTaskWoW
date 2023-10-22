from typing import List

import pytest

from first_task.data.website_data import Website
from first_task.utils import is_empty_or_none


def assert_that_website_popularity_more_than(website: Website, expected_popularity):
    if website.popularity < expected_popularity:
        pytest.fail(__build_expected_higher_popularity_error_message(website, expected_popularity))


def assert_websites_popularity_more_than(websites: List[Website], expected_popularity):
    error_message = ''
    for website in websites:
        if website.popularity < expected_popularity:
            error_message += __build_expected_higher_popularity_error_message(website, expected_popularity)
    if not is_empty_or_none(error_message):
        pytest.fail(error_message)


def __build_expected_higher_popularity_error_message(website: Website, expected_popularity):
    return f'{website.name} (Frontend:{website.frontend}\\Backend:{website.backend}) has ' \
           f'{website.popularity} unique visitors per month. (Expected more than {expected_popularity})\n'
