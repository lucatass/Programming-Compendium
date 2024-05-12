from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tag_name

class Field(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    definition = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add = True)
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name='fields')
    
    def __str__(self):
        return f"{self.title} - {self.id}"
    
