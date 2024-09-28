from django.db import models
from django.db.models import Model, DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField, TextField, PositiveIntegerField


class ZnackyAut(Model):
    znacka = CharField(max_length=128)

    def __str__(self):
        return self.znacka

class TypKaroserie(Model):
    karoserie = CharField(max_length=128)

    def __str__(self):
        return self.karoserie

class Inzeraty(Model):
    popis = CharField(max_length=128)
    znacka = ForeignKey(ZnackyAut, on_delete=DO_NOTHING)
    karoserie = ForeignKey(TypKaroserie, on_delete=DO_NOTHING)
    vykon = CharField(max_length=128)
    rok_vyroby = PositiveIntegerField(max_length=4)
    cena = PositiveIntegerField()
    datum_pridani = DateTimeField()
    pocet_zobrazeni = PositiveIntegerField(default=0)
    vytvoreno = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.popis} - {self.znacka} - {self.karoserie} - {self.rok_vyroby} - "










# rok_vyroby = PositiveIntegerField(
#         validators=[MinValueValidator(1900), MaxValueValidator(2024)],
#         help_text="Zadejte rok výroby mezi 1900 a 2024"