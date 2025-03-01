from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)

    def _str_(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Message from {self.name}"
    
    
class Project(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)  

    image = models.ImageField(upload_to='projects/',blank=True, null=True)

    def __str__(self):
        return self.name  