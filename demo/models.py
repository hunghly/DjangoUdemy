from django.db import models

# Create your models here.
class Book(models.Model):
    STATUS = (
        (0, 'Unknown'),
        (1, 'processed'),
        (2, 'paid')
    )
    GENRE = (
        ("AC", "Action"),
        ("FAN", "Fantasy"),
        ("NF", "Non-fiction"),
        ("FC", "Fiction")
    )
    FRIENDLY = (
       ("KF", "Kid-Friendly"),
       ("NKF", "Not-Kid-Friendly") 
    )
    title = models.CharField(max_length=36, null=True, unique=True)
    # Sets the genre based on a list of options
    genre = models.CharField(max_length=50, choices=GENRE)
    # Sets the kid-friendly param to whether it's kid friendly or not
    kid_friendly = models.CharField(blank=True, max_length=50, choices=FRIENDLY)
    # Sets the status to a dropdown based on the choices above
    status = models.IntegerField(choices=STATUS, null=True)
    # Sets the description to a textfield with max length of 500 words, allows for it to be blank
    description = models.TextField(max_length=500, blank=True)
    # Sets the price to 0 by default, and sets the max decimal places to 2
    price = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    # Sets the published date
    published = models.DateField(blank=True, null=True)

    # Sets if the book is published
    is_book_published = models.BooleanField(default=False)
    
    # Sets the cover image
    cover = models.ImageField(upload_to="covers/", blank=True)