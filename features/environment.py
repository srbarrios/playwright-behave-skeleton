from behave.fixture import use_fixture_by_tag
from behave.runner import Context
from playwright.sync_api import sync_playwright

FIXTURE_REGISTRY = {
    'fixture.browser': lambda context, *args, **kwargs: None
}

def before_all(context):
    """
    This hook runs once at the start of the entire test session.
    It's equivalent to 'run_once_per_session' from your original conftest.py.
    """
    print("\n\n--- Setting up the test session... ---")
    context.playwright = sync_playwright().start()

def after_all(context):
    """
    This hook runs once at the end of the entire test session.
    It's equivalent to 'run_once_per_session' teardown.
    """
    print("\n--- Tearing down the test session... ---")
    context.playwright.stop()

def before_scenario(context, scenario):
    """
    This hook runs before each scenario.
    It's equivalent to 'pytest_bdd_before_scenario'.
    """
    print(f"\n\n--> Starting Scenario: '{scenario.name}'")
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    """
    This hook runs after each scenario.
    It's equivalent to 'pytest_bdd_after_scenario'.
    """
    print(f"\n<-- Finished Scenario: '{scenario.name}'")
    context.browser.close()

def before_tag(context: Context, tag: str):
    if tag.startswith('fixture.'):
        return use_fixture_by_tag(tag, context, FIXTURE_REGISTRY)
    return None
