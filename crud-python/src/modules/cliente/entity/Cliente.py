# APENAS ACESSA AS PROPRIEDADES DO CLIENTE
class Cliente:
	
	def __init__(self, nome, cpf, tel):
		self.cliente = {
			'nome': nome,
			'cpf': cpf,
			'tel': tel
		}
  
	def getCliente(self):
		return self.cliente

	# pode editar as propriedades