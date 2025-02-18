import configparser

config = configparser.RawConfigParser()
config.read(r"Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getapplication_url():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getusermail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password

