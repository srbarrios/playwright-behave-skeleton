from behave import given, when, then
from playwright.sync_api import Page, expect

@given('I am on the login page')
def go_to_login_page(context):
    """Navigates to the login page."""
    page: Page = context.page
    page.goto("https://oubiti.com/login.html")

@when('I enter valid credentials')
def enter_valid_credentials(context):
    """Fills in the username and password fields."""
    page: Page = context.page
    page.get_by_label("Username").fill("testuser")
    page.get_by_label("Password").fill("testpass")

@when('I click the login button')
def click_login_button(context):
    """Clicks the login button."""
    page: Page = context.page
    page.get_by_role("button", name="Login").click()

@then('I should be redirected to a login success page')
def verify_login_success(context):
    """Asserts that the user has successfully logged in."""
    page: Page = context.page
    expect(page).to_have_url("https://oubiti.com/login-success.html")
    expect(page.get_by_text("You have successfully logged in.")).to_be_visible()