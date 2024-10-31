# importa o repository
from modules.cliente.repository.clienteRepository import ClienteRepository

repository = ClienteRepository()

class Create:
    def __init__(self):
        pass
    
    def createCliente(self, cliente):
        repository.salvar(cliente)
        print('cliente')