from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Select, FileInput
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=30,blank=True)
    description = models.CharField(max_length=200,blank=True)
    keywords = models.CharField(max_length=200,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False,unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['title']
    def __str__(self):
        full_path=[self.title]
        k=self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return '-> '.join(full_path[::-1])

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200,blank=True)
    keywords = models.CharField(max_length=200,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    Yazar = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField()
    slug = models.SlugField(null=False,unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    comment = models.CharField(max_length=150)
    rate = models.IntegerField()
    status = models.CharField(max_length=10,choices=STATUS,blank=True,default='New')
    ip=models.CharField(max_length=20,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject','comment','rate']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields=['category','title','description','keywords','image','Yazar','price','amount','detail','slug']
        widgets ={
            'title': TextInput(attrs ={'class':'input','placeholder':'title'}),
            'keywords': TextInput(attrs={'class': 'input', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'input', 'placeholder': 'description'}),
            'Yazar': TextInput(attrs={'class': 'input', 'placeholder': 'Yazar'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
            'price': TextInput(attrs={'class': 'input', 'placeholder': 'price'}),
            'amount': TextInput(attrs={'class': 'input', 'placeholder': 'amount'}),
            'detail': CKEditorWidget(),

        }

class ProductImageForm(ModelForm):
    class Meta:
        model = Images
        fields = ['title','image']
