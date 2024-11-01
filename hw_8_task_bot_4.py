# Створюємо декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found. Enter an existing user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Please provide the correct number of arguments."
    return inner

# Створюємо словник для збереження контактів
contacts = {}

# Функція для додавання нового контакту
@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added with phone number '{phone}'."

# Функція для пошуку телефону за ім'ям
@input_error
def get_phone(args):
    name = args[0]
    return f"{name}: {contacts[name]}"

# Функція для відображення всіх контактів
@input_error
def show_all():
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

# Основна функція для обробки команд
def main():
    print("Hello! I'm your assistant. Enter a command.")
    while True:
        command = input("Enter a command: ").strip().lower()
        if command in ["exit", "close", "goodbye"]:
            print("Goodbye!")
            break
        elif command.startswith("add"):
            args = input("Enter the name and phone: ").split()
            print(add_contact(args))
        elif command == "phone":
            args = input("Enter the name: ").split()
            print(get_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Unknown command. Try 'add', 'phone', 'all', 'exit'.")

if __name__ == "__main__":
    main()
