from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Video(BaseModel):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')  # Videoni yuklash uchun fayl maydoni
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='videos')
    img = models.ImageField(upload_to='images/', default='default_video.jpg')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
