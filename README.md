# CSV Cleaner

**A Python tool for cleaning and validating CSV files.**

**Инструмент на Python для очистки и проверки CSV-файлов.**

---

## English

### Features

- Read CSV files using Python's built-in `csv` module.
- Remove completely empty rows.
- Remove duplicate rows.
- Validate records (name, age, city).
- Separate valid and invalid records.
- Create a backup of the original CSV file.
- Save cleaned data to a separate CSV file.
- Handle common file and permission errors.
- Includes automated unit tests.

### Requirements

- Python 3.9 or newer.
- No external libraries required.

### Project structure

```text
csv-cleaner/
├── csv_cleaner.py
├── test_csv_cleaner.py
├── .gitignore
└── README.md
```

### Input CSV format

The program expects three columns:

```csv
name,age,city
Alex,20,Moscow
Bob,25,Kazan
Charlie,19,Perm
```

### Usage

1. Clone the repository:

```bash
git clone https://github.com/Akeinich/csv-cleaner.git
```

2. Open the project directory:

```bash
cd csv-cleaner
```

3. Place your input file named `data.csv` in the project directory.

4. Run the program:

```bash
python csv_cleaner.py
```

The program creates:

- `data_backup.csv` — backup of the original file.
- `cleaned_data.csv` — processed CSV file.

### Running tests

```bash
python -m unittest test_csv_cleaner -v
```

### Technologies

- Python
- CSV
- pathlib
- shutil
- unittest

### Project status

Completed educational project. The application includes CSV processing, validation, error handling, backup creation, and automated tests.

---

## Русский

### Возможности

- Чтение CSV-файлов с помощью встроенного модуля `csv`.
- Удаление полностью пустых строк.
- Удаление дублирующихся записей.
- Проверка данных (имя, возраст, город).
- Разделение корректных и некорректных записей.
- Создание резервной копии исходного CSV-файла.
- Сохранение обработанных данных в отдельный CSV-файл.
- Обработка распространённых ошибок чтения и записи файлов.
- Автоматизированные модульные тесты.

### Требования

- Python версии 3.9 или новее.
- Дополнительные библиотеки не требуются.

### Структура проекта

```text
csv-cleaner/
├── csv_cleaner.py
├── test_csv_cleaner.py
├── .gitignore
└── README.md
```

### Формат входного CSV-файла

Программа ожидает три столбца:

```csv
name,age,city
Alex,20,Moscow
Bob,25,Kazan
Charlie,19,Perm
```

Где:
- `name` — имя;
- `age` — возраст;
- `city` — город.

### Установка и запуск

1. Склонируйте репозиторий:

```bash
git clone https://github.com/Akeinich/csv-cleaner.git
```

2. Перейдите в папку проекта:

```bash
cd csv-cleaner
```

3. Поместите исходный файл с названием `data.csv` в папку проекта.

4. Запустите программу:

```bash
python csv_cleaner.py
```

После выполнения программа создаст:

- `data_backup.csv` — резервную копию исходного файла.
- `cleaned_data.csv` — файл с обработанными данными.

### Запуск тестов

Для запуска всех автоматизированных тестов выполните:

```bash
python -m unittest test_csv_cleaner -v
```

### Используемые технологии

- Python
- CSV
- pathlib
- shutil
- unittest

### Статус проекта

Завершённый учебный проект. Реализованы обработка CSV-файлов, проверка данных, обработка ошибок, создание резервных копий и автоматизированное тестирование.