def pr_func(name_func, *args):
    name = name_func.__name__.title().replace('_', ' ') + ":"
    print(name, *args)


def open_browser(browser_name):
    pr_func(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    pr_func(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    pr_func(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="https://ya.ru/")
find_registration_button_on_login_page(page_url="https://ya.ru/", button_text="Find")