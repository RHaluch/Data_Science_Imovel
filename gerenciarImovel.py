import Conexao

def numeroQuartos(imovel, dataBase):

    #categorizar de acordo com o numero de suites e dormitorios

    # alto padrão - ID = 3 ------------------------------------------------------------------------------------------
    if (int(imovel['suites']) >= 2 and int(imovel['dormitorios']) >= 2):
        result = Conexao.executarQuery('select 1 from numeroQuartos where idNumeroQuartos=3', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar o ALTO padrão
            Conexao.executarInsert('insert into numeroQuartos values (3, "ALTO PADRAO - 2 SUITES + DORMITORIOS")',
                                   dataBase)
        return '3,'

    # medio padrão - ID = 2 ----------------------------------------------------------------------------------------
    elif (int(imovel['suites']) == 1 and (
            int(imovel['dormitorios']) > 1 and int(imovel['dormitorios']) <= 3)):
        result = Conexao.executarQuery('select 1 from numeroQuartos where idNumeroQuartos=2',dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar o MEDIO padrão
            Conexao.executarInsert('insert into numeroQuartos values (2, "MEDIO PADRAO - 1 SUITE + DORMITORIOS")',
                                   dataBase)

        return '2,'

    # baixo padrão - ID = 1 ----------------------------------------------------------------------------------------
    elif (int(imovel['suites']) == 1 or int(imovel['dormitorios']) == 1):
        result = Conexao.executarQuery('select 1 from numeroQuartos where idNumeroQuartos=1', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar o BAIXO padrão
            Conexao.executarInsert('insert into numeroQuartos values (1, "BAIXO PADRAO - 1 SUITE SOMENTE")',
                                   dataBase)
        return '1,'

    else: # caso não encaixe nas anteriores ou não tenha dados cadastrar sem classificação ------------------------
        result = Conexao.executarQuery('select 1 from numeroQuartos where idNumeroQuartos=0', dataBase)
        if (result.__len__() == 0):
             Conexao.executarInsert('insert into numeroQuartos values (0, "SEM CLASSIFICAÇÂO")',
                               dataBase)
        return '0,'

def areaUtil(imovel, dataBase):

    #substituir virgula por ponto para comparar com float
    area = imovel['area_privativa'].replace(',', '.')

    #classificação da area util do imovel --------------------------------------------------------------------

    # baixo padrão ------------------------
    if(float(area)<50 and float(area)>0):
        result = Conexao.executarQuery('select 1 from areaUtil where idAreaUtil=1', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar o baixo padrão
            Conexao.executarInsert('insert into areaUtil values (1, "BAIXO PADRAO - MENOR DE 50 METROS")',
                                   dataBase)
        return '1,'

    # medio padrão ------------------------------
    elif (float(area) >=50 and float(area)<=100):
        result = Conexao.executarQuery('select 1 from areaUtil where idAreaUtil=2', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar o medio padrão
            Conexao.executarInsert('insert into areaUtil values (2, "MEDIO PADRAO - ENTRE 50 E 100 METROS")',
                                   dataBase)
        return '2,'

    # alto padrão ---------------------------------
    elif (float(area) > 100):
        result = Conexao.executarQuery('select 1 from areaUtil where idAreaUtil=3', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar o alto padrão
            Conexao.executarInsert('insert into areaUtil values (3, "ALTO PADRAO - MAIOR DE 100 METROS")',
                                   dataBase)
        return '3,'

    # se por acaso area não entrar nas classificações ------------------------------------------
    else:
        result = Conexao.executarQuery('select 1 from areaUtil where idAreaUtil=0', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar sem informação
            Conexao.executarInsert('insert into areaUtil values (0, "SEM INFORMACAO")',
                                   dataBase)
        return '0,'

"""def faixaPreco(imovel, dataBase):  DUVIDA =========================================

    #substituir virgula por ponto para comparar com float
    preco = imovel['area_privativa'].replace(',', '.')

    if(float(area)<50 and float(area)>0):
        result = Conexao.executarQuery('select 1 from areaUtil where idAreaUtil=1', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar o baixo padrão
            Conexao.executarInsert('insert into areaUtil values (1, "BAIXO PADRAO - MENOR DE 50 METROS")',
                                   dataBase)
        return '1,'

    elif (float(area) >=50 and float(area)<=100):
        result = Conexao.executarQuery('select 1 from areaUtil where idAreaUtil=2', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar o medio padrão
            Conexao.executarInsert('insert into areaUtil values (2, "MEDIO PADRAO - ENTRE 50 E 100 METROS")',
                                   dataBase)
        return '2,'

    elif (float(area) > 100):
        result = Conexao.executarQuery('select 1 from areaUtil where idAreaUtil=3', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar o alto padrão
            Conexao.executarInsert('insert into areaUtil values (3, "ALTO PADRAO - MAIOR DE 100 METROS")',
                                   dataBase)
        return '3,'

    else:
        result = Conexao.executarQuery('select 1 from areaUtil where idAreaUtil=0', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar sem informação
            Conexao.executarInsert('insert into areaUtil values (0, "SEM INFORMACAO")',
                                   dataBase)
        return '0,'
"""

def Categoria(imovel, dataBase):

    # cadastrar categoria do imovel - apartamento, casa, sobrado etc -----------------------------------------------------

    #QUITINETE -------------------------------
    if ('KITNET' in imovel['categoria'].upper() or 'KITNETE' in imovel['dormitorios'].upper() or 'QUITINETE' in imovel['categoria'].upper() or 'KITINETE' in imovel['categoria'].upper()):
        result = Conexao.executarQuery('select 1 from categoriaImovel where idCategoriaImovel=1', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar a quitinete
            Conexao.executarInsert('insert into categoriaImovel values (1, "QUITINETE")', dataBase)
        return '1,'

    # APARTAMENTO -----------------------------
    elif ('APARTAMENTO' in imovel['categoria'].upper() or 'APT' in imovel['categoria'].upper() or 'APTO' in imovel['categoria'].upper()):
        result = Conexao.executarQuery('select 1 from categoriaImovel where idCategoriaImovel=2', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar a categoria apartamento
            Conexao.executarInsert('insert into categoriaImovel values (2, "APARTAMENTO")', dataBase)
        return '2,'

    # SOBRADO ---------------------------------------
    elif ('SOBRADO' in imovel['categoria'].upper()):
        result = Conexao.executarQuery('select 1 from categoriaImovel where idCategoriaImovel=3', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar a categoria sobrado
            Conexao.executarInsert('insert into categoriaImovel values (3, "SOBRADO")', dataBase)
        return '3,'

    # CASA -----------------------------------------------
    elif ('CASA' in imovel['categoria'].upper()):
        result = Conexao.executarQuery('select 1 from categoriaImovel where idCategoriaImovel=4', dataBase)
        if (result.__len__() == 0):
            # caso não exista cadastrar a categoria casa
            Conexao.executarInsert('insert into categoriaImovel values (4, "CASA")', dataBase)
        return '4,'
    else:
        #caso de não reconhecer categoria ---------------------
        Conexao.executarInsert('insert into categoriaImovel values (0, "SEM CLASSIFICACAO")', dataBase)
        return '0,'

def cadastrarImovel(imovel, dataBase):

    # verificar se já exite imovel com este ID ----------------------------------------------------------
    result = Conexao.executarQuery('select 1 from imovel where idImovel = ' + imovel['id'], dataBase)
    if (result.__len__() == 0):
        # caso não exista cadastrar as informações
        #começar a montar query
        query = ('insert into imovel values (') + imovel['id'] + ','

        #classificar o numero de quartos --------------------------------------
        query += numeroQuartos(imovel, dataBase)

        # classificar a faixa de preço - DUVIDA!!!!!!!!!!! ------------------------
        # query += faixaPreco(imovel, dataBase)
        query += '1,'

        #classificar a area util ------------------------------
        query += areaUtil(imovel, dataBase)

        # classificar o imovel em categorias - casa, apartamento e etc -------------------------
        query += Categoria(imovel, dataBase)

        #numero de vagas de garagem e banheiros ------------------------------------
        query += imovel['vagas'] + ',' + imovel['banheiros'] + ')'

        #cadastrar novo imovel ----------------------------------------------------
        Conexao.executarInsert(query, dataBase)
        print('\ncomando pra salvar na tabela imovel: ', query)

    return int(imovel['id'])