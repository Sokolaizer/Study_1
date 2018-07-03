#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

# Установка параметров
API_HOST = "https://hostaname"
APP_ID = "SOME_APP_ID"
APP_SECRET = "SOME_APP_SECRET"
REDIRECT_URI = "https://apphost/authorized"

# Авторизация приложения

# Так как приложение доверенное, авторизация пользователя не требуется
body = {
    'grant_type': 'client_credentials',
    'redirect_uri': REDIRECT_URI,
    'client_id': APP_ID,
    'client_secret': APP_SECRET,
}

request_url = "{host}/oauth/token".format(host=API_HOST)
response = requests.post(request_url, data=body)
if response.status_code == 200:
    # Получение токена доступа
    access_token = response.json()['access_token']
elif response.status_code == 401:
    print('Ошибка авторизации: {error}'.format(error=response.json()['error']))
    exit(1)
else:
    print('Неизвестная ошибка')
    exit(2)

# Установка заголовков
headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer {access_token}'.format(access_token=access_token)  # Заголовок авторизации
}

# Получение информации об идентификаторе клиента
request_url = "{host}/api/ver1.0/user/".format(host=API_HOST)
response = requests.get(request_url, headers=headers)
user_info = response.json()
print("Client ID: {client_id}".format(client_id=user_info['client_id']))

# Запрос к API, получение списка добавочных клиента
request_url = "{host}/api/ver1.0/client/@me/extension/".format(host=API_HOST)
response = requests.get(request_url, headers=headers)
extension_list = response.json()

# Запрос к API, получение статуса каждого добавочного номера пользователя
for extension in extension_list:
    request_url = "{host}/api/ver1.0/extension/{extension_id}/registration/".format(host=API_HOST,
                                                                                    extension_id=extension['id'])
    response = requests.get(request_url, headers=headers)
    reg_status = response.json()
    # Если добавочный номер зарегистрирован, выводится информация о регистрации
    if reg_status['registered']:
        for registration in reg_status['registrations']:
            print('Extension {extension_name} is registered from device {device}, from {real_address}'.format(
                extension_name=extension['name'], **registration))
    else:
        print('Extension {extension_name} is not registered'.format(extension_name=extension['name']))