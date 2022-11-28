import csv
import pandas as pd
dados = 'dados.csv'
bd=[]
# with open(dados, 'r', encoding='utf-8') as dados:
#     dt=csv.reader(dados,delimiter=';')
#     for line in dt:
#         bd.append(line)
# df=pd.DataFrame(bd, columns=['Nome','Login','Senha'])
# cl=[]
# dl=[]
# n="dbhskfhsdkjhf"
# senha="123456"
#
#
# if df.loc[df['Login'] == n] is not list:
#     print(1)
# # if str(c.iat[0,2])==senha:
# #     print(1)

nome_usuario = "ney"
senha = "123456"
dados = 'dados.csv'
bd = []
with open(dados, 'r', encoding='utf-8', newline='') as dados :
    for linha in dados :
        linha = linha.split(';')
        bd.append(linha.split())
        print(bd)
    for nome_usuario in bd:
        print(bd[1])
        print(bd[2])
        if nome_usuario == nome and senha == password :
            print(1)



















