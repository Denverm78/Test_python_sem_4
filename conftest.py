import yaml
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser1 = testdata["browser"]
    username = testdata['username']
    password = testdata['password']
    url = testdata['url']
    url1 = testdata['url1']
    user_token = testdata['user_token']


@pytest.fixture(scope="session")
def browser():
    if browser1 == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def login(username1=username, password1=password):
    obj_data = requests.post(url=url, data={'username': username1, 'password': password1})
    token = obj_data.json()['token']
    return token


@pytest.fixture()
def post_post():
    obj_data = requests.post(url=url1, headers={"X-Auth-Token": user_token}, data={
        'username': 'Roman83',
        'password': '5a45102d64',
        'title': 'Название',
        'description': 'Описание',
        'content': 'Содержимое'
    })
    return obj_data.json()['description']


