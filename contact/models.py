from django.db import models
from django.utils import timezone

# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show(boolean),
# picture (image)
# owner(foreign key)

# class Category(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)


# class Owner(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    created_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    # id_category = models.ForeignKey(Category[id], on_delete=models.CASCADE)
    # id_owner = models.ForeignKey(Owner.id, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
