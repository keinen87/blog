from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify

class Profile(models.Model):
    # users => User
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to="avatar")
    phone = models.TextField()
    skype = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.user.first_name
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        
    def _get_age(self):
        return str(200)
    age = property(_get_age)

class Post(models.Model):
    slug = models.SlugField(blank=True)
    title = models.TextField()
    pub_date = models.DateField(default=timezone.now)
    short_desc = models.TextField()
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = str(self.id) + "-" + slugify(self.title)
        super().save(*args, **kwargs)

class PostProxy(Post):
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        self.title = self.title + "OK!"
        super().save(*args, **kwargs)
        


# table: profile
#         id (uniq)
#         name

# table: post
#         id (uniq)
#         profile_id (no uniq)
#         post_text

# profile(1), profile(2)
# post(1,2), post(2,2)
  
