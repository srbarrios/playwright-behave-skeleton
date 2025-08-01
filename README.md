# Playwright-Behave Skeleton

This project serves as a skeleton for a BDD (Behavior-Driven Development) test automation framework using Playwright and `behave`. The purpose is to provide a sample project structure for writing end-to-end tests in Python with a focus on clear, human-readable feature files and reusable step definitions.

## Key Components

The project is composed of the following key files and directories:

  * **`requirements.txt`**: This file lists all the Python dependencies required for the project, including `behave`, `playwright`, and `behave-playwright`.
  * **`features/`**: This directory is where Gherkin `.feature` files are stored, as well as the `environment.py` file.
      * `login.feature`: A sample feature file that defines a scenario for a "Successful login with valid credentials".
      * `environment.py`: This file contains hooks that run at specific points in the test lifecycle, such as before and after the entire test session or before and after each scenario. This is where the Playwright browser is initialized and closed.
  * **`features/steps/`**: This directory contains the Python step definition files that implement the logic for the steps defined in the feature files.
      * `login_steps.py`: Contains the `@given`, `@when`, and `@then` functions that use the Playwright `Page` object to interact with a web page and verify outcomes.

## How It Works

1.  **Test Discovery**: `behave` is configured to find and run tests defined by the Gherkin `.feature` files within the `features/` directory.
2.  **Scenario to Steps**: For each scenario found, `behave` matches the steps (e.g., "Given I am on the login page") to the step definition functions (e.g., `@given('I am on the login page')`) in the `features/steps/` directory.
3.  **Test Execution**: The step definition functions use Playwright's API to perform actions like navigating to a URL (`page.goto(...)`), filling in form fields (`page.get_by_label(...)`), and clicking buttons (`page.click()`). The Playwright `Page` object is shared across steps via `behave`'s `context` object.
4.  **Setup and Teardown**: The hooks in `environment.py` run at specific points to manage the browser session and perform any necessary setup or cleanup tasks.

## How to Run the Tests

1.  **Install Dependencies**: First, ensure you have Python and `pip` installed. Navigate to the project root directory and install the required packages using the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Tests**: From the project root directory, execute the tests using `behave`.

    ```bash
    behave features/
    ```

    `behave` will automatically discover the `login.feature` file in the `features/` directory and run the scenario using the step definitions from `login_steps.py`. The `environment.py` file will also run the setup and teardown hooks during the test session and for each scenario.