from app_metaglossario.entity_relationship_models import *


def pour_entire_simple_model():

    # questo algoritmo va ottimizzato mettendo i cicli delle etichette delle colonne al posto di richiamare ogni elemento del database con la propria etichetta

    print("Inizia il riversamento di tutti i dati dal modello glossary_entry al modello acquired_terminology!")

    import pandas as pd
    from app_metaglossario.models import glossary_entry, acquired_terminology

    all_entries = glossary_entry.objects.all()

    # for element in all_entries[:10]:
    #     print(element.Lemma)
        
    for element in all_entries:

        entry = acquired_terminology.objects.create()
        
        if not pd.isnull(element.Lemma):
            entry.Lemma=element.Lemma

        if not pd.isnull(element.Acronimo):
            entry.Acronimo=element.Acronimo

        if not pd.isnull(element.Definizione):    
            entry.Definizione=element.Definizione

        if not pd.isnull(element.Ambito_riferimento):    
            entry.Ambito_riferimento=element.Ambito_riferimento

        if not pd.isnull(element.Autore_definizione):    
            entry.Autore_definizione=element.Autore_definizione

        if not pd.isnull(element.Posizione_definizione):    
            entry.Posizione_definizione=element.Posizione_definizione

        if not pd.isnull(element.Url_definizione):    
            entry.Url_definizione=element.Url_definizione

        if not pd.isnull(element.Titolo_documento_fonte):    
            entry.Titolo_documento_fonte=element.Titolo_documento_fonte

        if not pd.isnull(element.Autore_documento_fonte):    
            entry.Autore_documento_fonte=element.Autore_documento_fonte

        if not pd.isnull(element.Host_documento_fonte):    
            entry.Host_documento_fonte=element.Host_documento_fonte

        if not pd.isnull(element.Url_documento_fonte):    
            entry.Url_documento_fonte=element.Url_documento_fonte

        if not pd.isnull(element.Commento_entry):    
            entry.Commento_entry=element.Commento_entry

            
        entry.Data_inserimento_entry = element.Data_inserimento_entry
        entry.Id_statico_entry = element.Id_statico_entry               
        entry.Admin_approval_switch = element.Admin_approval_switch

        entry.save()

    print("Riversamento terminato con successo!")




def pour_entire_file_model():

    # questo algoritmo va ottimizzato mettendo i cicli delle etichette delle colonne al posto di richiamare ogni elemento del database con la propria etichetta

    print("Inizia il riversamento della terminologia di tutti i file salvati nel modello glossary_file verso il modello acquired_terminology...")

    import pandas as pd
    
    from app_metaglossario.models import glossary_file, acquired_terminology

    # tutti gli oggetti nel modello glossario sono salvati qui
    all_files = glossary_file.objects.all()
    
    for file_element in all_files: 
   
        # per ogni foglio nel modello
        print("Inizia la lettura del foglio %s per estrarne la terminologia riga per riga..." % file_element.Glossary_file)
        
        # accedo all'attributo file del modello
        # salva il contenuto del file in una variabile = dataframe
        excel_sheet = pd.read_excel(file_element.Glossary_file)

        print("*****") 
        print(excel_sheet)
        print("*****")       

        print("Sbobinatura del dataframe in vettori...")        
        
        col_lemma = excel_sheet.Lemma
        col_acronimo = excel_sheet.Acronimo
        col_definizione = excel_sheet.Definizione
        col_ambito_riferimento = excel_sheet.Ambito_riferimento
        col_autore_definizione = excel_sheet.Autore_definizione
        col_posizione_definizione = excel_sheet.Posizione_definizione
        col_url_definizione = excel_sheet.Url_definizione
        col_titolo_documento_fonte = excel_sheet.Titolo_documento_fonte
        col_autore_documento_fonte = excel_sheet.Autore_documento_fonte
        col_host_documento_fonte = excel_sheet.Host_documento_fonte
        col_url_documento_fonte = excel_sheet.Url_documento_fonte
        col_commento_entry = excel_sheet.Commento_entry
        col_data_inserimento_entry = excel_sheet.Data_inserimento_entry
        col_id_statico_entry = excel_sheet.Id_statico_entry
        col_admin_approval_switch = excel_sheet.Admin_approval_switch

        print("Inizia il riversamento di dati dal foglio %s al modello acquired_terminology..." % file_element.Glossary_file)

        for i in range(len(col_lemma)):

        # assegna i valori agli attributi uno per uno per evitare i NaN
            
            entry = acquired_terminology.objects.create()
            
            if not pd.isnull(col_lemma[i]):
                entry.Lemma=col_lemma[i]

            if not pd.isnull(col_acronimo[i]):
                entry.Acronimo=col_acronimo[i]

            if not pd.isnull(col_definizione[i]):    
                entry.Definizione=col_definizione[i]

            if not pd.isnull(col_ambito_riferimento[i]):    
                entry.Ambito_riferimento=col_ambito_riferimento[i]

            if not pd.isnull(col_autore_definizione[i]):    
                entry.Autore_definizione=col_autore_definizione[i]

            if not pd.isnull(col_posizione_definizione[i]):    
                entry.Posizione_definizione=col_posizione_definizione[i]

            if not pd.isnull(col_url_definizione[i]):    
                entry.Url_definizione=col_url_definizione[i]

            if not pd.isnull(col_titolo_documento_fonte[i]):    
                entry.Titolo_documento_fonte=col_titolo_documento_fonte[i]

            if not pd.isnull(col_autore_documento_fonte[i]):    
                entry.Autore_documento_fonte=col_autore_documento_fonte[i]

            if not pd.isnull(col_host_documento_fonte[i]):    
                entry.Host_documento_fonte=col_host_documento_fonte[i]

            if not pd.isnull(col_url_documento_fonte[i]):    
                entry.Url_documento_fonte=col_url_documento_fonte[i]

            if not pd.isnull(col_commento_entry[i]):    
                entry.Commento_entry=col_commento_entry[i]

                
            entry.Data_inserimento_entry=col_data_inserimento_entry[i]
            entry.Id_statico_entry=col_id_statico_entry[i]               
            entry.Admin_approval_switch=col_admin_approval_switch[i]

            entry.save()


        print("Riversamento dei dati di %s terminato con successo!" % file_element.Glossary_file)
        print("*****")
    
        
    print("La terminologia di tutti i file salvati nel modello glossary_file è stata riversata nel modello acquired_terminology!")





