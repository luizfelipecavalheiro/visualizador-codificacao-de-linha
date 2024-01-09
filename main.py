import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk) 


#Funcao que verifica o tipo de padrão escolhido e chama funcao que gera os valores do gráfico de um respectivo padrão
def verifica_padrao(padrao, entrada):
    lista = []
    for i in range(len(entrada)):
      if(entrada[i] == '0'):
        lista.append(0)
      else:
        lista.append(1)
  
    if padrao == "NRZ-I":
      nrz_i(lista)
    elif padrao == "NRZ-L":
      nrz_l(lista)
    elif padrao == "AMI":
      ami(lista)
    elif padrao == "Pseudoternário":
      pseudoternario(lista)
    elif padrao == "Manchester":  
      manchester(lista)
    elif padrao == "Manchester Diferencial":
      manchester_diferencial(lista)

#Funcao que gera os valores do gráfico padrão NRZ-I
def nrz_i(entrada):
    lista_nrz_i = []
  
    if entrada[0] == 0:
      lista_nrz_i.append(1)
    else:
      lista_nrz_i.append(-1)
  
    for i in range(len(entrada)):
      if entrada[i] == 0 or i == 0:
        lista_nrz_i.append(lista_nrz_i[-1])
      elif entrada[i] == 1:
        lista_nrz_i.append(lista_nrz_i[-1]*-1)
      
        
        
    plota_grafico(lista_nrz_i)
  

#Funcao que gera os valores do gráfico padrão NRZ-L
def nrz_l(entrada):
    lista_nrz_l = []

    if entrada[0] == 0:
      lista_nrz_l.append(-1)
    else:
      lista_nrz_l.append(1)
      
    for i in range(len(entrada)):
      if entrada[i] == 1:
        lista_nrz_l.append(1)
      else:
        lista_nrz_l.append(-1)
      
    plota_grafico(lista_nrz_l)

#Funcao que gera os valores do gráfico padrão AMI
def ami(entrada):
    lista_ami = []
    troca = False
    if(entrada[0] == 1):
      lista_ami.append(1)
    else:
      lista_ami.append(0)
  
    for i in range(len(entrada)):
      if entrada[i] == 1:
        if troca == False:
          lista_ami.append(1)
          troca = True
        else:
          lista_ami.append(-1)
          troca = False   
      else:
        lista_ami.append(0)
    plota_grafico(lista_ami)
      
#Funcao que gera os valores do gráfico padrão Pseudoternário
def pseudoternario(entrada):
    lista_pseudo = []
    troca = False
    
    if(entrada[0] == 0):
      lista_pseudo.append(1)
    else:  
      lista_pseudo.append(0)
      
    for i in range(len(entrada)):
      if entrada[i] == 0:
        if troca == False:
          lista_pseudo.append(1)
          troca = True
        else:
          lista_pseudo.append(-1)
          troca = False   
      else:
        lista_pseudo.append(0)
    plota_grafico(lista_pseudo)

#Funcao que gera os valores do gráfico padrão Manchester
def manchester(entrada):
    lista_manchester = []
    
    if entrada[0] == 1:
      lista_manchester.append(-1)
    else:
      lista_manchester.append(1)
  
    for i in range(len(entrada)):
      if(entrada[i] == 1):
        lista_manchester.append(-1)
        lista_manchester.append(1)
      else:
        lista_manchester.append(1)
        lista_manchester.append(-1)
    plota_grafico(lista_manchester)

#Funcao que gera os valores do gráfico padrão Manchester Diferencial
def manchester_diferencial(entrada):
    lista_mandif = []

    if entrada[0] == 1:
      lista_mandif.append(1)
    else:
      lista_mandif.append(-1)
      
  
    for i in range(len(entrada)):
      if(entrada[i] == 1 or i == 0):
        lista_mandif.append(lista_mandif[-1])
        lista_mandif.append(lista_mandif[-1]*-1)
      else:
        lista_mandif.append(lista_mandif[-1]*-1)
        lista_mandif.append(lista_mandif[-1]*-1)
    plota_grafico(lista_mandif)

