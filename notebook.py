class Note(object):#Note 클래스
    def __init__(self, contents = None):
        self.contents = contents

    def write_contnts(self, contents):
        self.contents = contents
    def remove_all(self):
        self.contents=""
    def __str__(self):
        return self.contents

class NoteBook(object):#Notebook 클래스
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes={}

    def add_note(self, note, page = 0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number = self.page_number + 1
            else:
                self.notes = {page:note}
                self.page_number = self.page_number + 1
        else:
            print("페이지가 모두 채워졌다.")

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않는다.")

    def get_number_of_pages(self):
        return len(self.notes.keys())

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notees.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않는다.")

    def get_number_of_pages(self):
        return len(self.notes.keys())
