from django.shortcuts import render, redirect

# per la ricerca
from django.db.models import Q

# per la paginazione
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger

from .models import prepared_terminology


def glossario(request):   

    query = request.GET.get('q') #q è variabile risultante dalla query del database
    # non sostuituirla col valore vuoto

    template = "glossario.html" #il template è sempre lo stesso

    all_entries = prepared_terminology.objects.all() #funziona lo stesso anche se dice Class 'glossary_entry' has no 'objects' memberpylint(no-member)

    # se la query è stata fatta
    if query:

        query = request.GET.get('q') #q è variabile risultante dalla query del database

        selected_entries = prepared_terminology.objects.filter(Q(Acronimo__icontains=query)|Q(Ambito_riferimento__icontains=query)|Q(Autore_definizione__icontains=query)|Q(Autore_documento_fonte__icontains=query)|Q(Data_inserimento_entry__icontains=query)|Q(Definizione__icontains=query)|Q(Host_documento_fonte__icontains=query)|Q(Id_statico_entry__icontains=query)|Q(Lemma__icontains=query)|Q(Posizione_definizione__icontains=query)|Q(Titolo_documento_fonte__icontains=query)|Q(Url_definizione__icontains=query)|Q(Url_documento_fonte__icontains=query))
        # Q(Acronimo__icontains=query dice quali sono i campi in cui cercare l'input specificato dall'utente

        # Pagination
        paginator = Paginator(selected_entries, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        selected_entries = paginator.get_page(page)

        # context = {'all_entries':selected_entries}
        #return render(request, template, context)
        # {'nome della variabile con cui sarà richiamato nel template':contenuto}
        return render(request, template, {'all_entries':selected_entries, 'query':query})

    # se non è stata fatta nessuna query
    else:

        # Pagination
        paginator = Paginator(all_entries, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        all_entries = paginator.get_page(page)

        return render(request, template, {'all_entries':all_entries, 'query':query})