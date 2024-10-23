import random
import string
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """Gera uma senha aleatória com base nas opções selecionadas."""
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:  # Garantir que ao menos uma categoria foi selecionada
        return "Escolha ao menos uma opção!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    """Função chamada ao clicar no botão 'Gerar'."""
    length = length_scale.get()
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()
    
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Configura a janela principal
root = ThemedTk(theme="arc")  # Use um tema estético
root.title("Gerador de Senhas")
root.geometry("400x400")

# Estilos
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))

# Elementos da interface
length_label = ttk.Label(root, text="Comprimento da senha:")
length_label.pack(pady=10)

# Controle deslizante para o comprimento da senha
length_scale = tk.Scale(root, from_=8, to=32, orient=tk.HORIZONTAL)
length_scale.set(12)  # Valor padrão
length_scale.pack(pady=5)

# Opções de caracteres
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

upper_check = ttk.Checkbutton(root, text="Incluir letras maiúsculas", variable=upper_var)
upper_check.pack(pady=5)

lower_check = ttk.Checkbutton(root, text="Incluir letras minúsculas", variable=lower_var)
lower_check.pack(pady=5)

digits_check = ttk.Checkbutton(root, text="Incluir números", variable=digits_var)
digits_check.pack(pady=5)

special_check = ttk.Checkbutton(root, text="Incluir caracteres especiais", variable=special_var)
special_check.pack(pady=5)

generate_button = ttk.Button(root, text="Gerar", command=on_generate)
generate_button.pack(pady=20)

password_label = ttk.Label(root, text="Senha gerada:")
password_label.pack(pady=10)

password_entry = ttk.Entry(root, width=40)
password_entry.pack(pady=5)

# Inicia a aplicação
root.mainloop()
