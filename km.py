import tkinter as tk
from tkinter import messagebox

# Função para salvar os dados da empresa no arquivo
def salvar_empresa():
    nome_empresa = entry_nome_empresa.get()
    cnpj = entry_cnpj.get()

    if not nome_empresa or not cnpj:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    with open("empresas.txt", "a") as file:
        file.write(f"{nome_empresa},{cnpj}\n")
    
    messagebox.showinfo("Sucesso", "Empresa cadastrada com sucesso!")
    entry_nome_empresa.delete(0, tk.END)
    entry_cnpj.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro de Empresas")
root.geometry("400x200")

# Campos de entrada para nome da empresa e CNPJ
tk.Label(root, text="Nome da Empresa:").pack(pady=5)
entry_nome_empresa = tk.Entry(root, width=50)
entry_nome_empresa.pack(pady=5)

tk.Label(root, text="CNPJ:").pack(pady=5)
entry_cnpj = tk.Entry(root, width=50)
entry_cnpj.pack(pady=5)

# Botão para salvar a empresa
tk.Button(root, text="Salvar Empresa", command=salvar_empresa).pack(pady=20)

# Iniciar o loop principal da interface
root.mainloop()
