from app_metaglossario.entity_relationship_models import *
from app_metaglossario.models import prepared_terminology
# from app_metaglossario.models import displaying_terminology

# per far funzionare il salvataggio delle cartelle
import os    
from django.contrib.staticfiles import finders


def algoritmo_SR():

    print("Viene richiamato l'algoritmo SR!")

    # algoritmo per generare la struttura relazionale

    # nota: ci sono dati con lo stesso ID perchè sono i lemmi inglesi eliminati

    import numpy as np
    import pandas as pd
    


    #setta la dimensione dell'ID    
    ID_dimension = 1000000

    print("Inizia la creazione della struttura relazionale dei dati contenuti in prepared_terminology...")
    
    # copia i dati del modello prepared_terminology in un dataframe    

    prepared_entries = prepared_terminology.objects.all()   

    # genera un oggettos trano che contine i nomi delle colonne
    # nomi_campi_prepared_terminology = prepared_terminology._meta.fields

    # devo trovare il modo per farlo in automatico
    # nomi_campi_prepared_terminology = ["Lemma", "Acronimo", "Definizione", "Ambito_riferimento", "Autore_definizione", "Posizione_definizione", "Url_definizione", "Titolo_documento_fonte", "Autore_documento_fonte", "Host_documento_fonte", "Url_documento_fonte", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"]

    # lista coi nomi delle colonne del modello
    nomi_campi_prepared_terminology = [field.name for field in prepared_terminology._meta.get_fields()[1:]]

    # elimino la colonna dell'id stabilito da python
    # nomi_campi_prepared_terminology = nomi_campi_prepared_terminology[1:]

    L_GI = len(prepared_entries)
    nC = len(nomi_campi_prepared_terminology)

    print("Vengono impostate le dimensioni del dataframe:")
    print("Righe (L_GI): %s" % L_GI)
    print("Colonne (nC): %s" % nC)   


    print("Viene generato il dataframe che contiene la copia dei dati del modello prepared_terminology...")

    # creo il dataframe
    GI = pd.DataFrame(columns=nomi_campi_prepared_terminology)

    


    for element in prepared_entries:

        # "Lemma", "Acronimo", "Definizione", "Ambito_riferimento", "Autore_definizione", "Posizione_definizione", "Url_definizione", "Titolo_documento_fonte", "Autore_documento_fonte", "Host_documento_fonte", "Url_documento_fonte", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"
        new_entry = {"Lemma":element.Lemma, "Acronimo":element.Acronimo, "Definizione":element.Definizione, "Ambito_riferimento":element.Ambito_riferimento, "Autore_definizione":element.Autore_definizione, "Posizione_definizione":element.Posizione_definizione, "Url_definizione":element.Url_definizione, "Titolo_documento_fonte":element.Titolo_documento_fonte, "Autore_documento_fonte":element.Autore_documento_fonte, "Host_documento_fonte":element.Host_documento_fonte, "Url_documento_fonte":element.Url_documento_fonte, "Commento_entry":element.Commento_entry, "Data_inserimento_entry":element.Data_inserimento_entry, "Id_statico_entry":element.Id_statico_entry, "Admin_approval_switch":element.Admin_approval_switch}
        
        GI = GI.append(new_entry, ignore_index=True)

  
    GI = GI.sort_values(['Lemma', 'Id_statico_entry'])
    GI = GI.reset_index(drop=True)

    print(GI)



    # preparo il tabellone fatto con le tabelle di ID e campi corrispondenti adiacenti    
    print("Vengono preparati gli ID da associare a ciascun oggetto del metaglossario...")

    label_IDs_prestampa = []

    for i in range(nC):
        label_IDs_prestampa.append("ID_db_" + nomi_campi_prepared_terminology[i])
    
    ID_dimension = 1000000

    IDs_prestampa_content = []

    # mentre per python il primo indice è 0, nella mia riga io ci metto 1
    for i in range(L_GI):        
        IDs_prestampa_content.append([ (ID_dimension * (j+1) ) + (i+1) for j in range(nC) ])
            

    IDs_prestampa = pd.DataFrame(IDs_prestampa_content, columns=label_IDs_prestampa)   

    del IDs_prestampa_content

    # devo ordinare dalla A alla Z la tabella della terminolgia
    # poi devo reincollare il vettore di ogni colonna già ordinata dalla A alla Z


    Elab1 = pd.concat([IDs_prestampa, GI], axis=1)

    print("Viene preparata la tabella di ID e terminologia Elab1...")

    print("Gli ID di Elab 1 vengono assegnati in ordine numerico ascendente con l'ordine alfabetico (A->Z) di ogni colonna.")

    del GI


    # vedi i print
    for j in range(nC):

        Elab1 = Elab1.sort_values([nomi_campi_prepared_terminology[j], "Id_statico_entry"])
        Elab1 = Elab1.reset_index(drop=True)
        Elab1.iloc[:, j] = IDs_prestampa.iloc[:, j]   
        


     

    
    print(Elab1)

    # tengo traccia delle ripetizioni presenti in ogni colonna del dataframe

    # creo le labe per il df ripetizioni
    label_ripetizioni = []

    for i in range(nC):
        label_ripetizioni.append("Ripetizioni_di_" + nomi_campi_prepared_terminology[i])

    # creo i dati per il df ripetizioni
    ripetizioni_content = []
    
    ripetizioni_content.append([ 0 for j in range(nC) ])

    # creo  il df ripetizioni
    ripetizioni = pd.DataFrame(ripetizioni_content, columns=label_ripetizioni)
    

    # inizia la riscrittura degli id per mettere uguali queli che corrispondono ad oggetti uguali

    #ordino il glossario alfabeticamente per X

    # pone uguali id di elementi guuali


    # salto il fatto che id statico non ha ripetizioni perchè c'è l'interruttore di show/hide

    label_Elab1 = nomi_campi_prepared_terminology + label_IDs_prestampa

    print("***********************************")

    print("Inizia lo scansionamento della terminologia e dei metadati per individuare elementi uguali...")
    
    
    # faccio il megaciclo in cui rendo uguagli gli id di oggetti uguali adiacenti (ordiant in ordine alfabetico)
    for j in range(nC):

        Elab1 = Elab1.sort_values([nomi_campi_prepared_terminology[j], "Id_statico_entry"])
        Elab1 = Elab1.reset_index(drop=True)

        # uno in meno perchè devo fare confronto tra i e i+1
        for i in range(L_GI-1):

            # se gli oggetti consecutivi sono uguali
            if Elab1.iloc[i+1, j+nC] == Elab1.iloc[i, j+nC] :

                # poni l'id successivo uguale a quello attuale
                Elab1.iloc[i+1, j] = Elab1.iloc[i, j] 

                ripetizioni.iloc[0, j] = ripetizioni.iloc[0, j] + 1


    Elab1 = Elab1.sort_values(["Lemma", "Id_statico_entry"])
    Elab1 = Elab1.reset_index(drop=True)
 
    print("Gli elementi uguali dentro Elab1 hanno ricevuto lo stesso Id_db!")
    print(Elab1)

    # creo un dataframe per gli ogetti univoci (L_GI-ripetizioni)

    label_oggetti_univoci = []

    for j in range(nC):
        label_oggetti_univoci.append("Oggetti_univoci_di_" + nomi_campi_prepared_terminology[j])

    # creo i dati per il df ripetizioni
    oggetti_univoci_content = []
    
    oggetti_univoci_content.append([ L_GI - ripetizioni.iloc[0, j] for j in range(nC) ])   
    

    # creo  il df ripetizioni
    oggetti_univoci = pd.DataFrame(oggetti_univoci_content, columns=label_oggetti_univoci)

    

    print("Il metaglossario Elab1 possiede i seguenti numeri di oggetti univoci:")

    print(np.transpose(oggetti_univoci))


    # Inizia il ciclo di sostituzioni degli ID con ID ordinati in linea con gli ID statici

    #  ossia:
    #  tutte le colonne sono ordinate per ID statici,
    #  un ciclo i scorre le colonne, e:
    #  un ciclo j scorre tutta la colonna, e:
    #  l'ID corrente(j) viene salvato come bersaglio da sostituire
    #  viene generato un ID del tipo x000000[contatore del ciclo j /ossia prestampaIDs(j,i)] e salvato come sostituto
    #  un ciclo k scorre tutta la colonna DALLA CELLA CORRENTE VERSO IL BASSO (onde evitare di sovrascrivere i precedenti) e sostituisce altre celle uguali al bersaglio con il sostuituto

    print("***********************************")

    print("Viene eseguita la riclassificazione degli ID dei singoli oggetti per realizzare le tabelle relazionali del database...")

    # col_scan 1 To L_GI, 1 To nC
    # avvenuta_sost  1 To L_GI, 1 To nC

    #  va bene anche df_zeros = df * 0

    avvenuta_sost = pd.DataFrame(0, index=np.arange(L_GI), columns=label_IDs_prestampa)


    # ordino il glossario alfabeticamente per IDS, una sola volta
    Elab1 = Elab1.sort_values("Id_statico_entry")
    Elab1 = Elab1.reset_index(drop=True)

    # in col scan ci metto gli id di elab1 ordinati per ids
    col_scan = Elab1[label_IDs_prestampa]

    

    pd.options.mode.chained_assignment = None  # default='warn'
    # https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas

    # in VBA, solo negli offset accade che righe e colonne hanno il sistema ribaltato rispetto a x=0 e coordinate scambiate
    # nelle matrici si ragiona normalmente in (righe, colonne)

    for i in range(nC):
    # ciclo delle colonne
    # per l'ID statico non devo farlo ... ma non è più in ultima poizione

        for j in range(L_GI):
        #ciclo delle righe

            Bersaglio = col_scan.iloc[j, i]
            Sostituto = IDs_prestampa.iloc[j, i] # questi sono gli id 1000001 , 10000002, ecc

            

            for k in range(j, L_GI): #[j, j+1,...,L_GI-1, L_GI]
            # ciclo del check per una riga di tutti i duoi doppioni nella colonna
            # 'deve andare fino a L_GI-1 : deve controllare la colonna fino in fondo, ma senza modificare gli elementi prima della colonna j
            # 'ciclo di sola sostituzione: non mettere else

                

                if col_scan.iloc[k, i] == Bersaglio and avvenuta_sost.iloc[k, i] == 0:
                            
                    col_scan.iloc[k, i] = Sostituto                             
                    avvenuta_sost.iloc[k, i] = 1


    # incollo col_scan sulla parte ID di Elab 1
    
    Elab1[ label_IDs_prestampa ] = col_scan [label_IDs_prestampa]

    print(Elab1[ label_IDs_prestampa ])

    del IDs_prestampa
    del avvenuta_sost
    del col_scan

    # 'ora devo compattare gli ID per non lasciare buchi
    for j in range(nC):

        Elab1 = Elab1.sort_values([nomi_campi_prepared_terminology[j], "Id_statico_entry"])
        Elab1 = Elab1.reset_index(drop=True)
        

    Elab1 = Elab1.sort_values(["Id_statico_entry"])
    Elab1 = Elab1.reset_index(drop=True)

    print("La riclassificazione degli ID dei singoli oggetti è terminata!")

 
    print(Elab1)

    print("***********************************")

    print("Vengono generate le tabelle per il database...")

    print("Viene generata la tabella delle entità Things con tutti gli oggetti del database e i loro Id relazionali...")

    # creazione della tabella things: id e oggetti
    # concat: axis: 0 per la concatenazione in colonna, 1 per la concatenazione in riga

    # concatena in colonna gli id di tutti gli oggetti
    # incolla uno sotto l'altra le colonne degli id
    Things_ID = pd.concat([Elab1[j] for j in label_IDs_prestampa], axis=0) 

    L_Things = len(Things_ID.index)

    # concatena in colonna gli oggetti
     # incolla uno sotto l'altra le colonne degli oggetti
    Things_oggetti = pd.concat([Elab1[j] for j in nomi_campi_prepared_terminology], axis=0)

    # crea la tabella things
    # concatena in riga id e oggetti    
    Things = pd.concat([Things_ID, Things_oggetti], axis=1) # è dataframe

    # assegno il nome alle colonne
    Things.columns=['ID_db_Thing','Thing']

    # resetto gli indici altrimenti mi tiene gli indici di Elab1
    Things = Things.reset_index(drop=True)

    print(Things)

    del Things_ID
    del Things_oggetti

    print("Vengono generate le tabelle relazionali...")


    # ["Lemma", "Acronimo", "Definizione", "Ambito_riferimento", "Autore_definizione", "Posizione_definizione", "
    # Url_definizione", "Titolo_documento_fonte", "Autore_documento_fonte", "Host_documento_fonte", 
    # "Url_documento_fonte", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"]
    
    # ID_db_

    is_Acronimo_of = pd.concat([ Elab1["ID_db_Acronimo"], Elab1["ID_db_Lemma"], Elab1["Acronimo"], Elab1["Lemma"] ], axis=1)

    is_Lemma_of = pd.concat( [Elab1["ID_db_Lemma"], Elab1["ID_db_Definizione"], Elab1["Lemma"], Elab1["Definizione"] ], axis=1)

    is_Ambito_riferimento_of = pd.concat([ Elab1["ID_db_Ambito_riferimento"], Elab1["ID_db_Definizione"], Elab1["Ambito_riferimento"], Elab1["Definizione"] ], axis=1)

    is_Autore_definizione_of = pd.concat([ Elab1["ID_db_Autore_definizione"], Elab1["ID_db_Definizione"], Elab1["Autore_definizione"], Elab1["Definizione"] ], axis=1)

    is_Posizione_definizione_of = pd.concat([ Elab1["ID_db_Posizione_definizione"], Elab1["ID_db_Definizione"], Elab1["Posizione_definizione"], Elab1["Definizione"] ], axis=1)

    is_Url_definizione_of = pd.concat([ Elab1["ID_db_Url_definizione"], Elab1["ID_db_Definizione"], Elab1["Url_definizione"], Elab1["Definizione"] ], axis=1)

    is_Titolo_documento_fonte_of = pd.concat([ Elab1["ID_db_Titolo_documento_fonte"], Elab1["ID_db_Definizione"], Elab1["Titolo_documento_fonte"], Elab1["Definizione"] ], axis=1)

    is_Autore_documento_fonte_of = pd.concat([ Elab1["ID_db_Autore_documento_fonte"], Elab1["ID_db_Titolo_documento_fonte"], Elab1["Autore_documento_fonte"], Elab1["Titolo_documento_fonte"] ], axis=1)

    is_Host_documento_fonte_of = pd.concat([ Elab1["ID_db_Host_documento_fonte"], Elab1["ID_db_Titolo_documento_fonte"], Elab1["Host_documento_fonte"], Elab1["Titolo_documento_fonte"] ], axis=1)

    is_Url_documento_fonte_of = pd.concat([ Elab1["ID_db_Url_documento_fonte"], Elab1["ID_db_Titolo_documento_fonte"], Elab1["Url_documento_fonte"], Elab1["Titolo_documento_fonte"] ], axis=1)

    is_Commento_entry_of = pd.concat([ Elab1["ID_db_Commento_entry"], Elab1["ID_db_Id_statico_entry"], Elab1["Commento_entry"], Elab1["Id_statico_entry"] ], axis=1)
    
    is_Data_inserimento_entry_of = pd.concat([ Elab1["ID_db_Data_inserimento_entry"], Elab1["ID_db_Id_statico_entry"], Elab1["Data_inserimento_entry"], Elab1["Id_statico_entry"] ], axis=1)
    

    # is_Id_statico_entry_of è lunga nC*L_GI perchè collega gli id_statici a nC entità del database
    ###

    Id_statico_entry_impilati_per_nC = pd.concat([Elab1["Id_statico_entry"] for j in range(nC)], axis=0)   
    # resetto gli indici altrimenti mi tiene gli indici di Elab1
    Id_statico_entry_impilati_per_nC = Id_statico_entry_impilati_per_nC.reset_index(drop=True)
    Id_statico_entry_impilati_per_nC = pd.DataFrame(Id_statico_entry_impilati_per_nC) # è dataframe

    ID_db_Id_statico_entry_impilati_per_nC = pd.concat([Elab1["ID_db_Id_statico_entry"] for j in range(nC)], axis=0)  
    # resetto gli indici altrimenti mi tiene gli indici di Elab1
    ID_db_Id_statico_entry_impilati_per_nC = ID_db_Id_statico_entry_impilati_per_nC.reset_index(drop=True)
    ID_db_Id_statico_entry_impilati_per_nC = pd.DataFrame(ID_db_Id_statico_entry_impilati_per_nC) # è dataframe
  
    is_Id_statico_entry_of = pd.concat( [ ID_db_Id_statico_entry_impilati_per_nC, Things["ID_db_Thing"], Id_statico_entry_impilati_per_nC, Things["Thing"] ], axis=1)

    ####

    is_Admin_approval_switch_of = pd.concat([ Elab1["ID_db_Admin_approval_switch"], Elab1["ID_db_Id_statico_entry"], Elab1["Admin_approval_switch"], Elab1["Id_statico_entry"] ], axis=1)
    
    



    # volgio salvarmi i dataframe in delle tabelle così mi salvo i dati 
    # cosi non ho bisogno di far ricorrere ogni volta l'algoritmo relazionele se voglio
    # lanciare quello che mi crea il modello dei nodi per la visualizzazione



    # import os    
    # from django.contrib.staticfiles import finders
    # queste 2 righe le ho inserite all'inizio

    saving_file_name = 'Elab1.xlsx'

    saving_folder_name = 'saved_dataframes'

    finders.find(saving_folder_name)
    searched_locations = finders.searched_locations
    df_dir = os.path.join(searched_locations[0]+r'\\'+saving_folder_name+r'\\'+saving_file_name)
    Elab1.to_excel(df_dir)

    print("Il dataframe Elab1 è stato salvato in una tabella excel nella directory %s !" % df_dir)


    # creo una copia di elab1 per il download agli utenti, ci metto solo elementi non sensibili

    Terminologia_metaglossario = pd.concat([ Elab1["Lemma"], Elab1["Acronimo"], Elab1["Definizione"], Elab1["Ambito_riferimento"], Elab1["Autore_definizione"], Elab1["Posizione_definizione"], Elab1["Url_definizione"], Elab1["Titolo_documento_fonte"], Elab1["Autore_documento_fonte"], Elab1["Host_documento_fonte"], Elab1["Url_documento_fonte"], Elab1["Commento_entry"], Elab1["Data_inserimento_entry"], Elab1["Id_statico_entry"] ], axis=1)

    saving_file_name = 'Terminologia_metaglossario.xlsx'

    saving_folder_name = 'saved_dataframes'

    finders.find(saving_folder_name)
    searched_locations = finders.searched_locations
    df_dir = os.path.join(searched_locations[0]+r'\\'+saving_folder_name+r'\\'+saving_file_name)
    Terminologia_metaglossario.to_excel(df_dir)

    print("Il dataframe Terminologia_metaglossario è stato salvato in una tabella excel nella directory %s !" % df_dir)
												

    del Elab1
    del Terminologia_metaglossario
    del Id_statico_entry_impilati_per_nC
    del ID_db_Id_statico_entry_impilati_per_nC

    ###########

    # ELIMINA LE RIGHE RIPETUTE dalle tabelle relazionali

    print("La tabella delle entità e le tabelle relazionali vengono ripulite degli elementi ridondanti...")

    # dataframe 1x1
    righe_eliminate_Things = pd.DataFrame([0], columns=["Righe_eliminate_di_Things"])


    colonne_Things = list(Things.columns.values)        

    Things = Things.sort_values( [ colonne_Things[0], colonne_Things[1] ] )
    Things = Things.reset_index(drop=True)

    print(Things)

    last_ID_unique_A = Things.iloc[0, 0] 
    last_ID_unique_B = Things.iloc[0, 1] 


    for i in range(1, L_Things): # da 1 a L_T

        if Things.iloc[i, 0] == last_ID_unique_A and Things.iloc[i, 1] == last_ID_unique_B:

            Things.iloc[i, :] = "ELIMINARE"
            righe_eliminate_Things.iloc[0, 0] = righe_eliminate_Things.iloc[0, 0] + 1 # solo una colonna (j = 1 costante)


        # handle Nan

        # questo è impossibile perchè tutti gli ID_db non sono NaN di sicuro

        # elif np.isnan(Things.iloc[i, 0]) and np.isnan(last_ID_unique_A) and Things.iloc[i, 1] == last_ID_unique_B:

        #     Things.iloc[i, :] = "ELIMINARE"
        #     righe_eliminate.iloc[0, j] = righe_eliminate.iloc[0, j] + 1

        elif Things.iloc[i, 0] == last_ID_unique_A and np.isnan(Things.iloc[i, 1]) and np.isnan(last_ID_unique_B):

            Things.iloc[i, :] = "ELIMINARE"
            righe_eliminate_Things.iloc[0, j] = righe_eliminate_Things.iloc[0, j] + 1


        # questo è impossibile perchè tutti gli ID_db non sono NaN di sicuro

        # elif np.isnan(Things.iloc[i, 0]) and np.isnan(last_ID_unique_A) and np.isnan(Things.iloc[i, 1]) and np.isnan(last_ID_unique_B):

        #     Things.iloc[i, :] = "ELIMINARE"
        #     righe_eliminate.iloc[0, j] = righe_eliminate.iloc[0, j] + 1



        else:
            last_ID_unique_A = Things.iloc[i, 0] 
            last_ID_unique_B = Things.iloc[i, 1] 

    

    
    indexNames = Things[ Things[colonne_Things[0]] == "ELIMINARE" ].index

    # Delete these row indexes from dataFrame
    Things.drop(indexNames, inplace=True)
    Things = Things.reset_index(drop=True)
    L_Things=len(Things) # devo aggiornare la lunghezza di Things

    print("Things")
    print(Things)

    
    print("--------------------")




    Tabelle_relazionali = [is_Acronimo_of, is_Lemma_of, is_Ambito_riferimento_of, is_Autore_definizione_of, is_Posizione_definizione_of, is_Url_definizione_of, is_Titolo_documento_fonte_of, is_Autore_documento_fonte_of, is_Host_documento_fonte_of, is_Url_documento_fonte_of, is_Commento_entry_of, is_Data_inserimento_entry_of, is_Id_statico_entry_of, is_Admin_approval_switch_of]

    nomi_Tabelle_relazionali = ["is_Acronimo_of", "is_Lemma_of", "is_Ambito_riferimento_of", "is_Autore_definizione_of", "is_Posizione_definizione_of", "is_Url_definizione_of", "is_Titolo_documento_fonte_of", "is_Autore_documento_fonte_of", "is_Host_documento_fonte_of", "is_Url_documento_fonte_of", "is_Commento_entry_of", "is_Data_inserimento_entry_of", "is_Id_statico_entry_of", "is_Admin_approval_switch_of"]



    label_righe_eliminate = []

    for i in range(nC):
        label_righe_eliminate.append("Righe_eliminate_di_" + nomi_campi_prepared_terminology[i])

    # creo i dati per il df righe_eliminate
    righe_eliminate_content = []
    
    righe_eliminate_content.append([ 0 for j in range(nC) ])

    # creo il df righe_eliminate
    righe_eliminate = pd.DataFrame(righe_eliminate_content, columns=label_righe_eliminate)

    j=0 # serve solo per tracciare il n di righe eliminate

    for tabella in Tabelle_relazionali:

        colonne_tabella = list(tabella.columns.values)

        L_tabella = len(tabella.index)       

        tabella = tabella.sort_values( [ colonne_tabella[0], colonne_tabella[1] ] )
        tabella = tabella.reset_index(drop=True)
    
        last_ID_unique_A = tabella.iloc[0, 0] 
        last_ID_unique_B = tabella.iloc[0, 1] 


        for i in range(1, L_tabella): # da 1 a L_tabella

            if tabella.iloc[i, 0] == last_ID_unique_A and tabella.iloc[i, 1] == last_ID_unique_B:

                tabella.iloc[i, :] = "ELIMINARE"
                righe_eliminate.iloc[0, j] = righe_eliminate.iloc[0, j] + 1


            # handle Nan
            # questo è impossibile perchè tutti gli ID_db non sono NaN di sicuro

            # elif np.isnan(tabella.iloc[i, 0]) and np.isnan(last_ID_unique_A) and tabella.iloc[i, 1] == last_ID_unique_B:

            #     tabella.iloc[i, :] = "ELIMINARE"
            #     righe_eliminate.iloc[0, j] = righe_eliminate.iloc[0, j] + 1

            # elif tabella.iloc[i, 0] == last_ID_unique_A and np.isnan(tabella.iloc[i, 1]) and np.isnan(last_ID_unique_B):

            #     tabella.iloc[i, :] = "ELIMINARE"
            #     righe_eliminate.iloc[0, j] = righe_eliminate.iloc[0, j] + 1

            # elif np.isnan(tabella.iloc[i, 0]) and np.isnan(last_ID_unique_A) and np.isnan(tabella.iloc[i, 1]) and np.isnan(last_ID_unique_B):

            #     tabella.iloc[i, :] = "ELIMINARE"
            #     righe_eliminate.iloc[0, j] = righe_eliminate.iloc[0, j] + 1



            else:
                last_ID_unique_A = tabella.iloc[i, 0] 
                last_ID_unique_B = tabella.iloc[i, 1] 

        

        # cancellare le righe contrassegnate
        indexNames = tabella[ tabella[colonne_tabella[0]] == "ELIMINARE" ].index 
        # Delete these row indexes from dataFrame
        tabella.drop(indexNames, inplace=True)

        tabella = tabella.reset_index(drop=True)

        Tabelle_relazionali[j] = tabella

        print(nomi_Tabelle_relazionali[j])
        print(Tabelle_relazionali[j])

        print("--------------------")

        j=j+1


    print("La tabella delle entità e le tabelle relazionali sono state ripulite degli elementi ridondanti")

    

    print(np.transpose(righe_eliminate_Things))
    print(np.transpose(righe_eliminate))



    

    print("***********************************")

    # ####################

    # salvo in excel le tabelle relazionali perchè le voglio copiare in access per fare delle prove


    saving_folder_name = 'saved_dataframes'+ r'\\' +'tabelle_entita_e_relazionali'
    
    print("Le tabelle relazionali vengono salvate come fogli excel nella directory %s ..." % saving_folder_name)

    saving_file_name = 'Things.xlsx'

    finders.find(saving_folder_name)
    searched_locations = finders.searched_locations
    df_dir = os.path.join(searched_locations[0] + r'\\' + saving_folder_name + r'\\' + saving_file_name)
    Things.to_excel(df_dir)

    print("La tabella delle entità Things è stata salvata in una tabella excel!")

    
    n_tabelle = len(Tabelle_relazionali)

    for k in range(n_tabelle):

        tabella = Tabelle_relazionali[k]
        # nome_tabella = nomi_Tabelle_relazionali[k]

        saving_file_name = nomi_Tabelle_relazionali[k] + r'.xlsx'

        # questa riga l'ho già messa sopra, quindi non devo ripeterla per tutto il ciclo
        # saving_folder_name = 'saved_dataframes'+ r'\\' +'tabelle_entita_e_relazionali'

        finders.find(saving_folder_name)
        searched_locations = finders.searched_locations
        df_dir = os.path.join(searched_locations[0] + r'\\' + saving_folder_name + r'\\' + saving_file_name)
        tabella.to_excel(df_dir)

        print("La tabella relazionale %s è stata salvata in una tabella excel!" % nomi_Tabelle_relazionali[k] )

    

    ##################### ##################### ####################


    # copia le tabelle di entità e relazionali nel modello per disporre i dati
    print("Le tabelle relazionali elaborate vengono riversate nei modelli del metaglossario...")

    # inizio a lavorare sui modelli
    # li metto tutti in minuscolo per non guastare postgresql

    # https://stackoverflow.com/questions/34425607/how-to-write-a-pandas-dataframe-to-django-model

    modelli_relazionali_metaglossario = [ model_is_acronimo_of, model_is_lemma_of, model_is_ambito_riferimento_of, model_is_autore_definizione_of, model_is_posizione_definizione_of, model_is_url_definizione_of, model_is_titolo_documento_fonte_of, model_is_autore_documento_fonte_of, model_is_host_documento_fonte_of, model_is_url_documento_fonte_of, model_is_commento_entry_of, model_is_data_inserimento_entry_of, model_is_id_statico_entry_of, model_is_admin_approval_switch_of ]
    nomi_modelli_relazionali_metaglossario = [ "model_is_acronimo_of", "model_is_lemma_of", "model_is_ambito_riferimento_of", "model_is_autore_definizione_of", "model_is_posizione_definizione_of", "model_is_url_definizione_of", "model_is_titolo_documento_fonte_of", "model_is_autore_documento_fonte_of", "model_is_host_documento_fonte_of", "model_is_Url_documento_fonte_of", "model_is_commento_entry_of", "model_is_data_inserimento_entry_of", "model_is_id_statico_entry_of", "model_is_admin_approval_switch_of" ]

    # già definito prima
    # n_tabelle = len(modelli_relazionali_metaglossario)

    # genera il modello things

    model_things.objects.all().delete()
    print("Eliminati tutti i dati dentro model_things!")
    print("Viene generato il modello model_things....")

    # per things
    for i in range(L_Things):             
            # non ci sono NaN            
            model_things.objects.create(id_thing=Things.iloc[i, 0], thing=Things.iloc[i, 1])


    print("È stato generato il modello model_things!")


    # per le tabelle relazionali

    for k in range(n_tabelle):

        tabella = Tabelle_relazionali[k]
        modello = modelli_relazionali_metaglossario[k]

        colonne_tabella = list(tabella.columns.values) 

        L_tabella = len(tabella.index)       

        # dovrebbero essere già ordinate, ma non importa
        tabella = tabella.sort_values( [ colonne_tabella[0], colonne_tabella[1] ] )
        tabella = tabella.reset_index(drop=True)

        modello.objects.all().delete()
        print("Eliminati tutti i dati dentro %s!" % nomi_modelli_relazionali_metaglossario[k])
        print("Viene generato il modello %s..." % nomi_modelli_relazionali_metaglossario[k])

        for i in range(L_tabella):             
            # non ci sono NaN            
            modello.objects.create(id_soggetto=tabella.iloc[i, 0], id_oggetto=tabella.iloc[i, 1])

        print("È stato generato il modello %s!" % nomi_modelli_relazionali_metaglossario[k])



    ############



    ##############







    


