# importa 
# from create import Create
from modules.cliente.usecase.create import Create
from modules.cliente.entity.Cliente import Cliente

usecase = Create()

class ClienteUseCase:

    def __init__(self):
        self.clienteList: list[Cliente] = []
    
    def setCliente(self, cliente):
        usecase.createCliente(cliente)
    
    def getCliente(self):
        return self.clienteList

    def addCliente(self, cliente):
        return self.clienteList.append(cliente)