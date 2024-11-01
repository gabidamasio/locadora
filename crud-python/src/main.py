from modules.Cliente import Cliente

cliente = Cliente()

def show_menu():
    print("╔════════════════════════════════════════════════════╗")
    print("║            BEM-VINDO AO SISTEMA DE GESTÃO          ║")
    print("║                     LOCADORA                       ║")
    print("╠════════════════════════════════════════════════════╣")
    print("║                                                    ║")
    print("║   Neste sistema, você pode gerenciar as seguintes  ║")
    print("║   opções:                                          ║")
    print("║                                                    ║")
    print("║   1. Cliente - Gerencie os clientes da locadora    ║")
    print("║   2. Carro - Gerencie a frota de carros            ║")
    print("║   3. Aluguel - Gerencie os contratos de aluguel    ║")
    print("║   0. Sair - Saia do sistema                        ║")
    print("║                                                    ║")
    print("╚════════════════════════════════════════════════════╝")

    
def main():
    
        while True:
            show_menu()
            opcao = int(input("Digite uma opção: "))
            
            if opcao == 0:
                print("╔════════════════════════════════════════════════════╗")
                print("║                 SAINDO DO SISTEMA...               ║")
                print("╚════════════════════════════════════════════════════╝")
                exit()
                break
            
            while opcao != 1 and opcao != 2 and opcao != 3:
                print('\n')
                print("╔════════════════════════════════════════════════════╗")
                print("║                   ESCOLHA INVÁLIDA!                ║")
                print("║         Por favor, selecione uma opção válida.     ║")
                print("╚════════════════════════════════════════════════════╝")
                opcao = int(input("Digite uma opção válida: "))
            
            if opcao == 1:
                cliente.menu_cliente()
            
            elif opcao == 2:
                print("╔════════════════════════════════════════════════════╗")
                print("║                   MÓDULO CARRO                     ║")
                print("╚════════════════════════════════════════════════════╝")
                
            elif opcao == 3:
                print("╔════════════════════════════════════════════════════╗")
                print("║                   MÓDULO ALUGUEL                   ║")
                print("╚════════════════════════════════════════════════════╝")
                
            
            
main()