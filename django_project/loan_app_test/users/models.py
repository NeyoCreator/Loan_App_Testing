from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#model 1
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')

    #BE MORE DESCIPTIVE 
    def __str__(self):
        return f'{self.user.username} Profile'

    # def  save(self):
    #     super().save()

    #     img = Image.open(self.image.url)

    #     if img.height > 300 or img.width > 300 :
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image_path)


#model 2
class BankStatement(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', default=True)
    #docfile = models.FileField(upload_to='documents/%Y/%m/%d')