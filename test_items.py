import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_product_page_contains_button_to_add_to_cart(browser):
    browser.get(link)

    time.sleep(30)

    button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(button) > 0, "Страница товара не содержит кнопку добавления в корзину"
