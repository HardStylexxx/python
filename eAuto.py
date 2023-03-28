
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#CRIANDO OBJETO E SETANDO DADOS DO SERVIDOR
host = 'ex. smtp.gmail.com'
port = 587
user = 'email user'
password = 'senha'
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)

#EFETUANDO LOGIN
print('Login...')
server.ehlo()
server.starttls()
server.login(user, password)

#CRIANDO MENSAGEM
print('Criando mensagem...')
message = 'Olá, Noob!'
email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = ['emailx','emaily']
email_msg['Subject'] = 'teste'
print('Adicionando texto...')
email_msg.attach(MIMEText(message, 'plain'))
mensagem = MIMEText(message,'plain')

#ENVIANDO O EMAIL
print('Enviando mensagem...')
server.sendmail(email_msg['From'], email_msg['To'], mensagem.as_string())
print('Mensagem enviada!')
server.quit()
