import requests
import AppConfig

class RequestManager:
    def __init__(self):
        self.name = 'Hello'

    def createPayload(self, start_date, end_date):
        return {'start_datetime': start_date, 'end_datetime': end_date, 'order': 'desc', 'per_page': 100000, 'page': 1}

    def setHeaders(self, access_token):
        headers = {
            'Content-type': 'application/json',
            'Authorization': 'Bearer {access_token}'.format(access_token=access_token)
        }
        return headers

    def sendRequest(self, payload, headers, cfg: AppConfig.AppConfig):
        response = requests.get(
            'https://apiproxy.telphin.ru:443/api/ver1.0/client/{client_id}/calls/'.format(client_id=cfg.client_id),
            headers=headers, params=payload)

        return response

    def getAccessToken(self, cfg: AppConfig.AppConfig):

        API_HOST = "https://apiproxy.telphin.ru:443"
        APP_ID = "56676304672b4ff6bc480785bdbdcec7"
        APP_SECRET = "6b21b4a4a19b4a97b186530b2f5d4f7a"

        if cfg is not None and isinstance(cfg, AppConfig.AppConfig):
            API_HOST = cfg.api_host
            APP_ID = cfg.api_id
            APP_SECRET = cfg.app_secret

        body = {
            'grant_type': 'client_credentials',
            'client_id': APP_ID,
            'client_secret': APP_SECRET
        }

        request_url = "{host}/oauth/token".format(host=API_HOST)
        response = requests.post(request_url, data=body, json=None)
        if response.status_code == 200:
            access_token = response.json()['access_token']
        elif response.status_code == 401:
            print('Authorization Error: {error}'.format(error=response.json()['error']))
            exit(1)
        else:
            print("HTTP Error#", response.status_code)
            exit(2)

        return access_token
