# from app_metaglossario.entity_relationship_models import *
# from app_metaglossario.node_models import *
# # from app_metaglossario.models import displaying_terminology


# def algoritmo_WD():

#     print("Viene richiamato l'algoritmo WD!")

#     # algoritmo per organizzare i dati per la visualizzazione
#     # la chiave è costruire una vista che permette di vedere un oggetto alla volta, 
#     # col punto di vista incentrato su quell'oggetto, circondato dai related.

#     # nota: ci sono dati con lo stesso ID perchè sono i lemmi inglesi eliminati

#     import numpy as np
#     import pandas as pd

#     # importa la tabella excel Elab 1 e salvala come dataframe

#     import os    
#     from django.contrib.staticfiles import finders

#     # devo importare non elab1 ma le tabelle relazionali

    

#     saving_folder_name = 'saved_dataframes'
#     ER_folder_name = 'tabelle_entita_e_relazionali'
#     finders.find(saving_folder_name)
#     searched_locations = finders.searched_locations
#     folder_Elab_dir = os.path.join(searched_locations[0]+r'\\'+saving_folder_name)
#     folder_ER_dir = os.path.join(searched_locations[0]+r'\\'+saving_folder_name+r'\\'+ER_folder_name)


#     nomi_Tabelle_relazionali = ["is_Acronimo_of", "is_Lemma_of", "is_Ambito_riferimento_of", "is_Autore_definizione_of", "is_Posizione_definizione_of", "is_Url_definizione_of", "is_Titolo_documento_fonte_of", "is_Autore_documento_fonte_of", "is_Host_documento_fonte_of", "is_Url_documento_fonte_of", "is_Commento_entry_of", "is_Data_inserimento_entry_of", "is_Id_statico_entry_of", "is_Admin_approval_switch_of"]

#     Things = pd.read_excel(folder_ER_dir+r'\\Things.xlsx', head=True, index_col=0)

    

#     is_Acronimo_of = pd.read_excel(folder_ER_dir+r'\\is_Acronimo_of.xlsx', head=True, index_col=0)
#     is_Lemma_of = pd.read_excel(folder_ER_dir+r'\\is_Lemma_of.xlsx', head=True, index_col=0)
#     is_Ambito_riferimento_of = pd.read_excel(folder_ER_dir+r'\\is_Ambito_riferimento_of.xlsx', head=True, index_col=0)
#     is_Autore_definizione_of = pd.read_excel(folder_ER_dir+r'\\is_Autore_definizione_of.xlsx', head=True, index_col=0)
#     is_Posizione_definizione_of = pd.read_excel(folder_ER_dir+r'\\is_Posizione_definizione_of.xlsx', head=True, index_col=0)
#     is_Url_definizione_of = pd.read_excel(folder_ER_dir+r'\\is_Url_definizione_of.xlsx', head=True, index_col=0)
#     is_Titolo_documento_fonte_of = pd.read_excel(folder_ER_dir+r'\\is_Titolo_documento_fonte_of.xlsx', head=True, index_col=0)
#     is_Autore_documento_fonte_of = pd.read_excel(folder_ER_dir+r'\\is_Autore_documento_fonte_of.xlsx', head=True, index_col=0)
#     is_Host_documento_fonte_of = pd.read_excel(folder_ER_dir+r'\\is_Host_documento_fonte_of.xlsx', head=True, index_col=0)
#     is_Url_documento_fonte_of = pd.read_excel(folder_ER_dir+r'\\is_Url_documento_fonte_of.xlsx', head=True, index_col=0)
#     is_Commento_entry_of = pd.read_excel(folder_ER_dir+r'\\is_Commento_entry_of.xlsx', head=True, index_col=0)
#     is_Data_inserimento_entry_of = pd.read_excel(folder_ER_dir+r'\\is_Data_inserimento_entry_of.xlsx', head=True, index_col=0)
#     is_Id_statico_entry_of = pd.read_excel(folder_ER_dir+r'\\is_Id_statico_entry_of.xlsx', head=True, index_col=0)
#     is_Admin_approval_switch_of = pd.read_excel(folder_ER_dir+r'\\is_Admin_approval_switch_of.xlsx', head=True, index_col=0)


#     Tabelle_relazionali = [is_Acronimo_of, is_Lemma_of, is_Ambito_riferimento_of, is_Autore_definizione_of, is_Posizione_definizione_of, is_Url_definizione_of, is_Titolo_documento_fonte_of, is_Autore_documento_fonte_of, is_Host_documento_fonte_of, is_Url_documento_fonte_of, is_Commento_entry_of, is_Data_inserimento_entry_of, is_Id_statico_entry_of, is_Admin_approval_switch_of]


