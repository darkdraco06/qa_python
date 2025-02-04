import pytest
from main import BooksCollector


@pytest.mark.parametrize('book_1, book_2', [['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']])
@pytest.mark.parametrize('genre_1, genre_2', [['Ужасы', 'Комедии']])

class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def collector(self):
        return BooksCollector()

    # добавляем две книги
    def test_add_new_book_add_two_books(self, collector, book_1, book_2, genre_1, genre_2):


        collector.add_new_book(book_1)
        collector.add_new_book(book_2)
        assert len(collector.get_books_genre()) == 2

    # добавляем книгу с длинным именем
    def test_add_new_book_add_book_long_name(self, collector, book_1, book_2, genre_1, genre_2):

        collector.add_new_book('Когда не можешь придумать название, то пиши первое что приходит в голову, пусть даже и не в твою')
        assert len(collector.get_books_genre()) == 0

    # добавляем книгу без имени
    def test_add_new_book_bokk_not_name(self, collector, book_1, book_2, genre_1, genre_2):

        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    # добавляем две одинаковые книги
    def test_add_new_book_add_two_identical_book(self, collector, book_1, book_2, genre_1, genre_2):

        collector.add_new_book(book_1)
        collector.add_new_book(book_1)
        assert len(collector.get_books_genre()) == 1

    # Присваиваем книге жанр
    def test_set_book_genre_set_genre_by_name(self, collector, book_1, book_2, genre_1, genre_2):

        collector.add_new_book(book_1)
        collector.set_book_genre(book_1, genre_1)
        assert collector.get_book_genre(book_1) == genre_1

    # получаем жанр книги по имени
    def test_get_book_genre_get_genre_by_name(self, collector, book_1, book_2, genre_1, genre_2):
        collector.add_new_book(book_1)
        collector.add_new_book(book_2)
        collector.set_book_genre(book_1, genre_1)
        collector.set_book_genre(book_2, genre_2)
        assert collector.get_book_genre(book_1) == genre_1
        assert collector.get_book_genre(book_2) == genre_2

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_get_all_books_by_genre(self, collector, book_1, book_2, genre_1, genre_2):
        collector.add_new_book(book_1)
        collector.add_new_book(book_2)
        collector.set_book_genre(book_1, genre_1)
        collector.set_book_genre(book_2, genre_2)
        assert book_1 in collector.get_books_with_specific_genre(genre_1) and book_2 in collector.get_books_with_specific_genre(genre_2)

    # получаем список книг с жанрами
    def test_get_books_genre_compare_two_dictionaries(self, collector, book_1, book_2, genre_1, genre_2):
        collector.add_new_book(book_1)
        collector.add_new_book(book_2)
        collector.set_book_genre(book_1, genre_1)
        collector.set_book_genre(book_2, genre_2)
        result = {book_1: genre_1, book_2: genre_2}
        assert collector.get_books_genre() == result

    # получаем список книг для детей
    def test_get_books_for_children_get_list_children_books(self, collector, book_1, book_2, genre_1, genre_2):
        collector.add_new_book(book_2)
        collector.set_book_genre(book_2, genre_2)
        assert book_2 in collector.get_books_for_children()

    # добавляем книги в избарнное
    def test_add_book_in_favorites_add_new_book_in_favorites(self, collector, book_1, book_2, genre_1, genre_2):
        collector.add_new_book(book_1)
        collector.set_book_genre(book_1, genre_1)
        collector.add_book_in_favorites(book_1)
        assert len(collector.get_list_of_favorites_books()) == 1

    # удаляем книги из избранного
    def test_delete_book_from_favorites_delete_book(self, collector, book_1, book_2, genre_1, genre_2):
        collector.add_new_book(book_1)
        collector.add_new_book(book_2)
        collector.set_book_genre(book_1, genre_1)
        collector.set_book_genre(book_2, genre_2)
        collector.add_book_in_favorites(book_1)
        collector.add_book_in_favorites(book_2)
        collector.delete_book_from_favorites(book_1)
        assert len(collector.get_list_of_favorites_books()) == 1

    # получаем список избранных книг
    def test_get_list_of_favorites_books_compare_two_dictionaries(self, collector, book_1, book_2, genre_1, genre_2):
        collector.add_new_book(book_1)
        collector.add_new_book(book_2)
        collector.set_book_genre(book_1, genre_1)
        collector.set_book_genre(book_2, genre_2)
        collector.add_book_in_favorites(book_1)
        collector.add_book_in_favorites(book_2)
        result = [book_1, book_2]
        assert collector.get_list_of_favorites_books() == result