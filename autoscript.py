import os
import subprocess
import urllib.request
import time
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
import sys

NOME_AULA = ""
NICKNAME = ""
textosCFSd = 0

PYTHON_URL = "https://www.python.org/ftp/python/2.7.15/python-2.7.15.amd64.msi"
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
INSTALLER_NAME = os.path.join(BASE_DIR, "python_installer.exe")
DEPENDENCIAS = ["pyautogui", "keyboard", "pyperclip", "tkinter"]  # Bibliotecas necessárias


# Função para atualizar o progresso e exibir a animação de carregamento
def atualizar_progresso(porcentagem, mensagem=""):
    """Atualiza a barra de progresso e exibe uma mensagem com animação."""
    carregando_animacao = ['|', '/', '-', '\\']
    for i in range(3):  # Animar o carregamento por um tempo
        print(f"\r{mensagem} ({porcentagem}%) {carregando_animacao[i % 4]}", end='', flush=True)
        time.sleep(0.1)

# Função para verificar se o Python está instalado
def verificar_python():
    """Verifica se o Python está instalado."""
    atualizar_progresso(10, "Verificando se o Python está instalado...")
    try:
        subprocess.run(["where", "python"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=True)
        atualizar_progresso(20, "Python encontrado!")
        print("Python já instalado.")
        return True
    except subprocess.CalledProcessError as e:
        atualizar_progresso(20, "Python não encontrado.")
        print(f"Erro ao verificar instalação do Python: {e}")
        return False

# Função para baixar o instalador do Python
def baixar_python():
    """Baixa o instalador do Python."""
    atualizar_progresso(30, "Baixando o Python...")
    try:
        urllib.request.urlretrieve(PYTHON_URL, INSTALLER_NAME)
        atualizar_progresso(60, "Download concluído.")
        print("Instalador do Python baixado com sucesso.")
    except Exception as e:
        atualizar_progresso(60, f"Erro ao baixar o Python: {e}")
        print(f"Erro ao baixar o Python: {e}")
        sys.exit(1)

# Função para instalar o Python
def instalar_python():
    """Instala o Python silenciosamente."""
    atualizar_progresso(70, "Instalando o Python...")
    try:
        subprocess.run([INSTALLER_NAME, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)
        atualizar_progresso(75, "Instalação concluída.")
        print("Python instalado com sucesso.")
    except subprocess.CalledProcessError as e:
        atualizar_progresso(75, f"Erro ao instalar o Python: {e}")
        print(f"Erro ao instalar o Python: {e}")
        sys.exit(1)
        
# Função para verificar e instalar a biblioteca pyperclip
def verificar_e_instalar_pyperclip():
    """Verifica e solicita a instalação manual da biblioteca pyperclip."""
    atualizar_progresso(79, "Verificando a biblioteca 'pyperclip'...")
    try:
        import pyperclip
        atualizar_progresso(83, "Biblioteca 'pyperclip' já instalada.")
        print("Biblioteca 'pyperclip' já instalada.")
    except ImportError:
        atualizar_progresso(85, "Biblioteca 'pyperclip' não encontrada.")
        print("\nA biblioteca 'pyperclip' não está instalada.")
        print("Abra um novo CMD e digite: pip install pyperclip")
        input("Após instalar manualmente, aperte Enter para prosseguir...")
        try:
            import pyperclip
            atualizar_progresso(90, "Biblioteca 'pyperclip' instalada com sucesso.")
            print("Biblioteca 'pyperclip' instalada com sucesso.")
        except ImportError:
            atualizar_progresso(95, "Erro: Biblioteca 'pyperclip' ainda não instalada.")
            print("Erro: A biblioteca 'pyperclip' ainda não está instalada.")
            sys.exit(1)

# Função para verificar e instalar a biblioteca tkinter
def verificar_e_instalar_tkinter():
    """Verifica e solicita a instalação manual da biblioteca tkinter."""
    atualizar_progresso(87, "Verificando a biblioteca 'tkinter'...")
    try:
        import tkinter
        atualizar_progresso(87, "Biblioteca 'tkinter' já instalada.")
        print("Biblioteca 'tkinter' já instalada.")
    except ImportError:
        atualizar_progresso(90, "Biblioteca 'tkinter' não encontrada.")
        print("\nA biblioteca 'tkinter' não está instalada.")
        print("Abra um novo CMD e digite: pip install tk")
        input("Após instalar manualmente, aperte Enter para prosseguir...")
        try:
            import tkinter
            atualizar_progresso(92, "Biblioteca 'tkinter' instalada com sucesso.")
            print("Biblioteca 'tkinter' instalada com sucesso.")
        except ImportError:
            atualizar_progresso(95, "Erro: Biblioteca 'tkinter' ainda não instalada.")
            print("Erro: A biblioteca 'tkinter' ainda não está instalada.")
            sys.exit(1)

# Função para verificar e instalar a biblioteca keyboard
def verificar_e_instalar_keyboard():
    """Verifica e solicita a instalação manual da biblioteca keyboard."""
    atualizar_progresso(95, "Verificando a biblioteca 'keyboard'...")
    try:
        import keyboard
        atualizar_progresso(96, "Biblioteca 'keyboard' já instalada.")
        print("Biblioteca 'keyboard' já instalada.")
    except ImportError:
        atualizar_progresso(97, "Biblioteca 'keyboard' não encontrada.")
        print("\nA biblioteca 'keyboard' não está instalada.")
        print("Abra um novo CMD e digite: pip install keyboard")
        input("Após instalar manualmente, aperte Enter para prosseguir...")
        try:
            import keyboard
            atualizar_progresso(98, "Biblioteca 'keyboard' instalada com sucesso.")
            print("Biblioteca 'keyboard' instalada com sucesso.")
        except ImportError:
            atualizar_progresso(99, "Erro: Biblioteca 'keyboard' ainda não instalada.")
            print("Erro: A biblioteca 'keyboard' ainda não está instalada.")
            sys.exit(1)
            
def colar_texto(texto):
    import pyperclip
    import keyboard
    """Copia o texto para a área de transferência e cola."""
    pyperclip.copy(texto)
    keyboard.press_and_release('ctrl+v')
    keyboard.press_and_release('shift+enter')

def executar_script_principal():
    import keyboard
    keyboard.unhook_all()
    # Simula 'Ctrl+A'
    keyboard.press_and_release('ctrl+a')
    # Simula 'Delete'
    keyboard.press_and_release('delete')
    """Executa o script principal."""
    global textosCFSd
    global NICKNAME
    print("\nExecutando o script principal...")
    print(textosCFSd)
    textosCFSd = textosCFSd + 1
    print(textosCFSd)
    print("Posicione o cursor onde deseja colar os textos. Aguarde a execução ao pressionar Ctrl + Enter.")

    if NOME_AULA == "CFSd":
        # Usando f-strings para substituir {NICKNAME} corretamente
        textos1 = [
            f"Olá, recruta. Eu sou o(a) instrutor(a) {NICKNAME}",
            "Seja bem-vindo(a) à RCC! Permaneça em silêncio e preste atenção ao conteúdo repassado na instrução.",
            "Se eu sair do jogo, me aguarde 5 minutos e caso eu não retorne, volte para o batalhão.",
            "Entendido, recruta?"
        ]
        
        textos2 = [
            f"Sussurrar {NICKNAME} AULAINS", 
            "Caso seja necessário, utilize o comando PAUSAR.AULA / RETOMAR.AULA",
            "para pausar e retomar o script passado pelo bot, respectivamente."
        ]
        
        textos3 = [
            "[TESTE TEÓRICO]", 
            "Agora, irei fazer algumas perguntas relacionadas à aula. Caso erre duas questões, será reprovado(a).",
            "1) Quais são os 3 requisitos necessários para o alistamento?"
        ]
        
        textos4 = [
            "2) Qual pronome deve ser utilizado ao se dirigir a SUPERIORES de patente/cargo?"
        ]
        
        textos5 = [
            "3) Como deve estar a missão de um recruta?"
        ]
        
        textos6 = [
            "4) Qual é a forma correta de assumir um superior na recepção?"
        ]
        
        textos7 = [
            f"Sussurrar {NICKNAME} RETOMARAULA",
        ]
        
        textos8 = [
            "Os dois comandos restantes (apresente-se e dispensado) serão ensinados em um dos cursos de soldado.",
            "[NEGRITO]",
            f"Sussurrar {NICKNAME} Caso o recruta já esteja falando em negrito, retome o script após o spoiler abaixo."
        ]
        
        textos9 = [
            "Lembrando que a utilização do negrito é indispensável nas dependências da instituição.",
            f"Sussurrar {NICKNAME} FINALIZARAULA",
        ]
        
        textos10 = [
            "Coloque uma boina preta e escreva em sua missão:",
            f"Sussurrar {NICKNAME} Envie a missão nova do soldado: [RCC] Soldado [SUA TAG].",
        ]
        
        textos11 = [
            "Aguarde, irei postar a instrução.",
        ]
    
        if textosCFSd == 1:
            # Enviando os textos com o pyautogui.write()
            for i, texto in enumerate(textos1):
                time.sleep(10)
                colar_texto(texto)
                atualizar_progresso(((i + 1) / len(textos1)) * 100, f"Inserindo texto {i+1}/{len(texto)}...")

            # Exibe a tela com o botão "Continuar" após o envio de textos1
            exibir_tela_continuar(textos2)
            
        if textosCFSd == 2:
            exibir_tela_continuar(textos3)
        
        if textosCFSd == 3:
            exibir_tela_continuar(textos4)
        
        if textosCFSd == 4:
            exibir_tela_continuar(textos5)
        
        if textosCFSd == 5:
            exibir_tela_continuar(textos6)
            
        if textosCFSd == 6:
            exibir_tela_aprovado_reprovado()
            
        if textosCFSd == 7:
            exibir_tela_continuar(textos7)
            
        if textosCFSd == 8:
            exibir_tela_continuar(textos8)
            
        if textosCFSd == 9:
            exibir_tela_negrito()
        
        if textosCFSd == 10:
            exibir_tela_continuar(textos9)
        
        if textosCFSd == 11:
            exibir_tela_continuar(textos10)
            
        if textosCFSd == 12:
            exibir_tela_continuar(textos11)
        
    textosCFSd = 0
    print("CONCLUIDO")

def exibir_tela_continuar(textos):
    """Exibe uma tela com botão 'Continuar' para prosseguir com os textos."""
    def continuar():
        """Função para prosseguir com os textos ao clicar no botão."""
        for i, texto in enumerate(textos):
            time.sleep(10)
            colar_texto(texto)
            atualizar_progresso(((i + 1) / len(textos)) * 100, f"Inserindo texto {i+1}/{len(texto)}...")
        root.quit()  # Encerra o loop principal
        root.destroy()  # Destroi a janela após o loop terminar
        executar_script_principal()

    root = tk.Tk()
    root.title("Continuar")
    root.geometry("300x150")
    
    label = tk.Label(root, text="Clique em 'Continuar'.", font=("Arial", 12))
    label.pack(pady=20)

    continuar_button = tk.Button(root, text="Continuar", font=("Arial", 12), command=continuar)
    continuar_button.pack()

    root.mainloop()
    

def exibir_tela_aprovado_reprovado():
    """Exibe uma tela com botão 'Aprovado e Reprovado' para prosseguir com os textos."""
    def aprovado():
        root.quit()  # Encerra o loop principal
        root.destroy()  # Destroi a janela após o loop terminar
        executar_script_principal()
    def reprovado():
        textos = [
            "Lamento, você está reprovado(a). Mas não desista, retorne ao batalhão e aliste-se novamente.",
            "Para isso, pesquise no navegador de quartos por RCC e entre no primeiro quarto da lista.",
            "Confio no seu potencial e sei que é capaz de ser aprovado(a)!"
        ]
        for i, texto in enumerate(textos):
            time.sleep(10)
            colar_texto(texto)
            atualizar_progresso(((i + 1) / len(textos)) * 100, f"Inserindo texto {i+1}/{len(texto)}...")
        root.quit()  # Encerra o loop principal
        root.destroy()  # Destroi a janela após o loop terminar

    root = tk.Tk()
    root.title("Continuar")
    root.geometry("300x150")
    
    label = tk.Label(root, text="Clique em 'Continuar'.", font=("Arial", 12))
    label.pack(pady=20)

    aprovado_button = tk.Button(root, text="Aprovado", font=("Arial", 12), command=aprovado)
    reprovado_button = tk.Button(root, text="Reprovado", font=("Arial", 12), command=reprovado)
    aprovado_button.pack()
    reprovado_button.pack()

    root.mainloop()
    

def exibir_tela_negrito():
    """Exibe uma tela com botão 'Aprovado e Reprovado' para prosseguir com os textos."""
    def com():
        root.quit()  # Encerra o loop principal
        root.destroy()  # Destroi a janela após o loop terminar
        executar_script_principal()
    def sem():
        textos = [
            "Sussurrar {NICKNAME} Use o spoiler 'Caso o recruta não saiba utilizar o negrito:' no script do fórum"
        ]
        for i, texto in enumerate(textos):
            time.sleep(10)
            colar_texto(texto)
            atualizar_progresso(((i + 1) / len(textos)) * 100, f"Inserindo texto {i+1}/{len(texto)}...")
        root.quit()  # Encerra o loop principal
        root.destroy()  # Destroi a janela após o loop terminar
        executar_script_principal()

    root = tk.Tk()
    root.title("Continuar")
    root.geometry("300x150")
    
    label = tk.Label(root, text="Clique em 'Continuar'.", font=("Arial", 12))
    label.pack(pady=20)

    com_button = tk.Button(root, text="Com Negrito", font=("Arial", 12), command=com)
    sem_button = tk.Button(root, text="Sem Negrito", font=("Arial", 12), command=sem)
    com_button.pack()
    sem_button.pack()

    root.mainloop()


def aguardar_atalho():
    import keyboard
    """Aguarda o atalho Ctrl + Enter para iniciar o script."""
    print("\nAguardando Ctrl + Enter para iniciar o script...")
    keyboard.wait("ctrl+enter")
    executar_script_principal()

def iniciar_script():
    """Inicia o processo de execução ao selecionar a aula."""
    atalho_thread = threading.Thread(target=aguardar_atalho, daemon=True)
    atalho_thread.start()
    while atalho_thread.is_alive():
        time.sleep(0.1)

def on_click_aula(aula):
    """Ação ao clicar em uma aula."""
    print(f"Aula {aula} selecionada.")
    global NOME_AULA
    NOME_AULA = aula
    iniciar_script()

def configurar_gui():
    """Configura a interface gráfica do Tkinter."""
    root = tk.Tk()
    root.title("Sistema de Aulas")
    root.geometry("300x400")
    root.config(bg="white")

    def capturar_nickname():
        nickname = simpledialog.askstring("Nickname do Instrutor", "Digite seu nickname:")
        if nickname:
            global NICKNAME
            NICKNAME = nickname
            label_nickname.config(text=f"Instrutor: {nickname}")
            button_frame.pack(pady=20)

    label_nickname = tk.Label(root, text="Instrutor: Nenhum", font=("Arial", 14), bg="white", fg="black")
    label_nickname.pack(pady=20)

    button_frame = tk.Frame(root, bg="white")
    button_cfsd = tk.Button(button_frame, text="CFSd", font=("Arial", 12), bg="blue", fg="white", command=lambda: on_click_aula("CFSd"))

    button_cfsd.pack(fill="x", pady=5)

    button_start = tk.Button(root, text="Trocar Nick", font=("Arial", 12), bg="blue", fg="white", command=capturar_nickname)
    button_start.pack(pady=30)

    root.mainloop()

if __name__ == "__main__":
    if not verificar_python():
        atualizar_progresso(0, "Iniciando download e instalação do Python...")
        baixar_python()
        instalar_python()
    else:
        atualizar_progresso(20, "Python já está instalado.")

    verificar_e_instalar_pyperclip()
    verificar_e_instalar_tkinter() 
    verificar_e_instalar_keyboard()
    configurar_gui()
