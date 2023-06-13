import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont


def mostrar_mensagem():
    if len(meses_clicados) == 12:
        mensagem = "Te amarei de janeiro a janeiro, até o mundo acabar ❤️"
        label.configure(text=mensagem)


def botao_clicado(mes):
    if mes not in meses_clicados:
        meses_clicados.append(mes)


def resetar_selecao():
    meses_clicados.clear()
    label.configure(text="")


janela = tk.Tk()
janela.title("Mês do Amor")

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

meses_clicados = []

botao_config = {
    "height": 2,
    "padx": 10,
    "pady": 5,
    "relief": tk.RAISED,
    "bd": 2,
    "borderwidth": 2,
    "bg": "lightgray",
    "fg": "black",
    "font": tkfont.Font(size=12),
}

canvas = tk.Canvas(janela)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(janela, orient=tk.HORIZONTAL, command=canvas.xview)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

canvas.configure(xscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(
    scrollregion=canvas.bbox("all")))

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

for i, mes in enumerate(meses):
    botao_config["width"] = len(mes) + 2
    botao = tk.Button(
        frame, text=mes, command=lambda m=mes: botao_clicado(m), **botao_config)
    botao.grid(row=i // 3, column=i % 3, padx=5, pady=5)

botao_final = tk.Button(
    janela, text="Mostrar frase\n completa", **botao_config)
botao_final.configure(command=mostrar_mensagem)
botao_final.pack(pady=10, padx=10)

botao_reset = tk.Button(janela, text="Resetar", **botao_config)
botao_reset.configure(command=resetar_selecao)
botao_reset.pack(pady=10, padx=10)

label = tk.Label(janela, text="")
label.pack()

janela.mainloop()
