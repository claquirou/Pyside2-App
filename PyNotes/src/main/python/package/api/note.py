import os
import json
from uuid import uuid4
from glob import glob

from package.api.constants import NOTE_DIR



def get_notes():
    notes = []

    NOTE_FILES = glob(os.path.join(NOTE_DIR, "*.json"))
    for fichier in NOTE_FILES:
        with open(fichier, "r") as f:
            note_data = json.load(f)
            note_uuid = os.path.splitext(os.path.basename(fichier))[0]
            note_title = note_data.get("title")
            note_content = note_data.get("content")
            note = Note(uuid=note_uuid, title=note_title, content=note_content)
            notes.append(note)

    return notes

class Note:
    def __init__(self, title="", content="", uuid=None):
        if uuid:
            self.uuid = uuid
        else:
            self.uuid = str(uuid4())

        self.title = title
        self.content = content

    def __repr__(self):
        return f"{self.title} ({self.uuid})"

    def __str__(self):
        return self.title

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, str):
            self._content = value
        else:
            raise TypeError("Valeur invalide (Besoin d'une chaine de caractère)")

    def delete(self):
        os.remove(self.path)
        if os.path.exists(self.path):
            return False
        return True

    def delete_path(self, title):
        NOTE_FILES = glob(os.path.join(NOTE_DIR, "*.json"))
        for fichier in NOTE_FILES:
            with open(fichier, "r") as f:
                note_data = json.load(f)
                note_title = note_data.get("title")

                if title == note_title:
                    os.remove(fichier)

    @property
    def path(self):
        return os.path.join(NOTE_DIR, self.uuid + ".json")

    def save(self):
        if not os.path.isdir(NOTE_DIR):
            os.makedirs(NOTE_DIR)

        data = {"title": self.title, "content": self.content}
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    notes = get_notes()
    print(notes)