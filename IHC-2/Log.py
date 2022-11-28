import csv
from PyQt5 import  uic,QtWidgets
import time
import pandas as pd

def chama_segunda_tela():
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    dados = 'dados.csv'
    bd = []
    with open(dados, 'r', encoding='utf-8') as dados :
        dt = csv.reader(dados, delimiter=';')
        for line in dt:
            bd.append(line)
    df = pd.DataFrame(bd, columns=['Nome', 'Login', 'Senha'])
    d=(df["Login"]== nome_usuario)
    for i in d:
        if i==True:
            c=df.loc[df['Login'] == nome_usuario]
            print(c)
            print(str(c.iat[0, 2]))
            if str(c.iat[0, 2]) == senha:
                primeira_tela.close()
                segunda_tela.show()
            else:
                primeira_tela.label_4.setText("Dados de login incorretos!")
        else:
            primeira_tela.label_4.setText("Erro de Cadastro")

def limpar():
    primeira_tela.lineEdit.setText("")
    primeira_tela.lineEdit_2.setText("")
    primeira_tela.label_4.setText("")

def logout():
    primeira_tela.lineEdit.setText("")
    primeira_tela.lineEdit_2.setText("")
    primeira_tela.label_4.setText("")
    segunda_tela.close()
    primeira_tela.show()

def abre_tela_cadastro():
    tela_cadastro.show()

def chama_primeira_tela():
    tela_cadastro.close()
    primeira_tela.show()

def fechar_primeira_tela():
    primeira_tela.lineEdit.setText("")
    primeira_tela.lineEdit_2.setText("")
    primeira_tela.label_4.setText("")
    primeira_tela.close()

def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()
    primeira_tela.lineEdit.setText("")
    primeira_tela.lineEdit_2.setText("")

    if (senha == c_senha):
        try:
            dados = 'dados.csv'
            with open(dados, 'a', encoding='utf-8') as dados:
                dados.write(nome+";"+login+";"+senha+"\n")

            time.sleep(0.5)
            tela_cadastro.lineEdit.setText("")
            tela_cadastro.lineEdit_2.setText("")
            tela_cadastro.lineEdit_3.setText("")
            tela_cadastro.lineEdit_4.setText("")
            tela_cadastro.close()

        except (ValueError, TypeError) as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela_cadastro.label_6.setText("As senhas digitadas estão diferentes")



app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("tela1.ui")
segunda_tela = uic.loadUi("tela2.ui")
tela_cadastro = uic.loadUi("tela3.ui")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
tela_cadastro.pushButton_2.clicked.connect(chama_primeira_tela)
segunda_tela.pushButton.clicked.connect(logout)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
tela_cadastro.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
tela_cadastro.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
primeira_tela.pushButton_2.clicked.connect(abre_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar)
primeira_tela.pushButton_3.clicked.connect(fechar_primeira_tela)
primeira_tela.pushButton_4.clicked.connect(limpar)

primeira_tela.show()
app.exec()