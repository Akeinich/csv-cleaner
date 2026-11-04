import csv
from pathlib import Path
import shutil

def read_csv(file_path):
    rows = []

    base_dir = Path(__file__).resolve().parent
    csv_file = base_dir / file_path

    try:
        with open(csv_file, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []

    except PermissionError:
        print(f"Нет доступа к файлу {file_path}.")
        return []

    except UnicodeDecodeError:
        print(f"Не удалось прочитать {file_path}: проверьте кодировку файла.")
        return []

    return rows


def remove_empty_rows(rows):
    clear_rows = []
    for row in rows:
        if all(not value.strip() for value in row):
            continue
        clear_rows.append(row)
    return clear_rows


def remove_duplicates(rows):
    excl_rows = []
    for row in rows:
        if row not in excl_rows:
            excl_rows.append(row)
    return excl_rows


def validate_row(row):
    if len(row) != 3:
        return False
    
    name = row[0].strip()
    age = row[1].strip()
    city = row[2].strip()
    
    if not name:
        return False

    if not city:
        return False
    try:
        age = int(age)
    except ValueError:
        return False

    if age <= 0:
        return False
    
    return True


def validate_rows(rows):
    invalid_rows = []
    validated_rows = []
    for row in rows:
        if validate_row(row):
            validated_rows.append(row)
        else:
            invalid_rows.append(row)

    return validated_rows, invalid_rows

def backup_csv(file_path):
    base_dir = Path(__file__).resolve().parent
    csv_file = base_dir / file_path
    backup_file = base_dir / "data_backup.csv"

    try:
        shutil.copy2(csv_file, backup_file)

    except FileNotFoundError:
        print(f"Файл {file_path} не найден. Резервная копия не создана.")
        return None

    except PermissionError:
        print(f"Нет доступа к исходному файлу или папке для резервной копии.")
        return None

    except IsADirectoryError:
        print(f"Вместо файла указан путь к папке: {file_path}.")
        return None

    except OSError as error:
        print(f"Не удалось создать резервную копию: {error}")
        return None

    return backup_file

def save_csv(rows, file_path):
    base_dir = Path(__file__).resolve().parent
    csv_file = base_dir / file_path
    temp_file = csv_file.with_suffix(".tmp")
    saved = False
    try:
        with open(temp_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        temp_file.replace(csv_file)
        saved = True
        return True
    
    except PermissionError:
        print(f"Нет доступа для записи в файл {file_path}.")
        return False

    except IsADirectoryError:
        print(f"Указан путь к папке, а не к файлу: {file_path}.")
        return False

    except FileNotFoundError:
        print(f"Папка для файла {file_path} не найдена.")
        return False

    except OSError as error:
        print(f"Не удалось сохранить файл {file_path}: {error}")
        return False
    finally:
        if not saved and temp_file.exists():
            temp_file.unlink()

data = read_csv("data.csv")

if not data:
    print("Файл пустой или не удалось его прочитать.")
    exit()

header = data[0]
rows = data[1:]

if not rows:
    print("В CSV нет записей для обработки.")
    exit()

cleaned_data = remove_empty_rows(rows)
excl_data = remove_duplicates(cleaned_data)
valid_data, invalid_data = validate_rows(excl_data)
while True:   
    answer = input("Удалить некорректные строки? (да/нет): ").strip().lower()
    if answer in ["да", "нет"]:
        break
    else:
        print("Пожалуйста, введите 'да' или 'нет'.")

if answer.lower() == "да":
    final_data = valid_data
else:
    final_data = valid_data + invalid_data

print("Итоговые данные:")
for row in final_data:
    print(row)

if invalid_data:
    print("\nНайдены некорректные строки:")
    for row in invalid_data:
        print(row)

result = backup_csv("data.csv")
if result is None:
    print("Не удалось создать резервную копию. Работа программы остановлена.")
    exit()
print(f"Резервная копия создана: {result}")

saved = save_csv([header] + final_data, "cleaned_data.csv")
if not saved:
    print("Не удалось сохранить файл. Работа программы остановлена.")
    exit()
print("Файл успешно сохранён!")

