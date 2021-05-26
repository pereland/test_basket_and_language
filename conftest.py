import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='es', help="Choose lang")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    language = request.config.getoption("language")
    if language == "ru":
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "fr":
        link = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "es":
        link = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "ar":
        link = "http://selenium1py.pythonanywhere.com/ar/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "ca":
        link = "http://selenium1py.pythonanywhere.com/ca/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "cs":
        link = "http://selenium1py.pythonanywhere.com/cs/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "da":
        link = "http://selenium1py.pythonanywhere.com/da/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "de":
        link = "http://selenium1py.pythonanywhere.com/de/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "en-gb":
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "el":
        link = "http://selenium1py.pythonanywhere.com/el/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "fi":
        link = "http://selenium1py.pythonanywhere.com/fi/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "it":
        link = "http://selenium1py.pythonanywhere.com/it/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "ko":
        link = "http://selenium1py.pythonanywhere.com/ko/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "nl":
        link = "http://selenium1py.pythonanywhere.com/nl/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "pl":
        link = "http://selenium1py.pythonanywhere.com/pl/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "pt":
        link = "http://selenium1py.pythonanywhere.com/pt/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "pt-br":
        link = "http://selenium1py.pythonanywhere.com/pt-br/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "ro":
        link = "http://selenium1py.pythonanywhere.com/ro/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "sk":
        link = "http://selenium1py.pythonanywhere.com/sk/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "uk":
        link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    if language == "zh-cn":
        link = "http://selenium1py.pythonanywhere.com/zh-cn/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
    yield browser
    print("\nquit browser..")
    browser.quit()




