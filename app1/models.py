from django.db import models

class Club(models.Model):
    nom = models.CharField(max_length=50)
    logo = models.ImageField()
    davlat = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Player(models.Model):
    ism = models.CharField(max_length=70)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    qiymat = models.PositiveSmallIntegerField()
    yosh = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ism

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    eski = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='sotuvlar')
    yangi = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='transferlar')
    taxmin_narx = models.PositiveSmallIntegerField()
    narx = models.PositiveSmallIntegerField()
    mavsum = models.CharField(max_length=10)

    def __str__(self):
        return self.player.ism
