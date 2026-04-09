from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self, filename: str) -> None:
        pass

    @abstractmethod
    def save(self) -> None:
        pass

    @abstractmethod
    def get_content(self) -> str:
        pass

class WordDocument(Document):
    def __init__(self):
        print("创建 Word 文档")

    def open(self, filename: str) -> None:
        print(f"打开文档: {filename}")

    def save(self) -> None:
        print("保存文档")

    def get_content(self) -> str:
        return "[Word 文档内容]"

class ExcelDocument(Document):
    def __init__(self):
        print("创建 Excel 文档")

    def open(self, filename: str) -> None:
        print(f"打开文档: {filename}")

    def save(self) -> None:
        print("保存文档")

    def get_content(self) -> str:
        return "[Excel 表格数据]"

class Application(ABC):
    def __init__(self):
        self._document = None

    def new_document(self):
        self._document = self.create_document()

    @abstractmethod
    def create_document(self) -> Document:
        pass

    def get_document(self):
        return self._document

class WordApplication(Application):
    def create_document(self) -> Document:
        return WordDocument()

class ExcelApplication(Application):
    def create_document(self) -> Document:
        return ExcelDocument()

def main():
    print("=== Word 应用程序 ===")
    word_app = WordApplication()
    word_app.new_document()
    doc = word_app.get_document()
    doc.open("年度报告.docx")
    print(f"Word 文档内容: {doc.get_content()}")
    doc.save()

    print("\n=== Excel 应用程序 ===")
    excel_app = ExcelApplication()
    excel_app.new_document()
    doc = excel_app.get_document()
    doc.open("销售数据.xlsx")
    print(f"Excel 文档内容: {doc.get_content()}")
    doc.save()

if __name__ == "__main__":
    main()
