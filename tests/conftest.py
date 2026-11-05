import pytest
from playwright.sync_api import Playwright, Page
from collections.abc import Generator
from typing import Any


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email = page.get_by_test_id("registration-form-email-input").locator("input")
    email.fill("user.name@gmail.com")

    username = page.get_by_test_id("registration-form-username-input").locator("input")
    username.fill("username")

    password = page.get_by_test_id("registration-form-password-input").locator("input")
    password.fill("password")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    context.storage_state(path="browser-state.json")

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Generator[Page, Any, None]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()
