import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_product_page_contains_button_to_add_to_cart(browser):
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    