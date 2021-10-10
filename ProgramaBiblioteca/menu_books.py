#_*_ coding: utf8 _*_
from styles.menu_books_style import MenuBookEsthetic as Style
import styles.styles_utils as su
from database.books import Book
from database.authors import Author
from database.categories import Category


class MenuBook:

    def run(self):
        while True:
            option = Style().options()

            if option['option'] == Style().option_1:  # Read/Leer
                Book().read_books()

            elif option['option'] == Style().option_2:  # Create/Crear
                title = input(Style.title)

                Author().read_authors()
                authors_str = input(Style.authors_str).replace(" ", "").split(",")
                authors = [int(i) for i in authors_str]

                Category().read_categories()
                categories_str = input(Style.categories_str).replace(" ", "").split(",")
                categories = [int(i) for i in categories_str]

                Book().create_book(title, authors, categories)

                Book().read_books()
                print("       ↑")

            elif option['option'] == Style().option_3:  # Update/Actualizar
                Book().read_books()

                current_book_id = input(Style.current_book_id)
                new_book_title = input(Style.new_book_title)
                Book().update_title_book(current_book_id, new_book_title)

            elif option['option'] == Style().option_4:  # Delete/Eliminar
                Book().read_books()

                book_id = input(Style.book_id)
                Book().delete_book(book_id)

            elif option['option'] == Style().option_5:  # Volver al menu principal
                su.beep(times=2)
                break

            su.waiting_user()

if __name__ == '__main__':
    MenuBook().run()