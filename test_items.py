import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_guest_should_see_cart_button(browser):
    assert browser.find_element_by_css_selector("#add_to_basket_form > button")