#Funcao que adiciona o Gráfico na figura
def plota_grafico(entrada):
    grafico = fig.add_subplot()
    grafico.set_title("Padrão: " + texto_combobox.get() + "  Entrada: " + entry_entrada_bits.get())
    grafico.plot(entrada,color='red',drawstyle='steps-pre')
    
    grafico.axhline(y = 0, color = 'g', linestyle = 'dashed')
    grafico.grid()

    
#Funcao que exibe o frame do gráfico
def show_frame_grafico():
    canvas.draw() 
    canvas.get_tk_widget().pack() 

    toolbar.pack()
    toolbar.update()   
    canvas.get_tk_widget().pack()

    button_voltar.pack()    
    frame_grafico.pack()
    frame_principal.forget()
    

#Funcao que exibe o frame da tela principal (que contem as opções de entrada de bits e padrão)
def show_frame_principal():
    fig.clear()
    canvas.get_tk_widget().forget()
    toolbar.forget()
    frame_grafico.forget()
    frame_principal.pack()

  
#Funcao que verifica se há dados na entrada
def controle_dados():
  
    padrao = texto_combobox.get()
    if not padrao:
      showinfo(
          title='Ops...',
          message=f'Por favor, selecione um padrão!!'
      )

    entrada = entry_entrada_bits.get()
    if not entrada:
      showinfo(
          title='Ops...',
          message=f'Por favor, digite uma entrada em bits!!'
      )

    if entrada and padrao:
      verifica_padrao(padrao,entrada)
      show_frame_grafico()


#Funcao que verifica se os caracteres da entrada sao binários
def somente_binarios(char):
    if char == '0' or char == '1':
      return True
    else:
      return False
  

#Criacao da tela e suas definiçẽos
janela = tk.Tk()
janela.title("Códigos de Linha - Comunicacação de Dados")

janela.geometry('640x480')
janela.configure(background="#77DD77")

#Criacao de 2 frames
frame_principal = tk.Frame(janela)
frame_principal.configure(background="#77DD77")
frame_grafico = tk.Frame(janela)
frame_grafico.configure(background="#77DD77")

#Label combobox
label_padrao = tk.Label(frame_principal,text="Padrão de Comunicação")
label_padrao.configure(background="#77DD77")
label_padrao.pack()

#Combobox
texto_combobox = tk.StringVar()
combobox_padrao = ttk.Combobox(frame_principal,textvariable=texto_combobox)
combobox_padrao ['values'] = ["NRZ-I","NRZ-L","AMI","Pseudoternário","Manchester","Manchester Diferencial"]
combobox_padrao.configure(state='readonly')
combobox_padrao.pack()

#Label Entry
label_entrada_bits = tk.Label(frame_principal,text="\nDigite o valor da entrada em Bits")
label_entrada_bits.configure(background="#77DD77")
label_entrada_bits.pack()

#Entry
validacao = frame_principal.register(somente_binarios)
entry_entrada_bits = tk.Entry(frame_principal, validate='key', validatecommand=(validacao,'%S'))
entry_entrada_bits.pack()

#Button Gerar Gráfico
button_gerar_grafico = tk.Button(frame_principal,
                                 text='Gerar Gráfico',
                                 background="#001A5F",
                                 foreground="#FFFFFF",
                                 command = controle_dados)

#Button Voltar
button_voltar = tk.Button(frame_grafico,
                          text="Voltar",
                          background="#001A5F",
                          foreground="#FFFFFF",
                          command=show_frame_principal)

#Figura do Gráfico
fig = Figure(figsize = (7, 5), dpi = 75) 

#Tela contendo a figura
canvas = FigureCanvasTkAgg(fig, master = janela)

#Barra de ferramentas do matplotlib que precisa ser carregada no Tkinter
toolbar = NavigationToolbar2Tk(canvas, janela)
toolbar.forget()

button_gerar_grafico.pack()
frame_principal.pack()

janela.mainloop()


