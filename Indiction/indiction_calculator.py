# -*- coding: utf-8 -*-
"""
Created on: 26.04.2025
Project: Indiction Calculator
"""

import tkinter as tk
from tkinter import ttk


class IndictionCalculator:
    """Калькулятор индиктовых дат."""
    CYCLE_LENGTH = 532  # 28 * 19
    EPOCH_OFFSET = 5508  # ЭСМ = 5508 + ГНЭ

    def to_indiction(self, year_ce):
        """Перевод года в индиктовую дату."""
        try:
            esm = self.EPOCH_OFFSET + year_ce
            ks = esm % 28 or 28  # КС
            kl = esm % 19 or 19  # КЛ
            ind = esm % 15 or 15  # Индикт
            return {"ЭСМ": esm, "КС": ks, "КЛ": kl, "Индикт": ind}
        except ValueError as e:
            return {"Ошибка": str(e)}

    def from_indiction(self, ks_target, kl_target, ind_target):
        """Перевод индиктовой даты в год."""
        try:
            for esm_candidate in range(1, 532 * 100):
                if (esm_candidate % 28 == ks_target % 28 and
                    esm_candidate % 19 == kl_target % 19 and
                    esm_candidate % 15 == ind_target % 15):
                    esm = esm_candidate
                    break
            else:
                return {"Ошибка": "Не удалось найти ЭСМ"}

            year_ce = esm - self.EPOCH_OFFSET
            return {"ЭСМ": esm, "Год нашей эры": year_ce}
        except ValueError as e:
            return {"Ошибка": str(e)}


# GUI
def create_gui():
    """Создание графического интерфейса."""
    calc = IndictionCalculator()

    root = tk.Tk()
    root.title("Индиктовый калькулятор для папани")
    root.geometry("500x500")
    root.configure(bg="#f4efe9")

    title = tk.Label(root,
                     text=("«Время идёт кругами."
                           " Но ты можешь знать, где находишься.»"),
                     font=("Times New Roman", 10, "bold", "italic"),
                     bg="#f4efe9", wraplength=480, pady=10)
    title.pack()

    notebook = ttk.Notebook(root)
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    notebook.add(frame1, text="Из года н.э.")
    notebook.add(frame2, text="Из индикта")
    notebook.pack(expand=True, fill="both", padx=10, pady=10)

    # Вкладка 1 — год → индикт
    def convert_to_indiction():
        """Перевод года в индиктовую дату."""
        try:
            year = int(entry_year.get())
            if year <= 0:
                raise ValueError("Введите положительный год")
            res = calc.to_indiction(year)
            result1.config(text=(
                f"ЭСМ: {res['ЭСМ']}\n"
                f"КС: {res['КС']}, КЛ: {res['КЛ']}, Индикт: {res['Индикт']}"))
        except ValueError as e:
            result1.config(text=f"Ошибка: {e}")

    tk.Label(frame1,
             text="Введите год нашей эры:",
             font=("Arial", 12)).pack(pady=5)
    entry_year = tk.Entry(frame1, font=("Arial", 12))
    entry_year.pack()
    btn1 = tk.Button(frame1, text="Перевести", command=convert_to_indiction)
    btn1.pack(pady=5)
    result1 = tk.Label(frame1, text="", font=("Arial", 12), fg="darkblue")
    result1.pack(pady=10)

    # Вкладка 2 — индикт → год
    def convert_from_indiction():
        """Перевод индиктовой даты в год."""
        try:
            ks = int(entry_ks.get())
            kl = int(entry_kl.get())
            ind = int(entry_ind.get())
            if (ks <= 0 or ks > 28 or
                    kl <= 0 or kl > 19 or
                    ind <= 0 or ind > 15):
                raise ValueError(
                    "Введите корректные значения для КС, КЛ, Индикта")
            res = calc.from_indiction(ks, kl, ind)
            if "Ошибка" in res:
                result2.config(text=f"Ошибка: {res['Ошибка']}")
            else:
                result2.config(text=(f"ЭСМ: {res['ЭСМ']}\n"
                                     f"Год нашей эры: {res['Год нашей эры']}"))
        except ValueError as e:
            result2.config(text=f"Ошибка: {e}")

    tk.Label(frame2, text="Круг Солнцу (КС):", font=("Arial", 12)).pack()
    entry_ks = tk.Entry(frame2, font=("Arial", 12))
    entry_ks.pack()
    tk.Label(frame2, text="Круг Луне (КЛ):", font=("Arial", 12)).pack()
    entry_kl = tk.Entry(frame2, font=("Arial", 12))
    entry_kl.pack()
    tk.Label(frame2, text="Индикт:", font=("Arial", 12)).pack()
    entry_ind = tk.Entry(frame2, font=("Arial", 12))
    entry_ind.pack()

    btn2 = tk.Button(frame2,
                     text="Вычислить год",
                     command=convert_from_indiction)
    btn2.pack(pady=5)
    result2 = tk.Label(frame2, text="", font=("Arial", 12), fg="darkgreen")
    result2.pack(pady=10)

    footer = tk.Label(root,
                      text="github.com/marteszibellina | © 2025 ",
                      font=("Arial", 8), bg="#f4efe9", pady=10)
    footer.pack(side="bottom")

    root.mainloop()


create_gui()
