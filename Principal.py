import json, Conexao
import gerenciarImovel, gerenciarLocal, gerenciarOperacao

#abrir e carregar arquivo json
arquivo = open('imobiliaria.json', encoding="UTF-8").read()
imoveis = json.loads(arquivo)

#conectar com base MySQL
dataBase = Conexao.conectar()

#para cada imovel do json ----------------------------------------------------------------------------
for item in imoveis:

	#começando a preparar registro da tabela fato com um dicionario
	fato={}

	#cadastrar ou trazer informações do imovel para tabela fato
	fato.update({'idImovel':gerenciarImovel.cadastrarImovel(item, dataBase)})

	#cadastrar operacao ou trazer uma ja existente para a tabela fato
	fato.update({"idOperacao":gerenciarOperacao.cadastrarOperacao(item, dataBase)})

	#cadastrar ou trazer cep para tabela fato
	fato.update({'cep':gerenciarLocal.cadastrarLocal(item, dataBase)})

	print('\nValores para tabela fato: ')
	print(fato)

Conexao.desconectar(dataBase)

