<h1 align="center">+ WebLoginChecker 2020 +</h1>
<p align="center">
  <h3 align='center'>Check web login passwords</h3>
</p>
  <p align="center">⭐️ & 🔱</p>
  <p align="center">
    <a href="https://github.com/lxndroc">
      <img src="https://img.shields.io/badge/Coded%20By-@lxndroc--@aoctut-yellow" />
    </a>
    <img src="https://img.shields.io/badge/Version-2020-yellow" />
    <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
      <img src="https://img.shields.io/badge/Licence-CC%20BY--NC--SA%204.0-yellow" />
    </a>
    <a href="https://instagram.com/aoctut/">
      <img src="https://img.shields.io/badge/Contact-@aoctut-yellow" />
    </a>
  </p>
  <p align="center">
    <a href="https://python.org/">
      <img src="https://img.shields.io/badge/Built%20with-Python3-yellow" />
    </a>
    <a href="https://selenium.dev/selenium/docs/api/py/">
      <img src="https://img.shields.io/badge/Built%20with-Selenium%20WebDriver-yellow" />
    </a>
    <a href="https://google.com/chrome/">
      <img src="https://img.shields.io/badge/Powered%20by-Google%20Chrome-yellow" />
    </a>
  </p>

## Contents
* Purpose
* Method
* Installation
* Execution
* Licence
* Help
* Contribution

## Purpose
* The program checks a list of passwords for a given username at a website login page and finds if and which is accepted.

## Method
* The code follows the procedural paradigm & automated browsing via the Selenium WebDriver that sends & displays actions onto the Chrome web browser with appropriate delays.

## Installation
### 1. `Python 3.6` & above
* [Download](https://python.org/downloads/) the installer.
* Run & follow the steps of the installer.
* This is the used programming language.
### 2. `Selenium WebDriver for Chrome`
* [Download](http://chromedriver.chromium.org/downloads) the compressed `chromedriver` installer corresponding to your Chrome version & OS version.
* The used Chrome version is on the 1st output line when requesting `chrome://version` in Chrome's search bar.
* The filename to download is `chromedriver_win32.zip` for Windows & `chromedriver_mac64.zip` for Mac.
* Unzip the compressed installer.
* Run & follow the steps of the installer.
* This is the automatic driver for Chrome.
### 3. `selenium` package
* Install with `pip install selenium` from the terminal.
* These are the Python bindings to the `Selenium Webdriver`.
### 4. `Google Chrome`
* [Download](https://google.com/chrome/) the installer.
* Run & follow the steps of the installer.
* This is the web browser Chrome.
### 5. `WebLoginChecker`
* [Download](https://github.com/lxndroc/WebLoginChecker/blob/master/WebLoginChecker.py) the Python source.
* Set the value of `DRIVER_PATH` on line 20 to the path of the chromedriver executable on your operating system (OS), e.g. `DRIVER_PATH = 'D:/utils/net/chromedriver'` or `DRIVER_PATH = '/users/username/utils/net/chromedriver'`.
* Set the value of `WEBSITE` on line 67 to the URL of the website to be checked.
* Set the value of `USERNAME_SELECTOR` on line 69 to the username field selector.
* Set the value of `PASSWORD_SELECTOR` on line 71 to the password field selector.
* Set the value of `LOGIN_BUTTON_SELECTOR` on line 73 to the login button selector.
* Set the value of `PASS_LIST` on line 75 to the path and filename containing the passwords to be checked.
* If any of the previous 5 is left blank the user is asked for a value on the terminal.
* This is the source code of the program.

## Execution
* Run `WebLoginChecker` with `python WebLoginChecker.py` from the terminal.
* Just `WebLoginChecker.py` or double clicking may also work.

### Process
  1. The program loads Chrome.
  2. If any of the required details, that is, website, username selector, password selector, login button selector, or password list filename, is missing it is asked from the user in the terminal.
  3. The program visits the provided website on Chrome.
  4. If the website does not exist it prints a message in the terminal and stops.
  5. It enters the username and password into the entry boxes of the webpage using the provided element selectors for them. 5. It presses the login button using the provided element selector for this.
  6. It displays the number, username, and password of each attempt in the terminal.
  7. If the password is found or the website does not allow further attempts it prints a message in the terminal and stops. Else it returns to step 5.
  
### Sample Output
Due to handling confidential data there is no sample output.

## Licence
WebLoginChecker is released with the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) licence](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Help
To ask for help with running the bot, you can contact us on [Instagram](https://instagram.com/aoctut/).

## Contribution
  * To offer us suggestions or financial support to improve the bot, you can contact us on [Instagram](https://instagram.com/aoctut/).
  * To contribute to this project, you can fork this repository, make improvements, and submit them via a pull request.

#### + THANK YOU FOR BEING HERE 🙏+
