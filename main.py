import tkinter as tk
from tkinter import messagebox

import numpy_financial as npf


def van(investment, benefit, cost, interest_rate, years):
    """
    Calcula el valor actual neto (VAN) de un proyecto de inversión.

    Args:
        investment (float): La inversión inicial del proyecto.
        benefit (float): El beneficio anual del proyecto.
        cost (float): El costo anual del proyecto.
        interest_rate (float): La tasa de interes.
        years (int): El número de años del proyecto.

    Returns:
        float: El valor actual neto del proyecto.

    """
    result = -1 * investment

    for i in range(years):
        result += (benefit - cost) / pow(1 + interest_rate, i + 1)
    return result



def bc(investment, benefit, cost, interest_rate, years):
    """
    Calcula el beneficio/costo (B/C) de un proyecto de inversión.

    Args:
        investment (float): La inversión inicial del proyecto.
        benefit (float): El beneficio anual del proyecto.
        cost (float): El costo anual del proyecto.
        interest_rate (float): La tasa de interes.
        years (int): El número de años del proyecto.

    Returns:
        float: El beneficio/costo del proyecto.

    """
    dominator = 0
    denominator = investment
    for i in range(years):
        dominator += (benefit / pow(1 + interest_rate, i + 1))

    for i in range(years):
        denominator += (cost / pow(1 + interest_rate, i + 1))

    return dominator / denominator



def tir(investment, benefit, cost, years):
    """
    Calcula la tasa interna de retorno (TIR) de un proyecto de inversión.

    Args:
        investment (float): La inversión inicial del proyecto.
        benefit (float): El beneficio anual del proyecto.
        cost (float): El costo anual del proyecto.
        years (int): El número de años del proyecto.

    Returns:
        float: La tasa interna de retorno del proyecto.

    """
    flujos_de_caja = [-investment]
    for i in range(years):
        flujos_de_caja.append(benefit - cost)

    tir = npf.irr(flujos_de_caja)
    return tir


def tr(investment, benefit, cost):
    """
    Calcula el tiempo de recuperación del capital (TR) de un proyecto de inversión.

    Args:
        investment (float): La inversión inicial del proyecto.
        benefit (float): El beneficio anual del proyecto.
        cost (float): El costo anual del proyecto.

    Returns:
        float: El tiempo de recuperación del capital en meses.

    """
    return 12 * (investment) / (benefit - cost)


def eval_project():
    """
    Evalúa un proyecto de inversión y muestra los resultados en una ventana de tkinter.

    """
    window = tk.Tk()
    window.title("Evaluación de Proyecto")

    # Variables de entrada
    investment_var = tk.DoubleVar()
    benefit_var = tk.DoubleVar()
    cost_var = tk.DoubleVar()
    rate_var = tk.DoubleVar()
    years_var = tk.IntVar()

    def evaluate_project():
        investment = investment_var.get()
        benefit = benefit_var.get()
        cost = cost_var.get()
        rate = rate_var.get()
        years = years_var.get()

        VAN = van(investment, benefit, cost, rate, years)
        BC = bc(investment, benefit, cost, rate, years)
        TIR = tir(investment, benefit, cost, years)
        TR = tr(investment, benefit, cost)

        flags = {
            'VAN': 0,
            'BC': 1,
            'TIR': rate
        }

        VAN_INTERPRETATION = "El proyecto es económicamente {}"
        BC_INTERPRETATION = "POR CADA S/ 1.0 Invertido hay una {} de {}"
        TIR_INTERPRETATION = "Los flujos de caja son {} para recuperar la inversión"

        if VAN < flags["VAN"]:
            VAN_INTERPRETATION = VAN_INTERPRETATION.format("NO FACTIBLE")
        else:
            VAN_INTERPRETATION = VAN_INTERPRETATION.format("FACTIBLE")

        if BC < flags["BC"]:
            BC_INTERPRETATION = BC_INTERPRETATION.format("PERDIDA", f"S/ {1 - BC}")
        else:
            BC_INTERPRETATION = BC_INTERPRETATION.format("GANANCIA", f"S/ {1 - BC}")

        if TIR < flags["TIR"]:
            TIR_INTERPRETATION = TIR_INTERPRETATION.format("INSUFICIENTES")
        else:
            TIR_INTERPRETATION = TIR_INTERPRETATION.format("SUFICIENTES")

        table_data = [
            ['Indicador', 'Valor', 'Condicional', 'Interpretacion'],
            ['VAN', f"S/ {VAN:.2f}", f'VAN > {flags["VAN"]}', VAN_INTERPRETATION],
            ['B/C', f"{BC:.2f}", f'B/C > {flags["BC"]}', BC_INTERPRETATION],
            ['TIR', f"{TIR:.2f} %", f'TIR > {flags["TIR"]}', TIR_INTERPRETATION]
        ]

        table_window = tk.Toplevel(window)

        table_window.title("Tabla de Evaluación")

        for i, row in enumerate(table_data):
            for j, cell in enumerate(row):
                label = tk.Label(table_window, text=cell, borderwidth=1, relief="solid", padx=10, pady=5)
                label.grid(row=i, column=j, sticky="nsew")

        for i in range(len(table_data[0])):
            table_window.columnconfigure(i, weight=1)
        for i in range(len(table_data)):
            table_window.rowconfigure(i, weight=1)
            
        forecast(VAN, TR, flags)

    # UI
    window.geometry("300x300")
    
    investment_label = tk.Label(window, text="Inversión:")
    investment_entry = tk.Entry(window, textvariable=investment_var)

    benefit_label = tk.Label(window, text="beneficio:")
    benefit_entry = tk.Entry(window, textvariable=benefit_var)

    cost_label = tk.Label(window, text="costo:")
    cost_entry = tk.Entry(window, textvariable=cost_var)

    rate_label = tk.Label(window, text="tasa de interés:")
    rate_entry = tk.Entry(window, textvariable=rate_var)

    years_label = tk.Label(window, text="años:")
    years_entry = tk.Entry(window, textvariable=years_var)

    evaluate_button = tk.Button(window, text="Evaluar", command=evaluate_project)

    investment_label.pack()
    investment_entry.pack()
    benefit_label.pack()
    benefit_entry.pack()
    cost_label.pack()
    cost_entry.pack()
    rate_label.pack()
    rate_entry.pack()
    years_label.pack()
    years_entry.pack()
    evaluate_button.pack()

    window.mainloop()


def forecast(VAN, TR, flags):
    statement = "\nEl proyecto es {} dado que los indicadores económicos evaluados {} con los criterios de rentabilidad necesario. A su vez, la duración para realizar el proyecto es de {} meses."

    if VAN < flags["VAN"]:
        messagebox.showinfo("Evaluación de Proyecto", statement.format("NO FACTIBLE", "NO CUMPLEN", TR))
    else:
        messagebox.showinfo("Evaluación de Proyecto", statement.format("FACTIBLE", "CUMPLEN", TR))


if __name__ == "__main__":
    eval_project()
