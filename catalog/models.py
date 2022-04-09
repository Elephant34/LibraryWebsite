import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    """Model representing a book genre
    """

    name = models.CharField(
        max_length=256,
        help_text="Enter a book genre (e.g. Action, Biology, Fantasy, Sci-Fi)"
    )

    def __str__(self):
        """String representation of the genre
        """

        return self.name

class Series(models.Model):
    """Model representing book series
    """
    class Meta:
        verbose_name_plural = "series"

    name = models.CharField(
        max_length=512,
        help_text="Enter the series name"
    )

    def get_absolute_url(self):
        """Returns the url to book detail page
        """

        return reverse('series-detail', args=[str(self.id)])

    def __str__(self):
        """String representation of the series name
        """

        return self.name


class Author(models.Model):
    """Model representing an author
    """
    
    class Meta:
        ordering = ["last_name", "first_name"] # Will sort by surname first then first name

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    
    def get_absolute_url(self):
        """Returns the url to view specific author instance
        """

        return reverse("author-detail", args=[str(self.id)])
    
    def __str__(self):
        """String representation of the author
        """

        return f"{self.last_name}, {self.first_name}"

class Book(models.Model):
    """Model representing a general book but not a specific copy of said book
    """

    class Meta:
        ordering = ["series", "series_volume_number"]


    title = models.CharField(max_length=512)

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True
    )

    summary = models.TextField(
        max_length=1000,
        help_text="Enter a short description of the book"
    )
    genre = models.ManyToManyField(
        Genre,
        help_text="Pick an appropriate genre for the book"
    )

    series = models.ForeignKey(
        Series,
        help_text="Enter the series this book belongs to- or leave blank",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    series_volume_number = models.PositiveIntegerField(
        help_text="Enter the number in the series this book falls- or leave blank",
        null=True,
        blank=True
    )

    isbn = models.CharField(
        'ISBN',
        max_length=13,
        unique=True,
        help_text='13 Character <a href="https://isbnsearch.org">ISBN number</a>'
    )

    def get_absolute_url(self):
        """Returns the url to book detail page
        """

        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """String representation of the book
        """

        return self.title

class BookInstance(models.Model):
    """A specific instance of a book- allows for multiple copies of the same book to exist
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique identifier of the book across all locations",
        editable=False,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.RESTRICT
    )


    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )
    current_holder = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    
    def __str__(self):
        """String representation of the specific book
        """

        return f'({self.id}) {self.book.title}'
