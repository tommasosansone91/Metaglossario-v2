function concatena_s(id, string1, string2) {

    // unisce due stringhe in ingresso e incolla la risultante

    var c_string = string1 + string2;
    
    document.getElementById(id).href = c_string;

    }

function concatena_1(id){

    // dai l'id dell'elemento che contiene nell'href l'url del glossario
    // la funzione prende l'url del glossario messo in href e lo concatena con la scrittura dell'id tatico entry 

    var url_glossario = document.getElementById(id).href

    var string2 = "?q={{ entry.Id_statico_entry }}"

    var c_string = url_glossario + string2;
    
    document.getElementById(id).href = c_string;

    }