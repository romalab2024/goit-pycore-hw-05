import sys
import re
from typing import List, Dict, Callable

# Функція для парсингу рядка лог-файлу
def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3].strip()
    }

# Функція для завантаження всіх логів з файлу
def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

# Функція для фільтрації логів за рівнем логування
def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return [log for log in logs if log["level"] == level.upper()]

# Функція для підрахунку записів за рівнями логування
def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts

# Функція для відображення підрахунку логів за рівнями у вигляді таблиці
def display_log_counts(counts: Dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

# Функція для виведення детальної інформації для певного рівня логування
def display_logs(logs: List[dict]):
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

# Основна функція для запуску скрипта
def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях до файлу логів> [рівень логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    # Підрахунок і відображення статистики за рівнями логування
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    # Якщо вказано рівень логування, виводимо детальні записи цього рівня
    if len(sys.argv) > 2:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        display_logs(filtered_logs)

if __name__ == "__main__":
    main()
