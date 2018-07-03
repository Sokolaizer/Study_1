from datetime import datetime
from datetime import timedelta
import CallData
import EmailSender
from AppConfig import AppConfig
from RequestManager import RequestManager

cfg = AppConfig.loadCfg()

end_date = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
start_date = datetime.strftime(datetime.now()-timedelta(seconds=299), '%Y-%m-%d 00:00:00')
week_num = datetime.isocalendar(datetime.now())[1]
client_id = 1534

rManager = RequestManager()
token = (rManager.getAccessToken(123))
payload = rManager.createPayload(start_date, end_date)
headers = rManager.setHeaders(token)

res = rManager.sendRequest(payload, headers, cfg)
cData = CallData.CallsData.createFromJson(res.content)
cData.saveAsExcel()

EmailSender.EmailSender.sendReport('Неделя {week}, тел.звонки ELARSCAN (Bulgaria, Hungary, Belgium).xlsx'.format(week=week_num), ['rkozlov@elar.ru'])
