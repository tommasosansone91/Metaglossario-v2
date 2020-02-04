from django.contrib import admin
from .models import glossary_entry 
from .models import glossary_file
from .models import acquired_terminology
from .models import prepared_terminology
# from .models import displaying_terminology

# importa tutti i modelli del metaglossario
from app_metaglossario.entity_relationship_models import *

# importa tutti i modelli di punto di vista nodale
from app_metaglossario.node_models import *

# per il tool import export
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# funzionano ma vs studio li legge male

# queste due funzioni sono collegate al widget import export utilizzabile solo dall'admin

class glossary_entry_resource(resources.ModelResource):
    class Meta:
        model = glossary_entry
        
        # fields = ('id', 'name', 'price',) # per includere i campi
        # exclude = ('id','Data_inserimento_entry','Id_statico_entry','Admin_approval_switch' ) # per escludere i campi

# questa classe definita in questo modo mi permette di usare il tool import export
class Controllo_import_export(ImportExportModelAdmin, admin.ModelAdmin):
    pass


# Register your models here.
# per ogni modello, registralo con una nuova linea del tipo
# admin.site.register(modello)

# questa scrittura mi permette di usare il tool import export
admin.site.register(glossary_entry, Controllo_import_export)

# solo il modello accoppiato ad import-export prende in ingresso un secondo argomento quando registrato,
# il secondo argomento è la funzione admin in cui in realtà viene messo pass

# altri modelli
admin.site.register(glossary_file)
admin.site.register(acquired_terminology, Controllo_import_export)
admin.site.register(prepared_terminology, Controllo_import_export)
# admin.site.register(displaying_terminology, Controllo_import_export)


# qui registro i modelli a nodi
# admin.site.register(model_node)

#qui registro i modelli del metaglossario : tabelle relazionali ed entirà
admin.site.register(model_things, Controllo_import_export)
admin.site.register(model_is_acronimo_of, Controllo_import_export)
admin.site.register(model_is_lemma_of, Controllo_import_export)
admin.site.register(model_is_ambito_riferimento_of, Controllo_import_export)
admin.site.register(model_is_autore_definizione_of, Controllo_import_export)
admin.site.register(model_is_posizione_definizione_of, Controllo_import_export)
admin.site.register(model_is_url_definizione_of, Controllo_import_export)
admin.site.register(model_is_titolo_documento_fonte_of, Controllo_import_export)
admin.site.register(model_is_autore_documento_fonte_of, Controllo_import_export)
admin.site.register(model_is_host_documento_fonte_of, Controllo_import_export)
admin.site.register(model_is_url_documento_fonte_of, Controllo_import_export)
admin.site.register(model_is_commento_entry_of, Controllo_import_export)
admin.site.register(model_is_data_inserimento_entry_of, Controllo_import_export)
admin.site.register(model_is_id_statico_entry_of, Controllo_import_export)
admin.site.register(model_is_admin_approval_switch_of, Controllo_import_export)

# per permettere l'esportazione delle tabelle relazionali e dela tabella delle entità

        # fields = ('id', 'name', 'price',) # per includere i campi
        # exclude = ('id','Data_inserimento_entry','Id_statico_entry','Admin_approval_switch' ) # per escludere i campi
        
class model_things_resource(resources.ModelResource):
    class Meta:
        model = model_things

class model_is_acronimo_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_acronimo_of

class model_is_lemma_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_lemma_of

class model_is_ambito_riferimento_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_ambito_riferimento_of

class model_is_autore_definizione_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_autore_definizione_of

class model_is_posizione_definizione_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_posizione_definizione_of

class model_is_url_definizione_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_url_definizione_of

class model_is_titolo_documento_fonte_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_titolo_documento_fonte_of

class model_is_autore_documento_fonte_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_autore_documento_fonte_of

class model_is_host_documento_fonte_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_autore_documento_fonte_of

class model_is_host_documento_fonte_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_url_documento_fonte_of

class model_is_commento_entry_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_commento_entry_of

class model_is_data_inserimento_entry_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_data_inserimento_entry_of

class model_is_id_statico_entry_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_id_statico_entry_of

class model_is_admin_approval_switch_of_resource(resources.ModelResource):
    class Meta:
        model = model_is_admin_approval_switch_of







