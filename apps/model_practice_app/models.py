# Inside models.py
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Blog object: {} {}>".format(self.name, self.desc)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # Notice the association made with ForeignKey for a one-to-many relationship
    # There can be many comments to one blog
    blog = models.ForeignKey(Blog, related_name = "comments")
    def __repr__(self):
        return "<Blog object: {} {}>".format(self.name, self.desc)

class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    blogs = models.ManyToManyField(Blog, related_name = "admins")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Blog object: {} {}>".format(self.name, self.desc)


# SET 2 ONE TO MANY
# class Author(models.Model):
    # name = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # def __repr__(self):
        # return "<Blog object: {} {}>".format(self.name, self.desc)
# 
# class Book(models.Model):
    # title = models.CharField(max_length=255)
    # author = models.ForeignKey(Author, related_name="books")
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # def __repr__(self):
        # return "<Blog object: {} {}>".format(self.name, self.desc)

# USERS ASSIGNMENT
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Blog object: {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.age)

# USERS ASSIGNMENT AnSWERS
# Know how to retrieve all users.
# User.objects.all()

# Know how to get the last user.
# User.objects.last()

# Create a few records in the users
# User.objects.create(first_name="Ted", last_name="Tedderson", email="ted@gmail.com", age=35)

# Know how to get the first user.
# User.objects.first()

# Know how to get the users sorted by their first name (order by first_name DESC)
# User.objects.order_by("first_name")

# Get the record of the user whose id is 3 and UPDATE the person's last_name to something else.
# the_user = User.objects.get(id=3)
# the_user.last_name = "Tammy"
# the_user.save()

# Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).
# User.objects.get(id=2).delete()

