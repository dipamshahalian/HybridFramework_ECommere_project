import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.conftest import setup

class Test_001_Login:
    baseURL = ReadConfig.getapplication_url()
    username = ReadConfig.getusermail()
    password = ReadConfig.getpassword()
    # --> in congig.ini
    logger = LogGen.loggen()


    # Mark for

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*******Test_001_Login*******")
        self.logger.info("*******Verifying Home Page Title*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # self.driver.close()
        if act_title=="Account Login":
            assert True
            self.driver.close()
            self.logger.info("*******HomePage title test Passed*******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "homePageTitle.png")
            self.driver.close()
            self.logger.error("*******HomePage title test Failed*******")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*******Verifying Login test*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp= LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        # self.driver.close()
        act_title = self.driver.title
        if act_title=="My Account":
            assert True
            self.driver.close()
            self.logger.info("*******Dashboard title test passed*******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "dashboardTitle.png")
            self.driver.close()
            self.logger.error("*******Dashboard title test failed*******")
            assert False
