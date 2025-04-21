import tkinter as tk
import os
from tkinter import messagebox
from clima import buscar_temperatura_e_umidade
from excel_utils import salvar_dados_excel

def capturar():
    dados = buscar_temperatura_e_umidade()
    if dados:
        salvar_dados_excel(dados)
        messagebox.showinfo(
            "Previsão atualizada com sucesso!",
            f"📅 Data: {dados['data']}\n🕒 Hora: {dados['hora']}\n🌡️ Temperatura: {dados['temperatura']}\n💧 Umidade: {dados['umidade']}\n\nOs dados foram salvos na planilha com sucesso!"
        )
      
        btn_abrir.pack(pady=(10, 0))
    else:
        messagebox.showerror("Erro", "Erro ao buscar os dados da previsão.")

def abrir_planilha():
    caminho = "dados.xlsx"
    if os.path.exists(caminho):
        os.startfile(caminho)
    else:
        messagebox.showwarning("Arquivo não encontrado", "A planilha ainda não foi gerada.")

janela = tk.Tk()
janela.title("Previsão do tempo de São Paulo")
janela.geometry("400x200")
janela.resizable(False, False)
janela.configure(bg="#F1F2F6")


janela.update_idletasks()
largura = janela.winfo_width()
altura = janela.winfo_height()
x = (janela.winfo_screenwidth() // 2) - (largura // 2)
y = (janela.winfo_screenheight() // 2) - (altura // 2)
janela.geometry(f"+{x}+{y}")


fonte_titulo = ("Segoe UI", 11, "bold")
fonte_botao = ("Segoe UI", 10)


label_instrucao = tk.Label(janela, text="Atualizar previsão na planilha:", font=fonte_titulo, bg="#F1F2F6", fg="#333")
label_instrucao.pack(pady=(30, 10))

btn = tk.Button(
    janela,
    text="Buscar previsão",
    font=fonte_botao,
    command=capturar,
    relief="groove",
    padx=12,
    pady=4
)
btn.pack()


btn_abrir = tk.Button(
    janela,
    text="Abrir planilha Excel",
    font=fonte_botao,
    command=abrir_planilha,
    relief="groove",
    padx=12,
    pady=4
)

janela.mainloop()

