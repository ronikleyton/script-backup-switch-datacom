
class Error(Exception):
    """Classe base para as exceções do módulo requisition_pool_olt"""
    pass


class ManufacturerError(Error):
    """Exceção lançada quando fabricante não está no enum dos fabricantes disponíveis.

    Attributes:
        manufacturer -- O fabricante informado
    """

    def __init__(self, manufacturer):
        self.message = "As funcionalidades para OLT do fabricante {} não está disponível".format(manufacturer)

    def __str__(self):
        return self.message


class TimeOutError(Error):
    """Exceção lançada quando excede o tempo de espera pela resposta da olt."""

    def __init__(self):
        self.message = "Olt excedeu o tempo máximo de resposta"

    def __str__(self):
        return self.message


class ConnectionError(Error):
    """Exceção lançada quando o script não consegue se conectar com a olt."""

    def __init__(self):
        self.message = "Não foi possível estabelecer conexão com a olt"

    def __str__(self):
        return self.message


class CommandError(Error):
    """Exceção lançada quando um error é gerado durante a execução de um dos scripts da OLT."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class FunctionNotFoundError(Error):
    """Exceção lançada quando não existe funcionalidade disponível para a OLT desse fabricante

    Attributes:
        manufacturer -- O fabricante informado
    """

    def __init__(self, manufacturer):
        self.message = "Funcionalidade não disponível para OLT do fabricante {}".format(manufacturer)

    def __str__(self):
        return self.message
