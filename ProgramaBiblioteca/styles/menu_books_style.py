#_*_ coding: utf8 _*_
import inquirer
import styles.styles_utils as su
import styles.shell_colors as c


class MenuBookEsthetic:
    title = f"\n{c.green_b}Titulo del libro a agregar: {c.end}"
    authors_str = f"\n{c.green_b}Indique por ID Autor/es (separados por coma): {c.end}"
    categories_str = f"\n{c.green_b}Indique por ID Categoria/s (separadas por coma): {c.end}"
    current_book_id = f"\n{c.green_b}ID del libro a actualizar: {c.end}"
    new_book_title = f"\n{c.green_b}Nuevo titulo del libro: {c.end}"
    book_id = f"\n{c.green_b}ID del libro a eliminar: {c.end}"

    def __init__(self):
        self.message = f"{c.cyan}Sistema de gestion de {c.underline}{c.bold}Libros{c.end}"
        self.option_1 = f'- {c.bg_blue_hi}{c.white_b} Listar Libros {c.end} {c.blue}<{c.end}'
        self.option_2 = f'- {c.bg_green}{c.white_b} Agregar Libro {c.end} {c.blue}<{c.end}'
        self.option_3 = f'- {c.bg_green}{c.white_b} Actualizar Libro {c.end} {c.blue}<{c.end}'
        self.option_4 = f'- {c.bg_red_hi}{c.white_b} Eliminar Libro {c.end} {c.blue}<{c.end}'
        self.option_5 = f'- {c.bg_white_hi}{c.red_i} VOLVER! {c.end} {c.blue}<{c.end}'

    def options(self):
        su.clean_console()
        menu_options = [
            inquirer.List('option',
                          message=self.message,
                          choices=[
                              self.option_1,
                              self.option_2,
                              self.option_3,
                              self.option_4,
                              self.option_5
                          ],
                          carousel=True
                          )
        ]

        return inquirer.prompt(menu_options)