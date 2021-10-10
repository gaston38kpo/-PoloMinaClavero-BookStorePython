# _*_ coding: utf8 _*_
import styles.styles_utils as su
from styles.menu_main_style import MainMenuEsthetic as Style

# Cada menu separado para garantizar su funcionamiento individual
from menu_books import MenuBook
from menu_authors import MenuAuthor
from menu_categories import MenuCategory
from database.db import Database


class MainMenu:            

    def run(self):

        while True:
            option = Style().options()

            if option['option'] == Style().option_1:  # Libros
                MenuBook().run()
            elif option['option'] == Style().option_2:  # Autores
                MenuAuthor().run()
            elif option['option'] == Style().option_3:  # Categorias
                MenuCategory().run()
            elif option['option'] == Style().option_4:  # Respaldar BDs
                Database().backup_now()
                su.waiting_user()
            elif option['option'] == Style().option_5:  # Restaurar BDs
                Database().restore_from_backup()
                su.waiting_user()
            elif option['option'] == Style().option_6:  # Eliminar BDs
                Database().remake_dbs()
                su.waiting_user()
            elif option['option'] == Style().option_7:  # Salir
                Style().goodbye()

if __name__ == '__main__':
    MainMenu().run()