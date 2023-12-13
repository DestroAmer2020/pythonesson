class RandomBookGenerator:
    def generate_book(self):
        book_type = random.choice(["Scientific", "Fiction", "Manual"])
        title = "Random Book"
        author = "Anonymous"
        if book_type == "Scientific":
            builder = ScientificBookBuilder(book_type, title, author)
            builder.add_references(self.generate_random_content())
            builder.add_glossary(self.generate_random_content())
        elif book_type == "Fiction":
            builder = FictionBookBuilder(book_type, title, author)
            builder.add_characters(self.generate_random_content())
        else:
            builder = ManualBookBuilder(book_type, title, author)
            builder.add_image("random_image.jpg")
        director = BookDirector()
        director.construct(builder, self.generate_random_content())
        return builder.book
    def generate_random_content(self):
        # Логіка генерації рандомного контенту
        # Наприклад, генерація випадкових слів або фраз
        content = []
        for _ in range(random.randint(5, 20)):
            sentence = ' '.join(random.choice(words) for _ in range(random.randint(5, 15)))
            content.append(sentence)
        return content
# Приклад використання генератора
random_book_generator = RandomBookGenerator()
random_book = random_book_generator.generate_book()
print(random_book)