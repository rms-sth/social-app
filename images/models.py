from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name= 'images_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True) #SEO Friendly ur
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)#index for query performance. Used while using filter, exclude or orderby

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)# Django creates imtermediatory join table using the primary keys of both models


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug]) # : =>colon specifies absolute path