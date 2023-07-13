from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("main.py", base=base)] # Nome do Arquivo que contém seu código

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Cadastro_de_Clientes",
    options = options,
    version = "4.0",
    description = 'Sistema para cadastrar clientes e funcionários, integrado ao banco de dados sql e utilizando tkinter para integração gráfica.',
    executables = executables
)