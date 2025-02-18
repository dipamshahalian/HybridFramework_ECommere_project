from selenium.webdriver.common.by import By


class EditAccountDetail:
    editAccount_lnk = "//a[normalize-space()='Edit your account information']"
    firstname_txt = "//input[@id='input-firstname']"
    lastname_txt = "//input[@id='input-lastname']"
    email_txt = "//input[@id='input-email']"
    telephone_txt = "//input[@id='input-telephone']"
    submit_btn = "//input[@value='Continue']"
    # success_text = "//div[@class='alert alert-success alert-dismissible']"

    def __init__(self,driver):
        self.driver=driver

    def ClickOnEditAccount(self):
        self.driver.find_element(By.XPATH,self.editAccount_lnk).click()

    def EditFirstName(self,firstname):
        self.driver.find_element(By.XPATH, self.firstname_txt).clear()
        self.driver.find_element(By.XPATH,self.firstname_txt).send_keys(firstname)

    def EditLastName(self,lastname):
        self.driver.find_element(By.XPATH, self.lastname_txt).clear()
        self.driver.find_element(By.XPATH,self.lastname_txt).send_keys(lastname)

    def EditEmail(self,email):
        self.driver.find_element(By.XPATH, self.email_txt).clear()
        self.driver.find_element(By.XPATH,self.email_txt).send_keys(email)

    def EditNumber(self,telephone):
        self.driver.find_element(By.XPATH, self.telephone_txt).clear()
        self.driver.find_element(By.XPATH,self.telephone_txt).send_keys(telephone)

    def ClickOnSubmit(self):
        self.driver.find_element(By.XPATH,self.submit_btn).click()

    # This cant be called as str value cant be called
    # def SuccessMsg(self):
    #     msg = self.driver.find_element(By.XPATH,self.success_text).text
    #     return msg

