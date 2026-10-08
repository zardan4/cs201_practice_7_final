"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"
SUBJECTS = {
    0: 'Математика',
    1: 'Python',
    2: 'English',
}

with open(INPUT_FILE, 'r') as f:
    next(f)

    subjects = {}
    best_student = {}

    for line in f:
        # students_total += 1
        cells = line.strip().split(',')

        name = cells[0]
        grades = [float(num) for num in cells[1:]]

        # додаємо до сумарної кількості оцінок
        for (i, g) in enumerate(grades):

            if i not in subjects:
                subjects[i] = {
                    'grades_total': 0,
                    'students_total': 0
                }

            subjects[i]['grades_total'] += g
            subjects[i]['students_total'] += 1

        # перевіряємо на найліпшого учня
        avg_grade = sum(grades) / len(grades) if len(grades) > 0 else 0

        # ініціалізація перших даних об'єкту
        if 'avg_grade' not in best_student or 'name' not in best_student:
            best_student['avg_grade'] = avg_grade
            best_student['name'] = name

        if best_student['avg_grade'] < avg_grade:
            best_student['avg_grade'] = avg_grade
            best_student['name'] = name

with open(OUTPUT_FILE, 'w') as f:
    f.write('Середній бал по класу:\n')

    # виведемо результати для кожного предмету
    for (i, name) in SUBJECTS.items():
        curr = subjects[i]

        f.write(f'{name}: {(curr['grades_total'] / curr['students_total']) if curr['students_total'] > 0 else 0:.1f}\n')

    # результат найліпшого студента
    f.write('\n')
    f.write(f'Найкращий студент: {best_student['name']}({best_student['avg_grade']})')

# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
