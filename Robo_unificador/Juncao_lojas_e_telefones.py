import pandas as pd

def procv_posApp(adesao, posApp, tel):
    posApp_ade = pd.merge(adesao, posApp, on='CPF', how='left')
    posApp_total = pd.merge(posApp_ade, tel, on='CPF', how='left')
    posApp_total.to_csv(
        'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\arquivos_finais\\POS VENDA_ME_CONSISTENCIAS_37400_54420.csv',
        index=False, sep=';'
        )
    print('ADE adcionada ao POS VENDA_ME_CONSISTENCIAS_37400_54420')
    return


def procv_posME(adesao, posME, tel):
    posME_ade = pd.merge(adesao, posME, on='CPF', how='left')
    posME_total = pd.merge(posME_ade, tel, on='CPF', how='left')
    posME_total.to_csv(
        'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\arquivos_finais\\POS VENDA_ME_CONSISTENCIAS_39540_50178_53360_54354.csv',
        index=False, sep=';'
        )
    print('ADE adcionada ao POS VENDA_ME_CONSISTENCIAS_39540_50178_53360_54354')
    
    return


def procv_posFgts(adesao, posFgts):
    posFgts_ade = pd.merge(adesao, posFgts, on='CPF', how='left')
    posFgts_ade.to_csv(
        'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\arquivos_finais\\TRATATIVAS FGTS_BOT.csv',
        index=False, sep=';'
        )
    
    
    return


def procv_posFgts(adesao, posFgts):
    pos1 = pd.merge(adesao, posFgts, on='CPF', how='left')
    pos1.to_csv(
        'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\arquivos_finais\\TRATATIVAS FGTS_BOT.csv',
        index=False, sep=';')
    print('ADE adcionada ao TRATATIVAS FGTS_BOT')
    return


def procv_posWebsite(adesao, posWebsite):
    posWebsite = pd.merge(adesao, posWebsite, on='CPF', how='left')
    posWebsite.to_csv(
         'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\arquivos_finais\\TRATATIVAS WEBSITE_54862.csv', index=False, sep=';'
         )
    print('ADE adcionada ao TRATATIVAS WEBSITE_54862')
    
    return


# INITIALIZE
"""1.0 Procv entre cpf e ADE"""
# Procv Python
# df_juncao.drop_duplicates()

# Telefone
tel = pd.read_csv('telefone.csv', sep=';',
                  low_memory=False)

# Pos App
posApp = pd.read_csv('base_dividida\\POS VENDA_ME_CONSISTENCIAS_37400_54420_.csv', sep=';')
adesao_1 = pd.read_csv('C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\cpf_ade\\dock_posApp.csv', sep=';')
                      
procv_posApp(adesao_1, posApp, tel)
    
# Pos ME
posME = pd.read_csv('base_dividida\\POS VENDA_ME_CONSISTENCIAS_39540_50178_53360_54354_.csv', sep=';')
adesao_2 = pd.read_csv('C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\cpf_ade\\dock_posME.csv', sep=';')

procv_posME(adesao_2, posME, tel)


# Pos FGTS
posFgts = pd.read_csv('base_dividida\\TRATATIVAS FGTS_BOT_.csv', sep=';')
adesao_3 = pd.read_csv('C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\cpf_ade\\dock_posFgtsBot.csv', sep=';')

procv_posFgts(adesao_3, posFgts)

# Pos App
# posWebsite = pd.read_csv('base_dividida\\TRATATIVAS WEBSITE_54862_.csv', sep=';')
# adesao_4 = pd.read_csv('C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\cpf_ade\\dock_posWebSite.csv', sep=';')

# procv_posWebsite(adesao_4, posWebsite)