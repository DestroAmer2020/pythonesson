# Основні класи
class PageRegistry:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PageRegistry, cls).__new__(cls)
            cls._instance.pages = set()
        return cls._instance
    def add_page(self, page_id):
        self.pages.add(page_id)
class BookBuilder:
    def __init__(self, book_type, title, author):
        self.book = {"type": book_type, "title": title, "author": author}
        self.page_registry = PageRegistry()
    def add_page(self, content):
        page_id = len(self.page_registry.pages) + 1
        self.page_registry.add_page(page_id)
        self.book[page_id] = content
    def set_format(self, format_type):
        self.book["format"] = format_type
class ScientificBookBuilder(BookBuilder):
    def add_references(self, references):
        self.add_page({"references": references})
    def add_glossary(self, glossary):
        self.add_page({"glossary": glossary})
class FictionBookBuilder(BookBuilder):
    def add_characters(self, characters):
        self.add_page({"characters": characters})
class ManualBookBuilder(BookBuilder):
    def add_image(self, image):
        self.add_page({"image": image})
class BookDirector:
    def construct(self, builder, content):
        builder.add_page(content)
        builder.set_format("PDF")
# Основний код
scientific_builder = ScientificBookBuilder("Scientific", "The Science Book", "John Scientist")
scientific_builder.add_references("1. Scientific Reference 1\n2. Scientific Reference 2")
scientific_builder.add_glossary("1. Glossary Term 1\n2. Glossary Term 2")
fiction_builder = FictionBookBuilder("Fiction", "The Novel", "Jane Author")
fiction_builder.add_characters("1. Protagonist - The Hero\n2. Antagonist - The Villain")
manual_builder = ManualBookBuilder("Manual", "The Manual", "Manual Author")
manual_builder.add_image("manual_image.jpg")
director = BookDirector()
# Генерація книг
scientific_book = scientific_builder.book
fiction_book = fiction_builder.book
manual_book = manual_builder.book
# Виведення книг
print(scientific_book)
print(fiction_book)
print(manual_book)