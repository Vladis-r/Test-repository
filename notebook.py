from marshmallow import fields, Schema


class Genre:
  def __init__(self, pk=None, code=None, title_ru=None):
    self.pk = pk
    self.code = code
    self.title_ru = title_ru


class GenreSchema(Schema):
  code = fields.Str()
  title_ru = fields.Str()



class Book:
    def __init__(self, pk=None, title=None, price=None, genre=None, pages=None):
        self.pk = pk
        self.title = title
        self.price = price
        self.genre = genre
        self.pages = pages

class BookSchema(Schema):
    title = fields.Str()
    price = fields.Int()
    genre = fields.Pluck(GenreSchema, "title_ru")
    pages = fields.Int()


genre_fiction = Genre(pk=1, code="ficton", title_ru="Художественное")
genre_it = Genre(pk=2, code="it", title_ru="Книги по IT")
genre_documentary = Genre(pk=2, code="documentary", title_ru="Документальное")

books = [
    Book(1, "Изучаем Python", 340, genre_it),
    Book(2, "Как я решил завести змей", 520, genre_fiction),
    Book(3, "Моя история в Google", 240, genre_documentary)
]

result = BookSchema(many=True).dump(books)
print(result)
# [
#   {
#      "title": ...,
#      "price": ...,
#      "pages": ...,
#      "genre": {
#        "code": ...,
#        "title_ru": ...,
#      }
#   },
# ...
# ]