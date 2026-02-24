"""
Calculadora
"""
import math
import re
import tkinter
import winsound

import customtkinter
from simpleeval import simple_eval


def main():
    """
    Função principal da calculadora.
    """
    try:

        def transformar_raizes(expressao):
            """
            Transforma todas as ocorrências de nraizx em x**(1/n).
            
            Args:
                expressao (str): expressão matemática do visor
            
            Returns:
                str: expressão com raízes convertidas
            """
            try:
                padrao_raiz = r"(\d+(?:\.\d+)?)\u207F\u221A(\d+(?:\.\d+)?)"

                # Função que será chamada para cada ocorrência
                def substitui(match):
                    indice = match.group(1)
                    base = match.group(2)
                    return f"{base}**(1/{indice})"

                # Substitui todas as ocorrências no texto
                expressao_transformada = re.sub(padrao_raiz, substitui, expressao)
                return expressao_transformada
            
            except Exception as erro:
                visor.delete(0, "end")
                visor.insert("end", "Erro")
                winsound.Beep(900, 500)


        def calcula(expressao):
            """
            Calcula o valor da expressão do visor.

            Args:
                expressao: recebe a expressao matemática que é o conteúdo do visor.
            """
            try:
                expressao = visor.get()

                # Substituir símbolos da calculadora por operadores matemáticos
                expressao = expressao.replace("x", "*")
                expressao = expressao.replace(chr(247), "/")
                expressao = expressao.replace("^", "**")
                expressao = expressao.replace("%", "/100")

                # Detetar padrão do tipo raiz xraizn e transformar em taiz n-ésima
                padrao_raiz = r"(\d+(?:\.\d+)?)raiz(\d+(?:\.\d+)?)"

                # Avaliar a expressão de forma segura
                expressao = transformar_raizes(expressao)
                resultado = simple_eval(expressao)
                if resultado.is_integer():
                    resultado = int(resultado)
                
                visor.delete(0, "end")
                visor.insert("end", resultado)
                janela.focus()

            except Exception as erro:
                visor.delete(0, "end")
                visor.insert("end", "Erro")
                winsound.Beep(900, 500)


        def clique(tecla):
            """
            Exibe no visor a tecla que foi premida.
            Suporta os operadores: +, -, *, /, ^, % e raiz n-ésima no formato xraizn.
            
            Args:
                tecla (str): recebe o valor da tecla premida.
            """
            # Pega posição atual do cursor
            posicao = visor.index("insert")

            # Insere exatamente onde o cursor está
            visor.insert(posicao, tecla)

            # Move cursor após o que foi inserido
            visor.icursor(posicao + len(tecla))

            # Garante que a visualização acompanhe
            visor.xview_moveto(1)


        def limpa_visor():
            """
            Limpa o visor
            """
            visor.delete(0, "end")
            janela.focus()
        

        def backspace():
            """
            Apaga um valor da direita para a esquerda
            """
            posicao = visor.index("insert")

            if posicao > 0:
                visor.delete(posicao - 1)
        

        # Cria a janela
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        janela = customtkinter.CTk()
        janela.title("Calculadora")
        janela.geometry("237x500")
        janela.resizable(width=False, height=False)
        
        # Cria a entrada de dados (visor)
        visor = customtkinter.CTkEntry(
            janela, 
            width = 217, 
            height = 70, 
            font = ("Calibri", 50), 
            text_color = "black", 
            fg_color = "white"
        )
        visor.place(x=10, y=20)

        # Cria os botões
        botao_clear = customtkinter.CTkButton(janela, 
            command=limpa_visor, 
            text="C", 
            font=("Calibri", 20, "bold"), 
            width=107, 
            height=50, 
            border_width=1, 
            text_color="black", 
            fg_color="yellow", 
            hover_color="gray"
        )
        botao_clear.place(x=10, y=100)

        b_abrir_parenteses = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("("), 
            text="(", font = ("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            text_color="black", 
            fg_color="green", 
            hover_color="gray"
        )
        b_abrir_parenteses.place(x=120, y=100)

        b_fechar_parenteses = customtkinter.CTkButton(
            janela, 
            command=lambda: clique(")"), 
            text=")", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            text_color="black", 
            fg_color="green", 
            hover_color="gray"
        )
        b_fechar_parenteses.place(x=175, y=100)

        b_0 = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("0"), 
            text="0", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            hover_color="gray"
        )
        b_0.place(x=10, y=155)

        b_1 = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("1"), 
            text="1", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            hover_color="gray"
        )
        b_1.place(x=65, y=155)

        b_2 = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("2"), 
            text="2", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            hover_color="gray"
        )
        b_2.place(x=120, y=155)

        b_3 = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("3"), 
            text="3", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            hover_color="gray"
        )
        b_3.place(x=175, y=155)

        b_4 = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("4"), 
            text="4", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            hover_color="gray"
        )
        b_4.place(x=10, y=210)

        b_5 = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("5"), 
            text="5", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            hover_color="gray"
        )
        b_5.place(x=65, y=210)

        b_6 = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("6"), 
            text="6", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            hover_color="gray"
        )
        b_6.place(x=120, y=210)

        b_7 = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("7"), 
            text="7", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            hover_color="gray"
        )
        b_7.place(x=175, y=210)

        b_8 = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("8"), 
            text="8", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            hover_color="gray"
        )
        b_8.place(x=10, y=265)

        b_9 = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("9"), 
            text="9", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            hover_color="gray"
        )
        b_9.place(x=65, y=265)

        b_igual = customtkinter.CTkButton(
            janela, 
            command=lambda: calcula(visor), 
            text="=", 
            font=("Calibri", 20, "bold"), 
            width=107, 
            height=50, 
            border_width=1, 
            text_color="black", 
            fg_color="yellow", 
            hover_color="gray"
        )
        b_igual.place(x=120, y=265)

        b_soma = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("+"), 
            text="+", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            text_color="white", 
            fg_color="purple", 
            hover_color="gray"
        )
        b_soma.place(x=10, y=320)

        b_subtracao = customtkinter.CTkButton(
            janela, 
            command = lambda: clique("-"), 
            text="-", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            text_color="white", 
            fg_color="purple", 
            hover_color="gray"
        )
        b_subtracao.place(x=65, y=320)

        b_multiplicacao = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("x"), 
            text="x", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            text_color="white", 
            fg_color="purple", 
            hover_color="gray"
        )
        b_multiplicacao.place(x=120, y=320)

        b_divisao = customtkinter.CTkButton(
            janela, 
            command=lambda: clique(chr(247)), 
            text=chr(247), 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            text_color="white", 
            fg_color="purple", 
            hover_color="gray"
        )
        b_divisao.place(x=175, y=320)

        b_potenciacao = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("^"), 
            text="x\u02B8", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            text_color="white", 
            fg_color="purple", 
            hover_color="gray"
        )
        b_potenciacao.place(x=10, y=375)

        b_radiciacao = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("\u207F\u221A"), 
            text="\u207F\u221A", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            text_color="white", 
            fg_color="purple", 
            hover_color="gray"
        )
        b_radiciacao.place(x=65, y=375)

        b_percentual = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("%"), 
            text="%", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            text_color="black", 
            fg_color="green", 
            hover_color="gray"
        )
        b_percentual.place(x=120, y=375)

        b_ponto = customtkinter.CTkButton(
            janela, 
            command=lambda: clique("."), 
            text=".", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            text_color="black", 
            fg_color="green", 
            hover_color="gray"
        )
        b_ponto.place(x=175, y=375)

        b_pi = customtkinter.CTkButton(
            janela, 
            command=lambda: clique(math.pi), 
            text="pi", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            text_color="white", 
            fg_color="red", 
            hover_color="gray"
        )
        b_pi.place(x=10, y=430)

        b_e = customtkinter.CTkButton(
            janela, 
            command=lambda: clique(math.e), 
            text="e", 
            font=("Calibri", 20, "bold"), 
            width=50, 
            height=50, 
            border_width=1, 
            text_color="white", 
            fg_color="red", 
            hover_color="gray"
        )
        b_e.place(x=65, y=430)

        b_backspace = customtkinter.CTkButton(
            janela, 
            command=backspace, 
            text="\u232B", 
            font=("Calibri", 20, "bold"), 
            width=107, 
            height=50, 
            border_width=1, 
            text_color="black", 
            fg_color="yellow", 
            hover_color="gray"
        )
        b_backspace.place(x=120, y=430)

        # Cria o loop da janela
        janela.mainloop()

    except Exception as erro:
        tkinter.messagebox.showerror("Erro", f"Ocorreu o erro {erro}. Por favor entre em contacto com o programador.")


if __name__ == "__main__":
    main()
else:
    tkinter.messagebox.showerror("Erro", "Não foi possível inicar a aplicação. Por favor entre em contacto com o programador.")
