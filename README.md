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
* [Download](https://github.com/lxndroc/WebLoginChecker/blob/master/password_list.txt) the sample password list text file.
* Set the value of `DRIVER_PATH` on line 20 to the path of the chromedriver executable on your operating system (OS), e.g. `DRIVER_PATH = 'D:/utils/net/chromedriver'` or `DRIVER_PATH = '/users/username/utils/net/chromedriver'`.
* Set the value of `WEBSITE` on line 72 to the URL of the website to be checked.
* Set the value of `USERNAME_SELECTOR` on line 74 to the username field CSS selector. This can be found by right clicking on the username input field and then right clicking on the highlighted line under the Elements tab and selecting Copy > Copy selector from the drop-down menu.
* Set the value of `PASSWORD_SELECTOR` on line 76 to the password field CSS selector. This can be found similarly to the username selector.
* Set the value of `LOGIN_BUTTON_SELECTOR` on line 78 to the login button CSS selector. This can be found similarly to the username selector.
* If any of the previous 4 is left blank the user is asked for a value in the terminal.
* Replace the 3 passwords in the `password_list.txt` with the passwords to be checked, 1 per line.
* These are the source code and the input file of the program.

## Execution
* Run `WebLoginChecker` with `python WebLoginChecker.py` from the terminal.
* Just `WebLoginChecker.py` or double clicking may also work.

### Process
  1. The program loads Chrome.
  2. If any of the required details, that is, website, username CSS selector, password CSS selector, login button CSS selector, or password list filename, is missing it is asked from the user in the terminal.
  3. The program visits the provided website on Chrome.
  4. It prints a message in the terminal informing whether the website is accessible.
  5. If the website is not accessible it exits.
  6. If the provided username CSS selector is found it enters the username into the corresponding entry box of the webpage. Else it exits.
  7. If the password list has remaining passwords it reads the next one. Else it exits.
  8. If the provided password CSS selector is found it enters the next password into the corresponding entry box of the webpage. Else it exits.
  9. If the provided login button CSS selector is found it presses the login button. Else it exits.
  10. It prints the number, username, password, and result of each attempt in the terminal.
  11. If the password is found or the website does not allow further attempts it prints a message in the terminal, waits for 1 min for the user to check what happened, and exits. Else it returns to step 6.
  
### Sample Output
```
        WebLoginChecker 2020 - by @lxndroc-@aoctut
        ------------------------------------------

[The url was replaced below to keep it safer]
[v] Website https://[url].com/ is accessible!

[The following 2 lines can be ignored]
DevTools listening on ws://127.0.0.1:53693/devtools/browser/f92c5a82-ff80-437e-9b62-24c138900cef
[32084:33248:0602/093816.431:ERROR:device_event_log_impl.cc(208)] [09:38:16.431] Bluetooth: bluetooth_adapter_winrt.cc:1060 Getting Default Adapter failed.
------------------------------------------
[!] 1. User: test
       Password: wEb_pAs1!
[x] Login unsuccessful!
------------------------------------------
[!] 2. User: test
       Password: &p@sS#2.1
[x] Login unsuccessful!
------------------------------------------
[!] 3. User: test
       Password: p@sswOrd%3
[x] Login unsuccessful!
------------------------------------------
[!] Exiting
```

## Licence
WebLoginChecker is released with the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) licence](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Help
To ask for help with running the bot, you can contact us on [Instagram](https://instagram.com/aoctut/).

## Contribution
  * To offer us suggestions or financial support to improve the bot, you can contact us on [Instagram](https://instagram.com/aoctut/).
  * To contribute to this project, you can fork this repository, make improvements, and submit them via a pull request.

#### + THANK YOU FOR BEING HERE 🙏+