def pour_latest_entry():
    
    print("Il record inserito viene riversato nel modello acquired_terminology!")

    import pandas as pd
    from app_metaglossario.models import glossary_entry, acquired_terminology

    element = glossary_entry.objects.latest('Data_inserimento_entry')

    entry = acquired_terminology.objects.create()
        
    if not pd.isnull(element.Lemma):
        entry.Lemma=element.Lemma

    if not pd.isnull(element.Acronimo):
        entry.Acronimo=element.Acronimo

    if not pd.isnull(element.Definizione):    
        entry.Definizione=element.Definizione

    if not pd.isnull(element.Ambito_riferimento):    
        entry.Ambito_riferimento=element.Ambito_riferimento

    if not pd.isnull(element.Autore_definizione):    
        entry.Autore_definizione=element.Autore_definizione

    if not pd.isnull(element.Posizione_definizione):    
        entry.Posizione_definizione=element.Posizione_definizione

    if not pd.isnull(element.Url_definizione):    
        entry.Url_definizione=element.Url_definizione

    if not pd.isnull(element.Titolo_documento_fonte):    
        entry.Titolo_documento_fonte=element.Titolo_documento_fonte

    if not pd.isnull(element.Autore_documento_fonte):    
        entry.Autore_documento_fonte=element.Autore_documento_fonte

    if not pd.isnull(element.Host_documento_fonte):    
        entry.Host_documento_fonte=element.Host_documento_fonte

    if not pd.isnull(element.Url_documento_fonte):    
        entry.Url_documento_fonte=element.Url_documento_fonte

    if not pd.isnull(element.Commento_entry):    
        entry.Commento_entry=element.Commento_entry

        
    entry.Data_inserimento_entry=element.Data_inserimento_entry
    entry.Id_statico_entry=element.Id_statico_entry               
    entry.Admin_approval_switch=element.Admin_approval_switch

    entry.save()

    print("Riversamento terminato con successo!")


