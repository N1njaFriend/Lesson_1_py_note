from datetime import datetime
import json

class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp

# Создание новой заметки
def create_note(id, title, body):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return Note(id, title, body, timestamp)

# Сохранение заметок в файл
def save_notes(notes, filename):
    with open(filename, "w") as file:
        json.dump([note.__dict__ for note in notes], file)

# Загрузка заметок из файла
def load_notes(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            notes = [Note(**note_data) for note_data in data]
            return notes
    except FileNotFoundError:
        return []

# Редактирование заметки по идентификатору
def edit_note(notes, id, new_title, new_body):
    for note in notes:
        if note.id == id:
            note.title = new_title
            note.body = new_body
            note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
    return False

# Удаление заметки по идентификатору
def delete_note(notes, id):
    for note in notes.copy():
        if note.id == id:
            notes.remove(note)
            return True
    return False

# Пользовательский интерфейс
def main():
    filename = "notes.json"
    notes = load_notes(filename)

    while True:
        print("1. Создать заметку")
        print("2. Показать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            id = input("Введите идентификатор заметки: ")
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            note = create_note(id, title, body)
            notes.append(note)
            save_notes(notes, filename)
            print("Заметка успешно создана")

        elif choice == "2":
            for note in notes:
                print(f"Идентификатор: {note.id}")
                print(f"Заголовок: {note.title}")
                print(f"Текст: {note.body}")
                print(f"Дата/время: {note.timestamp}")
                print()

        elif choice == "3":
            id = input("Введите идентификатор заметки для редактирования: ")
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            if edit_note(notes, id, new_title, new_body):
                save_notes(notes, filename)
                print("Заметка успешно отредактирована")
            else:
                print("Заметка с указанным идентификатором не найдена")

        elif choice == "4":
            id = input("Введите идентификатор заметки для удаления: ")
            if delete_note(notes, id):
                save_notes(notes, filename)
                print("Заметка успешно удалена")
            else:
                print("Заметка с указанным идентификатором не найдена")

        elif choice == "5":
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()