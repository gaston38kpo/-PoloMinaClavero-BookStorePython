# _*_ coding: utf8 _*_
import random
from time import sleep
import inquirer
import styles.shell_colors as c
import styles.styles_utils as su


class MainMenuEsthetic:
    def __init__(self):
        self.message = f"{c.cyan}Eh {c.underline}{self.get_random_nick()}!{c.end}{c.cyan} que vas a gestionar hoy?{c.end}"
        self.option_1 = f'- {c.bg_blue_hi}{c.white_b} Libros {c.end} {c.blue}<{c.end}'
        self.option_2 = f'- {c.bg_blue_hi}{c.white_b} Autores {c.end} {c.blue}<{c.end}'
        self.option_3 = f'- {c.bg_blue_hi}{c.white_b} Categorias {c.end} {c.blue}<{c.end}'
        self.option_4 = f'- {c.bg_green}{c.white_b} Respaldar Datos {c.end} {c.blue}<{c.end}'
        self.option_5 = f'- {c.bg_green}{c.white_b} Restaurar Datos {c.end} {c.blue}<{c.end}'
        self.option_6 = f'- {c.bg_red_hi}{c.white_b} Eliminar Datos TODOS! {c.end} {c.blue}<{c.end}'
        self.option_7 = f'- {c.bg_white_hi}{c.red_i} SALIR! {c.end} {c.blue}<{c.end}'

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
                              self.option_5,
                              self.option_6,
                              self.option_7
                          ],
                          carousel=True
                          )
        ]
        return inquirer.prompt(menu_options)

    def get_random_nick(self):
        nicks = ['adamantium', 'animal', 'artista', 'bestia', 'brontosaurio', 'caimán', 'campeón', 'canallita', 'capitán', 
        'caza de combate', 'champion', 'chulazo', 'ciclón', 'coloso', 'coronel', 'crack', 'depredador', 'elemento', 'espectro', 
        'fenómeno', 'fiera', 'figura', 'furia', 'gacela', 'genio', 'gigante', 'godzilla', 'golfo', 'goliat', 'hacha', 'helicóptero', 
        'héroe', 'jefe', 'johnny bravo', 'killer', 'king kong', 'león', 'lobezno', 'maestro','maquina', 'maquinola', 'mastodonte', 
        'mole', 'monster truck', 'mostrenco', 'mostro', 'ninja', 'numero 1', 'paladin', 'pieza', 'prenda', 'presa', 'canario', 
        'referente', 'robocop', 'samurai', 'semental', 'socio', 'superman', 'tanque', 'terminator', 'terremoto', 'tifón', 'tigre', 
        'tiranosaurio', 'titán', 'torero', 'tornado', 'toro', 'tsunami', 'valiente', 'vaquero', 'velociraptor', 'vikingo', 'vividor', 
        'willyrex', 'zeus', 'ídolo']

        return random.choice(nicks).title()

    def goodbye(self):
        su.delay_print(f"\n{c.reverse}Adiós crack!{c.end}\n", delay=.1, sound=True)
        sleep(1)
        exit()
