#_*_ coding: utf8 _*_
from styles.menu_authors_style import MenuAuthorEsthetic as Style
import styles.styles_utils as su
from database.authors import Author


class MenuAuthor:

    def run(self):

        while True:
            option = Style().options()

            if option['option'] == Style().option_1:  # Read/Leer
                Author().read_authors()

            elif option['option'] == Style().option_2:  # Create/Crear
                last_name = input(Style.last_name)
                first_name = input(Style.first_name)
                Author().create_author(last_name, first_name)
                
                Author().read_authors()
                print("       ↑")


            elif option['option'] == Style().option_3:  # Update/Actualizar
                Author().read_authors()

                current_author_id = input(Style.current_author_id)
                new_author_last_name = input(Style.new_author_last_name)
                new_author_first_name = input(Style.new_author_first_name)
                Author().update_author(current_author_id, new_author_last_name, new_author_first_name)

            elif option['option'] == Style().option_4:  # Delete/Eliminar
                Author().read_authors()

                author_id = input(Style.author_id)
                Author().delete_author(author_id)

            elif option['option'] == Style().option_5:  # Volver al menu principal
                su.beep(times=2)
                break

            su.waiting_user()

if __name__ == '__main__':
    MenuAuthor().run()