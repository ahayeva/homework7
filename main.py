import json
def add_to_json(data_animal):
    try:
        with open('animals.json', 'r') as file:
            data = json.load(file)
    except Exception as err:
        data= []
    data.append(data_animal)
    with open('data.json', 'w') as json_file:




if __name__ == "__main__":
    nick = input("введіть ім'я тварини: ")
    breed = input("введіть породу тварини: ")
    food = input("підберіть їжу для тварини")
    type = input("тип тварини")
    animal_frame = {
        "nick": "nick",
        "breed": "breed",
        "food": "food",
        "type": "type"
        add_to_json(data_animal)
    }
    add_to_json(data_animal)













# def sumNumbers(a, b):
#     return a + b
#
# def createIntials (name, last_name, fathers_name):
#     intitials = False
#     try:
#         intitials = f"{last_name.capitalize()} {name[0].upper()}. {fathers_name[0].upper()}."
#     except Exception as err:
#         print("сталась помилка")
#     return intitials
#
#
# def runProgram():
#     sumNumbers(1, 2)
#     print(createIntials("Anna", "Ahaieva","Pavlivna"))
#     if intitials:
#         print(intitials)
#     temperature = input("введіть температуру")
#     if temperature >0:
#         print("teplo")
#

#     active = True
#     while active:
#         try:
#             runProgram()
#         except Exception as err:
#             print(err)
#         finally:
#             ch = input("бажаєте продовжити користування (N | Y):")
#             if ch.lower() == "n":
#                 active = False

    # try:
        # num =int("test")
    #     print(num)
    # except Exception as err: #передбачення помилки
    #     try:
    #         print(err)
    #         print('')
    #
    # finally:
    #     print("Some text")