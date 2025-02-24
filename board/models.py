from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20)
    writer = models.CharField(max_length=20)
    content = models.TextField()
    regdate = models.DateTimeField(auto_now=True)
    file = models.FileField(null=True)
    read_count = models.IntegerField(default = 0)
    
    def __str__(self):
        return f"Board[id={self.id}, title={self.title}]"
    
    def increase_read_count(self):
        self.read_count +=1
        self.save()
        