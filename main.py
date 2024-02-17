import json
import datetime

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    try:
        with open("notes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def create_note_id(notes):
    if len(notes) == 0:
        return 1
    else:
        return max(notes, key=lambda x: x["id"])["id"] + 1

def create_note():
    notes = load_notes()
    note_id = create_note_id(notes)
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": note_id, "title": title, "body": body, "datetime": timestamp}
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно создана.")

def read_notes():
    notes = load_notes()
    if len(notes) == 0:
        print("\n")
        print("Список заметок пуст.")
        print("\n")
    else:
        for note in notes:
            print("\n")
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата/время создания: {note['datetime']}")
            print("\n")
            print()

def edit_note():
    notes = load_notes()
    if len(notes) == 0:
        print("\n")
        print("Список заметок пуст.")
        print("\n")
    else:
        note_id = int(input("Введите ID заметки для редактирования: "))
        for note in notes:
            if note["id"] == note_id:
                title = input("Введите новый заголовок заметки: ")
                body = input("Введите новый текст заметки: ")
                note["title"] = title
                note["body"] = body
                note["datetime"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_notes(notes)
                print("Заметка успешно отредактирована.")
                return
        print("\n")
        print("Заметка с данным ID не найдена.")
        print("\n")

def delete_note():
    notes = load_notes()
    if len(notes) == 0:
        print("\n")
        print("Список заметок пуст.")
        print("\n")
    else:
        note_id = int(input("Введите ID заметки для удаления: "))
        for note in notes:
            if note["id"] == note_id:
                notes.remove(note)
                save_notes(notes)
                print("Заметка успешно удалена.")
                return
        print("\n")
        print("Заметка с данным ID не найдена.")
        print("\n")

def main():
    while True:
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Введите номер команды: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите номер команды из списка.")

if __name__ == "__main__":
    main()
    