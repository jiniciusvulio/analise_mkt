import tkinter as tk
from tkinter import ttk
import pandas as pd

# calculo das metricas
def conv_rate(vis, conv):
	return (conv / vis) * 100

def cpa(tot, conv):
	return tot / conv

def roi(rec, tot):
	return (rec - tot) / tot * 100

def calc():
	vis = int(entry_vis.get())
	conv = int(entry_conv.get())
	tot = float(entry_tot.get())
	rec = float(entry_rec.get())

	convrt = conv_rate(vis, conv)
	cpera = cpa(tot, conv)
	roni = roi(rec, tot)

	results.set(f"Taxa de Conversão: {convrt: .2f}%\n"
		    f"Custo por Aquisição: R${cpera: .2f}\n"
		    f"Retorno sobre Investimento: {roni: .2f}%")

# main
root = tk.Tk()
root.title("Análise de Efetividade de Campanha de Marketing")
root.geometry('400x300')

# pesos na main
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# frame central
frame = ttk.Frame(root, padding="20")
frame.grid(column= 0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)

# labels e entries
ttk.Label(frame, text="Visitas:").grid(row=0, column=0, padx=10, pady=5)
entry_vis = ttk.Entry(frame)
entry_vis.grid(row=0, column=1, padx=10, pady=5, sticky="w")

ttk.Label(frame, text="Conversões:").grid(row=1, column=0, padx=10, pady=5)
entry_conv = ttk.Entry(frame)
entry_conv.grid(row=1, column=1, padx=10, pady=0, sticky="w")

ttk.Label(frame, text="Custo Total (R$):").grid(row=2, column=0, padx=10, pady=5)
entry_tot = ttk.Entry(frame)
entry_tot.grid(row=2, column=1, padx=10, pady=5, sticky="w")

ttk.Label(frame, text="Receita (R$):").grid(row=3, column=0, padx=10, pady=5)
entry_rec = ttk.Entry(frame)
entry_rec.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# botao
button_calc = ttk.Button(frame, text="Calcular", command=calc)
button_calc.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# resultados
results = tk.StringVar()
ttk.Label(frame, textvariable=results).grid(row=5, column=0, columnspan=2, padx= 10, pady=10)


root.mainloop()













