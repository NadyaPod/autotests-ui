from playwright.sync_api import expect
from playwright.sync_api import Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page) -> None:
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    block_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(block_text).to_be_visible()
    expect(block_text).to_have_text("There is no results")

    block_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(block_icon).to_be_visible()

    block_description = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(block_description).to_be_visible()
    expect(block_description).to_have_text("Results from the load test pipeline will be displayed here")