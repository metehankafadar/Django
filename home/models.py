from django.db import models

# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(blank=True,max_length=30)
    description = models.CharField(blank=True,max_length=200)
    keywords = models.CharField(blank=True,max_length=200)
    company = models.CharField(blank=True,max_length=150)
    address = models.CharField(blank=True,max_length=150)
    phone = models.CharField(blank=True,max_length=150)
    fax = models.CharField(blank=True,max_length=150)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=150)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    aboutus = models.TextField(blank=True)
    referances = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title