# DOJOS NINJAS ONE TO MANY
class Dojo(models.Model):
    name = models.CharField(max_length =255)
    city = models.CharField(max_length =255)
    state = models.CharField(max_length =255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Dojo object: {} {} {}>".format(self.name, self.city, self.state)

class Ninja(models.Model):
    first_name = models.CharField(max_length =255)
    last_name = models.CharField(max_length =255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Ninja object: {} {} {}>".format(self.first_name, self.last_name, self.dojo)

# DOJOS NINJAS ANSWERS
# Create 3 dojos
# Dojo.objects.create(name="hipster dojo", city="seattle", state="wa") X3

# Create 3 ninjas that belong to the first dojo you created.
# the dojo = Dojo.objects.get(id=1)
# Ninja.objects.create(first_name="ninja", last_name="uno", dojo=the_dojo)

# Create 3 more ninjas and have them belong to the second dojo you created.
# the dojo = Dojo.objects.get(id=2)
# Ninja.objects.create(first_name="ninja", last_name="uno", dojo=the_dojo)

# Create 3 more ninjas and have them belong to the third dojo you created.
# the dojo = Dojo.objects.get(id=3)
# Ninja.objects.create(first_name="ninja", last_name="uno", dojo=the_dojo)

# Be able to retrieve all ninjas that belong to the first Dojo
#Dojo.objects.first().ninjas.all()

# Be able to retrieve all ninjas that belong to the last Dojo
#Dojo.objects.last().ninjas.all()

# Ninja.objects.first().dojo
# Displays the first ninja objects related Dojo

## BOOKS/AUTHORS MANY TO MANY

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Book object: {} {}>".format(self.name, self.desc)

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Author object: {} {} {}>".format(self.first_name, self.last_name, self.email, self.books)

## BOOKS/AUTHORS ANSWERS

# Change the name of the 5th book to C#
    # the_book = Book.objects.get(id=5)
    # the_book.name = "C#"
    # the_book.save()

# Change the first_name of the 5th author to Ketul
    # the_author = Author.objects.get(id=5)
    # the_author.first_name = "Ketul"
    # the_author.save()

# Assign the first author to the first 2 books
    # the_author = Author.objects.first()
    # the_book1 = Book.objects.get(id=1)
    # the_book2 = Book.objects.get(id=2)
    # the_author.books.add(the_book1, the_book2)

# Assign the second author to the first 3 books
    # the_author = Author.objects.get(id=2)
    # the_book1 = Book.objects.get(id=1)
    # the_book2 = Book.objects.get(id=2)
    # the_book3 = Book.objects.get(id=3)
    # the_author.books.add(the_book1, the_book2, the_book3)

# Assign the third author to the first 4 books
    # the_author = Author.objects.get(id=3)
    # the_book1 = Book.objects.get(id=1)
    # the_book2 = Book.objects.get(id=2)
    # the_book3 = Book.objects.get(id=3)
    # the_book4 = Book.objects.get(id=4)
    # the_author.books.add(the_book1, the_book2, the_book3, the_book4)

# Assign the fourth author to the first 5 books (or in other words, all the books)
    # the_author = Author.objects.get(id=4)
    # the books = Book.objects.all()
    # for book in the_books:
    #   the_author.books.add(book)

# For the 3rd book, retrieve all the authors
    # the_book = Book.objects.get(id=3)
    # the_book.authors.all()

# For the 3rd book, remove the first author
    # the_author = Author.objects.get(id=1)
    # the_book = Book.objects.get(id=3)
    # the_book.authors.remove(the_author)

# For the 2nd book, add the 5th author as one of the authors
    # the_book = Book.objects.get(id=2)
    # the_author = Author.objects.get(id=5)
    # the_book.authors.add(the_author)

# Find all the books that the 3rd author is part of
    # the_author = Author.objects.get(id=3)
    # the_author.books.all()

# Find all the books that the 2nd author is part of
    # the_author = Author.objects.get(id=2)
    # the_author.books.all()

## LIKES/BOOKS

class User2(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<User2 object: {} {} {}>".format(self.first_name, self.last_name, self.email)

class Book2(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    uploader = models.ForeignKey(User2, related_name="uploaded_books")
    liked_users = models.ManyToManyField(User2, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Book2 object: {} {} {} {}>".format(self.name, self.desc, self.uploader, self.liked_users)

## LIKES/BOOKS ANSWERS

# Book.objects.first().uploader - this should return the user who uploaded the book
# 
# User.objects.first().uploaded_books - this should return all the books that are uploaded by the first user
# 
# Book.objects.first().liked_users - this should return all the users who liked the first book
# 
# User.objects.first().liked_books - this should return all the books that were liked by the first user
# 
# Create 3 different user accounts
#  User.objects.create(first_name="tom", last_name="thompson", email="tom@gmail.com")

# Have the first user create/upload 2 books.
#  the_user = User.objects.first()
#  Book.objects.create(name="The Expanse: Abadon's Gate", desc="Book 2", uploader=the_user)

# Have the second user create/upload 2 other books.
#  the_user = User.objects.get(id=2)
#  Book.objects.create

# Have the third user create/upload 2 other books.
#  the_user = User.objects.get(id=3)
#  Book.objects.create

# Have the first user like the last book and the first book
# the_user = User.objects.first()
# book1 = Book.objects.first()
# book2 = Book.objects.last()
# the_user.liked_books.add(book1, book2)

# Have the second user like the first book and the third book
# the_user = User2.objects.get(id=2)
# the_book = Book2.objects.first()
# the_book2 = Book2.objects.get(id=3)
# the_user.liked_books.add(the_book, thebook2)

# Have the third user like all books
# the_user = User.objects.get(id=3)
# the_book = Book.objects.all()
# for book in the_book:
#     the_user.liked_books.add(book)

# Display all users who like the first book
# the_book = Book.objects.first()
# the_book.liked_users.all()

# Display the user who uploaded the first book
# Book.objects.first().uploader

# Display all users who like the second book
# Book.objects.get(id=2).liked_users.all()

# Display the user who uploaded the second book
# Book.objects.get(id=2)uploader