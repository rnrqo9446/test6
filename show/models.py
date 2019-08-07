from django.db import models
from django.utils import timezone
# Create your models here.
#전시회는 문여닫 시간
#공연은 러닝타임
#장소(지도), 기간, 제목, 시간, 가격, 전화번호, 티켓링크 


class Exhibition(models.Model):
    title= models.CharField(max_length=300)
    date=models.CharField(max_length=300)
    time=models.CharField(max_length=300)
    tel=models.CharField(max_length=300)
    place1=models.CharField(max_length=300)
    place2=models.CharField(max_length=300)
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
    price=models.CharField(max_length=300)
    link=models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
