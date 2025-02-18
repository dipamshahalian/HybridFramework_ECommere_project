from selenium import webdriver
import pytest

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser): #get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #return the browser value to setup method
    return request.config.getoption("--browser")

#----------------------------Pytest HTML Report -------------------------------

# Hook to add environment info to HTML report
def pytest_configure(config):
    if hasattr(config, "stash"):
        from _pytest.stash import StashKey
        metadata_key = StashKey[dict]()
        config.stash[metadata_key] = {
            "Project Name": "TutorialsNinja Automation",
            "Module Name": "Login",
            "Tester": "Dipam"
        }

# Hook to modify/delete environment info in HTML report
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugins", None)
