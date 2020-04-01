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

def cadastrarFaixaPrecoAluguel(imovel, dataBase):

    # buscar e registrar valores para aluguel
    if "valor_aluguel" in imovel:

        valor = float(imovel['valor_aluguel'].replace(',', '.'))
        # if baixo valor de aluguel, maior que 0 e menor de 500 (ID - 1) -----------------------------------
        if (valor > 0 and valor < 500):
            result = Conexao.executarQuery('select 1 from faixaPreco where idFaixaPreco=1', dataBase)

            if (result.__len__() == 0):
                Conexao.executarInsert('insert into faixaPreco values (1,"BAIXO ALUGUEL MENOR DE 500")',
                                       dataBase)
            return "1"

        # aluguel de valor medio 500 - 1000 (ID - 2) -------------------------------------
        elif(valor >= 500 and valor < 1000):
            result = Conexao.executarQuery('select 1 from faixaPreco where idFaixaPreco=2', dataBase)

            if (result.__len__() == 0):
                Conexao.executarInsert('insert into faixaPreco values (2,"MEDIO ALUGUEL ENTRE 500 E 1000")',
                                       dataBase)
            return "2"

        # aluguel de valor alto maior ou igual a 1000 (ID - 3) -------------------------------------
        elif (valor >= 1000):
            result = Conexao.executarQuery('select 1 from faixaPreco where idFaixaPreco=3', dataBase)

            if (result.__len__() == 0):
                Conexao.executarInsert('insert into faixaPreco values (3,"ALTO ALUGUEL ENTRE MAIOR QUE 1000")',
                                       dataBase)
            return "3"
        #se valor não entrar na classificação -------------------------------------------------------
        else:
            result = Conexao.executarQuery('select 1 from faixaPreco where idFaixaPreco=0', dataBase)
            if (result.__len__() == 0):
                Conexao.executarInsert('insert into faixaPreco values (0,"VALOR SEM CLASSIFICAÇÂO  OU NÃO INFORMADO")',
                                       dataBase)
            return "0"

    # se não existir o campo valor_aluguel, salva como sem classificação ------------------------------
    else:
        result = Conexao.executarQuery('select 1 from faixaPreco where idFaixaPreco=0', dataBase)
        if (result.__len__() == 0):
            Conexao.executarInsert('insert into faixaPreco values (0,"VALOR SEM CLASSIFICAÇÂO OU NÃO INFORMADO")',
                                   dataBase)
        return "0"

def cadastrarFaixaPrecoVenda(imovel, dataBase):

    # buscar e registrar valores para venda
    if "valor_venda" in imovel:

        valor = float(imovel['valor_venda'].replace(',','.'))
        # if baixo valor de venda, maior que 0 e menor de 100 mil (ID - 4) -----------------------------------
        if (valor > 0 and valor < 100000.00):
            result = Conexao.executarQuery('select 1 from faixaPreco where idFaixaPreco=4', dataBase)

            if (result.__len__() == 0):
                Conexao.executarInsert('insert into faixaPreco values (4,"BAIXO VALOR VENDA MENOR DE 100.000 MIL")',
                                       dataBase)
            return "4"

        # venda de valor medio 100 mil - 1 milhão (ID - 5) -------------------------------------
        elif (valor >= 100000.00 and valor < 1000000.00):
            result = Conexao.executarQuery('select 1 from faixaPreco where idFaixaPreco=5', dataBase)

            if (result.__len__() == 0):
                Conexao.executarInsert('insert into faixaPreco values (5,"MEDIO VALOR VENDA ENTRE 100.000 MIL E 1,000.000 MILHÂO")',
                                       dataBase)
            return "5"

        # venda de valor alto  - maior ou igual a 1 milhão (ID - 6) -------------------------------------
        elif (valor >= 10000000.00):
            result = Conexao.executarQuery('select 1 from faixaPreco where idFaixaPreco=6', dataBase)

            if (result.__len__() == 0):
                Conexao.executarInsert('insert into faixaPreco values (6,"ALTO VALOR VENDA MAIOR QUE 1,000.000 MILHÂO")',
                                       dataBase)
            return "6"
        # se valor não entrar na classificação -------------------------------------------------------
        else:
            result = Conexao.executarQuery('select 1 from faixaPreco where idFaixaPreco=0', dataBase)
            if (result.__len__() == 0):
                Conexao.executarInsert('insert into faixaPreco values (0,"VALOR SEM CLASSIFICAÇÂO  OU NÃO INFORMADO")',
                                       dataBase)
            return "0"

    # se não existir o campo valor_venda, salva como sem classificação ------------------------------
    else:
        result = Conexao.executarQuery('select 1 from faixaPreco where idFaixaPreco=0', dataBase)
        if (result.__len__() == 0):
            Conexao.executarInsert('insert into faixaPreco values (0,"VALOR SEM CLASSIFICAÇÂO OU NÃO INFORMADO")',
                                   dataBase)
        return "0"

