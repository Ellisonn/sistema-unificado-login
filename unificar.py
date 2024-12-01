import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import shutil
import os

# Função para salvar os dados da empresa no arquivo
def salvar_empresa():
    nome_empresa = entry_nome_empresa.get()
    cnpj = entry_cnpj.get()

    if not nome_empresa or not cnpj:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    with open("empresas.txt", "a") as file:
        file.write(f"{nome_empresa},{cnpj}\n")
    
    carregar_empresas()
    messagebox.showinfo("Sucesso", "Empresa cadastrada com sucesso!")
    entry_nome_empresa.delete(0, tk.END)
    entry_cnpj.delete(0, tk.END)

# Função para carregar empresas cadastradas
def carregar_empresas():
    empresas = []
    if os.path.exists("empresas.txt"):
        with open("empresas.txt", "r") as file:
            for line in file:
                nome_empresa, cnpj = line.strip().split(',')
                empresas.append(nome_empresa)
    combo_empresas['values'] = empresas
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
root.title("Cadastro e Envio de Arquivos")
root.geometry("700x400")

# Frame de cadastro de empresas
frame_cadastro = tk.Frame(root)
frame_cadastro.pack(pady=20)

tk.Label(frame_cadastro, text="Cadastro de Empresas", font=("Arial", 14, "bold")).pack(pady=5)

tk.Label(frame_cadastro, text="Nome da Empresa:", font=("Arial", 12, "bold")).pack(pady=5)
entry_nome_empresa = tk.Entry(frame_cadastro, width=50)
entry_nome_empresa.pack(pady=5)

tk.Label(frame_cadastro, text="CNPJ:", font=("Arial", 12, "bold")).pack(pady=5)
entry_cnpj = tk.Entry(frame_cadastro, width=50)
entry_cnpj.pack(pady=5)

tk.Button(frame_cadastro, text="Salvar Empresa", command=salvar_empresa).pack(pady=20)

# Frame de envio de arquivos
frame_envio = tk.Frame(root)
frame_envio.pack(pady=20)

tk.Label(frame_envio, text="Envio de Arquivos", font=("Arial", 14, "bold")).pack(pady=5)

tk.Label(frame_envio, text="Selecione a Empresa:", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)
combo_empresas = ttk.Combobox(frame_envio, state="readonly")
combo_empresas.pack(side=tk.LEFT, padx=5)

tk.Label(frame_envio, text="Enviar Arquivo:", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)
tk.Button(frame_envio, text="Escolher Arquivo", command=enviar_arquivo).pack(side=tk.LEFT, padx=5)

# Carregar empresas cadastradas ao iniciar o programa
carregar_empresas()

# Iniciar o loop principal da interface
root.mainloop()
