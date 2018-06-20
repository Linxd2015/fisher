DEBUG = True
# 配置sqlalchemy的链接方式
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:8889/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'SECRET_KEY'

# Email配置
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'lxd880903@163.com'
MAIL_PASSWORD = '881013lxd881013'
