from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_valid_name(self):
        collector = BooksCollector()
        collector.add_new_book("Сияние")
        assert "Сияние" in collector.books_genre
        assert collector.books_genre["Сияние"] == ""

    @pytest.mark.parametrize(
        "book_name",
        [
            "a" * 41,
            "",
        ],
    )
    def test_add_new_book_invalid_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_set_book_genre_valid_genre(self):
        collector = BooksCollector()
        book_name = "Оно"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, "Ужасы")
        assert collector.get_book_genre(book_name) == "Ужасы"

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        book_name = "Мизери"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, "Романтика")
        assert collector.get_book_genre(book_name) == ""

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Тёмная башня")
        collector.set_book_genre("Тёмная башня", "Фантастика")
        collector.add_new_book("Зелёная миля")
        collector.set_book_genre("Зелёная миля", "Классика")
        result = collector.get_books_with_specific_genre("Фантастика")
        assert result == ["Тёмная башня"]

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Куджо")
        collector.set_book_genre("Куджо", "Мультфильмы")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        result = collector.get_books_for_children()
        assert "Куджо" in result
        assert "Оно" not in result

    def test_get_books_for_children_book_with_no_genre(self):
        collector = BooksCollector()
        book_name = "Книга без жанра"
        collector.add_new_book(book_name)
        result = collector.get_books_for_children()
        assert book_name not in result

    def test_get_books_for_children_all_books_have_adult_genres(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        result = collector.get_books_for_children()
        assert result == []

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = "Противостояние"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_no_duplicates_in_collection(self):
        collector = BooksCollector()
        book_name = "Воспламеняющая взглядом"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert list(collector.books_genre.keys()).count(book_name) == 1

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Тёмная башня")
        collector.set_book_genre("Тёмная башня", "Фантастика")
        expected = {"Тёмная башня": "Фантастика"}
        assert collector.get_books_genre() == expected
        empty_collector = BooksCollector()
        assert empty_collector.get_books_genre() == {}

    def test_get_book_genre(self):
        collector = BooksCollector()
        book_name = "Оно"
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ""
        collector.set_book_genre(book_name, "Ужасы")
        assert collector.get_book_genre(book_name) == "Ужасы"
        assert collector.get_book_genre("Неизвестная книга") is None

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
        collector.add_new_book("Противостояние")
        collector.add_book_in_favorites("Противостояние")
        assert "Противостояние" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book = "Противостояние"
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert book not in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites("Неизвестная книга")
        assert collector.get_list_of_favorites_books() == []
