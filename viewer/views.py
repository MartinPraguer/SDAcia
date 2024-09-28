from django.shortcuts import render
from viewer.models import ZnackyAut, TypKaroserie, Inzeraty

def index(request):
    return render(request, 'index.html', context={
        "inzeraty": Inzeraty.objects.order_by("-datum_pridani")[:5],
        "pocet_zobrazeni": Inzeraty.objects.order_by("-pocet_zobrazeni")[:5],

    })

def hledani(request):
    hledany_vyraz = request.GET.get('hledej', '')
    return render(request, 'hledani.html',
    context={"Inzeraty": Inzeraty.objects.filter(popis__icontains=hledany_vyraz)
})

