import configparser

config = configparser.RawConfigParser()
config.read("./Configuration/Base.ini")


class ReadConfig_Base():

    def getURL(self):
        return config.get("common details", "url")

