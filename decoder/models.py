from django.db import models

# Create your models here.
class MorseMapping(models.Model) :
    morse_code = models.CharField(max_length=10, unique=True)
    character = models.CharField(max_length=1, unique=True)

    def __str__(self) :
        return f"{self.morse_code} -> {self.character}"

    class Meta :
        ordering = ['character']
        verbose_name = "Morse Mapping"
        verbose_name_plural = "Morse Mappings"