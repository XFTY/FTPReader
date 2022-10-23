from ftplib import *

#breakpoint() # use in debug mode!!!

ftpk = FTP()
ftpk.encoding = 'utf-8'

class NoInSetuperr(Exception): ...

class USERNAME_PASSWORD_login_err(Exception): ...

class CANNOT_CONNECT_err(Exception): ...

class CANNOT_GET_WELCOME_ERR(Exception): ...

class control_ftp(object):
    def connect_ftp(IP:str,PORT:int,USER_NAME:str,USER_PASSWORD:str) -> None:
        try:
            ftpk.connect(IP,PORT)
            ftpk.login(USER_NAME,USER_PASSWORD)
        except ConnectionRefusedError:
            raise CANNOT_CONNECT_err(
                "无法连接到FTP服务器！请检查您的FTP服务器的IP地址:{}或端口:{}".format(IP,PORT)
                )
        except error_perm:
            raise USERNAME_PASSWORD_login_err(
                '[-] {}'.format('cannot login! Check your username and password!')
                )


    def download_file(filename:str,remotepath:str,localpath:str,bufsize=1024,encoding='utf-8'):
        try:
            ftpk.getwelcome()
        except:
            raise CANNOT_CONNECT_err()
        fl = open(localpath,'wb',encoding=encoding)
        ftpk.retrbinary('RETR '+remotepath,fl.write(),bufsize) 
        fl.close()

    def upload_file(ftp, remotepath, localpath, bufsize = 1024):
        fp = open(localpath, 'rb')
        ftpk.storbinary('STOR '+ remotepath , fp, bufsize)
        ftpk.set_debuglevel(0)
        fp.close()

    def dir():
        ftpk.dir()

control_ftp.connect_ftp('127.0.0.1',20,'','')