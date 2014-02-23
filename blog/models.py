from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date posted')
    num_comments = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost)
    author = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date posted')

    def __unicode__(self):
        return self.text

# tags
# no users
