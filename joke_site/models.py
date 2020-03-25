from django.db import models

class Joke_catagory(models.Model):
    title=models.CharField(max_length=50)

    def  __str__ (self):
        return self.title

class joke(models.Model):
    joke_title=models.CharField(max_length=100,default='SOME STRING')
    joke=models.TextField()
    Writter=models.CharField(max_length=200)

    joke_catagory=models.ForeignKey(

        'Joke_catagory',
        on_delete =models.CASCADE
    )
    def __str__(self):
        return self.joke_title