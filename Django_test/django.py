import paramiko, getpass
usr = input()
pwd = getpass.getpass
print(pwd)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.27.28',
               port=22,
               username=usr,
               password=str(pwd)
               )
stdin, stdout, stderr = client.exec_command('ifconfig')
data = stdout.read() + stderr.read()
o_file = open('output.txt', 'w', encoding='utf8')
print(data, file=o_file)
o_file.close()
client.close()
