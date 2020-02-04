from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError #serve per far funzionare il "compila almeno un campo del form"



# Create your models here.



# Fare uno switch che permetta di inserire in modalità standard o avanzata
# queste sono gli unici valori che puo assumere
# implementerò un dropdown menu nella sezione admin
Admin_approval_switch_choices=[
    ("show","show"), # 1=valore da inserire negli script (=variabile), 2=valore assunto in relatà nel db
    ("hide","hide"),
    ]


class glossary_entry(models.Model):

    # If blank=True then the field will not be required, whereas if it's False the field cannot be blank.
    #This includes the admin and your own custom forms.
    # The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form, you're going to also need your database to allow NULL values for that field. The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').

    ### unità linguistiche ###
    # 11 linguistiche + data, id, + switch admin 14 in totale

    Lemma = models.CharField(max_length=256, blank=True, null=True)
    
    Acronimo = models.CharField(max_length=25, blank=True, null=True)

    Definizione = models.TextField(blank=True, null=True) # sostituire con textfield?
    
    Ambito_riferimento = models.CharField(max_length=256, blank=True, null=True)

    Autore_definizione = models.TextField(blank=True, null=True)
    
    Posizione_definizione = models.TextField(blank=True, null=True)
    
    Url_definizione = models.URLField(max_length=400, blank=True, null=True)
    
    Titolo_documento_fonte = models.TextField(blank=True, null=True)
    
    Autore_documento_fonte = models.TextField(blank=True, null=True)
    
    Host_documento_fonte = models.TextField(blank=True, null=True)
    
    Url_documento_fonte = models.URLField(max_length=400, blank=True, null=True)

    

    #### data e ID ####

    # default è un attributo che mi fa apparire quel valore di default nella sezione admin,
    # o meglio nel modello, quando creo un elemento.
    # poi ovviamente lo vedo subito nella sezione admin

    # il default nel modello fa comparire il valore selazionato quando creo il contenuto dall'admin 
    # e quando aggiungo l'attributo: viene automaticamente aggiunto a tutti gli elementi del modello

    Commento_entry = models.TextField(blank=True, null=True)

    Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now )
    # Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now)

    Id_statico_entry = models.CharField(max_length=256, blank=False, null=False, default="ITCH00000")


    # switch per far apparire le cose solo se revisionate dall'admin nella sessione del glossario.
    # posso avere solo due scelte per questo switch, le definisco a priori nella root del modulo

    Admin_approval_switch = models.CharField(max_length=30,blank=False, null=False, default=Admin_approval_switch_choices[1], choices=Admin_approval_switch_choices)



    class Meta:
        ordering = ['Admin_approval_switch', 'Lemma', 'Data_inserimento_entry', 'Id_statico_entry']
        # il meno davanti all'attributo vuol dire che ordina al contrario
        # '-Admin_approval_switch', 
        # faccio comparire per primi gli hide-> nuovi inseriti
        # in realtà per come ho definito hide e show, se metto senza il meno davanti, mi mostra per prima hide (h viene prima di s)

    def clean(self):
        if not (self.Lemma or self.Acronimo or self.Definizione or  self.Ambito_riferimento or self.Autore_definizione or self.Posizione_definizione or self.Url_definizione or self.Titolo_documento_fonte or self.Autore_documento_fonte or self.Host_documento_fonte or self.Url_documento_fonte or self.Commento_entry):
            raise ValidationError("Non è stata inserita alcuna terminologia. Compilare almeno un campo del form.")
        # non mi restituisce questa scritta ma quella messa di default nelle views

    def __str__(self):    
        # print("%s is %d years old." % (name, age))    
        return  "%s - %s ----- [%s] - [%s]"  %  (self.Lemma, self.Id_statico_entry, self.Data_inserimento_entry, self.Admin_approval_switch)  
        #quello che fa apparire nella sezione admin, attributo che riassume tutti gli altri, quindi una primary key presumibilmente, pouò anche esesere la combinazione degli altri





class glossary_file(models.Model):

    Glossary_file = models.FileField(upload_to='uploaded_glossaries/', blank=False, null=False)

    Data_inserimento_glossary = models.DateField(blank=False, null=False, default=timezone.now )
    # Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now().date)


    class Meta:
        ordering = ['Data_inserimento_glossary', 'Glossary_file']
        # il meno davanti all'attributo vuol dire che ordina al contrario
        # '-Admin_approval_switch', 
        # faccio comparire per primi gli hide-> nuovi inseriti
        # in realtà per come ho definito hide e show, se metto senza il meno davanti, mi mostra per prima hide (h viene prima di s)

    def clean(self):
        if not (self.Glossary_file or self.Data_inserimento_glossary):
            raise ValidationError("Non è stato selezionato alcun glossario per il caricamento.")
        # non mi restituisce questa scritta ma quella messa di default nelle views

    def __str__(self):    
        # print("%s is %d years old." % (name, age))    
        return  "%s ----- [%s]"  %  (self.Glossary_file, self.Data_inserimento_glossary)  
        #quello che fa apparire nella sezione admin, attributo che riassume tutti gli altri, quindi una primary key presumibilmente, pouò anche esesere la combinazione degli altri


