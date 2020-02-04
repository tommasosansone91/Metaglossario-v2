from django.shortcuts import render, redirect

# per la ricerca
from django.db.models import Q

# per la paginazione
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger

# per il query wizard
import pandas as pd
import numpy as np



def metaglossario(request):
    
    # salva in variabile python ciò che il template mi indica come like_term, finisce anche nell'url
    # qui è vuoto
    like_term_query = request.GET.get('like_term')

    # senza  il comando LIKE
    Query_initial_string = "SELECT Lemmi.Thing, Acronimi.Thing, Definizioni.Thing, Titolo_documento_fonte.Thing, Url_documento_fonte.Thing FROM app_metaglossario_model_Things AS Url_documento_fonte INNER JOIN (app_metaglossario_model_is_Url_documento_fonte_of INNER JOIN ((((app_metaglossario_model_is_Lemma_of INNER JOIN ((app_metaglossario_model_Things AS Acronimi INNER JOIN app_metaglossario_model_is_Acronimo_of ON Acronimi.ID_Thing = app_metaglossario_model_is_Acronimo_of.ID_soggetto) INNER JOIN app_metaglossario_model_Things AS Lemmi ON app_metaglossario_model_is_Acronimo_of.ID_oggetto = Lemmi.ID_Thing) ON app_metaglossario_model_is_Lemma_of.ID_soggetto = Lemmi.ID_Thing) INNER JOIN app_metaglossario_model_Things AS Definizioni ON app_metaglossario_model_is_Lemma_of.ID_oggetto = Definizioni.ID_Thing) INNER JOIN app_metaglossario_model_is_Titolo_documento_fonte_of ON Definizioni.ID_Thing = app_metaglossario_model_is_Titolo_documento_fonte_of.ID_oggetto) INNER JOIN app_metaglossario_model_Things AS Titolo_documento_fonte ON app_metaglossario_model_is_Titolo_documento_fonte_of.ID_soggetto = Titolo_documento_fonte.ID_Thing) ON app_metaglossario_model_is_Url_documento_fonte_of.ID_oggetto = Titolo_documento_fonte.ID_Thing) ON Url_documento_fonte.ID_Thing = app_metaglossario_model_is_Url_documento_fonte_of.ID_soggetto ORDER BY Lemmi.Thing;"     
         # metto questa perchè è per dire che di default la stringa di query è quella senza like

    # backup stringa
    #  Query_initial_string = "SELECT Lemmi.Thing, Acronimi.Thing, Definizioni.Thing, Titolo_documento_fonte.Thing, Url_documento_fonte.Thing FROM app_metaglossario_model_Things AS Url_documento_fonte INNER JOIN (app_metaglossario_model_is_Url_documento_fonte_of INNER JOIN ((((app_metaglossario_model_is_Lemma_of INNER JOIN ((app_metaglossario_model_Things AS Acronimi INNER JOIN app_metaglossario_model_is_Acronimo_of ON Acronimi.ID_Thing = app_metaglossario_model_is_Acronimo_of.ID_soggetto) INNER JOIN app_metaglossario_model_Things AS Lemmi ON app_metaglossario_model_is_Acronimo_of.ID_oggetto = Lemmi.ID_Thing) ON app_metaglossario_model_is_Lemma_of.ID_soggetto = Lemmi.ID_Thing) INNER JOIN app_metaglossario_model_Things AS Definizioni ON app_metaglossario_model_is_Lemma_of.ID_oggetto = Definizioni.ID_Thing) INNER JOIN app_metaglossario_model_is_Titolo_documento_fonte_of ON Definizioni.ID_Thing = app_metaglossario_model_is_Titolo_documento_fonte_of.ID_oggetto) INNER JOIN app_metaglossario_model_Things AS Titolo_documento_fonte ON app_metaglossario_model_is_Titolo_documento_fonte_of.ID_soggetto = Titolo_documento_fonte.ID_Thing) ON app_metaglossario_model_is_Url_documento_fonte_of.ID_oggetto = Titolo_documento_fonte.ID_Thing) ON Url_documento_fonte.ID_Thing = app_metaglossario_model_is_Url_documento_fonte_of.ID_soggetto ORDER BY Lemmi.Thing;"     
    

    #da access a django sql puro

    #per evitare confilitti nel like cambia " con '"

    #cambia * con %

    # i nomi delle tabelle e delle relazioni protrebbero cambiare

    # ricerca in tutti i campi acq, metodo OR
    # Query_initial_string = "SELECT Lemmi.Thing, Acronimi.Thing, Definizioni.Thing FROM (app_metaglossario_model_is_Lemma_of INNER JOIN ((app_metaglossario_model_Things AS Acronimi INNER JOIN app_metaglossario_model_is_Acronimo_of ON Acronimi.ID_Thing = app_metaglossario_model_is_Acronimo_of.ID_soggetto) INNER JOIN app_metaglossario_model_Things AS Lemmi ON app_metaglossario_model_is_Acronimo_of.ID_oggetto = Lemmi.ID_Thing) ON app_metaglossario_model_is_Lemma_of.ID_soggetto = Lemmi.ID_Thing) INNER JOIN app_metaglossario_model_Things AS Definizioni ON app_metaglossario_model_is_Lemma_of.ID_oggetto = Definizioni.ID_Thing WHERE (((Lemmi.Thing) Like '%acq%') OR ((Acronimi.Thing) Like '%acq%') OR ((Definizioni.Thing) Like '%acq%')) ORDER BY Lemmi.Thing"

    # backup original string
    # Query_initial_string = "SELECT Lemmi.Thing, Acronimi.Thing, Definizioni.Thing FROM (app_metaglossario_model_is_Lemma_of INNER JOIN ((app_metaglossario_model_Things AS Acronimi INNER JOIN app_metaglossario_model_is_Acronimo_of ON Acronimi.ID_Thing = app_metaglossario_model_is_Acronimo_of.ID_soggetto) INNER JOIN app_metaglossario_model_Things AS Lemmi ON app_metaglossario_model_is_Acronimo_of.ID_oggetto = Lemmi.ID_Thing) ON app_metaglossario_model_is_Lemma_of.ID_soggetto = Lemmi.ID_Thing) INNER JOIN app_metaglossario_model_Things AS Definizioni ON app_metaglossario_model_is_Lemma_of.ID_oggetto = Definizioni.ID_Thing"

    
    template = "metaglossario.html" #il template è sempre lo stesso

    # no modello eprchè mi connetto diretto al db



    # se la query è stata fatta
    if like_term_query:
        
        like_term_query = request.GET.get('like_term')

        if "'" in like_term_query:

            like_term_query="Non inserire apostrofi! Query annullata."
            # non lo restituisce al template perchè c'è un javascript che 
            # copia e incolla il like_term e lo incolla negli hidden form

            
        

        # al posto di selected_entries

        # con il comando like con aggiunta dell'utente - solo termine like
        # l'element like_term è incatenato tra le % per usare il like con sql diretto
        Query_string = "SELECT Lemmi.Thing, Acronimi.Thing, Definizioni.Thing, Titolo_documento_fonte.Thing, Url_documento_fonte.Thing FROM app_metaglossario_model_Things AS Url_documento_fonte INNER JOIN (app_metaglossario_model_is_Url_documento_fonte_of INNER JOIN ((((app_metaglossario_model_is_Lemma_of INNER JOIN ((app_metaglossario_model_Things AS Acronimi INNER JOIN app_metaglossario_model_is_Acronimo_of ON Acronimi.ID_Thing = app_metaglossario_model_is_Acronimo_of.ID_soggetto) INNER JOIN app_metaglossario_model_Things AS Lemmi ON app_metaglossario_model_is_Acronimo_of.ID_oggetto = Lemmi.ID_Thing) ON app_metaglossario_model_is_Lemma_of.ID_soggetto = Lemmi.ID_Thing) INNER JOIN app_metaglossario_model_Things AS Definizioni ON app_metaglossario_model_is_Lemma_of.ID_oggetto = Definizioni.ID_Thing) INNER JOIN app_metaglossario_model_is_Titolo_documento_fonte_of ON Definizioni.ID_Thing = app_metaglossario_model_is_Titolo_documento_fonte_of.ID_oggetto) INNER JOIN app_metaglossario_model_Things AS Titolo_documento_fonte ON app_metaglossario_model_is_Titolo_documento_fonte_of.ID_soggetto = Titolo_documento_fonte.ID_Thing) ON app_metaglossario_model_is_Url_documento_fonte_of.ID_oggetto = Titolo_documento_fonte.ID_Thing) ON Url_documento_fonte.ID_Thing = app_metaglossario_model_is_Url_documento_fonte_of.ID_soggetto WHERE (( LOWER(Lemmi.Thing) Like LOWER('%" + like_term_query + "%') ) OR ( LOWER(Acronimi.Thing) Like LOWER('%" + like_term_query + "%')) OR ( LOWER(Definizioni.Thing) Like LOWER('%" + like_term_query + "%') ) OR ( LOWER(Titolo_documento_fonte.Thing) Like LOWER('%" + like_term_query + "%')) OR ( LOWER(Url_documento_fonte.Thing) Like LOWER('%" + like_term_query + "%') ) ) ORDER BY Lemmi.Thing;" 
        # backup stringa:
        #  Query_string = "SELECT Lemmi.Thing, Acronimi.Thing, Definizioni.Thing, Titolo_documento_fonte.Thing, Url_documento_fonte.Thing FROM app_metaglossario_model_Things AS Url_documento_fonte INNER JOIN (app_metaglossario_model_is_Url_documento_fonte_of INNER JOIN ((((app_metaglossario_model_is_Lemma_of INNER JOIN ((app_metaglossario_model_Things AS Acronimi INNER JOIN app_metaglossario_model_is_Acronimo_of ON Acronimi.ID_Thing = app_metaglossario_model_is_Acronimo_of.ID_soggetto) INNER JOIN app_metaglossario_model_Things AS Lemmi ON app_metaglossario_model_is_Acronimo_of.ID_oggetto = Lemmi.ID_Thing) ON app_metaglossario_model_is_Lemma_of.ID_soggetto = Lemmi.ID_Thing) INNER JOIN app_metaglossario_model_Things AS Definizioni ON app_metaglossario_model_is_Lemma_of.ID_oggetto = Definizioni.ID_Thing) INNER JOIN app_metaglossario_model_is_Titolo_documento_fonte_of ON Definizioni.ID_Thing = app_metaglossario_model_is_Titolo_documento_fonte_of.ID_oggetto) INNER JOIN app_metaglossario_model_Things AS Titolo_documento_fonte ON app_metaglossario_model_is_Titolo_documento_fonte_of.ID_soggetto = Titolo_documento_fonte.ID_Thing) ON app_metaglossario_model_is_Url_documento_fonte_of.ID_oggetto = Titolo_documento_fonte.ID_Thing) ON Url_documento_fonte.ID_Thing = app_metaglossario_model_is_Url_documento_fonte_of.ID_soggetto WHERE (( LOWER(Lemmi.Thing) Like LOWER('%" + like_term_query + "%') ) OR ( LOWER(Acronimi.Thing) Like LOWER('%" + like_term_query + "%')) OR ( LOWER(Definizioni.Thing) Like LOWER('%" + like_term_query + "%') ) OR ( LOWER(Titolo_documento_fonte.Thing) Like LOWER('%" + like_term_query + "%')) OR ( LOWER(Url_documento_fonte.Thing) Like LOWER('%" + like_term_query + "%') ) ) ORDER BY Lemmi.Thing;" 
        
    
    
    
    
    # se il termine like è stato lasciato vuoto
    else:

        # la query rimane quella dichiarata di default
        Query_string = Query_initial_string

    print("************************************************************")

    print("Query SQL acquisita: ")
    print(Query_string)

    #connessione al db

    

    import psycopg2 as pg2

    # questo poi come lo nascondo?

    # password 2 - .passwords.txt

    import os ###
    import django_heroku ###
    from decouple import config ###

    # per gestire user e password del database postgresql che cambiano ogni 24 ore sugli host
    import dj_database_url ###

    view_db_user = config("view_db_user")
    view_db_password = config("view_db_password")
    view_db_host = config("view_db_host")
    view_db_database = config("view_db_database")


    mydb = pg2.connect(user=view_db_user, password=view_db_password, host=view_db_host, database=view_db_database)


    #postgres://user:password@host:porta/database_name

    # query sul db
    my_cursor = mydb.cursor()
    my_cursor.execute(Query_string)

    query_result_list = my_cursor.fetchall()

    len_result_list = len(query_result_list) 
    
    

    #Parla alla console
    print("Query eseguita sul database con successo, %s risultati inviati al browser!" % len_result_list)

    print("************************************************************")

    # genera una tabella solo coi risultati da pubblicare

    # trasforma la lista di tuple in dataframe
    query_result_df = pd.DataFrame(query_result_list)

    #devo creare due dataframe, uno con things e uno con gli id da usare nel query wizard

    # seleziona dalla

    print("Risultati della query:")
    print(query_result_df)
    
    print("************************************************************")

    # trasforma il dataframe in una lista di liste
    query_result_lol = np.array(query_result_df)
    
    # trasforma il dataframe in una lista di tuple
    query_result_list = [tuple(sottolista) for sottolista in query_result_lol]
    

    # Pagination - funziona in questo punto ma se lo metti prima no
    paginator = Paginator(query_result_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    query_result_list = paginator.get_page(page) 


    #in questo dizionario stanno le variabili che le viste consegnano al template
    context_dict={'queryresult_key':query_result_list, 'len_result_list_key':len_result_list, 'like_term_query':like_term_query}

    return render(request, template, context_dict)