from datetime import datetime
import uuid


class Note:
    def __init__(
            self,
            note_id=str(uuid.uuid1())[0:3],
            title="текст",
            body="текст",
            date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    ):
        self.id = note_id
        self.title = title
        self.body = body
        self.date = date

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def set_id(self):
        self.id = str(uuid.uuid1())[0:3]

    def set_title(self, title):
        self.title = title

    def set_body(self, body):
        self.body = body

    def set_date(self):
        self.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(self):
        return f"{self.id};{self.title};{self.body};{self.date}"

    def map_note(self):
        return f"\nID: {self.id};\nНазвание: {self.title};\nОписание: {self.body};\nДата публикации: {self.date};"
