from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=1000)
    link = models.URLField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title

    

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title