import tkinter as tk
from tkinter import ttk

import numpy as np
import numpy_financial as npf

def calcular_pago():
    try:
        capital = float(capital_entry.get())
        cuotas = float(cuotas_entry.get())
        tasa = float(tasa_entry.get())
        tasa /= 100.0  # Convertir la tasa de porcentaje a fracción

        vc = valorCuota(tasa, cuotas, capital)
        vt = valorTotal(vc, cuotas)
        it = interesTotal(vt, capital)
        resultado_label.config(text=f"Resultado: {vc.round(0),vt.round(0),it.round(0)}")
    except ValueError:
        resultado_label.config(text="Ingrese valores numéricos válidos")

def valorCuota(rate, nper, pv):
    """
    Calcula el pago periódico para un préstamo.

    :param rate: Tasa de interés por período.
    :param nper: Número total de períodos de pago.
    :param pv: Valor presente, o monto principal del préstamo.
    :return: Pago periódico del préstamo.
    """
    if rate == 0:
        return -pv / nper
    else:
        return -npf.pmt(rate, nper, pv)
    
def valorTotal(valorC, nper):
    return valorC*nper

def interesTotal(valorT, pv):
    return valorT - pv

# Crear la ventana principal
app = tk.Tk()
app.title("Calculadora de Préstamos")

# Crear y posicionar widgets
capital_label = ttk.Label(app, text="Capital:")
capital_label.grid(row=0, column=0, padx=10, pady=10)

capital_entry = ttk.Entry(app)
capital_entry.grid(row=0, column=1, padx=10, pady=10)

cuotas_label = ttk.Label(app, text="Cuotas:")
cuotas_label.grid(row=1, column=0, padx=10, pady=10)

cuotas_entry = ttk.Entry(app)
cuotas_entry.grid(row=1, column=1, padx=10, pady=10)

tasa_label = ttk.Label(app, text="Tasa (%):")
tasa_label.grid(row=2, column=0, padx=10, pady=10)

tasa_entry = ttk.Entry(app)
tasa_entry.grid(row=2, column=1, padx=10, pady=10)

calcular_button = ttk.Button(app, text="Calcular", command=calcular_pago)
calcular_button.grid(row=3, column=0, columnspan=2, pady=10)

resultado_label = ttk.Label(app, text="Resultado:")
resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar el bucle de eventos
app.mainloop()

