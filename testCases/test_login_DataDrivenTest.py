import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.conftest import setup
from utilities import XLUtils

class Test002Login:
    baseURL = ReadConfig.getapplication_url()
    Path = "TutorialsNinja_Automation_project/TestData/Login_Frameworks.xlsx" #file path
    # --> in congig.ini
    logger = LogGen.loggen()

    # def test_login_ddt(self,setup):
    #     self.logger.info("*******Test_002_DDT_Login*******")
    #     self.logger.info("*******Verifying Login test*******")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #
    #     self.lp= LoginPage(self.driver)
    #
    #     self.rows = XLUtils.getRowCount(self.path, 'Sheet1') #rows
    #     print("Rows:", self.rows)
    #
    #     list_status=  [] #empty list variable
    #
    #     for r in range(2,self.rows+1):
    #
    #         self.user = XLUtils.readData(self.path, 'Sheet1', r,1)
    #         self.password = XLUtils.readData(self.path, 'Sheet1', r ,2)
    #         self.exp = XLUtils.readData(self.path, 'Sheet1' , r, 3)
    #
    #         self.lp.btnLogin()
    #
    #         self.lp.setusername(self.user)
    #         self.lp.setpassword(self.password)
    #         self.lp.clicklogin()
    #         time.sleep(5)
    #
    #         act_title = self.driver.title
    #         exp_title = 'My Account'
    #
    #         if act_title == exp_title:
    #             if self.exp == "Pass":
    #                 self.logger.info("**Passed**")
    #                 self.lp.clickLogout()
    #                 list_status.append("Pass")
    #                 time.sleep(5)
    #             elif self.exp =="Fail":
    #                     self.logger.info("**Failed**")
    #                     self.lp.btnLogin()
    #                     list_status.append("Fail")
    #                     time.sleep(5)
    #
    #         elif act_title != exp_title:
    #             if self.exp == 'Pass':
    #                 self.logger.info("***Failed***")
    #                 list_status.append("Fail")
    #             elif self.exp == 'Fail':
    #                 self.logger.info("***Passed***")
    #                 list_status.append("Pass")
    #
    #     if "Fail" not in list_status:
    #         self.logger.info("Login DDT Test Passed")
    #         self.driver.close()
    #         assert True
    #     else:
    #         self.logger.info("Login Test Failed")
    #         self.driver.close()
    #         assert False
    #
    #     self.logger.info("-----End of Login Test_002-------")

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("*******Test_002_DDT_Login*******")
        self.logger.info("*******Verifying Login test*******")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.Path, 'Sheet1') #rows
        self.logger.info(f"Total Rows in Excel: {self.rows}")

        list_status = [] #empty list variable

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.Path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.Path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.Path, 'Sheet1', r, 3)

            # self.lp.btnLogin()

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = 'My Account'
            self.logger.info(f"Actual Title: {act_title}, Expected Title: {exp_title}")

            # Check for expected and actual title match
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**Passed**")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                    time.sleep(5)
                elif self.exp == "Fail":
                    self.logger.info("**Failed** - Unexpected Pass")
                    self.lp.btnLogin()
                    list_status.append("Fail")

            else:
                if self.exp == "Pass":
                    self.logger.info("**Failed** - Expected Pass but Title did not match")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**Passed** - Expected Failure and Title did not match")
                    list_status.append("Pass")

            # Navigate back to login page before next iteration
            self.driver.get(self.baseURL)

        # Final assertion and logging
        if "Fail" not in list_status:
            self.logger.info("Login DDT Test Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login Test Failed")
            self.driver.close()
            assert False
        print(list_status)
        self.logger.info("-----End of Login Test_002-------")





