<img src="https://logovectorseek.com/wp-content/uploads/2021/11/datacom-group-ltd-logo-vector.png" width="400" height="200">

# Script-backup-switch-datacom
> Testado sobre equipamentos Datacom DMOS 6 e 7.

Este script tem como objetivo fazer backup das configurações e enviar para um servidor ftp de forma automatica. De maneira bem simples.

## Ciclo-Script

* Ele acessa o switch via telnet.
* Salva a configuração atual do equipamento.
* Envia o arquivo para o servidor tftp.

## Pré-Requisitos

* Instalar as dependencias do python para executar o script.
* Servidor TFTP.

## Iniciando

* Baixar o projeto para sua maquina.
* Preencher o arquivo .env com as informações do servidores, login e senhas.
* Adicionar as informações dos equipamentos no arquivo equipamentos.json, seguindo o exemplo.

```shell
{
"equipamentos" : 
  [ 
  {"hostname":"EXAMPLE1","ip":"172.32.1.10"}, 
  {"hostname":"EXAMPLE2","ip":"172.32.1.11"}
  ]
  }
```
* Obs: Nome do hostname tem que ser igual ao que está sendo usando no equipamento.


## Executando o script

* Após realizar todos os passos anteriores é só executar o arquivo main.py que automaticamente ele inicia o processo de backup de todos equipamentos cadastrado no arquivo equipamentos.json.


## Recursos

*  Caso o projeto consiga 50 stars eu inicio o desenvolvimento de um painel web com banco de dados para fazer o gerenciamento dos equipamentos.

## Licença

"The code in this project is licensed under MIT license."
