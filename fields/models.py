from django.db import models

# Create your models here.
class Tag (models.Model):
    name = models.CharField(max_length=50,  unique=True)
    
    def __str__(self):
        return self.name

class Field(models.Model):
    id_md = models.AutoField(primary_key=True)
    title_md = models.CharField(max_length=50, null=False, blank=False)
    definition_md = models.TextField(null=False, blank=False)
    vocabulary_md = models.BooleanField(default=False)
    pragmatic_programmer_md = models.BooleanField(default=False)
    created_date_md = models.DateTimeField(auto_now_add = True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title_md} - {self.id_md}"

