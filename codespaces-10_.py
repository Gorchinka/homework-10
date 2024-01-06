def create_pet_dictionary():
    pets = {}
    name = input("Введите имя питомца: ")
    type_of_pet = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    pets[name] = {
        'Вид питомца': type_of_pet,
        'Возраст питомца': age,
        'Имя владельца': owner_name
    }
    return pets

pets = create_pet_dictionary()

def get_info_as_string(pets):
    for name, pet_info in pets.items():
        age = pet_info['Возраст питомца']
        if age % 100 == 11 or age % 100 == 12 or age % 100 == 13 or age % 100 == 14:
            years_or_year = "года"
        elif age % 10 == 1:
            years_or_year = "год"
        else:
            years_or_year = "лет"
        print(f"Это {pet_info['Вид питомца']} по кличке \"{name}\". Возраст питомца: {age} {years_or_year}. Имя владельца: {pet_info['Имя владельца']}")

get_info_as_string(pets)