#_*_ coding: utf8 _*_
import inquirer
import styles.styles_utils as su
import styles.shell_colors as c


class MenuAuthorEsthetic:
    last_name = f"\n{c.green_b}Apellido del autor a agregar: {c.end}"
    first_name = f"\n{c.green_b}Nombre del autor a agregar: {c.end}"
    current_author_id = f"\n{c.green_b}ID del autor a actualizar: {c.end}"
    new_author_last_name = f"\n{c.green_b}Nuevo apellido del autor: {c.end}"
    new_author_first_name = f"\n{c.green_b}Nuevo nombre del autor: {c.end}"
    author_id = f"\n{c.green_b}Ingrese ID del autor a eliminar: {c.end}"

    def __init__(self):
        self.message = f"{c.cyan}Sistema de gestion de {c.underline}{c.bold}Autores{c.end}"
        self.option_1 = f'- {c.bg_blue_hi}{c.white_b} Listar Autores {c.end} {c.blue}<{c.end}'
        self.option_2 = f'- {c.bg_green}{c.white_b} Agregar Autor {c.end} {c.blue}<{c.end}'
        self.option_3 = f'- {c.bg_green}{c.white_b} Actualizar Autor {c.end} {c.blue}<{c.end}'
        self.option_4 = f'- {c.bg_red_hi}{c.white_b} Eliminar Autor {c.end} {c.blue}<{c.end}'
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