# Список рядків для запису у файл
lines = [
    "Це перший рядок.",
    "Це другий рядок.",
    "Це третій рядок.",
    "Це четвертий рядок.",
    "Це п'ятий рядок."
]


with open("practice.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")





# Відкриття файлу для запису (якщо файл не існує, він буде створений)
with open("practice.txt", "w") as file:
    # Запис кожного рядка в файл
    for line in lines:
        file.write(line + "\n")