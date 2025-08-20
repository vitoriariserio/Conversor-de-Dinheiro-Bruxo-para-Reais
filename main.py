from tkinter import END
import customtkinter as ctk

class Dinheiro:
    def __init__(self, galeao, nuque, sicle):
        self.galeao = galeao
        self.nuque = nuque
        self.sicle = sicle

class Conversor:
    def __init__(self, Dinheiro):
        self.Dinheiro = Dinheiro
    
    def converter(self, valor_em_reais, moeda_destino):
        if moeda_destino == 'galeao':
            valor_convertido = valor_em_reais / self.Dinheiro.galeao
        elif moeda_destino == 'nuque':
            valor_convertido = valor_em_reais / self.Dinheiro.nuque
        elif moeda_destino == 'sicle':
            valor_convertido = valor_em_reais / self.Dinheiro.sicle
        else:
            raise ValueError ('Moeda de destino não reconhecida')
        
        return valor_convertido

conversorWM = ctk.CTk()
conversorWM.title("Conversor de dinheiro Bruxo")
conversorWM.geometry("400x450")
ctk.set_appearance_mode('dark')
conversorWM.configure(fg_color='#1E1E2F')



label_one = ctk.CTkLabel(conversorWM, text="⚡ Conversor de Dinheiro Bruxo ⚡", font=ctk.CTkFont(size=20,weight='bold'), text_color="#FFD369", )
label_one.pack(pady=30)


saida_entry = ctk.CTkEntry(master=conversorWM, placeholder_text="Aguardando conversão...", font=ctk.CTkFont(size=14), width=200,height=35,corner_radius=10)
saida_entry.pack(padx=30, pady=10)


entrada_entry = ctk.CTkEntry(master=conversorWM, placeholder_text="VALOR EM REAIS",width=200,height=35,corner_radius=10)
entrada_entry.pack(padx=20, pady=20)


moeda_selecionada = ctk.StringVar(value="")

def optionmenu_callback(choice):
    moeda_selecionada.set(choice)  
opcoes = ["galeao", "nuque", "sicle"]
menu = ctk.CTkOptionMenu(
    conversorWM, 
    values=opcoes, 
    command=optionmenu_callback,
    fg_color="#00237B",
    dropdown_fg_color="#00237B", 
    text_color="#FFD369", 
    dropdown_text_color="#FFD369",
    width=200,
    height=35,
    corner_radius=10
)
menu.pack(pady=15)
menu.set('ESCOLHA A MOEDA',)


def button_event():
    try:
        valor = float(entrada_entry.get())
        moeda = moeda_selecionada.get()

        if moeda == "":
            saida_entry.delete(0, END)
            saida_entry.insert(0, "Escolha a moeda!")
            return

       
        taxas = Dinheiro(galeao=37.50, nuque=0.08, sicle=2.21)
        conversor = Conversor(taxas)

        resultado = conversor.converter(valor, moeda)

        saida_entry.delete(0, END)
        saida_entry.insert(0, f"{resultado:.2f}")

    except ValueError:
        saida_entry.delete(0, END)
        saida_entry.insert(0, "Valor inválido!")


Button = ctk.CTkButton(
    master=conversorWM, 
    text="CONVERTER", 
    fg_color="#FFD369",
    hover_color="#1E4BA5",
    text_color="#1E1E2F", 
    command=button_event,
    width=200,
    height=35,
    corner_radius=10
)
Button.pack(padx=50, pady=20)


footer_label = ctk.CTkLabel(master=conversorWM, text='⚡ Feito por vitoriariserio ⚡', font=ctk.CTkFont(size=10), text_color='#AAAAAA')
footer_label.pack(side="bottom", pady=10)

conversorWM.mainloop()