# qui devo riversare la terminologia contenuta in glossary_entry e glossary_file
class acquired_terminology(models.Model):

    # If blank=True then the field will not be required, whereas if it's False the field cannot be blank.
    #This includes the admin and your own custom forms.
    # The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form, you're going to also need your database to allow NULL values for that field. The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').

    Lemma = models.CharField(max_length=256, blank=True, null=True)
    
    Acronimo = models.CharField(max_length=25, blank=True, null=True)

    Definizione = models.TextField(blank=True, null=True) # sostituire con textfield?
    
    Ambito_riferimento = models.CharField(max_length=256, blank=True, null=True)

    Autore_definizione = models.TextField(blank=True, null=True)
    
    Posizione_definizione = models.TextField(blank=True, null=True)
    
    Url_definizione = models.URLField(max_length=400, blank=True, null=True)
    
    Titolo_documento_fonte = models.TextField(blank=True, null=True)
    
    Autore_documento_fonte = models.TextField(blank=True, null=True)
    
    Host_documento_fonte = models.TextField(blank=True, null=True)
    
    Url_documento_fonte = models.URLField(max_length=400, blank=True, null=True)

    Commento_entry = models.TextField(blank=True, null=True)

    Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now )

    Id_statico_entry = models.CharField(max_length=256, blank=False, null=False, default="ITCH00000")

    Admin_approval_switch = models.CharField(max_length=30,blank=False, null=False, default=Admin_approval_switch_choices[1], choices=Admin_approval_switch_choices)

    class Meta:
        ordering = ['Admin_approval_switch', 'Lemma', 'Data_inserimento_entry', 'Id_statico_entry']

    def __str__(self):    
            
        return  "%s - %s ----- [%s] - [%s]"  %  (self.Lemma, self.Id_statico_entry, self.Data_inserimento_entry, self.Admin_approval_switch)  



class prepared_terminology(models.Model):

    # If blank=True then the field will not be required, whereas if it's False the field cannot be blank.
    #This includes the admin and your own custom forms.
    # The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form, you're going to also need your database to allow NULL values for that field. The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').

    Lemma = models.CharField(max_length=256, blank=True, null=True)
    
    Acronimo = models.CharField(max_length=25, blank=True, null=True)

    Definizione = models.TextField(blank=True, null=True) # sostituire con textfield?
    
    Ambito_riferimento = models.CharField(max_length=256, blank=True, null=True)

    Autore_definizione = models.TextField(blank=True, null=True)
    
    Posizione_definizione = models.TextField(blank=True, null=True)
    
    Url_definizione = models.URLField(max_length=400, blank=True, null=True)
    
    Titolo_documento_fonte = models.TextField(blank=True, null=True)
    
    Autore_documento_fonte = models.TextField(blank=True, null=True)
    
    Host_documento_fonte = models.TextField(blank=True, null=True)
    
    Url_documento_fonte = models.URLField(max_length=400, blank=True, null=True)

    Commento_entry = models.TextField(blank=True, null=True)

    Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now )

    Id_statico_entry = models.CharField(max_length=256, blank=False, null=False, default="ITCH00000")

    Admin_approval_switch = models.CharField(max_length=30,blank=False, null=False, default=Admin_approval_switch_choices[1], choices=Admin_approval_switch_choices)

    class Meta:
        ordering = ['Admin_approval_switch', 'Lemma', 'Data_inserimento_entry', 'Id_statico_entry']

    def __str__(self):    
            
        return  "%s - %s ----- [%s] - [%s]"  %  (self.Lemma, self.Id_statico_entry, self.Data_inserimento_entry, self.Admin_approval_switch)  




# Il modello displaying terminology dovrebbe servirmi a disporre la terminologia in modo analogo in quanto faceva l'algoritmo WD
# ossia, per ogi oggetto, pubblicava attaccati tutti gi oggetti correlati, mettendoli come cliccabili.
# questo è molto sconveniente e servirebbe uno specialista del front end per realizzare un pagnatore dei testi troppo lunghi generati in ogni campo.

# class displaying_terminology(models.Model):

#     # If blank=True then the field will not be required, whereas if it's False the field cannot be blank.
#     #This includes the admin and your own custom forms.
#     # The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form, you're going to also need your database to allow NULL values for that field. The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').

#     Lemma = models.CharField(max_length=256, blank=True, null=True)
    
#     Acronimo = models.CharField(max_length=25, blank=True, null=True)

#     Definizione = models.TextField(blank=True, null=True) # sostituire con textfield?
    
#     Ambito_riferimento = models.CharField(max_length=256, blank=True, null=True)

#     Autore_definizione = models.TextField(blank=True, null=True)
    
#     Posizione_definizione = models.TextField(blank=True, null=True)
    
#     Url_definizione = models.URLField(max_length=400, blank=True, null=True)
    
#     Titolo_documento_fonte = models.TextField(blank=True, null=True)
    
#     Autore_documento_fonte = models.TextField(blank=True, null=True)
    
#     Host_documento_fonte = models.TextField(blank=True, null=True)
    
#     Url_documento_fonte = models.URLField(max_length=400, blank=True, null=True)

#     Commento_entry = models.TextField(blank=True, null=True)

#     Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now )

#     Id_statico_entry = models.CharField(max_length=256, blank=False, null=False, default="ITCH00000")

#     Admin_approval_switch = models.CharField(max_length=30,blank=False, null=False, default=Admin_approval_switch_choices[1], choices=Admin_approval_switch_choices)




#     class Meta:
#         ordering = ['Admin_approval_switch', 'Lemma', 'Data_inserimento_entry', 'Id_statico_entry']

#     def __str__(self):    
            
#         return  "%s - %s ----- [%s] - [%s]"  %  (self.Lemma, self.Id_statico_entry, self.Data_inserimento_entry, self.Admin_approval_switch)  
