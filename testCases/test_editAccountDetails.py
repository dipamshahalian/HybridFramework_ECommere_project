# import random
# import string
import time

from selenium.webdriver.common.by import By
import pytest
from pageObjects.EditAccountPage import EditAccountDetail
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.conftest import setup

@pytest.mark.sanity
@pytest.mark.regression
class Test_003_EditAccountDetails:
    baseURL = ReadConfig.getapplication_url()
    user = ReadConfig.getusermail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen() #Logger

    # #generating Random email ID
    # def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    #     return ''.join(random.choice(chars) for x in range(size))

    def test_EditAccountDetails(self,setup):
        self.logger.info("*** Test_003_Edit Account Details ***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.user)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("*** Login Successful ***")
        self.logger.info(" *** Editing Account Details ***")

        self.edit = EditAccountDetail(self.driver)
        self.edit.ClickOnEditAccount()

        ## for random email
        # self.email = self.random_generator() + "@gmail.com"
        self.edit.EditFirstName("ABC")
        self.edit.EditLastName("XYZ")
        self.edit.EditEmail("aliantest236+4020@gmail.com")
        self.edit.EditNumber("Abc@223133")
        self.edit.ClickOnSubmit()

        self.logger.info(" *** Values submitted ***")
        time.sleep(5)

        self.msg = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
        if "Success: Your account has been successfully updated." in self.msg:
            print("Passed")
            assert True
            self.driver.close()
            self.logger.info(" ***Test Case Passed*** ")
        else:
            print("Failed")
            self.driver.close()
            self.logger.error(" ***Test Case Failed*** ")
            assert False








