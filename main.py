import tkinter as tk
from tkinter import messagebox
import random

def mensagem_sucesso(titulo, mensagem):
    messagebox.showinfo(titulo, mensagem)

# FUNÇÕES DO SISTEMA 
def abrir_tela_principal():
    tela_login.pack_forget()
    tela_principal.pack(fill="both", expand=True)

def abrir_tela_agendamento():
    selecionado = lista_especialidades.curselection()
    if selecionado:
        medico_info = lista_especialidades.get(selecionado[0])
        label_medico_agendamento.config(text=medico_info)
        tela_principal.pack_forget()
        tela_agendamento.pack(fill="both", expand=True)
    else:
        mensagem_aviso("Atenção", "Por favor, selecione um médico antes de agendar.")

def voltar_para_principal():
    tela_agendamento.pack_forget()
    tela_principal.pack(fill="both", expand=True)

def confirmar_agendamento():
    horario = lista_horarios.get(tk.ACTIVE)
    medico = label_medico_agendamento.cget("text")
    if not horario:
        mensagem_aviso("Atenção", "Por favor, selecione um horário antes de confirmar.")
        return
    if horario in horarios_indisponiveis:
        mensagem_erro("Erro", f"O horário {horario} não está disponível para agendamento.")
        return
    protocolo = random.randint(100000, 999999)
    mensagem_sucesso(
        "Agendamento Confirmado",
        f"✅ Horário {horario} com {medico} agendado com sucesso!\nProtocolo: {protocolo}"
    )

def cadastrar_usuario():
    cpf = entrada_cpf.get()
    senha = entrada_senha.get()
    if cpf and senha:
        mensagem_sucesso("Cadastro", f"Usuário CPF {cpf} cadastrado com sucesso!")
        entrada_cpf.delete(0, tk.END)
        entrada_senha.delete(0, tk.END)
    else:
        mensagem_aviso("Erro", "Por favor, preencha CPF e senha para cadastrar.")

def filtrar_especialidades(event):
    filtro = entrada_pesquisa.get().lower()
    lista_especialidades.delete(0, tk.END)
    for medico in medicos:
        if filtro in medico.lower():
            lista_especialidades.insert(tk.END, medico)

# DADOS
medicos = [
    "Dr. João Silva - Dentista - CRO 12345",
    "Dra. Flávia Montenegro - Pediatra - CRO 54321",
    "Dr. Carlos Pereira - Clínico Geral - CRO 67890",
    "Dra. Ana Beatriz - Dermatologista - CRO 11223",
    "Dr. Ricardo Lopes - Cardiologista - CRO 33445",
    "Dra. Fernanda Costa - Oftalmologista - CRO 55667",
    "Dr. Marcos Vinicius - Ortopedista - CRO 77889",
    "Dra. Camila Souza - Ginecologista - CRO 99887"
]

horarios_disponiveis = [
    "20/09 - 08:00", "20/09 - 08:30", "20/09 - 09:00",
    "21/09 - 10:00", "21/09 - 11:00", "21/09 - 14:00"
]

# Horários já agendados / não disponíveis
horarios_indisponiveis = ["20/09 - 08:30", "21/09 - 11:00"]

# JANELA PRINCIPAL
janela = tk.Tk()
janela.title("Climed - Autoatendimento")
janela.geometry("450x650")
janela.configure(bg="white")

# TELA LOGIN
tela_login = tk.Frame(janela, bg="white")

tk.Label(tela_login, text="Bem-vindo ao Climed!", font=("Arial", 22, "bold"), fg="#007acc", bg="white").pack(pady=40)
tk.Label(tela_login, text="CPF", anchor="w", bg="white", font=("Arial", 12)).pack(fill="x", padx=50)
entrada_cpf = tk.Entry(tela_login, font=("Arial", 12))
entrada_cpf.pack(fill="x", padx=50, pady=5)

tk.Label(tela_login, text="Senha", anchor="w", bg="white", font=("Arial", 12)).pack(fill="x", padx=50)
entrada_senha = tk.Entry(tela_login, show="*", font=("Arial", 12))
entrada_senha.pack(fill="x", padx=50, pady=5)

tk.Button(tela_login, text="Entrar", bg="#007acc", fg="white", font=("Arial", 14, "bold"), command=abrir_tela_principal).pack(pady=15)
tk.Button(tela_login, text="Cadastrar", bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), command=cadastrar_usuario).pack(pady=5)
tk.Label(tela_login, text="Esqueceu a senha?", fg="gray", bg="white", cursor="hand2").pack(pady=10)
tela_login.pack(fill="both", expand=True)

# TELA PRINCIPAL 
tela_principal = tk.Frame(janela, bg="white")
tk.Label(tela_principal, text="Olá, Usuário!", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
tk.Label(tela_principal, text="CLIMED", font=("Arial", 24, "bold"), fg="#007acc", bg="white").pack(pady=10)

# Pesquisa de médicos
tk.Label(tela_principal, text="Pesquise médico ou especialidade:", bg="white", font=("Arial", 12)).pack(pady=5)
entrada_pesquisa = tk.Entry(tela_principal, font=("Arial", 12))
entrada_pesquisa.pack(fill="x", padx=40, pady=5)
entrada_pesquisa.bind("<KeyRelease>", filtrar_especialidades)

# Lista de médicos/especialidades
lista_especialidades = tk.Listbox(tela_principal, height=8, font=("Arial", 12))
for medico in medicos:
    lista_especialidades.insert(tk.END, medico)
lista_especialidades.pack(fill="x", padx=40, pady=10)

tk.Button(tela_principal, text="Agendar Consulta", bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), command=abrir_tela_agendamento).pack(pady=10)

# TELA AGENDAMENTO 
tela_agendamento = tk.Frame(janela, bg="white")
label_medico_agendamento = tk.Label(tela_agendamento, text="", font=("Arial", 14, "bold"), bg="white")
label_medico_agendamento.pack(pady=10)

tk.Label(tela_agendamento, text="Selecione o horário desejado:", bg="white", font=("Arial", 12)).pack(pady=10)
lista_horarios = tk.Listbox(tela_agendamento, height=6, font=("Arial", 12))
for hora in horarios_disponiveis:
    status = " (Indisponível)" if hora in horarios_indisponiveis else ""
    lista_horarios.insert(tk.END, hora + status)
lista_horarios.pack(fill="x", padx=40, pady=5)

tk.Button(tela_agendamento, text="Confirmar Agendamento", bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), command=confirmar_agendamento).pack(pady=10)
tk.Button(tela_agendamento, text="Voltar", bg="#f44336", fg="white", font=("Arial", 12, "bold"), command=voltar_para_principal).pack()
 
# INICIAR APLICAÇÃO 
janela.mainloop()
