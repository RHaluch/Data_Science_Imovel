import Conexao

def cadastrarOperacao(imovel, dataBase):

    #verificar tipo de operacao do imovel ---------------------------------------------

    #ALUGUEL E VENDA --------------------------------------------------------------------------
    if('ALUGUEL' in imovel['status'].upper() and 'VENDA' in imovel['status'].upper()):
        result = Conexao.executarQuery('select 1 from tipoOperacao where idTipoOperacao=1',dataBase)
        #cadastrar tipo de operacao 1 - ALUGUEL E VENDA
        if(result.__len__()==0):
            Conexao.executarInsert('insert into tipoOperacao values (1, "ALUGUEL E VENDA")',dataBase)
        return "1"

    #SOMENTE ALUGUEL
    elif ('ALUGUEL' in imovel['status'].upper()):
        result = Conexao.executarQuery('select 1 from tipoOperacao where idTipoOperacao=2', dataBase)
        # cadastrar tipo de operacao 2 - ALUGUEL
        if (result.__len__() == 0):
            Conexao.executarInsert('insert into tipoOperacao values (2, "ALUGUEL")', dataBase)
        return "2"

    #SOMENTE VENDA
    elif('VENDA' in imovel['status'].upper()):
        result = Conexao.executarQuery('select 1 from tipoOperacao where idTipoOperacao=3', dataBase)
        # cadastrar tipo de operacao 3 - VENDA
        if (result.__len__() == 0):
            Conexao.executarInsert('insert into tipoOperacao values (3, "VENDA")', dataBase)
        return "3"

    # CASO NÃO RECONHEÇA OU NÃO TENHA INFORMAÇÃO
    else:
        result = Conexao.executarQuery('select 1 from tipoOperacao where idTipoOperacao=0', dataBase)
        # cadastrar tipo de operacao 0 - NAO INFORMADO
        if (result.__len__() == 0):
            Conexao.executarInsert('insert into tipoOperacao values (0, "NAO INFORMADO")', dataBase)
        return "0"
