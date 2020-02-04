from django import forms
from .models import glossary_entry
from .models import glossary_file


class glossary_entry_form(forms.ModelForm):
                
    class Meta:
        model = glossary_entry
        fields = ["Lemma", "Acronimo", "Definizione", "Ambito_riferimento", "Autore_definizione", "Posizione_definizione", "Url_definizione", "Titolo_documento_fonte", "Autore_documento_fonte", "Host_documento_fonte", "Url_documento_fonte", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"]


class glossary_file_form(forms.ModelForm):

    class Meta:
        model = glossary_file
        fields = ["Glossary_file", "Data_inserimento_glossary"]






