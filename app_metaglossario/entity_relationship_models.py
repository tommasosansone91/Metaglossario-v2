from django.db import models

# Tabella delle entità


class model_things(models.Model): 

    id_thing = models.CharField(max_length=10, primary_key=True)
    thing = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['id_thing', 'thing']

    def __str__(self):                
        return  "[ %s ] : %s"  %  (self.id_thing, self.thing)


# Tabelle relazionali
class model_is_acronimo_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)


class model_is_lemma_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)



class model_is_ambito_riferimento_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)



class model_is_autore_definizione_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)



class model_is_posizione_definizione_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)



class model_is_url_definizione_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)


class model_is_titolo_documento_fonte_of(models.Model): 
    
    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)


class model_is_autore_documento_fonte_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)



class model_is_host_documento_fonte_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)



class model_is_url_documento_fonte_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)



class model_is_commento_entry_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)



class model_is_data_inserimento_entry_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)



class model_is_id_statico_entry_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)



class model_is_admin_approval_switch_of(models.Model): 

    id_soggetto = models.CharField(max_length=10)
    id_oggetto = models.CharField(max_length=10)

    class Meta:
        ordering = ['id_soggetto', 'id_oggetto']

    def __str__(self):                
        return  "[ %s ] <---> [ %s ]"  %  (self.id_soggetto, self.id_oggetto)



