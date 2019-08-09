from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
#전시회는 문여닫 시간
#공연은 러닝타임
#장소(지도), 기간, 제목, 시간, 가격, 전화번호, 티켓링크 

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):

        return self.category
    
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title= models.CharField(max_length=300)
    date=models.CharField(max_length=300)
    time=models.CharField(max_length=300)
    tel=models.CharField(max_length=300)
    place1=models.CharField(max_length=300)
    place2=models.CharField(max_length=300)
    place_url=models.CharField(max_length=300)
    price=models.CharField(max_length=300)
    link=models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class Exhibition(models.Model):
    title= models.CharField(max_length=300)
    date=models.CharField(max_length=300)
    time=models.CharField(max_length=300)
    tel=models.CharField(max_length=300)
    place1=models.CharField(max_length=300)
    place2=models.CharField(max_length=300)
    place_url=models.CharField(max_length=300)
    price=models.CharField(max_length=300)
    link=models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Musical(models.Model):
    title= models.CharField(max_length=300)
    date=models.CharField(max_length=300)
    time=models.CharField(max_length=300)
    tel=models.CharField(max_length=300)
    place1=models.CharField(max_length=300)
    place2=models.CharField(max_length=300)
    place_url=models.CharField(max_length=300)
    price=models.CharField(max_length=300)
    link=models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    

class Concert(models.Model):
    title= models.CharField(max_length=300)
    date=models.CharField(max_length=300)
    time=models.CharField(max_length=300)
    tel=models.CharField(max_length=300)
    place1=models.CharField(max_length=300)
    place2=models.CharField(max_length=300)
    place_url=models.CharField(max_length=300)
    price=models.CharField(max_length=300)
    link=models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Classic(models.Model):
    title= models.CharField(max_length=300)
    date=models.CharField(max_length=300)
    time=models.CharField(max_length=300)
    tel=models.CharField(max_length=300)
    place1=models.CharField(max_length=300)
    place2=models.CharField(max_length=300)
    place_url=models.CharField(max_length=300)
    price=models.CharField(max_length=300)
    link=models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('show.Post', related_name='comments', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='likes')
    dislikes = models.ManyToManyField(User, related_name='dislikes')
    

    def __str__(self):
        return self.text

    @property
    def count_likes(self):
        return self.likes.count()