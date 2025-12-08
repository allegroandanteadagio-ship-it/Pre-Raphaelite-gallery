from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя художника")
    birth_year = models.IntegerField(verbose_name="Год рождения")
    death_year = models.IntegerField(verbose_name="Год смерти", null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name="Страна", default="Великобритания")
    biography = models.TextField(verbose_name="Биография", blank=True)
    
    class Meta:
        verbose_name = "Художник"
        verbose_name_plural = "Художники"
    
    def __str__(self):
        return f"{self.name} ({self.birth_year}-{self.death_year if self.death_year else 'н.в.'})"

class Artwork(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="Художник")
    year = models.CharField(max_length=50, verbose_name="Год создания")
    dimensions = models.CharField(max_length=100, verbose_name="Размеры", blank=True)
    technique = models.CharField(max_length=100, verbose_name="Техника", default="Масло, холст")
    location = models.CharField(max_length=200, verbose_name="Местонахождение", default="Галерея Тейт, Лондон")
    description = models.TextField(verbose_name="Описание", blank=True)
    
    # ДОБАВЛЕННОЕ ПОЛЕ:
    image_url = models.URLField(verbose_name="Ссылка на изображение", blank=True, default="")
    
    class Meta:
        verbose_name = "Картина"
        verbose_name_plural = "Картины"
    
    def __str__(self):
        return f"{self.title} - {self.artist.name}"