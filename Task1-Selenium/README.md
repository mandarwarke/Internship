# Task 1: Selenium Test Automation

## Objective
Automate the testing of a sample web application's login and navigation functionality using Selenium WebDriver.

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- ChromeDriver

## Prerequisites
Ensure you have the following installed before running the script:

1. **Python (3.x)** – [Download here](https://www.python.org/downloads/)
2. **Google Chrome** – Ensure you have the latest version installed.
3. **ChromeDriver** – Download a version matching your Chrome version from [here](https://sites.google.com/chromium.org/driver/).
4. **Required Python Libraries**:
   ```sh
   pip install selenium pytest pytest-html
   ```

## Setup Instructions
1. **Clone this repository**:
   ```sh
   git clone <repository-url>
   cd Task1-Selenium
   ```
2. **Download ChromeDriver** and place it in the project directory.
3. **Ensure the correct path** to `chromedriver.exe` is set in the script:
   ```python
   chrome_driver_path = "D:\\Task1-Selenium\\chromedriver-win64\\chromedriver.exe"
   ```

## Running the Test Script
To execute the Selenium test, use the following command:
```sh
pytest login_test.py --html=report.html
```
This will run the test and generate an HTML report.

## Test Flow
1. Open the SauceDemo login page.
2. Enter the username and password.
3. Click on the login button.
4. Open the sidebar menu.
5. Click on 'All Items' to navigate to the inventory page.
6. Verify successful navigation.

## Expected Output
- The script should log in successfully and navigate to the inventory page.
- An `report.html` file will be generated, summarizing the test execution.

## Troubleshooting
- If the Chrome browser opens and closes immediately, ensure `chromedriver.exe` is compatible with your Chrome version.
- If `pytest` is not recognized, add Python's Scripts folder to the system PATH or reinstall pytest:
  ```sh
  pip install --upgrade pytest
  ```

