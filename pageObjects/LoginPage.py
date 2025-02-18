from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id = "input-email"
    textbox_password_id = "input-password"
    button_login_xpath= "//input[@value='Login']"
    # link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver


    def setusername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, "//a[@class='list-group-item'][normalize-space()='Logout']").click()

    def btnLogin(self):
        self.driver.find_element(By.XPATH,"//a[@class='list-group-item'][normalize-space()='Login']").click()







