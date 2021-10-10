# _*_ coding: utf8 _*_
import json
import os
import styles.styles_utils as su


class Database:
    def __init__(self):
        self.template_authors = [
            {
                "author_id": 1,
                "last_name": "Last_Name_Test",
                "first_name": "First_Name_Test"
            },
            {
                "ID": 1
            }
        ]

        self.template_categories = [
            {
                "category_id": 1,
                "name": "Category_Name_Test"
            },
            {
                "ID": 1
            }
        ]

        self.template_books = [
            {
                "book_id": 1,
                "title": "Book_Title_Test",
                "authors": [1],
                "categories": [1]
            },
            {
                "ID": 1
            }
        ]
        self.__create_db_if_not_exists()

    def __erase_dbs(self, db_name: str):
        '''Vuelve las bases de datos a cero'''

        with open(f'./database/{db_name}.json', 'w') as blank_db:
            if db_name == "authors":
                json.dump(self.template_authors, blank_db, indent=4)
            elif db_name == "categories":
                json.dump(self.template_categories, blank_db, indent=4)
            elif db_name == "books":
                json.dump(self.template_books, blank_db, indent=4)

    def __create_db_if_not_exists(self):
        '''Crea automaticamente las bases de datos si no las encuentra y
        las inicializa desde cero'''

        for db in ['authors', 'categories', 'books']:
            if not(os.path.exists(f'./database/{db}.json')):
                self.__erase_dbs(db)

    def __copy_db_from(self, db_name: str) -> None:
        '''Duplica los json'''

        with open(f'./database/{db_name}.json', 'r') as original_db:
            original_db = json.load(original_db)

        with open(f'./backupdb/{db_name}.json', 'w') as backup_db:
            json.dump(original_db, backup_db, indent=4)

    def __restore_db_from(self, db_name: str) -> None:
        '''Restaura los json'''

        with open(f'./backupdb/{db_name}.json', 'r') as backup_db:
            backup_db = json.load(backup_db)

        with open(f'./database/{db_name}.json', 'w') as original_db:
            json.dump(backup_db, original_db, indent=4)

    def backup_now(self):
        '''Respalda todos los datos actuales'''
        for db in ['authors', 'categories', 'books']:
            self.__copy_db_from(db)
        su.successful_operation()

    def remake_dbs(self):
        '''Vuelve las bases de datos a cero'''
        for db in ['authors', 'categories', 'books']:
            self.__erase_dbs(db)
        su.successful_operation()

    def restore_from_backup(self):
        '''Restaura todos los datos desde el backup'''
        for db in ['authors', 'categories', 'books']:
            self.__restore_db_from(db)
        su.successful_operation()
