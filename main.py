# Importa os módulos
from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_de_frame_1()
        root.mainloop()
    
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background="#1e3743")  
        self.root.geometry("700x500") # Configura o tamanho da tela ao abrir
        self.root.resizable(True, True) # Permite ou não o usuario de diminuir ou aumentar o tamanho da tela
        self.root.maxsize(width=900, height=700) # Configura a responsividade MÁXIMA da tela
        self.root.minsize(width=500, height=400) # Configura a responsividade MÍNIMA da tela

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=3) # highlightthickness adiciona uma borda em volta
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=3) # highlightthickness adiciona uma borda em volta
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_de_frame_1(self):
        # Criação de botão limpar
        self.btn_limpar = Button(self.frame_1, text="Limpar")
        self.btn_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Criação de botão buscar
        self.btn_limpar = Button(self.frame_1, text="Buscar")
        self.btn_limpar.place(relx=0.305, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação de botão novo
        self.btn_limpar = Button(self.frame_1, text="Novo")
        self.btn_limpar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação de botão alterar
        self.btn_limpar = Button(self.frame_1, text="Alterar")
        self.btn_limpar.place(relx=0.705, rely=0.1, relwidth=0.1, relheight=0.15)
            
        # Criação de botão buscar
        self.btn_limpar = Button(self.frame_1, text="Apagar")
        self.btn_limpar.place(relx=0.810, rely=0.1, relwidth=0.1, relheight=0.15)
            
        # Criação da label e entrada do código
        self.lb_codigo = Label(self.frame_1, text="Código")
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        # Criação da label e entrada do nome do cliente
        self.lb_nome = Label(self.frame_1, text="Nome")
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

            
        # Criação da label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text="Telefone")
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

            
        # Criação da label e entrada da cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade")
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

            

Application()
        