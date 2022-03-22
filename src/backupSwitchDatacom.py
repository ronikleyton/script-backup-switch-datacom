from telnetlib import Telnet
from exception.exceptions import *
from datetime import date
import time
import os
from dotenv import load_dotenv
import json

load_dotenv()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

f = open(f'{ROOT_DIR}/equipamentos.json')

equipamentos = json.load(f)['equipamentos']

def backupSwitchDatacom(equipamento):
  
    IP_SERVER_TFTP = os.environ.get('IP_SERVER_TFTP')
    
    data_atual = date.today()
    data_em_texto ="{}-{}-{}".format(data_atual.day, data_atual.month,data_atual.year)
    r = '\r'
    r = r.encode('ascii')
    try:
        equipamento.connection = Telnet(equipamento.ip, equipamento.port)

        # Realizando Login
        index, match_obj, text = equipamento.connection.expect(["login: ".encode('latin-1')], timeout=2)

        if not match_obj:
            raise CommandError(f"Falha na conexão, OLT RESPONSE: {text}")

        equipamento.connection.write(f"{equipamento.user}\r".encode('latin-1'))

        index, match_obj, text = equipamento.connection.expect(["Password:".encode('latin-1')], timeout=2)

        if not match_obj:
            raise CommandError(f"Falha no usuário, OLT RESPONSE: {text}")

        equipamento.connection.write(f"{equipamento.password}\r".encode('latin-1'))
        index, match_obj, text = equipamento.connection.expect(["#".encode('latin-1')], timeout=2)

        if not match_obj:
            raise CommandError("Falha ao informar a senha")

        nomeDoArquivo = f"{equipamento.hostname}-{data_em_texto}-config.txt"
        tftp = f"show running-config | save overwrite {nomeDoArquivo}"
        tftp = tftp.encode('ascii')
        equipamento.connection.write(tftp + r)
        time.sleep(50)
        index, match_obj, text = equipamento.connection.expect(["#".encode('latin-1')], timeout=2)



        if not match_obj:
            raise CommandError("Falha ao executar comando de conectar no tftp ")

        comando = f"copy file {nomeDoArquivo} tftp://{IP_SERVER_TFTP}/{equipamento.hostname}"
        comando = comando.encode('ascii')
        equipamento.connection.write(comando + r)

        time.sleep(5)
        index, match_obj, text = equipamento.connection.expect(["#".encode('latin-1')], timeout=2)

        if not match_obj:
            raise CommandError("Falha ao enviar arquivo ao servidor FTP")

        comando = f"file delete {nomeDoArquivo}"
        comando = comando.encode('ascii')
        equipamento.connection.write(comando + r)

        index, match_obj, text = equipamento.connection.expect(["#".encode('latin-1')], timeout=2)
        
        print('BackupFinalizado')
        equipamento.connection.close()

    except:
        equipamento.connection.close()
        raise ConnectionError()

class Equipamento:
    def __init__(self,hostname, ip,port, user, password):
        self.connection = None
        self.hostname = hostname
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password

for switch in equipamentos:
    try:
        PORT_TELNET = os.environ.get('PORT_TELNET')
        USER = os.environ.get('USER')
        PASS = os.environ.get('PASS')


        print(f"Iniciando Backup no Switch {switch['hostname']}")
        equipamento = Equipamento(switch['hostname'],switch['ip'],PORT_TELNET,USER,PASS)
        backupSwitchDatacom(equipamento)
    except Exception as error:
        print(error)
        pass