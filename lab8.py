'''
1 часть – написать программу в соответствии со своим вариантом задания. Составьте все различные дроби из чисел 3, 5, 7, 11, 13, 17.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
Выбираем пары дробей из первой части задания, у которых сумма числителей и знаменателей четная. Целевая функция: сумма числителя и знаменателя максимальна по модулю 5. 
вариант 21
Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной реализации (л.р. №7) разработать реализацию с использованием графического интерфейса. Допускается использовать любую графическую библиотеку питона.
Рекомендуется использовать внутреннюю библиотеку питона tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.
Никонова Дарья ИСТбд-21
'''
from fractions import Fraction
import tkinter as tk


def calculate_max_sum():
    fractions = set()
    numbers = [3, 5, 7, 11, 13, 17]
    
    # Получение количества пар дробей, указанных пользователем
    num_pairs = int(input_entry.get())
    
    # Генерация всех дробей и добавление их во множество fractions
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            fractions.add(Fraction(numbers[i], numbers[j]))
            fractions.add(Fraction(numbers[j], numbers[i]))
            fractions.add(Fraction(numbers[i], numbers[i]))
            fractions.add(Fraction(numbers[j], numbers[j]))

    max_fractions = []
    max_sum = 0

    # Итерация по всем возможным комбинациям дробей из fractions
    fractions_list = list(fractions)
    for i in range(len(fractions_list)):
        for j in range(i+1, len(fractions_list)):
            a = fractions_list[i]
            b = fractions_list[j]
            a_num, a_den = a.as_integer_ratio()
            b_num, b_den = b.as_integer_ratio()
            if ((a_num + b_num) % 2 == 0) and ((a_den + b_den) % 2 == 0):
                num_sum = int(str(a_num+b_num)[-1]) + int(str(a_den+b_den)[-1])
                if num_sum % 5 == 0:
                    if abs(num_sum) > abs(max_sum):
                        max_sum = num_sum
                        max_fractions = [(a, b)]
                    elif abs(num_sum) == abs(max_sum):
                        max_fractions.append((a, b))
                # Если количество найденных пар дробей достигло указанного числа, прекратить поиск
                if len(max_fractions) == num_pairs:
                    break
            
        if len(max_fractions) == num_pairs:
            break

    # Вывод результатов
    max_sum_label.config(text=f"Максимальная сумма по модулю 5: {max_sum}")
    fractions_output.delete(1.0, tk.END)
    for fraction_pair in max_fractions:
        fractions_output.insert(tk.END, f"{fraction_pair[0]} | {fraction_pair[1]}\n")

# Создание главного окна
root = tk.Tk()
root.title('Lab 8')
root.geometry("400x300")
root.resizable(False, False)

# Создание окна ввода
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

input_label = tk.Label(input_frame, text="Введите количество пар дробей (Всего 64):")
input_label.pack(side=tk.LEFT)

input_entry = tk.Entry(input_frame)
input_entry.pack(side=tk.LEFT)
input_entry.focus()

# Создание окна вывода максимальной суммы
max_sum_frame = tk.Frame(root)
max_sum_frame.pack(pady=10)

max_sum_label = tk.Label(max_sum_frame, text="Максимальная сумма по модулю 5: ")
max_sum_label.pack()

# Создание текстового поля для вывода дробей
fractions_output = tk.Text(root, height=10)
fractions_output.pack()

# Создание кнопки для расчета
calculate_button = tk.Button(root, text="Рассчитать", command=calculate_max_sum)
calculate_button.pack(pady=5)

root.mainloop()
