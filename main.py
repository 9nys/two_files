def write_to_file(user_input, filename):

    try:
        with open(filename, 'w') as file:
            file.write(user_input)
        print("Рядок успішно записано у файл", filename)
    except Exception as e:
        print("Сталася помилка при записі у файл:", str(e))


user_input = input("Введіть рядок для запису у файл: ")

filename = input("Введіть назву файлу для запису: ")

write_to_file(user_input, filename)
