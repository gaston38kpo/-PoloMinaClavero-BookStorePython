#_*_ coding: utf8 _*_
from main_menu import MainMenu
from database import db

if __name__ == '__main__':
    try:
        import inquirer
        
    except ImportError:
        print('(!)Por favor instale el paquete "inquirer"(!)\n\n>>> CMD:\n> pip install inquirer <<<\n\n')
        input('Presione ENTER para salir...')
        exit()
    db.Database()    
    MainMenu().run() 

