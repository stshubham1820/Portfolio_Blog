from django.db import models

# Create your models here.

class About(models.Model):
    mychoice = (('High School','High School'),('Bac','Bachelour'),('Master','Master'))
    Tag_line = models.CharField(max_length=100,verbose_name='Tag Line')
    summary = models.CharField(max_length=250,verbose_name='Summary')
    birthday = models.DateField(null=True,blank=True,verbose_name='DOB')
    age = models.IntegerField(null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    degree = models.CharField(max_length=50,choices=mychoice,null=True,blank=True)
    phone = models.CharField(max_length=10,unique=True)
    email = models.EmailField(null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    freelance = models.BooleanField(default=True,blank=True)#checkbox--
    description = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.Tag_line
