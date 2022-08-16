# Import
import pandas as pd


def transform_data(data):
    #data['Data'] = pd.to_datetime(data['Data'])
    #data['Resp. Corban'] = data['Resp. Corban'].astype(object)
    data['CPF'] = data['CPF'].astype(int)
    data['ADE'] = data['ADE'].astype(int)

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
        'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\base_dividida\\POS VENDA_ME_CONSISTENCIAS_37400_54420_.csv',
        index=False, sep=';'
        )

    # Pos ME
    df_pos_ME.to_csv(
        'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\base_dividida\\POS VENDA_ME_CONSISTENCIAS_39540_50178_53360_54354_.csv',
        index=False, sep=';'
        )

    # Pos Fgts Bot
    df_pos_fgts_bot.to_csv(
        'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\base_dividida\\TRATATIVAS FGTS_BOT_.csv',
        index=False, sep=';'
        )

    # Pos WEBSITE
    df_pos_WEBSITE.to_csv(
        'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\base_dividida\\TRATATIVAS WEBSITE_54862_.csv',
        index=False, sep=';'
        )
    
    print('SEPARAR CPF E ADE')
    
    dock_posApp = df_pos_app[['CPF', 'ADE']]
    dock_posME = df_pos_ME[['CPF', 'ADE']]
    dock_posFgtsBot = df_pos_fgts_bot[['CPF', 'ADE']]
    dock_posWebSite = df_pos_WEBSITE[['CPF', 'ADE']]

    # dock_posApp.to_csv('tel2.csv', index=False, sep=';')
    dock_posApp.to_csv(
        'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\cpf_ade\\dock_posApp.csv',
        index=False, sep=';'
        )

    dock_posME.to_csv(
        'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\cpf_ade\\dock_posME.csv',
        index=False, sep=';'
        )

    dock_posFgtsBot.to_csv(
        'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\cpf_ade\\dock_posFgtsBot.csv',
        index=False, sep=';'
        )

    dock_posWebSite.to_csv(
        'C:\\Users\\andre.borges\Downloads\\Tratativas_Diarias\\cpf_ade\\dock_posWebSite.csv',
        index=False, sep=';'
        )

    return


# INITIALIZE
df1 = pd.read_csv('base_unida.csv', sep=";")

print(f'Number of Rows and Cols: {df1.shape}')


"""0.0 Tranformar os dados"""

# transform_data(df1)


"""1.0 Separar as lojas"""

df2 = df1.copy()

separation_loja(df2)


"""1.1 Separar cpf e ADE"""

print(df2['Loja'].unique())

# separation_cpf_ade(df2)