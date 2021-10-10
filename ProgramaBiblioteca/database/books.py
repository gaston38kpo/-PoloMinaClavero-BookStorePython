#_*_ coding: utf8 _*_
import json
import styles.styles_utils as su
from database.authors import Author
from database.categories import Category


class Book:
    '''CRUD AUTORES
       ------------
        * C - Create
        * R - Read
        * U - Update
        * D - Delete

        Funciones:
        ----------
        * ateBook(title, authors, categories)
        * read_books()
        * update_title_book(current_book_id, new_book_title)
        * deleteAuthor(book_id)
        '''

    def __init__(self):
        self.file_books_db = './database/books.json'

    def __load_book_db(self) -> list:
        '''Retorna el contenido del json'''

        with open(self.file_books_db, 'r') as books_db:
            return json.load(books_db)

    def __dump_book_db(self, loaded_db: list) -> None:
        '''Reescribe el json con el nuevo contenido'''

        with open(self.file_books_db, 'w') as books_db:
            json.dump(loaded_db, books_db, indent=4)

    def create_book(self, title: str, authors: list[int], categories: list[int]) -> None:
        '''Create
           ------
            title: titulo del libro
            authors: lista de autores
            categories: lista de categorias
            '''

        try:
            loaded_db = self.__load_book_db()

            new_id = loaded_db[-1]["ID"] + 1

            loaded_db.remove(loaded_db[-1])

            loaded_db.append(
                {
                    "book_id": new_id,
                    "title": title.title(),
                    "authors": authors,
                    "categories": categories
                }
            )

            loaded_db.append(
                {
                    "ID": new_id
                }
            )

            self.__dump_book_db(loaded_db)

            su.successful_operation()
            su.waiting_user()

        except Exception as e:
            su.operation_failed(e)

    def read_books(self) -> None:
        '''Read
           ----
            Muestra todos los libros de la base de datos.
           '''

        su.reading()

        for book in self.__load_book_db()[:-1]:

            print(f"\n[{book['book_id']}] - {book['title']}", end=' ')

            for id_author in book['authors']:
                for author in Author()._Author__load_author_db()[:-1]:
                    if author['author_id'] == id_author:
                        print(f" - {author['last_name']} {author['first_name']}", end='')

            print(" (", end='')

            for id_category in book['categories']:
                for category in Category()._Category__load_category_db()[:-1]:
                    if category['category_id'] == id_category:
                        print(f" {category['name']}", end='')

            print(" )", end='')

        print()

    def update_title_book(self, current_book_id: str, new_book_title: str) -> None:
        '''Update
           ------
            current_book_id: id del libro a actualizar
            new_book_title: nuevo titulo del libro
            '''

        try:
            loaded_db = self.__load_book_db()

            for book in loaded_db:
                if book['book_id'] == int(current_book_id):
                    book['title'] = new_book_title.title()

                    self.__dump_book_db(loaded_db)

                    su.successful_operation()
                    break
            else:
                print('El libro no existe')

        except Exception as e:
            su.operation_failed(e)

    def delete_book(self, book_id: str) -> None:
        '''Delete
           ------
            book_id: id del libro a eliminar
            '''

        try:
            loaded_db = self.__load_book_db()

            # Busco el autor a eliminar
            for book in loaded_db:
                if book['book_id'] == int(book_id):
                    loaded_db.remove(book)
                    self.__dump_book_db(loaded_db)

                    su.successful_operation()
                    break
            else:
                print('El libro no existe')

        except Exception as e:
            su.operation_failed(e)
