#importando bibliotecas e modulos
import random
from tkinter import *

#janela do tkinter
janela = Tk()
janela.title('QUIZ de geografia')

'''==========funcoes==========='''
#funcao jogo
def jogo():
    #cria o botao proxima fase desabilitado
    botao_next = Button(janela, width=25, text="Próxima fase!", background = "plum", command=proxima_fase,state=DISABLED)
    botao_next.place(x=100, y=400)
    
    fase = fases[0]
    perguntafase = perguntas[0]

    #label pergunta
    label_pergunta = Label (text=perguntafase, font="Arial 14") 
    label_pergunta.place(x=100,y=200)
    
    #da um valor aleatorio para a
    a = random.choice(fase)
    '''botao1'''
    if a in respostas:
        botao1 = Button(janela, width=25, text=a, command=certo, background = "lightblue")
        botao1.place(x=100, y=300)
    else:
        botao1 = Button(janela, width=25, text=a, command=errado, background = "lightblue")
        botao1.place(x=100, y=300)
    fase.remove(a)
    
    #da um valor aleatorio para b
    b = random.choice(fase)
    '''botao2'''
    if b in respostas:
        botao2 = Button(janela, width=25, text=b, command=certo , background = "lightblue")
        botao2.place(x=300, y=300)                    
    else:
        botao2 = Button(janela, width=25, text=b, command=errado , background = "lightblue")
        botao2.place(x=300, y=300)   
    fase.remove(b)
    
    #da um valor aleatorio para c
    c = random.choice(fase)
    '''botao3'''
    if c in respostas:
        botao3 = Button(janela, width=25, text=c, command=certo , background = "lightblue")
        botao3.place(x=500, y=300)                         
    else:
        botao3 = Button(janela, width=25, text=c, command=errado , background = "lightblue")
        botao3.place(x=500, y=300)
    fase.remove(c)

#chama a proxima fase
def proxima_fase():
    fases.pop(0)
    perguntas.pop(0)
    label_resposta["text"] = ''
    jogo()
    
#chamada quando o botao clicado está com a resposta certa   
def certo():
    label_resposta["text"] = 'Você acertou!!!'
    #habilita o botao proxima fase
    botao_next = Button(janela, width=25, text="Próxima fase!", command=proxima_fase , background = "plum")
    botao_next.place(x=100, y=400)

#chamada quando o botao clicado está com a resposta errada   
def errado():
    label_resposta["text"] = 'Você errou'

#destroi a tela de boas vindas
def destruir():
    label_comecar.destroy()
    botao_comecar.destroy()

#chama a funcao que destroi a tela de boas vindas e começa o jogo
def comecar():
    destruir()
    jogo()
    
'''===informando valores==='''
#fase armazena as 3 respostas de cada pergunta. a primeira resposta armazenada é sempre a verdadeira.
fase1 = ['Vermelha', 'Roxa', 'Preta']
fase2 = ['Gelado', 'Desértico','Vulcânico']
fase3 = ['Fóssil', 'Esqueleto', 'Escavação']


#fases inclui todas as fases
fases = [fase1, fase2, fase3]

#pergunta
pergunta1 = 'Qual é a cor da Terra Roxa?'
pergunta2 = 'Qual é a natureza do Monte Everest?'
pergunta3 = 'Qual é o nome do resto de um ser vivo preservado naturalmente?'

#perguntas
perguntas = [pergunta1, pergunta2, pergunta3]

#resposta
#é o primeiro elemento de cada fase
#respostas
respostas = (fase1[0], fase2[0], fase3[0])

'''===criando as labels==='''
#label resposta
label_resposta = Label() 
label_resposta.place(x=100,y=500)

'''===inicio codigo==='''
#TEXTO DE ABERTURA DO JOGO
texto_comecar = ('''
                * Bem vindo ao QUIZ de Geografia! *

                (O código ainda está em fase de desenvolvimento)
                
                Informações do jogo:

                Cada fase exibe uma pergunta sobre Geografia com 3
                alternativas, sendo uma correta e duas incorretas.
                A próxima fase só é liberada quando o usuário acerta a resposta.
                

                Informações técnicas:

                Esse código utiliza as bibliotecas tkinter e random.
                As respostas são distribuídas nos botões de modo randômico,
                para a criança não 'decorar a posição da resposta'.
                
                ''')

#FRASE COMECAR
label_comecar = Label (text=texto_comecar, font="Arial 12",justify='center') 
label_comecar.place(x=100,y=100)

#BOTAO COMECAR
botao_comecar = Button(janela, width=25, text='COMEÇAR',background = "lightblue", command=comecar)
botao_comecar.place(x=300, y=450)

'''==============fimcodigo========================='''
#comandos adicionais da janela
janela.geometry("800x600+0+0")
janela.mainloop()