def cadastrarOperacao(imovel, dataBase):

    #verificar se imovel foi gravado ---------------------------------------------
    result = Conexao.executarQuery('select 1 from imovel where idImovel=' + imovel['id'], dataBase)
    if (result.__len__() > 0):

        #ALUGUEL --------------------------------------------------------------------------
        if('ALUGUEL' in imovel['status'].upper()):

            result = Conexao.executarQuery('select 1 from tipoOperacao where idImovel = ' + imovel['id'] +' and idTipoOperacao=1', dataBase)

            #se não existir faixa de preço de aluguel para este imovel ----------------------------
            if (result.__len__() == 0):
                # cadastrar a faixa de preço de ALUGUEL -------------------------------------------------
                aluguel = cadastrarFaixaPrecoAluguel(imovel, dataBase)

                #salvar operacao aluguel com a faixa de preço retornada -------------------------------------
                Conexao.executarInsert('insert into tipoOperacao values (1, '+ imovel['id'] + ',' + aluguel + ', "ALUGUEL")', dataBase)

        #VENDA ---------------------------------------------------------------------------------
        if('VENDA' in imovel['status'].upper()):
            result = Conexao.executarQuery(
            'select 1 from tipoOperacao where idImovel = ' + imovel['id'] + ' and idTipoOperacao=2', dataBase)

            # se não existir faixa de preço de venda para este imovel ----------------------------
            if (result.__len__() == 0):
                # cadastrar a faixa de preço de venda -------------------------------------------------
                venda = cadastrarFaixaPrecoVenda(imovel, dataBase)

                # salvar operacao venda com a faixa de preço retornada -------------------------------------
                Conexao.executarInsert(
                    'insert into tipoOperacao values (2, ' + imovel['id'] + ',' + venda + ', "VENDA")', dataBase)

        # CASO NÃO RECONHEÇA OU NÃO TENHA INFORMAÇÃO
        if not 'VENDA' in imovel['status'].upper() and not 'ALUGUEL' in imovel['status'].upper():
            result = Conexao.executarQuery('select 1 from tipoOperacao where idTipoOperacao=0', dataBase)
            # cadastrar tipo de operacao 0 - NAO INFORMADO
            if (result.__len__() == 0):
                Conexao.executarInsert('insert into tipoOperacao values (0, ' + imovel['id'] + ', 0, "NAO INFORMADO")', dataBase)
            return "0"

def cadastrarImovel(imovel, dataBase):

    # verificar se já exite imovel com este ID ----------------------------------------------------------
    result = Conexao.executarQuery('select 1 from imovel where idImovel = ' + imovel['id'], dataBase)
    if (result.__len__() == 0):
        # caso não exista cadastrar as informações
        #começar a montar query
        query = ('insert into imovel values (') + imovel['id'] + ','

        #classificar o numero de quartos --------------------------------------
        query += numeroQuartos(imovel, dataBase)

        #classificar a area util ------------------------------
        query += areaUtil(imovel, dataBase)

        # classificar o imovel em categorias - casa, apartamento e etc -------------------------
        query += Categoria(imovel, dataBase)

        #numero de vagas de garagem e banheiros ------------------------------------
        query += imovel['vagas'] + ',' + imovel['banheiros'] + ')'

        #cadastrar novo imovel ----------------------------------------------------
        Conexao.executarInsert(query, dataBase)

        print('\ncomando pra salvar na tabela imovel, ID - '+ imovel['id'] + ' ' + query)

    # cadastrar operacao(oes) para este imovel
    cadastrarOperacao(imovel, dataBase)

    return int(imovel['id'])