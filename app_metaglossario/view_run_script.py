from django.shortcuts import render, redirect
import time

# per gli script di management dei files
from .algoritmi_processing.script_gestione import *

# per gli script di calcolo tempo degli algoritmi
from .algoritmi_processing.script_ausiliari import *

# per gli script di elaborazione della terminologia
from .algoritmi_processing.PGI import algoritmo_PGI
from .algoritmi_processing.SR import algoritmo_SR
# from .algoritmi_processing.WD import algoritmo_WD


def run_script(request):   

    start_time = printout()

   
    # erase_glossary_entry()
    erase_acquired_terminology()

    # pour_entire_simple_model()
    pour_entire_file_model()
    # pour_latest_file()
    
    algoritmo_PGI()
    algoritmo_SR()
    # algoritmo_WD()

    # erase_database_tables()

    
    elapsed_time = round(time.time() - start_time)

    print("*** Script eseguito fino alla fine! ***")
    print("*** Tempo impiegato: %s s ***" % elapsed_time )

    finish_sound()

    return render(request, 'run_script.html', {})