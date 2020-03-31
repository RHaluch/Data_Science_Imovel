import Conexao
from unicodedata import normalize

def cadastrarLocal(imovel, dataBase):

    #verificar se cidade já existe no bd -----------------------------------------------------------------------------
    cidade = str(imovel['cidade']).upper()
    estado = str(imovel['uf']).upper()
    result = Conexao.executarQuery("select idCidade from cidade where nome like '" + cidade + "' and estado like '" + estado + "'", dataBase)

    #se não existir cadastra-la com o proximo id unico
    if (result.__len__() == 0):

        cidadeID = Conexao.executarQuery('select max(idCidade) from cidade', dataBase)
        if None in cidadeID[0]:
            cidadeID = 1
        else:
            cidadeID = cidadeID[0][0] + 1

        # salvar nova cidade no banco
        Conexao.executarInsert('insert into cidade values (' + str(cidadeID) + ',"'+cidade+'","'+estado+'")', dataBase)
    else:
        cidadeID = result[0][0]

    #verificar se o bairro já existe --------------------------------------------------------------------------------
    bairro = str(imovel['bairro']).upper()
    result = Conexao.executarQuery("select idBairro from bairro where nome like '" + bairro + "' and idCidade = " + str(cidadeID), dataBase)

    # se não existir cadastra-lo com o proximo id unico
    if (result.__len__() == 0):
        bairroID = Conexao.executarQuery('select max(idBairro) from bairro', dataBase)

        if None in bairroID[0]:
            bairroID = 1
        else:
            bairroID = bairroID[0][0] + 1

        # salvar novo bairro no banco
        Conexao.executarInsert('insert into bairro values (' + str(bairroID) + ',' + str(cidadeID) + ',"' + bairro +'")', dataBase)
    else:
        bairroID = result[0][0]

    # verificar se o cep já existe ----------------------------------------------------------------------------------
    cep = imovel['cep'].replace('-', '')
    result = Conexao.executarQuery('select cep from localizacao where cep = ' + cep, dataBase)

    if (result.__len__() == 0):
        # se não existir cadastra-lo
        rua = normalize('NFKD', str(imovel['endereco'])).encode('ASCII','ignore').decode('ASCII').upper()
        Conexao.executarInsert('insert into localizacao values (' + str(cep) + ',' + str(bairroID) + ', "' + rua + '")', dataBase)
        return cep
    else:
        return int(result[0][0])