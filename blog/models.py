from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='author', blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=212)  # 255
    content = models.TextField()
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='comments', blank=True, null=True)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=212)
    content = models.TextField()
    image = models.ImageField(upload_to='team')

    def __str__(self):
        return self.title


class Clients(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='clients')
    profession = models.CharField(max_length=212)
    content = models.TextField()

    def __str__(self):
        return self.name