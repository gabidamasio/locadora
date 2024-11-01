import json
import os

class Cliente:
    def _init_(self, props):
        nome = ''
        cpf = ''
        email = ''
        tel = ''
    
    def show_menu_cliente(self):
        print('\n')
        print("╔════════════════════════════════════════════════════╗")
        print("║                  MÓDULO CLIENTE                    ║")
        print("╠════════════════════════════════════════════════════╣")
        print("║  1. Cadastrar Cliente       📝                     ║")
        print("║  2. Listar Clientes         📋                     ║")
        print("║  3. Buscar Cliente          🔍                     ║")
        print("║  4. Deletar Cliente         ❌                     ║")
        print("║  0. Voltar                                         ║")
        print("╚════════════════════════════════════════════════════╝")
    
    def menu_cliente(self):
        self.show_menu_cliente()
        self.opcao_cliente = int(input("Escolha uma das opções que deseja: "))
        
        if self.opcao_cliente == 1:
    
            print("╔════════════════════════════════════════════════════╗")
            print("║                   CADASTRO CLIENTE                 ║")
            print("╚════════════════════════════════════════════════════╝")
            self.nome = input("Digite o nome do cliente: ")
            self.cpf = input("Digite o cpf do cliente: ")
            self.email = input("Digite o email do seu cliente: ")
            self.tel = input("Digite seu telefone: ")
            
            self.create()
            
    def create(self):
        clientes = {}
        clientes[self.cpf] = {
            'nome': self.nome,
            'email': self.email,
            'telefone': self.tel
        }
        
        print('Seu cliente: ', clientes)
        # SALVAR NO JSON.
            
        