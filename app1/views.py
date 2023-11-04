from django.shortcuts import render
from .models import *


def hamma_futbolchilar(request):
    data = {
        'players': Player.objects.all().order_by('-qiymat')
    }
    return render(request, 'players.html', data)


def transfers(request):
    data = {
        'transfers': Transfer.objects.all().order_by('-mavsum')
    }
    return render(request, 'latest-transfers.html', data)


def clubs(request):
    data = {
        'clubs': Club.objects.all().order_by('nom')
    }
    return render(request, 'clubs.html', data)


def tryouts(request):
    return render(request, 'tryouts.html')


def about(request):
    return render(request, 'about.html')


def archive(request):
    seasons = []
    for i in Transfer.objects.all().values('mavsum').distinct():
        seasons.append((i['mavsum']))
    data = {
        'mavsumlar': seasons
    }
    return render(request, 'transfer-archive.html', data)


def mavsum_transferlari(request, son):
    data = {
        'transfers': Transfer.objects.filter(mavsum__startswith=son).order_by('-narx')
    }
    return render(request, '2017-18season.html', data)


def davlat_clublari(request, nom):
    data = {
        'clubs': Club.objects.filter(davlat=nom.capitalize())
    }
    return render(request, 'england.html', data)

def club_players(request, nom):
    data = {
        'players': Player.objects.filter(club__nom=nom).order_by('-qiymat')
    }
    return render(request, 'country-clubs.html', data)


def u20players(request):
    data = {
        'players': Player.objects.filter(yosh__lt=21).order_by('qiymat')
    }
    return render(request, 'U-20 players.html', data)


def stats(request):
    return render(request, 'stats.html')