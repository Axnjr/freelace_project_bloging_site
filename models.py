from django.db import models
from datetime import datetime , date
import uuid
import random
ist = datetime.now()
n = random.randint(0,3)


class Blog(models.Model):
    title = models.CharField(max_length=40,default='title')
    categories = models.ForeignKey("Categories",on_delete=models.RESTRICT)
    link_to_pic = models.URLField(max_length=200000,default="https://tesla-cdn.thron.com/delivery/public/image/tesla/538ac149-d103-4834-9d38-641d8ae447ef/bvlatuR/std/4096x2560/Homepage-Model-S-Desktop-LHD")
    published_on = models.DateTimeField(default=ist)
    description = models.TextField(max_length=256,default="Read complete blog here...")
    blog_one = models.TextField(max_length=5000 , default="<style> img {display : block ; margin-left : auto ; margin-right : auto ;}; p{padding-inline: 4rem;}</style>")
    blog_two = models.TextField(max_length=5000 , blank=True , default="okok")
    blog_three = models.TextField(max_length=5000 , blank=True , default="okokk")
    blog_four = models.TextField(max_length=5000 , blank=True , default="okokok")
    blog_five = models.TextField(max_length=5000 , blank=True , default="okokk")
    likes = models.IntegerField(blank=True,default=0)
    views = models.IntegerField(blank=True,default=0)
    def __str__(self):
        return self.title

class Categories(models.Model):
    name = models.TextField(max_length=40,default='first')
    link_to_category_pic = models.URLField(max_length=200000,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmjP9Xb5XCJjAM12I0BubMOr-ROYGmv7OOBg&usqp=CAU")
    def __str__(self):
        return self.name

class Mailing_list(models.Model):
    name = models.TextField(max_length=50)
    email = models.EmailField(max_length=500)
    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.TextField(max_length=60)
    Email_of_user_who_asked = models.EmailField(max_length=500)
    user = models.TextField(max_length=10)
    posted_on = models.DateTimeField(default=ist)
    def __str__(self):
        return self.question



       
    

