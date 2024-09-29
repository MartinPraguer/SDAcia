
from viewer.models import ZnackyAut, TypKaroserie, Inzeraty, Komentare
from django.shortcuts import render, redirect
from django import forms
from django.db.models import Q
from viewer.models import ZnackyAut, TypKaroserie

def index(request):
    return render(request, template_name='index.html', context={
        "inzeraty": Inzeraty.objects.order_by("-datum_pridani")[:5],
        "pocet_zobrazeni": Inzeraty.objects.order_by("-pocet_zobrazeni")[:5],
        "nove_komentare": Komentare.objects.order_by("-datum_komentare").all()[:5]
    })

def hledani(request):
    hledany_vyraz = request.GET.get('hledej', '')
    hledany_vyraz_capitalized = hledany_vyraz.capitalize()
    return render(request, template_name='hledani.html', context={
        "inzeraty": Inzeraty.objects.filter(
            Q(popis__icontains=hledany_vyraz) | Q(znacka__znacka__icontains=hledany_vyraz_capitalized)
        )
    })


def podrobne_hledani(request):
    popis = request.GET.get('popis', '')
    znacka = request.GET.get('znacka', '')
    karoserie = request.GET.get('karoserie', '')
    vykon = request.GET.get('vykon', '')
    rok_vyroby_od = request.GET.get('rok_vyroby_od', '')
    rok_vyroby_do = request.GET.get('rok_vyroby_do', '')
    cena_od = request.GET.get('cena_od', '')
    cena_do = request.GET.get('cena_do', '')
    datum_pridani_od = request.GET.get('datum_pridani_od', '')
    datum_pridani_do = request.GET.get('datum_pridani_do', '')

    inzeraty = Inzeraty.objects.all()

    if popis:
        inzeraty = inzeraty.filter(popis__icontains=popis)
    if znacka:
        inzeraty = inzeraty.filter(znacka__znacka__icontains=znacka)
    if karoserie:
        inzeraty = inzeraty.filter(karoserie__karoserie__icontains=karoserie)
    if vykon:
        inzeraty = inzeraty.filter(vykon__icontains=vykon)
    if rok_vyroby_od:
        inzeraty = inzeraty.filter(rok_vyroby__gte=rok_vyroby_od)  # Rok výroby od
    if rok_vyroby_do:
        inzeraty = inzeraty.filter(rok_vyroby__lte=rok_vyroby_do)  # Rok výroby do
    if cena_od:
        inzeraty = inzeraty.filter(cena__gte=cena_od)
    if cena_do:
        inzeraty = inzeraty.filter(cena__lte=cena_do)
    if datum_pridani_od:
        inzeraty = inzeraty.filter(datum_pridani__date__gte=datum_pridani_od)  # Datum přidání od
    if datum_pridani_do:
        inzeraty = inzeraty.filter(datum_pridani__date__lte=datum_pridani_do)  # Datum přidání do

    znacky = ZnackyAut.objects.all()
    karoserie = TypKaroserie.objects.all()

    return render(request, template_name='podrobne_hledani.html', context={
        "inzeraty": inzeraty,
        "znacky": znacky,
        "karoserie": karoserie
    })

def inzeraty(request, pk):
    inzerat = Inzeraty.objects.get(pk=pk)
    inzerat.pocet_zobrazeni += 1
    inzerat.save()

    if request.method == 'POST':
        # Získat data z formuláře
        nick = request.POST.get('nick')
        text = request.POST.get('text')

        # Vytvořit a uložit nový komentář
        komentar = Komentare(
            nick=nick,
            text=text,
            inzeraty=inzerat
        )
        komentar.save()

        # Přesměrování na stejnou stránku, aby se zobrazil nový komentář
        return redirect('inzeraty', pk=inzerat.pk)

    return render(request, template_name='inzeraty.html', context={'inzerat': inzerat})


from django.shortcuts import render, redirect
from viewer.models import ZnackyAut, TypKaroserie, Inzeraty
from datetime import datetime

def pridat_inzerat(request):
    # Pokud je požadavek typu POST, zpracujeme data z formuláře
    if request.method == 'POST':
        popis = request.POST.get('popis')
        znacka_id = request.POST.get('znacka')
        karoserie_id = request.POST.get('karoserie')
        vykon = request.POST.get('vykon')
        rok_vyroby = request.POST.get('rok_vyroby')
        cena = request.POST.get('cena')

        # Vytvoření nového inzerátu a uložení do databáze
        inzerat = Inzeraty(
            popis=popis,
            znacka_id=znacka_id,
            karoserie_id=karoserie_id,
            vykon=vykon,
            rok_vyroby=rok_vyroby,
            cena=cena,
            datum_pridani=datetime.now()
        )
        inzerat.save()

        # Přesměrování zpět na hlavní stránku nebo kdekoliv je to potřeba
        return redirect('index')

    # Pokud je požadavek typu GET, zobrazíme formulář
    znacky = ZnackyAut.objects.all()
    karoserie = TypKaroserie.objects.all()

    return render(request, template_name='pridat_inzerat.html', context={
        'znacky': znacky,
        'karoserie': karoserie
    })

def inzeraty_list(request):
    inzeraty = Inzeraty.objects.all()  # Získání všech inzerátů
    return render(request, template_name='inzeraty_list.html', context={'inzeraty': inzeraty})