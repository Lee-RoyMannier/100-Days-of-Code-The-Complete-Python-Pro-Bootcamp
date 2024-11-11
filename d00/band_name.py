def display_welcoming_msg():
    print("Welcome to the Band Name Generator")


def get_informations():
    city_name = input("What's the name of the city you grew up in?")
    animal_name = input("What§s your pet's name?")

    return city_name, animal_name


def band_name_generator(city_name, animal_name):
    return city_name + " " + animal_name


def main():
    display_welcoming_msg()
    city_name, animal_name = get_informations()
    band_name = band_name_generator(city_name, animal_name)
    print(f"Your band name could be {band_name}")


main()