#     nC = len(Tabelle_relazionali)

#     print("Vengono importate le tabelle delle entità e relazionali dalla directory %s ..." % folder_ER_dir)

#     print("Things")
#     print(Things)
#     print("--------------------------------")

#     for k in range(nC):

#         print(nomi_Tabelle_relazionali[k])
#         print(Tabelle_relazionali[k])
#         print("--------------------------------")




#     # ora genero anche le tabelle ISIO separate pr entità

#     print("Vengono generate le tabelle ISIO: is_static_id_of + nomi entità, per l'algoritmo WD...")

#     # per generarle devo importare elab1
#     saving_file_name = 'Elab1.xlsx'

#     saving_folder_name = 'saved_dataframes'

#     finders.find(saving_folder_name)
#     searched_locations = finders.searched_locations
#     df_dir = os.path.join(searched_locations[0]+r'\\'+saving_folder_name+r'\\'+saving_file_name)

#     Elab1 = pd.read_excel(df_dir, head=True, index_col=0)    

#     print("Viene importato il dataframe Elab1 dalla directory %s !" % df_dir)

#     print(Elab1)    

#     L_GI = len(Elab1.index)
#     nC = len(Elab1.columns)
    
#     #il risultato di questa operazione è automaticamente un float!
#     # metto int dentro try per correggerlo

#     if (nC % 2) != 0:
#         raise ValueError("ERRORE! Il file in ingresso Elab1 deve necessariamente avere un numero di colonne pari, perchè formato da ID_db ed entità corrispondenti!")

#     nC = int(nC/2)

#     print("Dimensioni del dataframe:")
#     print("Righe (L_GI): %s" % L_GI)
#     print("Colonne (nC): %s" % nC)  

#     # salvo i nomi delle colonne
#     label_Elab1 = list(Elab1.columns)

#     # importo le tabelle che contengono solo l'id statico delle singole entità
#     ISIO_Lemma = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Definizione"], Elab1["Id_statico_entry"], Elab1["Definizione"] ], axis=1) # è dataframe
#     ISIO_Acronimo = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Acronimo"], Elab1["Id_statico_entry"], Elab1["Acronimo"] ], axis=1) 
#     ISIO_Definizione = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Definizione"], Elab1["Id_statico_entry"], Elab1["Definizione"] ], axis=1) 
#     ISIO_Ambito_riferimento = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Ambito_riferimento"], Elab1["Id_statico_entry"], Elab1["Ambito_riferimento"] ], axis=1)
#     ISIO_Autore_definizione = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Autore_definizione"], Elab1["Id_statico_entry"], Elab1["Autore_definizione"] ], axis=1) 
#     ISIO_Posizione_definizione = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Posizione_definizione"], Elab1["Id_statico_entry"], Elab1["Posizione_definizione"] ], axis=1) 
#     ISIO_Url_definizione = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Url_definizione"], Elab1["Id_statico_entry"], Elab1["Url_definizione"] ], axis=1)  
#     ISIO_Titolo_documento_fonte = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Titolo_documento_fonte"], Elab1["Id_statico_entry"], Elab1["Titolo_documento_fonte"] ], axis=1) 
#     ISIO_Autore_documento_fonte = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Autore_documento_fonte"], Elab1["Id_statico_entry"], Elab1["Autore_documento_fonte"] ], axis=1) 
#     ISIO_Host_documento_fonte = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Host_documento_fonte"], Elab1["Id_statico_entry"], Elab1["Host_documento_fonte"] ], axis=1) 
#     ISIO_Url_documento_fonte = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Url_documento_fonte"], Elab1["Id_statico_entry"], Elab1["Url_documento_fonte"] ], axis=1) 
#     ISIO_Commento_entry = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Commento_entry"], Elab1["Id_statico_entry"], Elab1["Commento_entry"] ], axis=1) 
#     ISIO_Data_inserimento_entry = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Data_inserimento_entry"], Elab1["Id_statico_entry"], Elab1["Data_inserimento_entry"] ], axis=1) 
#     ISIO_Admin_approval_switch = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Admin_approval_switch"], Elab1["Id_statico_entry"], Elab1["Admin_approval_switch"] ], axis=1) 



#     ##################################################
#     ##################################################
#     ##################################################
#     ##################################################
#     ##################################################
#     ##################################################
#     ##################################################

#     # usala per riempire il modello node, seguendo la struttura relazionale del metaglossario
#     # aggiungi commento entri e admin approval switch


#     #setta la dimensione dell'ID    
#     ID_dimension = 1000000
    


#     print("*****************************************")

#     # per proseguire devo usare sql per interrogare le tabelle di django


  
    