def pour_latest_file():    

    # questo algoritmo va ottimizzato mettendo i cicli delle etichette delle colonne al posto di richiamare ogni elemento del database con la propria etichetta

    import pandas as pd    
    from app_metaglossario.models import glossary_file, acquired_terminology

    latest_file_element = glossary_file.objects.latest('Data_inserimento_glossary')

    print("Inizia la lettura del foglio %s per estrarne la terminologia riga per riga..." % latest_file_element)
  
    excel_sheet = pd.read_excel(latest_file_element.Glossary_file)

    print("*****") 
    print(excel_sheet)
    print("*****")       

    print("Sbobinatura del dataframe in vettori...")        
    
    col_lemma = excel_sheet.Lemma
    col_acronimo = excel_sheet.Acronimo
    col_definizione = excel_sheet.Definizione
    col_ambito_riferimento = excel_sheet.Ambito_riferimento
    col_autore_definizione = excel_sheet.Autore_definizione
    col_posizione_definizione = excel_sheet.Posizione_definizione
    col_url_definizione = excel_sheet.Url_definizione
    col_titolo_documento_fonte = excel_sheet.Titolo_documento_fonte
    col_autore_documento_fonte = excel_sheet.Autore_documento_fonte
    col_host_documento_fonte = excel_sheet.Host_documento_fonte
    col_url_documento_fonte = excel_sheet.Url_documento_fonte
    col_commento_entry = excel_sheet.Commento_entry
    col_data_inserimento_entry = excel_sheet.Data_inserimento_entry
    col_id_statico_entry = excel_sheet.Id_statico_entry
    col_admin_approval_switch = excel_sheet.Admin_approval_switch

    print("Inizia il riversamento di dati dal foglio %s verso il modello acquired_terminology..." % latest_file_element)

    for i in range(len(col_lemma)):

    # assegna i valori agli attributi uno per uno per evitare i NaN
        
        entry = acquired_terminology.objects.create()
        
        if not pd.isnull(col_lemma[i]):
            entry.Lemma=col_lemma[i]

        if not pd.isnull(col_acronimo[i]):
            entry.Acronimo=col_acronimo[i]

        if not pd.isnull(col_definizione[i]):    
            entry.Definizione=col_definizione[i]

        if not pd.isnull(col_ambito_riferimento[i]):    
            entry.Ambito_riferimento=col_ambito_riferimento[i]

        if not pd.isnull(col_autore_definizione[i]):    
            entry.Autore_definizione=col_autore_definizione[i]

        if not pd.isnull(col_posizione_definizione[i]):    
            entry.Posizione_definizione=col_posizione_definizione[i]

        if not pd.isnull(col_url_definizione[i]):    
            entry.Url_definizione=col_url_definizione[i]

        if not pd.isnull(col_titolo_documento_fonte[i]):    
            entry.Titolo_documento_fonte=col_titolo_documento_fonte[i]

        if not pd.isnull(col_autore_documento_fonte[i]):    
            entry.Autore_documento_fonte=col_autore_documento_fonte[i]

        if not pd.isnull(col_host_documento_fonte[i]):    
            entry.Host_documento_fonte=col_host_documento_fonte[i]

        if not pd.isnull(col_url_documento_fonte[i]):    
            entry.Url_documento_fonte=col_url_documento_fonte[i]

        if not pd.isnull(col_commento_entry[i]):    
            entry.Commento_entry=col_commento_entry[i]

            
        entry.Data_inserimento_entry=col_data_inserimento_entry[i]
        entry.Id_statico_entry=col_id_statico_entry[i]               
        entry.Admin_approval_switch=col_admin_approval_switch[i]

        entry.save()


    print("Riversamento dei dati in %s terminato con successo!" % latest_file_element)
    print("*****")


    # per eliminare i glossari lo faccio manualmente (glossary_file)

    # elimina tutti i dati dentro acquired terminoliogy
def erase_acquired_terminology():

    from app_metaglossario.models import acquired_terminology
    acquired_terminology.objects.all().delete()
    print("Eliminati tutti i dati dentro acquired_terminology!")


# elimina tutti i dati dentro acquired terminoliogy
def erase_glossary_entry():

    from app_metaglossario.models import glossary_entry
    glossary_entry.objects.all().delete()
    print("Eliminati tutti i dati dentro glossary_entry!")


def erase_database_tables():

    modelli_metaglossario = [ model_Things, model_is_Acronimo_of, model_is_Lemma_of, model_is_Ambito_riferimento_of, model_is_Autore_definizione_of, model_is_Posizione_definizione_of, model_is_Url_definizione_of, model_is_Autore_documento_fonte_of, model_is_Url_documento_fonte_of, model_is_Commento_entry_of, model_is_Data_inserimento_entry_of, model_is_Id_statico_entry_of, model_is_Admin_approval_switch_of ]
   
    for modello in modelli_metaglossario:

        modello.objects.all().delete()
        print("Eliminati tutti i dati dentro %s!" % modello)  

    print("*********************************************") 
    print("Eliminati tutti i dati dentro i modelli di entità e relazioni del metaglossario!") 


# per il modello prepared la funzione di eliminazione è già insita nell'algoritmo PGI