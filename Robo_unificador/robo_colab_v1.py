# Import
import pandas as pd


def transform_data(data):
    data['Data'] = pd.to_datetime(data['Data'])
    data['Resp. Corban'] = data['Resp. Corban'].astype(object)
    data['CPF'] = data['CPF'].astype(int)
    data['Adesão'] = data['Adesão'].astype(int)
    data.dtypes

    return df1


def separation_loja(data2):
    df_pos_app = data2[(data2['Loja'] == '37400s') |
                       (data2['Loja'] == '37400') |
                       (data2['Loja'] == '54420') |
                       (data2['Loja'] == '37400A') |
                       (data2['Loja'] == '37400a') |
                       (data2['Loja'] == '37400e') |
                       (data2['Loja'] == '37400S') |
                       (data2['Loja'] == '37400E')]

    df_pos_ME = data2[(data2['Loja'] == '39540') |
                      (data2['Loja'] == '50178') |
                      (data2['Loja'] == '53360') |
                      (data2['Loja'] == '54345') |
                      (data2['Loja'] == '39540E') |
                      (data2['Loja'] == '39540s') |
                      (data2['Loja'] == '39540A') |
                      (data2['Loja'] == '39540S') |
                      (data2['Loja'] == '39540e') |
                      (data2['Loja'] == '39540a') |
                      (data2['Loja'] == '50178s')]

    df_pos_fgts_bot = data2[(data2['Loja'] == '54562') |
                            (data2['Loja'] == '54563') |
                            (data2['Loja'] == '54564') |
                            (data2['Loja'] == '54565') |
                            (data2['Loja'] == '54566') |
                            (data2['Loja'] == '54567') |
                            (data2['Loja'] == '54568') |
                            (data2['Loja'] == '54569') |
                            (data2['Loja'] == '54570')]

    df_pos_WEBSITE = data2[(data2['Loja'] == '54862')]


# Salvar nas pastas

    # dock_posApp.to_csv('tel2.csv', index=False, sep=';')

    # Pos App
    df_pos_app.to_csv(
        '/home/borges/Downloads/tratativas/Tratativas_Pos_App', index=False
        )

    # Pos ME
    df_pos_ME.to_csv(
        '/home/borges/Downloads/tratativas/Tratativas_PosME', index=False
        )

    # Pos Fgts Bot
    df_pos_fgts_bot.to_csv(
        '/home/borges/Downloads/tratativas/Tratativas_PosFgtsBot', index=False
        )

    # Pos WEBSITE
    df_pos_WEBSITE.to_csv(
        '/home/borges/Downloads/tratativas/Tratativas_PosWEBSITE', index=False
        )

    return


def separation_cpf_ade(data2):
    dock_posApp = data2[['CPF', 'Adesão']]
    dock_posME = data2[['CPF', 'Adesão']]
    dock_posFgtsBot = data2[['CPF', 'Adesão']]
    dock_posWebSite = data2[['CPF', 'Adesão']]

    # dock_posApp.to_csv('tel2.csv', index=False, sep=';')
    dock_posApp.to_csv(
        '/home/borges/Downloads/tratativas/dock_posApp.csv', index=False
        )

    dock_posME.to_csv(
        '/home/borges/Downloads/tratativas/dock_posME.csv', index=False
        )

    dock_posFgtsBot.to_csv(
        '/home/borges/Downloads/tratativas/dock_posFgtsBot.csv', index=False
        )

    dock_posWebSite.to_csv(
        '/home/borges/Downloads/tratativas/dock_posWebSite.csv', index=False
        )

    return


def procv_tel(posApp, poME, posFgts, posWebsite, tel):

    posApp_tel = pd.merge(posApp, tel, on='CPF', how='left')
    posApp_tel.to_csv(
         '/home/borges/Downloads/tratativas/TESTE_JUNCAO.csv', index=False
         )

    posME_tel = pd.merge(poME, tel, on='CPF', how='left')
    posME_tel.to_csv(
         '/home/borges/Downloads/tratativas/TESTE_JUNCAO.csv', index=False
         )

    posFgts_tel = pd.merge(posFgts, tel, on='CPF', index=False)
    posFgts_tel.to_csv(
         '/home/borges/Downloads/tratativas/TESTE_JUNCAO.csv', index=False
         )

    posWebsite = pd.merge(posWebsite, tel, on='CPF', how='left')
    posWebsite.to_csv(
         '/home/borges/Downloads/tratativas/TESTE_JUNCAO.csv', index=False
         )


# INITIALIZE
df1 = pd.read_csv('/home/borges/Downloads/base_unida.csv')

print(f'Number of Rows and Cols: {df1.shape}')


"""0.0 Tranformar os dados"""

transform_data(df1)


"""1.0 Separar as lojas"""

df2 = df1.copy()

separation_loja(df2)


"""1.1 Separar cpf e ADE"""

print(df2['Loja'].unique())

separation_cpf_ade(df2)

"""1.2 Procv entre cpf e tele"""
# Procv Python
# df_juncao.drop_duplicates()

dfj = pd.read_csv('base_unida.csv')
dfj = pd.read_csv('base_unida.csv')
dfj = pd.read_csv('base_unida.csv')
dfj = pd.read_csv('base_unida.csv')

# Telefones
dft = pd.read_csv('telefone.csv')
