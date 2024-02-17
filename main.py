from tkinter import *
from tkinter import messagebox
from functools import partial


def click(botao):
    global jogada
    global cont
    botao['text']=jogada    
    botao['state']='disabled'
    check()
    troca_jogada()
    cont += 1
    if cont >= 9:
        messagebox.showinfo(title='Empate!', message='Não há mais jogadas disponíveis.\nDeu Velha')
        continuar()




def troca_jogada():
    global jogada
    if jogada == 'X':
        jogada = 'O'
    else:
        jogada = 'X'



'''
1 2 3
4 5 6
7 8 9
'''
def check():
    global jogada
    if bt1['text'] == bt2['text'] == bt3['text'] == 'X':
        vitoria_x()
        continuar()
    elif bt4['text'] == bt5['text'] == bt6['text'] == 'X':
        vitoria_x()
        continuar()

    elif bt7['text'] == bt8['text'] == bt9['text'] == 'X':
        vitoria_x()
        continuar()

    elif bt1['text'] == bt4['text'] == bt7['text'] == 'X':
        vitoria_x()
        continuar()

    elif bt2['text'] == bt5['text'] == bt8['text'] == 'X':
        vitoria_x()
        continuar()

    elif bt3['text'] == bt6['text'] == bt9['text'] == 'X':
        vitoria_x()
        continuar()

    elif bt1['text'] == bt5['text'] == bt9['text'] == 'X':
        vitoria_x()
        continuar()

    elif bt3['text'] == bt5['text'] == bt7['text'] == 'X':
        vitoria_x()
        continuar()

    #------//------

    elif bt1['text'] == bt2['text'] == bt3['text'] == 'O':
        vitoria_o()
        continuar()

    elif bt4['text'] == bt5['text'] == bt6['text'] == 'O':
        vitoria_o()
        continuar()

    elif bt7['text'] == bt8['text'] == bt9['text'] == 'O':
        vitoria_o()
        continuar()

    elif bt1['text'] == bt4['text'] == bt7['text'] == 'O':
        vitoria_o()
        continuar()

    elif bt2['text'] == bt5['text'] == bt8['text'] == 'O':
        vitoria_o()
        continuar()

    elif bt3['text'] == bt6['text'] == bt9['text'] == 'O':
        vitoria_o()
        continuar()

    elif bt1['text'] == bt5['text'] == bt9['text'] == 'O':
        vitoria_o()
        continuar()

    elif bt3['text'] == bt5['text'] == bt7['text'] == 'O':
        vitoria_o()
        continuar()


def vitoria_x():
    messagebox.showinfo(title='Vitória!!', message='Parabéns!!! X Venceu!!!')


def vitoria_o():
    messagebox.showinfo(title='Vitória!!', message='Parabéns!!! O Venceu!!!')

def continuar():
    if messagebox.askyesno(title='Continue?', message='Vamos jogar outra partida?'):
      messagebox.showinfo(title='Preparando...', message='Estão prontos para outra partida?')
      recomecar()
    else:
      messagebox.showinfo(title='Até mais!', message='Foi uma honra jogar com vocês')
      janela.quit()


def recomecar():
    global cont
    cont=0
    bt1['text'] = ' '
    bt1['state'] = 'active'

    bt2['text'] = ' '
    bt2['state'] = 'active'

    bt3['text'] = ' '
    bt3['state'] = 'active'

    bt4['text'] = ' '
    bt4['state'] = 'active'

    bt5['text'] = ' '
    bt5['state'] = 'active'

    bt6['text'] = ' '
    bt6['state'] = 'active'

    bt7['text'] = ' '
    bt7['state'] = 'active'

    bt8['text'] = ' '
    bt8['state'] = 'active'

    bt9['text'] = ' '
    bt9['state'] = 'active'



jogada = 'X'
cont = 0
font=('arial', 30, 'bold')
wd=3
hi=2

janela = Tk()
janela.title('Jogo da Velha')

bt1 = Button(janela, 
             font=font, 
             width=wd, 
             height=hi,
             )
bt1['command']= partial(click, bt1)
bt2 = Button(janela, 
             font=font, 
             width=wd, 
             height=hi,
             )
bt2['command']= partial(click, bt2)
bt3 = Button(janela, 
             font=font, 
             width=wd, 
             height=hi,
             )
bt3['command']= partial(click, bt3)
bt4 = Button(janela, 
             font=font, 
             width=wd, 
             height=hi,
             )
bt4['command']= partial(click, bt4)
bt5 = Button(janela, 
             font=font, 
             width=wd, 
             height=hi,
             )
bt5['command']= partial(click, bt5)
bt6 = Button(janela, 
             font=font, 
             width=wd, 
             height=hi,
             )
bt6['command']= partial(click, bt6)
bt7 = Button(janela, 
             font=font, 
             width=wd, 
             height=hi,
             )
bt7['command']= partial(click, bt7)
bt8 = Button(janela, 
             font=font, 
             width=wd, 
             height=hi,
             )
bt8['command']= partial(click, bt8)
bt9 = Button(janela, 
             font=font, 
             width=wd, 
             height=hi,
             )
bt9['command']= partial(click, bt9)

bt1.grid(row=1, column=1)
bt2.grid(row=1, column=2)
bt3.grid(row=1, column=3)
bt4.grid(row=2, column=1)
bt5.grid(row=2, column=2)
bt6.grid(row=2, column=3)
bt7.grid(row=3, column=1)
bt8.grid(row=3, column=2)
bt9.grid(row=3, column=3)

janela.mainloop()
