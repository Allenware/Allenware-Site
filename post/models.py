
from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=32)
    content = models.TextField(max_length=200)
    picture = models.ImageField(upload_to='image')
    status = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'
        ordering = ['-pub_date']

    def __str__(self):
        prefix = self.author + " 's post: "
        content = self.content[:10] + '....' if len(self.content) > 10 else self.content
        return prefix + content


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=32)
    content = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
        ordering = ['post_id', '-pub_date']

    def __str__(self):
        prefix = self.author + " reply: "
        content = self.content[:10] + '....' if len(self.content) > 10 else self.content
        return prefix + content
