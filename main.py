# Importa os módulos
from tkinter import *
from tkinter import ttk
import sqlite3 as sql
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import  TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

root = Tk()

class Relatorios():
    def print_cliente(self):
        webbrowser.open("cliente.pdf")

    def gera_relatorio_cliente(self):
        self.c = canvas.Canvas("cliente.pdf")
        
        self.codigo_relatorio = self.codigo_entry.get()
        self.nome_relatorio = self.nome_entry.get()
        self.telefone_relatorio = self.telefone_entry.get()
        self.cidade_relatorio = self.cidade_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, "Ficha do Cliente")
        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, "Código: ")
        self.c.drawString(50, 670, "Nome: ")
        self.c.drawString(50, 640, "Telefone: ")
        self.c.drawString(50, 610, "Cidade: ")
        
        self.c.setFont("Helvetica", 18)
        self.c.drawString(150, 700, self.codigo_relatorio)
        self.c.drawString(150, 670, self.nome_relatorio)
        self.c.drawString(150, 640, self.telefone_relatorio)
        self.c.drawString(150, 610, self.cidade_relatorio)

        self.c.rect(20, 580, 550, 250, fill=False, stroke=True)

        self.c.showPage()
        self.c.save()
        self.print_cliente()


class Funcs():

    # Definindo a função de limpar os campos de input
    def limpar_cliente(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    # Função para conectar com o banco de dados
    def conecta_bd(self):
        self.conn = sql.connect("clientes.bd")
        self.cursor = self.conn.cursor();print("Conectando com o BANCO DE DADOS...")
    
    # Função para desconectar o banco de dados
    def desconecta_bd(self):
        self.conn.close() ; print("DESCONECTANDO do BANCO DE DADOS")

    # Função para criar o banco de dados
    def monta_tabela(self):
        self.conecta_bd()
        ### Criar tabela
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente(
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(40)
        )
        """)
        self.conn.commit(); print("BANCO DE DADOS criado.")
        self.desconecta_bd()

    # Função para salvar as variáveis que vão se repetir várias vezes
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()

    # Função para adicionar clientes
    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO cliente (nome_cliente, telefone, cidade) 
            VALUES (?, ?, ?) """, (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_cliente()

    # Função de select
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM cliente
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()

    # Função de double click
    def double_click(self, event):
        self.limpar_cliente()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, "values")
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    
    # Função de deletar cliente
    def delete_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM cliente WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpar_cliente()
        self.select_lista()

    # Função de alterar cliente
    def alterar_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""UPDATE cliente SET nome_cliente = ?, telefone = ?, cidade = ? WHERE cod = ?""", (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_cliente()

    # Função de buscar cliente
    def buscar_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())
        self.nome_entry.insert(END, "%")
        nome = self.nome_entry.get()
        self.cursor.execute("""
            SELECT cod, nome_cliente, telefone, cidade FROM cliente
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
        
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", END, values=i)
        self.limpar_cliente()
        self.desconecta_bd()


class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_de_frame_1()
        self.lista_frame_2()
        self.monta_tabela()
        self.select_lista()
        self.menus()
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
        self.btn_limpar = Button(self.frame_1, text="Limpar", border=2, bg="#7e81b8", fg="white", font=("Verdana", 8, "bold"), command=self.limpar_cliente)
        
        self.btn_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Criação de botão buscar
        self.btn_buscar = Button(self.frame_1, text="Buscar", border=2, bg="#7e81b8", fg="white", font=("Verdana", 8, "bold"), command=self.buscar_cliente)
        self.btn_buscar.place(relx=0.305, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação de botão novo
        self.btn_novo = Button(self.frame_1, text="Novo", border=2, bg="#7e81b8", fg="white", font=("Verdana", 8, "bold"), command=self.add_cliente)
        self.btn_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação de botão alterar
        self.btn_alterar = Button(self.frame_1, text="Alterar", border=2, bg="#7e81b8", fg="white", font=("Verdana", 8, "bold"), command=self.alterar_cliente)
        self.btn_alterar.place(relx=0.705, rely=0.1, relwidth=0.1, relheight=0.15)
            
        # Criação de botão Apagar
        self.btn_apagar = Button(self.frame_1, text="Apagar", border=2, bg="#7e81b8", fg="white", font=("Verdana", 8, "bold"), command=self.delete_cliente)
        self.btn_apagar.place(relx=0.810, rely=0.1, relwidth=0.1, relheight=0.15)
            
        # Criação da label e entrada do código
        self.lb_codigo = Label(self.frame_1, text="Código", bg="#dfe3ee", font=("Verdana", 8, "bold"))
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        # Criação da label e entrada do nome do cliente
        self.lb_nome = Label(self.frame_1, text="Nome", bg="#dfe3ee", font=("Verdana", 8, "bold"))
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

            
        # Criação da label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text="Telefone", bg="#dfe3ee", font=("Verdana", 8, "bold"))
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

            
        # Criação da label e entrada da cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade", bg="#dfe3ee", font=("Verdana", 8, "bold"))
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

    def lista_frame_2(self):
        # Configurando o cabeçario
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3", "col4"))
        
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="telefone")
        self.listaCli.heading("#4", text="Cidade")
        
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        # Configurando a posição da lista
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.94, relheight=0.85)

        # Criando scroll da lista
        self.scrolLista = Scrollbar(self.frame_2, orient="vertical")
        self.listaCli.configure(yscrollcommand=self.scrolLista.set) # setando na tela
        self.scrolLista.place(relx=0.955, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.double_click)

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit(): self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Relatórios", menu=filemenu2)

        filemenu.add_command(label="Sair", command=quit)
        filemenu.add_command(label="Limpar Cliente", command=self.limpar_cliente)

        filemenu2.add_command(label="Ficha do Cliente", command=self.gera_relatorio_cliente)

Application()
        