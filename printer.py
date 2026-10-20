from abc import ABC, abstractmethod
class Document(ABC):
    def __init__(self, title, text, ext, pages):
        self.title = title
        self.text = text
        self.ext = ext
        self.pages = pages
    @abstractmethod
    def print_document(self):
        pass

class WordDocument(Document):
    def print_document(self):
        print("Printing Word document")

class ExcellDocument(Document):
    def print_document(self):
        print("Printing Excel document")

class HtmlDocument(Document):
    def print_document(self):
        print("Printing HTML document")

class Printer:
    def __init__(self, model):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    def print_document(self, document):
        if isinstance(document, Document):
            print(f"Printer model: {self.model}")
            print(f"Document title: {document.title}")
            print(f"File extension: {document.ext}")
            print(f"Pages: {document.pages}")
            document.print_document()
            print("Document printed successfully")
        else:
            print("Error: Unsupported document")


def main():
    printer = Printer("HP LaserJet")
    word = WordDocument("Report", "Annual report text", ".docx", 4)
    excel = ExcellDocument("Sales", "Sales data", ".xlsx", 11)
    html = HtmlDocument("Website", "Website content", ".html", 17)
    print("Printer model:", printer.model)
    print()
    printer.print_document(word)
    print()
    printer.print_document(excel)
    print()
    printer.print_document(html)

if __name__ == "__main__":
    main()
