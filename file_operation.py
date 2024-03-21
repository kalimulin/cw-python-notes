import os
import Note


def write_file(array, mode):
    if os.path.isfile('notes.csv'):
        with open('notes.csv', mode) as file:
            for notes in array:
                file.write(Note.Note.to_string(notes))
                file.write('\n')
            file.close()

    else:
        print('Файл не найден')


def read_file():
    array = []
    try:
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        if len(notes) > 0:
            for n in notes:
                split_n = n.split(';')
                note = Note.Note(note_id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])
                array.append(note)
        else:
            print('Нет сохраненных заметок.')
    except OSError:
        print('Файл недоступен для чтения')
    finally:
        return array
