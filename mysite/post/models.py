from django.db import models
from django.contrib.auth.models import User


STSTUS = (
    (0,"Draft"),
    (1,"Publish")
    
)


class Post(models.Model):
    title      = models.CharField(max_length = 200,unique=True)
    slug       = models.SlugField(max_length=200,unique = True)
    author     = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts") 
    updated_on = models.DateTimeField(auto_now=True)
    created_on  = models.DateTimeField(auto_now_add=True)
    content    = models.TextField()
    status     = models.IntegerField(choices=STSTUS,default=0)
    
    class Meta:
        ordering = ['-created_on'] 
        
    def __str__(self):
        return self.title
     
     

class Comment(models.Model):
    post       = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name       = models.CharField(max_length = 60)
    email      = models.EmailField(blank =True,null=True)
    body       = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    active     = models.BooleanField(default=False)
    
    
    class Meta:
        ordering = ['-created_on']
        
    
    def __str__(self):
        return "نظر {} : {}".format(self.body,self.name)



class Book(models.Model):
    title =  models.CharField(max_length=70)
    pdf = models.FileField(upload_to='mahdi/')
    cover = models.ImageField(upload_to="mahdi/img/")
    
    
    
    
    
# model => learn django

class Usign(models.Model):
    title = models.CharField(max_length = 80)
    body = models.TextField()
    pictured =  models.ImageField(upload_to = "mahdi/img/learn/")
    
    


