from modules.cliente import usecase
from modules.cliente import entity

def main():
    print("Menu locadora")
    
    clienteUsecase = usecase.ClienteUseCase()   
    
    nome ='igor'
    cpf = '234'
    tel = '99'
    
    cliente = entity.Cliente(nome, cpf,tel)
    print(cliente.getCliente())
    
    print(clienteUsecase.getCliente()) 
    print(clienteUsecase.setCliente('Felipe')) 
    clienteUsecase.addCliente('Rayane')
    
    print(clienteUsecase.getCliente())
main()