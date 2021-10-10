#_*_ coding: utf8 _*_
from styles.menu_categories_style import MenuCategoryEsthetic as Style
import styles.styles_utils as su
from database.categories import Category


class MenuCategory:

    def run(self):

        while True:
            option = Style().options()

            if option['option'] == Style().option_1:  # Read/Leer
                Category().read_categories()

            elif option['option'] == Style().option_2:  # Create/Crear
                new_category = input(Style.new_category)
                Category().create_category(new_category)
                
                Category().read_categories()
                print("       ↑")

            elif option['option'] == Style().option_3:  # Update/Actualizar
                Category().read_categories()

                current_category_id = input(Style.current_category_id)
                new_category_name = input(Style.new_category_name)
                Category().update_category(current_category_id, new_category_name)

            elif option['option'] == Style().option_4:  # Delete/Eliminar
                Category().read_categories()

                category_id = input(Style.category_id)
                Category().delete_category(category_id)

            elif option['option'] == Style().option_5:  # Volver al menu principal
                su.beep(times=2)
                break

            su.waiting_user()

if __name__ == '__main__':
    MenuCategory().run()