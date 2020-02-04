def algoritmo_PGI():

    print("Viene richiamato l'algoritmo PGI!")

    # algoritmo per standardizzare i dati prima di incatenarli nella struttura relazionale

    # questo algoritmo va ottimizzato mettendo i cicli delle etichette delle colonne al posto di richiamare ogni elemento del database con la propria etichetta

    import pandas as pd
    from app_metaglossario.models import acquired_terminology, prepared_terminology

    print("Inizia la standardizzazione del formato dei dati per prepararli all'inserimento nel database...")
    
    # samtlisci il algoritmo perchè vanno bene i Nan

    # database di prima elaborazione
    # ppure uso degli spazi virtuali, ossia le variabili, per ogni scrittura

    #  svuoto il database destinazione 

    prepared_terminology.objects.all().delete()

    # lista del vecchio modello
    acquired_rows = acquired_terminology.objects.all()

    print("Il modello prepared_terminology è stato svuotato!")

    print("Inizia lo riempimento del modello prepared_terminology...")

    # compilo il nuovo modello coi dati 

    for element in acquired_rows:

        prepared_entry = prepared_terminology.objects.create()
        
        if not pd.isnull(element.Lemma):
            prepared_entry.Lemma = element.Lemma

        if not pd.isnull(element.Acronimo):
            prepared_entry.Acronimo = element.Acronimo

        if not pd.isnull(element.Definizione):    
            prepared_entry.Definizione = element.Definizione

        if not pd.isnull(element.Ambito_riferimento):    
            prepared_entry.Ambito_riferimento = element.Ambito_riferimento

        if not pd.isnull(element.Autore_definizione):    
            prepared_entry.Autore_definizione = element.Autore_definizione

        if not pd.isnull(element.Posizione_definizione):    
            prepared_entry.Posizione_definizione = element.Posizione_definizione

        if not pd.isnull(element.Url_definizione):    
            prepared_entry.Url_definizione = element.Url_definizione

        if not pd.isnull(element.Titolo_documento_fonte):    
            prepared_entry.Titolo_documento_fonte = element.Titolo_documento_fonte

        if not pd.isnull(element.Autore_documento_fonte):    
            prepared_entry.Autore_documento_fonte = element.Autore_documento_fonte

        if not pd.isnull(element.Host_documento_fonte):    
            prepared_entry.Host_documento_fonte = element.Host_documento_fonte

        if not pd.isnull(element.Url_documento_fonte):    
            prepared_entry.Url_documento_fonte = element.Url_documento_fonte

        if not pd.isnull(element.Commento_entry):    
            prepared_entry.Commento_entry = element.Commento_entry


            
        prepared_entry.Data_inserimento_entry = element.Data_inserimento_entry
        prepared_entry.Id_statico_entry = element.Id_statico_entry               
        prepared_entry.Admin_approval_switch = element.Admin_approval_switch

        prepared_entry.save()


    print("Riempimento del modello prepared_terminology terminato con successo!")

    print("Inizia l'elaborazione della terminologia contenuta nel modello prepared_terminology...")


    # upper, lower, title
    print("Inizia la modifica del formato del testo (uppercase/title)...")

    prepared_rows = prepared_terminology.objects.all()

    for prepared_entry in prepared_rows:

        if not pd.isnull(prepared_entry.Lemma):
            prepared_entry.Lemma.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Acronimo):
            prepared_entry.Acronimo.upper()
            
        if not pd.isnull(prepared_entry.Ambito_riferimento):    
            prepared_entry.Ambito_riferimento.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Autore_definizione):    
            prepared_entry.Autore_definizione.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Posizione_definizione):    
            prepared_entry.Posizione_definizione.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Titolo_documento_fonte):    
            prepared_entry.Titolo_documento_fonte.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Autore_documento_fonte):    
            prepared_entry.Autore_documento_fonte.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Host_documento_fonte):    
            prepared_entry.Host_documento_fonte.title() # non è veramente necessario

        prepared_entry.Id_statico_entry.upper() 

        prepared_entry.save()
        

    

       

    print("Modifica del formato del testo (uppercase/title) terminato con successo!")

    # sostituzione di doppi spazi e  acapo con degli spazi

    print("Inizia l'eliminazione dei doppi spazi dal testo...")
    
    rip_doppi_spazi = 3 # ripeto il ciclo 3 volte 

    prepared_rows = prepared_terminology.objects.all()

    for i in range(rip_doppi_spazi):    # ripeto il ciclo n volte 

        for prepared_entry in prepared_rows:        
            
            if not pd.isnull(prepared_entry.Lemma):
                prepared_entry.Lemma = prepared_entry.Lemma.replace("  ", " ")

            if not pd.isnull(prepared_entry.Acronimo):
                prepared_entry.Acronimo = prepared_entry.Acronimo.replace("  ", " ")

            if not pd.isnull(prepared_entry.Definizione):    
                prepared_entry.Definizione = prepared_entry.Definizione.replace("  ", " ")

            if not pd.isnull(prepared_entry.Ambito_riferimento):    
                prepared_entry.Ambito_riferimento = prepared_entry.Ambito_riferimento.replace("  ", " ")

            if not pd.isnull(prepared_entry.Autore_definizione):    
                prepared_entry.Autore_definizione = prepared_entry.Autore_definizione.replace("  ", " ")

            if not pd.isnull(prepared_entry.Posizione_definizione):    
                prepared_entry.Posizione_definizione = prepared_entry.Posizione_definizione.replace("  ", " ")

            if not pd.isnull(prepared_entry.Titolo_documento_fonte):    
                prepared_entry.Titolo_documento_fonte = prepared_entry.Titolo_documento_fonte.replace("  ", " ")

            if not pd.isnull(prepared_entry.Autore_documento_fonte):    
                prepared_entry.Autore_documento_fonte = prepared_entry.Autore_documento_fonte.replace("  ", " ")

            if not pd.isnull(prepared_entry.Host_documento_fonte):    
                prepared_entry.Host_documento_fonte = prepared_entry.Host_documento_fonte.replace("  ", " ")
            
            if not pd.isnull(prepared_entry.Commento_entry):    
                prepared_entry.Commento_entry = prepared_entry.Commento_entry.replace("  ", " ")                      
        

            # non possono esserci doppi spazi in data, id e switch

            prepared_entry.save()



    # elimina spazi da davanti e dietro


    print("Eliminazione dei doppi spazi terminata con successo!")
    print("Inizia l'eliminazione degli spazi all'inizio e alla fine di ogni cella...")

    prepared_rows = prepared_terminology.objects.all()

    for prepared_entry in prepared_rows:        
        
        if not pd.isnull(prepared_entry.Lemma):
            if prepared_entry.Lemma[0] == " ":
                prepared_entry.Lemma = prepared_entry.Lemma[1:]
            if prepared_entry.Lemma[-1] == " ":
                prepared_entry.Lemma = prepared_entry.Lemma[0:-1]

        if not pd.isnull(prepared_entry.Acronimo):
            if prepared_entry.Acronimo[0] == " ":
                prepared_entry.Acronimo = prepared_entry.Acronimo[1:]
            if prepared_entry.Acronimo[-1] == " ":
                prepared_entry.Acronimo = prepared_entry.Acronimo[0:-1]


        if not pd.isnull(prepared_entry.Definizione):    
            if prepared_entry.Definizione[0] == " ":
                prepared_entry.Definizione = prepared_entry.Definizione[1:]
            if prepared_entry.Definizione[-1] == " ":
                prepared_entry.Definizione = prepared_entry.Definizione[0:-1]

        if not pd.isnull(prepared_entry.Ambito_riferimento):    
            if prepared_entry.Ambito_riferimento[0] == " ":
                prepared_entry.Ambito_riferimento = prepared_entry.Ambito_riferimento[1:]
            if prepared_entry.Ambito_riferimento[-1] == " ":
                prepared_entry.Ambito_riferimento = prepared_entry.Ambito_riferimento[0:-1]

        if not pd.isnull(prepared_entry.Autore_definizione):    
            if prepared_entry.Autore_definizione[0] == " ":
                prepared_entry.Autore_definizione = prepared_entry.Autore_definizione[1:]
            if prepared_entry.Autore_definizione[-1] == " ":
                prepared_entry.Autore_definizione = prepared_entry.Autore_definizione[0:-1]

        if not pd.isnull(prepared_entry.Posizione_definizione):    
            if prepared_entry.Posizione_definizione[0] == " ":
                prepared_entry.Posizione_definizione = prepared_entry.Posizione_definizione[1:]
            if prepared_entry.Posizione_definizione[-1] == " ":
                prepared_entry.Posizione_definizione = prepared_entry.Posizione_definizione[0:-1]

        if not pd.isnull(prepared_entry.Url_definizione):    
            if prepared_entry.Url_definizione[0] == " ":
                prepared_entry.Url_definizione = prepared_entry.Url_definizione[1:]
            if prepared_entry.Url_definizione[-1] == " ":
                prepared_entry.Url_definizione = prepared_entry.Url_definizione[0:-1]

        if not pd.isnull(prepared_entry.Titolo_documento_fonte):    
            if prepared_entry.Titolo_documento_fonte[0] == " ":
                prepared_entry.Titolo_documento_fonte = prepared_entry.Titolo_documento_fonte[1:]
            if prepared_entry.Titolo_documento_fonte[-1] == " ":
                prepared_entry.Titolo_documento_fonte = prepared_entry.Titolo_documento_fonte[0:-1]

        if not pd.isnull(prepared_entry.Autore_documento_fonte):    
            if prepared_entry.Autore_documento_fonte[0] == " ":
                prepared_entry.Autore_documento_fonte = prepared_entry.Autore_documento_fonte[1:]
            if prepared_entry.Autore_documento_fonte[-1] == " ":
                prepared_entry.Autore_documento_fonte = prepared_entry.Autore_documento_fonte[0:-1]

        if not pd.isnull(prepared_entry.Host_documento_fonte):    
            if prepared_entry.Host_documento_fonte[0] == " ":
                prepared_entry.Host_documento_fonte = prepared_entry.Host_documento_fonte[1:]
            if prepared_entry.Host_documento_fonte[-1] == " ":
                prepared_entry.Host_documento_fonte = prepared_entry.Host_documento_fonte[0:-1]

        if not pd.isnull(prepared_entry.Url_documento_fonte):    
            if prepared_entry.Url_documento_fonte[0] == " ":
                prepared_entry.Url_documento_fonte = prepared_entry.Url_documento_fonte[1:]
            if prepared_entry.Url_documento_fonte[-1] == " ":
                prepared_entry.Url_documento_fonte = prepared_entry.Url_documento_fonte[0:-1]

        if not pd.isnull(prepared_entry.Commento_entry):    
            if prepared_entry.Commento_entry[0] == " ":
                prepared_entry.Commento_entry = prepared_entry.Commento_entry[1:]
            if prepared_entry.Commento_entry[-1] == " ":
                prepared_entry.Commento_entry = prepared_entry.Commento_entry[0:-1]
        
        if not pd.isnull(prepared_entry.Id_statico_entry):
            if prepared_entry.Id_statico_entry[0] == " ":
                prepared_entry.Id_statico_entry = prepared_entry.Id_statico_entry[1:]
            if prepared_entry.Id_statico_entry[-1] == " ":
                prepared_entry.Id_statico_entry = prepared_entry.Id_statico_entry[0:-1]       


        prepared_entry.save()

    print("Eliminazione degli spazi all'inizio e alla fine di ogni cella terminata con successo!")

    print("Standardizzazione del formato dei dati terminata con successo!")

    print("I dati sono ora in un formato standard e possono essere processati per la realizzazione della struttura relazionale!")

