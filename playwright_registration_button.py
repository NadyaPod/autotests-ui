from playwright.sync_api import sync_playwright, expect
from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(AppRoute.REGISTRATION)

    registration_button = page.get_by_test_id("registration-page-registration-button")
    expect(registration_button).to_be_disabled()

    email = page.get_by_test_id("registration-form-email-input").locator("input")
    email.fill("user.name@gmail.com")

    username = page.get_by_test_id("registration-form-username-input").locator("input")
    username.fill("username")

    password = page.get_by_test_id("registration-form-password-input").locator("input")
    password.fill("password")

    expect(registration_button).to_be_enabled()



