from django.db import models


# Create your models here.


class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    # to return search content not the object
    def __str__(self):
        return '{}'.format(self.search)

    # to rename searchs
    class Meta:
        verbose_name_plural = 'Searches'

