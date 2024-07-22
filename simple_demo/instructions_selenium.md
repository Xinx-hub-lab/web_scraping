
# Instructions on Selenium

## Tutorials
[Get started with ChromeDriver](https://developer.chrome.com/docs/chromedriver/get-started) by Chrome for Developers

[Selenium Python Tutorial](https://www.geeksforgeeks.org/selenium-python-tutorial/) by GeeksforGeeks

[Browse Youtube](https://stackoverflow.com/questions/74590398/selenium-python-driver-doesnt-click-or-press-the-key-for-the-button-all-the-tim) in Stackoverflow

[How to speed up Selenium](https://www.zenrows.com/blog/selenium-slow#choose-selectors-with-better-performance) in zenrows

## Chrome Issues

### 1. Version Control

According to instructions by Google Chrome, versions after 115 does not collapes on the version difference between Google Chrome and ChromeDriver. The ChromeDriver version I used is 126.0.6478.182, whereas the chrome browser I used is 126.0.6478.183. It does work.

### 2. Path Specification
The downloaded chromedriver must be stated with a path in script, whereas the chrome browser path specification is unnecessary, as it automatically follows the chrome default path.

## Chrome Driver Execution

1. Locate chromedriver in Finder:
    - Navigate to the directory where chromedriver is located

2. Open chromedriver Manually:
    - Right-click on `chromedriver` and select "Open"
    - You should see a dialog saying that the file can’t be opened because Apple cannot check it for malicious software. Click "Open" again
    - This will add an exception for `chromedriver` in Gatekeeper and allow it to run

3. Grant Execute Permissions (if needed):
    - If you haven't already, ensure chromedriver has execute permissions:
    ```bash
    chmod +x /path/to/chromedriver
    ```