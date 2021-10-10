#_*_ coding: utf8 _*_
import json
import styles.styles_utils as su


class Category:
    '''CRUD CATEGORIAS
       ---------------
        * C - Create
        * R - Read
        * U - Update
        * D - Delete

        Funciones:
        ----------
        * create_category(new_category)
        * read_categories()
        * update_category(current_category_id, new_category_name)
        * delete_category(category_id)
        '''

    def __init__(self):
        self.file_categories_db = './database/categories.json'

    def __load_category_db(self) -> list:
        '''Retorna el contenido del json'''

        with open(self.file_categories_db, 'r') as categories_db:
            return json.load(categories_db)

    def __dump_category_db(self, loaded_db: list) -> None:
        '''Reescribe el json con el nuevo contenido'''

        with open(self.file_categories_db, 'w') as categories_db:
            json.dump(loaded_db, categories_db, indent=4)

    def create_category(self, new_category: str) -> None:
        '''Create Category
           ------
            new_category: nombre de la categoria a agregar
            '''

        try:
            loaded_db = self.__load_category_db()

            new_id = loaded_db[-1]["ID"] + 1 

            loaded_db.remove(loaded_db[-1])

            loaded_db.append(
                {
                    "category_id": new_id,
                    "name": new_category.title()
                }
            )

            loaded_db.append(
                {
                    "ID": new_id
                }
            )

            self.__dump_category_db(loaded_db)

            su.successful_operation()
            su.waiting_user()

        except Exception as e:
            su.operation_failed(e)

    def read_categories(self) -> None:
        '''Read Categories
           ----
            Muestra todas las categorias de la base de datos.
           '''

        su.reading()

        for category in self.__load_category_db()[:-1]:
            print(f"[{category['category_id']}] - {category['name']}")

    def update_category(self, current_category_id: str, new_category_name: str) -> None:
        '''Update Category
           ------
            current_category_id: id de la categoria a actualizar

            new_category_name: nuevo nombre de la categoria
            '''

        try:
            loaded_db = self.__load_category_db()

            for category in loaded_db:
                if category['category_id'] == int(current_category_id):
                    category['name'] = new_category_name.title()

                    self.__dump_category_db(loaded_db)

                    su.successful_operation()
                    break
            else:
                print('La categoria no existe')

        except Exception as e:
            su.operation_failed(e)

    def delete_category(self, category_id: str) -> None:
        '''Delete Category
           ------
            category_id: id de la categoria a eliminar
            '''

        try:
            loaded_db = self.__load_category_db()

            # Busco la categoria a eliminar
            for category in loaded_db[:-1]:
                if category['category_id'] == int(category_id):
                    loaded_db.remove(category)

                    self.__dump_category_db(loaded_db)

                    # Elimino todas las relaciones de la categoria
                    with open("./database/books.json", "r") as loaded_book_db_r:
                        loaded_book_db = json.load(loaded_book_db_r)

                    for book in loaded_book_db[:-1]:
                        if int(category_id) in book['categories']:
                            book['categories'].remove(int(category_id))

                            with open("./database/books.json", 'w') as loaded_book_db_w:
                                json.dump(loaded_book_db,
                                          loaded_book_db_w, indent=4)

                    su.successful_operation()
                    break
            else:
                print('La categoria no existe')

        except Exception as e:
            su.operation_failed(e)
