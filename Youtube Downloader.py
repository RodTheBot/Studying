import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

def baixar_video():
    url = entrada_url.get()
    caminho_destino = entrada_caminho.get()

    if not url.strip():
        messagebox.showerror("Erro", "Por favor, insira uma URL válida.")
        return

    if not caminho_destino.strip():
        caminho_destino = "./"

    opcoes = {
        'format': 'best',
        'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", "Vídeo baixado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def selecionar_pasta():
    caminho = filedialog.askdirectory()
    if caminho:
        entrada_caminho.delete(0, tk.END)
        entrada_caminho.insert(0, caminho)

# Janela Principal
janela = tk.Tk()
janela.title("Downloader de Vídeos")
janela.geometry("400x200")

# URL do vídeo
tk.Label(janela, text="URL do Vídeo:").pack(pady=5)
entrada_url = tk.Entry(janela, width=50)
entrada_url.pack(pady=5)

# Caminho para salvar
tk.Label(janela, text="Pasta de Destino:").pack(pady=5)
entrada_caminho = tk.Entry(janela, width=50)
entrada_caminho.pack(pady=5)

botao_selecionar_pasta = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
botao_selecionar_pasta.pack(pady=5)

# Botão de download
botao_baixar = tk.Button(janela, text="Baixar Vídeo", command=baixar_video)
botao_baixar.pack(pady=10)

# Executar o loop da interface
janela.mainloop()
