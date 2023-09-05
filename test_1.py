from testpage import OperationHelper
from testpage import token_auth
import logging
import time
import yaml
import requests

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)
    name = data["username"]
    paswd = data["password"]
    url = data['url']
    url1 = data['url1']


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    time.sleep(3)
    assert testpage.get_error_text() == "401", "Test_1 FAIL"


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(name)
    testpage.enter_pass(paswd)
    testpage.click_login_button()
    time.sleep(2)
    assert testpage.get_profile_text() == f"Hello, {name}", "Test_2 FAIL"


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationHelper(browser)
    testpage.click_to_do_new_post()
    testpage.enter_title("Название")
    testpage.enter_description("Описание")
    testpage.enter_content("Содержимое")
    testpage.click_save_post_button()
    time.sleep(5)
    assert testpage.get_title_text() == "Название", "Test_3 FAIL"



def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationHelper(browser)
    testpage.click_contact_button()
    testpage.enter_name("Роман")
    testpage.enter_email("roman@mail.ru")
    testpage.enter_contact_content("Текст")
    testpage.contact_us_save_button()
    time.sleep(3)
    assert testpage.get_alert_text() == "Form successfully submitted", "Test_4 FAIL"

# Тесты из первого семинара
def test_step5(login):
    logging.info("Test5 Starting")
    assert 'Содержимое' in token_auth(login)


def test_step6(post_post):
    logging.info("Test6 Starting")
    assert 'Описание' in post_post
