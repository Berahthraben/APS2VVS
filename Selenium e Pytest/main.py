from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
import pytest


def teste_tabs():  # Testa elementos de UI dispostos em tabs no DemoQA
    driver = webdriver.Firefox()
    driver.get("https://demoqa.com/tabs")
    tab_what = driver.find_element(by=By.ID, value="demo-tab-what")
    tab_origin = driver.find_element(by=By.ID, value="demo-tab-origin")
    tab_use = driver.find_element(by=By.ID, value="demo-tab-use")
    driver.implicitly_wait(0.5)
    tab_what.click()
    if not tab_what.get_attribute("aria-selected"):
        driver.quit()
        pytest.fail("Tab 'what' não selecionada! Teste falhado")
    tab_origin.click()
    if not tab_origin.get_attribute("aria-selected"):
        driver.quit()
        pytest.fail("Tab 'origin' não selecionada! Teste falhado")
    tab_use.click()
    if not tab_use.get_attribute("aria-selected"):
        driver.quit()
        pytest.fail("Tab 'use' não selecionada! Teste falhado")
    driver.quit()

