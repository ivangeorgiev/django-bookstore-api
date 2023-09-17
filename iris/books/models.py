from django.db import models


class Author(models.Model):
    author_id = models.BigAutoField(primary_key=True)
    author_name = models.CharField(max_length=400)

    class Meta:
        db_table = "author"
        ordering = ["author_name", "author_id"]

    def __str__(self):
        return self.author_name


class Publisher(models.Model):
    publisher_id = models.BigAutoField(primary_key=True)
    publisher_name = models.CharField(max_length=400)

    class Meta:
        db_table = "publisher"
        ordering = ["publisher_name", "publisher_id"]

    def __str__(self):
        return self.publisher_name


class BookLanguage(models.Model):
    language_id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=8)
    language_name = models.CharField(max_length=50)

    class Meta:
        db_table = "book_language"
        ordering = ["language_name", "language_id"]

    def __str__(self):
        return self.language_name


class Book(models.Model):
    book_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=400)
    isbn13 = models.CharField(max_length=13)
    language = models.ForeignKey(BookLanguage, on_delete=models.RESTRICT)
    num_pages = models.IntegerField()
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, related_name="books", on_delete=models.RESTRICT)
    authors = models.ManyToManyField(Author, related_name="books", through="BookAuthor")

    class Meta:
        db_table = "book"
        ordering = ["title", "book_id"]

    def __str__(self):
        return self.title


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = "book_author"
