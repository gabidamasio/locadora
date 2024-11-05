
import json 
import os
class Cliente:
    def __init__(self):
        self.nome = ''
        self.cpf = ''
        self.data_nascimento = ''
        self.email = ''
        self.telefone = ''
        self.endereco =''
        self.opcao = ''
        self.arquivo_json_cliente = self.inicializarJson()
    
    def inicializarJson(self): 
        caminho_json = 'C:\\Users\\mdmar\\OneDrive\\Área de Trabalho\\Projetos Faculdade\\locadora\\crud-python\\src\\modules\\dataBase\\cliente.json'

        
        if not os.path.exists(caminho_json):
            with open(caminho_json, 'w') as arquivo:
               json.dump({}, arquivo)

        return caminho_json
        
    def showMenuCliente(self):
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║                  MÓDULO CLIENTE                    ║")
        print("╠════════════════════════════════════════════════════╣")
        print("║  1. Cadastrar Cliente       📝                     ║")
        print("║  2. Listar Clientes         📋                     ║")
        print("║  3. Buscar Cliente          🔍                     ║")
        print("║  4. Deletar Cliente         ❌                     ║")
        print("║  5. Atualizar Cliente       ✏️                     ║")  
        print("║  0. Voltar                                         ║")
        print("╚════════════════════════════════════════════════════╝")

    
    def mainCliente(self):
        self.showMenuCliente()
        self.opcao = int(input("Escolha uma das opções que deseja: "))
        
        while True:
            match self.opcao:
                case 0:
                    print('ok')
                case 1:
                    self.criarDadosCliente()
                case 2:
                    self.listarClientes()
                
                case 3:
                    self.buscarCliente()
                
                case 4: 
                    self.deletarCliente()
                
                case 5:
                    self.atualizarCliente()

                case _:
                    print('\n')
                    print("╔════════════════════════════════════════════════════╗")
                    print("║                   ESCOLHA INVÁLIDA!                ║")
                    print("║         Por favor, selecione uma opção válida.     ║")
                    print("╚════════════════════════════════════════════════════╝")
                    self.opcao = int(input("Digite uma opção válida: "))
            

    def criarDadosCliente(self):
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║                   CADASTRO CLIENTE  📝             ║")
        print("╚════════════════════════════════════════════════════╝")
        print("")
        print("════════════ Informe os dados pessoais do cliente ════")
        self.cpf = input("CPF: ")
        self.validarCPF(self.cpf)
        self.nome = input("Nome completo: ")
        self.data_nascimento = input("Data de nascimento(dd/mm/yy): ")
        self.email = input("E-mail: ")
        self.telefone = input("Telefone: ")
        self.endereco = input("Endereço: ")
       
        self.create()
           
    def create(self):
        dados = self.lerJson(self.arquivo_json_cliente)
        
        cliente = {}
        cliente[self.cpf] = {
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'data_nascimento': self.data_nascimento,
            'endereco': self.endereco
        }
        dados.update(cliente)
        self.escreverJson(self.arquivo_json_cliente, dados)
        
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║        CADASTRO REALIZADO COM SUCESSO  ✅          ║")
        print("╚════════════════════════════════════════════════════╝")
        print("Deseja realizar mais alguma operação em Cliente?")
        self.mainCliente()
    
    def listarClientes(self):
        print("╔════════════════════════════════════════════════════╗")
        print("║              LISTAGEM DE CLIENTES  📋              ║")
        print("╚════════════════════════════════════════════════════╝")
                       
        dados = self.lerJson(self.arquivo_json_cliente)
        for chave in dados:
            cliente = dados[chave]
            
            print("")
            print("╔════════════════════════════════════════════════════╗")
            print("║ Nome:", cliente['nome'])
            print("║ CPF:", cliente['cpf']),
            print("║ Data de nascimento: ", cliente['data_nascimento']),
            print("║ E-mail : ", cliente['email']),
            print("║ Telefone:", cliente['telefone']),
            print("║ Endereço:", cliente['endereco']),
            print("╚════════════════════════════════════════════════════╝")
        
        print("Deseja realizar mais alguma operação em Cliente?")
        self.mainCliente()
    
    def buscarCliente(self):
        print("╔════════════════════════════════════════════════════╗")
        print("║                BUSCAR CLIENTE  🔍                  ║")
        print("╚════════════════════════════════════════════════════╝")
        cpf = input("Informe o CPF do cliente que deseja buscar: ")

        dados = self.lerJson(self.arquivo_json_cliente)

        if cpf in dados:
            cliente = dados[cpf]
            print("╔════════════════════════════════════════════════════╗")
            print("║ Nome:", cliente['nome'])
            print("║ CPF:", cliente['cpf'])
            print("║ Data de nascimento:", cliente['data_nascimento'])
            print("║ E-mail:", cliente['email'])
            print("║ Telefone:", cliente['telefone'])
            print("║ Endereço:", cliente['endereco'])
            print("╚════════════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════════════════════╗")
            print("║              CPF NÃO ENCONTRADO!                   ║")
            print("╚════════════════════════════════════════════════════╝")

        print("Deseja realizar mais alguma operação em Cliente?")
        self.mainCliente()

    def deletarCliente(self):
        print("╔════════════════════════════════════════════════════╗")
        print("║                DELETAR CLIENTE  ❌                  ║")
        print("╚════════════════════════════════════════════════════╝")
        cpf = input("Informe o CPF do cliente a ser deletado: ")

        dados = self.lerJson(self.arquivo_json_cliente)

        if cpf in dados:
            del dados[cpf]
            self.escreverJson(self.arquivo_json_cliente, dados)
            print("╔════════════════════════════════════════════════════╗")
            print("║          CLIENTE DELETADO COM SUCESSO  ✅          ║")
            print("╚════════════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════════════════════╗")
            print("║              CPF NÃO ENCONTRADO!                   ║")
            print("╚════════════════════════════════════════════════════╝")

        print("Deseja realizar mais alguma operação em Cliente?")
        self.mainCliente()

    def atualizarCliente(self):
        print("╔════════════════════════════════════════════════════╗")
        print("║                ATUALIZAR CLIENTE  ✏️               ║")
        print("╚════════════════════════════════════════════════════╝")
    
        cpf = input("Informe o CPF do cliente que deseja atualizar: ")
    
        dados = self.lerJson(self.arquivo_json_cliente)
    
        if cpf in dados:
            cliente = dados[cpf]
        
            print("╔════════════════════════════════════════════════════╗")
            print("║                   DADOS ATUAIS DO CLIENTE          ║")
            print("╠════════════════════════════════════════════════════╣")
            print(f"║ Nome:             {cliente['nome']}")
            print(f"║ CPF:              {cliente['cpf']}")
            print(f"║ Data de Nascimento: {cliente['data_nascimento']}")
            print(f"║ E-mail:           {cliente['email']}")
            print(f"║ Telefone:         {cliente['telefone']}")
            print(f"║ Endereço:         {cliente['endereco']}")
            print("╚════════════════════════════════════════════════════╝")

            while True:
                print("\n╔════════════════════════════════════════════════════╗")
                print("║               O QUE VOCÊ DESEJA ATUALIZAR?         ║")
                print("╠════════════════════════════════════════════════════╣")
                print("║ 1. Nome                                           ║")
                print("║ 2. Data de Nascimento                             ║")
                print("║ 3. E-mail                                          ║")
                print("║ 4. Telefone                                        ║")
                print("║ 5. Endereço                                        ║")
                print("║ 0. Sair                                           ║")
                print("╚════════════════════════════════════════════════════╝")
            
                opcao_atualizar = int(input("Escolha a opção que deseja atualizar: "))
            
                match opcao_atualizar:
                    case 1:
                        nome = input(f"Nome atual: {cliente['nome']}. Novo Nome: ")
                        if nome:
                            cliente['nome'] = nome
                    case 2:
                        data_nascimento = input(f"Data de Nascimento atual: {cliente['data_nascimento']}. Nova Data: ")
                        if data_nascimento:
                            cliente['data_nascimento'] = data_nascimento
                    case 3:
                        email = input(f"E-mail atual: {cliente['email']}. Novo E-mail: ")
                        if email:
                            cliente['email'] = email
                    case 4:
                        telefone = input(f"Telefone atual: {cliente['telefone']}. Novo Telefone: ")
                        if telefone:
                            cliente['telefone'] = telefone
                    case 5:
                        endereco = input(f"Endereço atual: {cliente['endereco']}. Novo Endereço: ")
                        if endereco:
                            cliente['endereco'] = endereco
                    case 0:
                        break
                    case _:
                        print("Opção inválida, por favor escolha uma opção válida.")

                atualizar_cliente = input("Deseja atualizar outro dado? (s/n): ")
                if atualizar_cliente.lower() != 's':
                    break

            dados[cpf] = cliente
            self.escreverJson(self.arquivo_json_cliente, dados)
        
            print("╔════════════════════════════════════════════════════╗")
            print("║          CLIENTE ATUALIZADO COM SUCESSO  ✅        ║")
            print("╚════════════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════════════════════╗")
            print("║              CPF NÃO ENCONTRADO!                   ║")
            print("╚════════════════════════════════════════════════════╝")
    
        print("Deseja realizar mais alguma operação em Cliente?")
        self.mainCliente()

    def validarCPF(self, cpf):
        dados = self.lerJson(self.arquivo_json_cliente)
        
        if cpf in dados:
            print('')
            print('Esse cpf já pertence a um cliente no sistema!')
            print('Informe um novo cpf')
            self.criarDadosCliente()


    def lerJson(self, arquivo):
        with open(arquivo, 'r', encoding = "utf-8") as j:
            return json.load(j)
    
    def escreverJson(self, arquivo, dados):
        with open(arquivo, 'w', encoding = "utf-8") as j:
            json.dump(dados, j, indent=4, ensure_ascii = False)
