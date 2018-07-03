import smtplib
import email.utils
from datetime import datetime
from datetime import timedelta
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


class EmailSender:
    def __init__(self):
        return

    @staticmethod
    def sendReport(reportFilePath, reportRecieverAddress):
        week_num = datetime.isocalendar(datetime.now())[1]
        end_date = datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M')
        start_date = datetime.strftime(datetime.now() - timedelta(seconds=299), '%d-%m-%Y 00:00')
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Неделя #{week}. Тел.звонки ELARSCAN (Bulgaria, Hungary, Belgium)'.format(week=week_num)
        msg['From'] = 'ДСРИТС  <dsrits@elar.ru>'
        msg['To'] = ';'.join(reportRecieverAddress)

        text = "Добрый день, Дмитрий Рудольфович!\n\nСтатистика звонков с {start} по {end} во вложении.\n\n\n\nВнимание! Данное сообщение сформировано автоматически\n\n\n\nС уважением,\nДмитрий Топорин\nВедущий системный администратор\nДепартамент сопровождения и развития ИТ-сервисов\nКорпорация ЭЛАР".format(
            start=start_date, end=end_date)

        html = """\
        <html>

        <body lang="RU">
        <div class="WordSection1">
        <p class="MsoNormal"><span style="font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;">Добрый день, Дмитрий Рудольфович!<o:p></o:p></span></p>
        <p class="MsoNormal"><span style="font-size:10.0pt;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;">Статистика звонков с {start} по {end} во вложении.<o:p></o:p></span></p>
        <p class="MsoNormal"><span style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;"><o:p>&nbsp;</o:p></span></p>
        <p class="MsoNormal"><span style="font-size:10.0pt;font-weight:bold;font-family:&quot;Arial&quot;,&quot;sans-serif&quot;">Внимание! Данное сообщение сформировано автоматически.<o:p></o:p></span></p>
        </div></body></html>""".format(start=start_date, end=end_date)

        fp = open(reportFilePath, 'rb')
        message = MIMEText(html, 'html')
        #message = MIMEText(text, 'text')
        attachment = MIMEBase('application', 'alternative')
        attachment.set_payload(fp.read())
        fp.close()
        attachment.add_header('Content-Disposition', 'attachment', filename='Неделя {week}, тел.звонки ELARSCAN (Bulgaria, Hungary, Belgium).xlsx'.format(week=week_num))
        encoders.encode_base64(attachment)
        msg.attach(attachment)
        msg.attach(message)

        server = smtplib.SMTP('elar-hub1.elar.local', 25)
        server.ehlo()
        server.sendmail(msg['From'], reportRecieverAddress, msg.as_string())
        server.quit()

        return True
