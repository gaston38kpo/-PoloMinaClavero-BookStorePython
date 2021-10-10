#_*_ coding: utf8 _*_
import json
import styles.styles_utils as su

class Author:
    '''CRUD AUTORES
       ------------
        * C - Create
        * R - Read
        * U - Update
        * D - Delete

        Funciones:
        ----------
        * create_author(last_name, first_name)
        * read_authors()
        * update_author(current_author_id, new_author_last_name, new_author_first_name)
        * delete_author(last_name, first_name)
        '''

    def __init__(self):
        self.file_authors_db = './database/authors.json'

    def __load_author_db(self) -> list:
        '''Retorna el contenido del json'''

        with open(self.file_authors_db, 'r') as authors_db:
            return json.load(authors_db)

    def __dump_author_db(self, loaded_db: list) -> None:
        '''Reescribe el json con el nuevo contenido'''

        with open(self.file_authors_db, 'w') as authors_db:
            json.dump(loaded_db, authors_db, indent=4)

    def create_author(self, last_name: str, first_name: str) -> None:
        '''Create Author
           ------
            last_name: apellido
            first_name: nombre / nombres
            '''

        try:
            loaded_db = self.__load_author_db()

            new_id = loaded_db[-1]["ID"] + 1

            loaded_db.remove(loaded_db[-1])

            loaded_db.append(
                {
                    "author_id": new_id,
                    "last_name": last_name.title(),
                    "first_name": first_name.title()
                }
            )

            loaded_db.append(
                {
                    "ID": new_id
                }
            )

            self.__dump_author_db(loaded_db)

            su.successful_operation()
            su.waiting_user()

        except Exception as e:
            su.operation_failed(e)

    def read_authors(self) -> None:
        '''Read Authors
           ----
            Muestra todos los autores de la base de datos.
           '''

        su.reading()

        for author in self.__load_author_db()[:-1]:
            print(
                f"[{author['author_id']}] {author['last_name']} {author['first_name']}")

    def update_author(self, current_author_id: str, new_author_last_name: str, new_author_first_name: str) -> None:
        '''Update Author
           ------
            current_author_id: id del autor a actualizar
            new_author_last_name: nuevo apellido del autor
            new_author_first_name: nuevo nombre del autor
            '''

        try:
            loaded_db = self.__load_author_db()

            for author in loaded_db:
                if author['author_id'] == int(current_author_id):
                    author['last_name'] = new_author_last_name.title()
                    author['first_name'] = new_author_first_name.title()

                    self.__dump_author_db(loaded_db)

                    su.successful_operation()
                    break
            else:
                print('El autor no existe')

        except Exception as e:
            su.operation_failed(e)

    def delete_author(self, author_id: str) -> None:
        '''Delete Author
           ------
            author_id: id del autor a eliminar
            '''

        try:
            loaded_db = self.__load_author_db()

            # Busco el autor a eliminar
            for author in loaded_db[:-1]:
                if int(author_id) == author['author_id']:
                    loaded_db.remove(author)

                    self.__dump_author_db(loaded_db)

                    # Elimino todas las relaciones de la categoria
                    with open("./database/books.json", "r") as loaded_book_db_r:
                        loaded_book_db = json.load(loaded_book_db_r)

                    for book in loaded_book_db[:-1]:
                        if int(author_id) in book['authors']:
                            book['authors'].remove(int(author_id))

                            with open("./database/books.json", 'w') as loaded_book_db_w:
                                json.dump(loaded_book_db,
                                          loaded_book_db_w, indent=4)

                    su.successful_operation()
                    break

            else:
                print('El autor no existe')

        except Exception as e:
            su.operation_failed(e)
