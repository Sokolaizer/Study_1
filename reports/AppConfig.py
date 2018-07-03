import json

class AppConfig:
    def __init__(self):
        self.api_host = ''
        self.client_id = ''
        self.app_secret = ''
        self.api_id = ''

    @staticmethod
    def loadCfg():
        with open("config/server.cfg") as data_file:
            data = json.load(data_file)
            #tmp = json.loads(data)
            cfg = AppConfig()
            cfg.api_host = data['server']['api_host']
            cfg.client_id = data['server']['client_id']
            cfg.app_secret = data['server']['app_secret']
            cfg.api_id = data['server']['api_id']
            return cfg
