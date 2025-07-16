import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/Base.ini")


class ReadConfig_Base():

    def getURL(self):
        return config.get("Common Details", "url")

