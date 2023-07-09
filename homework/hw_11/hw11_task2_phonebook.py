# Task 2
# Extend Phonebook application
# Functionality of Phonebook application:
# Add new entries 
# Search by first name 
# Search by last name 
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
# The first argument to the application should be the name of the phonebook. Application should load JSON data, if it is present in the folder with application, else raise an error. After the user exits, all data should be saved to loaded JSON.

import json

def load_phonebook(phonebook_file):
    try:
        with open(phonebook_file) as file:
            phonebook_data = json.load(file)
        return phonebook_data
    except FileNotFoundError:
        raise Exception("Файл не знайдено")
    


def save_phonebook(phonebook_data, phonebook_file):
    with open(phonebook_file, 'w') as file:
        json.dump(phonebook_data, file, indent = 2) # indent=2 для людського вигляду файлу



def add_new_entries(phonebook_data):
    first_name = input("Введіть ім'я: ")
    last_name = input("Введіть прізвище: ")
    telephone_number = input("Введіть номер телефону: ")
    country = input("Введіть країну: ")
    city = input("Введіть місто: ")

    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "telephone_number": telephone_number,
        "country": country,
        "city": city
    }   
    phonebook_data.append(contact)
    print("Додавання пройшло успішно")  



# Search by first name
def search_by_first_name(phonebook_data):
    first_name = input("Введіть ім'я для пошуку: ")
    results = [contact for contact in phonebook_data if contact["first_name"] == first_name]
    if results:
        print("Результати пошуку:")
        for result in results:
            print_contact(result)
    else:
        print("Відповідних записів не знайдено")     



# Search by last name 
def search_by_last_name(phonebook_data):
    last_name = input("Введіть прізвище для пошуку: ")
    results = [contact for contact in phonebook_data if contact["last_name"] == last_name]
    if results:
        print("Результати пошуку:")
        for result in results:
            print_contact(result)
    else:
        print("Відповідних записів не знайдено")          



#Search by full name
def search_by_full_name(phonebook_data):
    full_name = input("Введіть повне ім'я для пошуку: ")
    results = [entry for entry in phonebook_data if (entry["first_name"] + " " + entry["last_name"]) == full_name]
    if results:
        print("Результати пошуку:")
        for result in results:
            print_contact(result)
        else:
            print("Відповідних записів не знайдено")    



#Search by telephone number
def search_by_telephone_number(phonebook_data):
    phone_number = input("Введіть номер телефону для пошуку: ")
    results = [contact for contact in phonebook_data if contact["phone_number"] == phone_number]
    if results:
        print("Результати пошуку:")
        for result in results:
            print_contact(result)
    else:
        print("Відповідних записів не знайдено") 



#Search by city or country
def search_by_city_or_country(phonebook_data):
    location = input("Введіть країну або місто для пошуку: ")
    results = [contact for contact in phonebook_data if (contact["city"] == location or contact["country"] == location)]
    if results:
        print("Результати пошуку:")
        for result in results:
            print_contact(result)
    else:
        print("Відповідних записів не знайдено") 



#Delete a record for a given telephone number 
def delete_record(phonebook_data):
    phone_number = input("Введіть номер телефону для видалення: ")
    contact_found = False
    for contact in phonebook_data:
        if contact["phone_number"] == phone_number:
            phonebook_data.remove(contact)
            contact_found = True
            break
    if contact_found:
        print("Запис успішно видалено")
    else:
        print("За вказаним номером телефону не знайдено жодного запису")      



#Update a record for a given telephone number
def update_record(phonebook_data):
    phone_number = input("Введіть номер телефону для оновлення: ")
    contact_found = False
    for contact in phonebook_data:
        if contact["phone_number"] == phone_number:
            contact["first_name"] = input("Введіть нове ім'я: ")
            contact["last_name"] = input("Введіть нове прізвище: ")
            contact["country"] = input("Введіть нову країну: ")
            contact["city"] = input("Введіть нове місто: ")
            contact_found = True
            break
    if contact_found:
        print("Запис успішно оновлено")
    else:
        print("За вказаним номером телефону не знайдено жодного запису")



# print 
def print_contact(contact):
    print("First Name:", contact["first_name"])
    print("Last Name:", contact["last_name"])
    print("Phone Number:", contact["phone_number"])
    print("Country:", contact["country"])
    print("City:", contact["city"])
    print()



def main(phonebook_file):
    phonebook_data = load_phonebook(phonebook_file)
    while True:
        print("Phonebook Application")
        print("1. Додати новий контакт")
        print("2. Знайти за іменем")
        print("3. Знайти за прізвищем")
        print("4. Знайти за повним іменем")
        print("5. Знайти за номером телефону")
        print("6. Знайти за країною або містом")
        print("7. Видалити запис за номером телефону")
        print("8. Оновити запис за номером телефону")
        print("9. Вийти")

        choice = input("Введіть свій вибір (1-9): ")
        if choice == "1":
            add_new_entries(phonebook_data)
        elif choice == "2":
            search_by_first_name(phonebook_data)
        elif choice == "3":
            search_by_last_name(phonebook_data)
        elif choice == "4":
            search_by_full_name(phonebook_data)
        elif choice == "5":
            search_by_telephone_number(phonebook_data)
        elif choice == "6":
            search_by_city_or_country(phonebook_data)
        elif choice == "7":
            delete_record(phonebook_data)
        elif choice == "8":
            update_record(phonebook_data)
        elif choice == "9":
            save_phonebook(phonebook_data, phonebook_file)
            print("Телефонну книгу збережено. Вихід із програми здійснено")
            break
        else:
            print("Невірний вибір. Будь ласка спробуйте ще раз")



if __name__ == '__main__':
    phonebook_file = 'phonebook.json' 
    main(phonebook_file)            