from os import path
import sqlite3


def db_init_with_first_start():
    if path.exists('database\pastes.csv'):
        pass
    else:
        with open('database\pastes.csv', 'w') as file:
            writer = csv.writer(file, delimiter='~')
            writer.writerow(
                ['code', 'paste']
            )


def read_db() -> dict:
    """Читает базу данных и возвращает словарь с ключом по pcode"""
    data = {}
    with open('database\pastes.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter='~')
        for row in reader:
            data[row['code']] = [row['1'], row['2'], row['3'], row['4'],
                                 row['5'], row['6'], row['7'], row['8']]
    return data
