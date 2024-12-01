import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import shutil
import os

# Função para carregar empresas cadastradas
def carregar_empresas():
    empresas = []
    if os.path.exists("empresas.txt"):
        with open("empresas.txt", "r") as file:
            for line in file:
                nome_empresa, cnpj = line.strip().split(',')
                empresas.append(nome_empresa)
    return empresas

# Função para abrir uma caixa de diálogo de seleção de arquivo e salvar na pasta raiz
def enviar_arquivo():
    empresa_selecionada = combo_empresas.get()
    if not empresa_selecionada:
        messagebox.showerror("Erro", "Selecione uma empresa!")
        return
    
    file_path = filedialog.askopenfilename(filetypes=[("Todos os arquivos", "*.*")])
    if file_path:
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(os.getcwd(), file_name)
        shutil.copy(file_path, dest_path)
        messagebox.showinfo("Arquivo Enviado", f"Arquivo {file_name} enviado com sucesso para a empresa {empresa_selecionada}!")

# Configuração da janela principal
root = tk.Tk()
root.title("Envio de Arquivos")
root.geometry("500x200")
root.configure(bg='orange')

# Frame principal para centralizar os widgets
frame = tk.Frame(root, bg='orange')
frame.pack(padx=20, pady=20, fill=tk.X)

# Seleção da empresa
tk.Label(frame, text="Selecione a Empresa:", font=("Arial", 12, "bold"), bg='orange').pack(side=tk.LEFT, padx=5)
empresas = carregar_empresas()
combo_empresas = ttk.Combobox(frame, values=empresas, state="readonly")
combo_empresas.pack(side=tk.LEFT, padx=5)

# Botão de Enviar Arquivo
tk.Label(frame, text="Enviar Arquivo:", font=("Arial", 12, "bold"), bg='orange').pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Escolher Arquivo", command=enviar_arquivo).pack(side=tk.LEFT, padx=5)

# Iniciar o loop principal da interface
root.mainloop()
