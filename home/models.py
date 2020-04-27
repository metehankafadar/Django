from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from django.forms import ModelForm, Textarea, TextInput


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
    aboutus = RichTextUploadingField(blank=True)
    referances = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactFormMessage(models.Model):
    STATUS=(
        ('New','New'),
        ('Read','Read'),
    )
    name =models.CharField(blank=True,max_length=50)
    email=models.CharField(blank=True,max_length=50)
    subject=models.CharField(blank=True,max_length=50)
    message=models.CharField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip=models.CharField(blank=True,max_length=20)
    note=models.CharField(blank=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactFormu(ModelForm):
    class Meta:
        model=ContactFormMessage
        fields = ['name','email','subject','message']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','placeholder':'Name & Surname','required':"required"}),
            'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'subject','required':"required"}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Adress','required':"required"}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message','rows':'10' ,'required':"required"}),
        }