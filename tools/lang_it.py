# -*- coding: utf-8 -*-
# Set di item italiano per la Bussola professionale. Stessa struttura e ordine di make_busola_pdf.py.
TYPES = ["R", "I", "A", "S", "E", "C"]
TYPE_NAME = {"R": "Realistico", "I": "Investigativo", "A": "Artistico", "S": "Sociale", "E": "Intraprendente",
             "C": "Convenzionale"}
TYPE_DESC = {
    "R": "lavorare con le mani, attrezzi, macchine, natura; risultati concreti",
    "I": "analizzare, fare ricerca, capire come funzionano le cose",
    "A": "creare, esprimersi, progettare, lavorare senza regole fisse",
    "S": "insegnare, sostenere, assistere e consigliare le persone",
    "E": "convincere, guidare, vendere, assumersi rischi",
    "C": "struttura, dati, procedure, precisione e controllo",
}

INT = {
    "R": ["Riparare o fare la manutenzione di apparecchi, macchine o dispositivi.",
          "Montare, collegare e mettere in funzione un impianto tecnico.",
          "Lavorare con gli attrezzi in un'officina (legno, metallo, elettronica).",
          "Lavorare all'aperto: in un cantiere, in un bosco o in una fattoria.",
          "Guidare o manovrare veicoli, droni o macchinari.",
          "Costruire qualcosa di fisico da zero, seguendo un progetto.",
          "Scoprire perché un dispositivo non funziona e ripararlo con le proprie mani.",
          "Prendersi cura di piante, animali o di un terreno."],
    "I": ["Analizzare dati per trovare una tendenza o una causa nascosta.",
          "Capire a fondo come funziona un sistema complesso.",
          "Fare esperimenti e verificare ipotesi.",
          "Leggere studi scientifici o tecnici del proprio settore.",
          "Risolvere un difficile problema logico che non ha ancora una soluzione.",
          "Costruire un modello matematico o statistico.",
          "Indagare sulla causa principale di un guasto o di un incidente.",
          "Imparare da solo/a una nuova tecnologia o teoria fino a padroneggiarla."],
    "A": ["Progettare l'aspetto visivo di un prodotto, di un'app o di uno spazio.",
          "Scrivere testi, racconti o articoli.",
          "Comporre, cantare o produrre musica.",
          "Fotografare, filmare o montare video.",
          "Inventare un concetto o un'idea completamente nuova.",
          "Recitare, presentare o improvvisare davanti a un pubblico.",
          "Lavorare senza regole fisse, dove conta lo stile personale.",
          "Disegnare, dipingere o creare oggetti decorativi."],
    "S": ["Spiegare qualcosa di complicato a chi sta appena iniziando.",
          "Aiutare una persona ad attraversare un periodo difficile.",
          "Tenere un corso o un workshop.",
          "Assistere persone malate, anziane o con disabilità.",
          "Fare da mediatore in un conflitto tra due persone.",
          "Fare da mentore a un/una collega più giovane.",
          "Lavorare a un progetto che migliora la vita di una comunità.",
          "Ascoltare e consigliare le persone che Le chiedono consiglio."],
    "E": ["Convincere un cliente a scegliere la Sua soluzione.",
          "Guidare un team verso un obiettivo ambizioso.",
          "Avviare un'attività o un progetto proprio.",
          "Negoziare un contratto, un prezzo o uno stipendio.",
          "Presentare un'idea alla direzione per ottenere un budget.",
          "Prendere decisioni rapide con informazioni incomplete.",
          "Costruire una rete di contatti professionali.",
          "Competere per risultati misurabili (vendite, quota di mercato)."],
    "C": ["Tenere una registrazione precisa di cifre, documenti o scorte.",
          "Verificare che un processo rispetti regole e standard.",
          "Organizzare informazioni in tabelle, banche dati o archivi.",
          "Preparare budget, fatture o rapporti finanziari.",
          "Seguire una procedura chiara, passo dopo passo, senza errori.",
          "Pianificare calendari, scadenze e risorse.",
          "Controllare la qualità di un prodotto o di una documentazione.",
          "Mettere ordine in un sistema caotico di file, dati o processi."],
}

CONF = {
    "R": ["Riparare un apparecchio elettrico o elettronico.",
          "Usare in sicurezza gli utensili elettrici.",
          "Leggere un disegno tecnico e lavorare seguendolo.",
          "Montare un mobile o un impianto semplice senza istruzioni dettagliate."],
    "I": ["Analizzare un insieme di dati e trarre conclusioni corrette.",
          "Capire un articolo scientifico o una documentazione tecnica complessa.",
          "Trovare la causa di un problema complesso escludendo sistematicamente le ipotesi.",
          "Applicare la statistica o la matematica a un problema reale."],
    "A": ["Creare un design visivo dall'aspetto professionale.",
          "Scrivere un testo che cattura l'attenzione.",
          "Avere idee originali quando gli altri sono bloccati.",
          "Esprimere un'idea attraverso immagini, suoni o movimento."],
    "S": ["Insegnare qualcosa a un gruppo in modo che tutti capiscano.",
          "Calmare una persona agitata.",
          "Capire che cosa prova qualcuno senza che lo dica.",
          "Sostenere qualcuno nel raggiungere un obiettivo personale."],
    "E": ["Convincere un gruppo scettico.",
          "Condurre una riunione fino a una decisione.",
          "Negoziare un accordo vantaggioso per sé.",
          "Vendere un prodotto o un servizio."],
    "C": ["Gestire un budget o una contabilità senza errori.",
          "Creare un sistema di organizzazione usato anche da altri.",
          "Lavorare con fogli Excel complessi.",
          "Rispettare scadenze e procedure rigorose."],
}

ANCHORS = [
    ("TF", "Competenza tecnico-funzionale",
     ["Voglio diventare un/una esperto/a ricercato/a nella mia specializzazione.",
      "Mi sento più realizzato/a quando uso ad alto livello le mie competenze specialistiche.",
      "Rifiuterei una promozione che mi portasse fuori dal mio campo di competenza."],
     "L'identità professionale nasce dall'essere molto bravi in un campo. Cerchi ruoli da esperto e percorsi tecnici, "
     "non solo manageriali. Attenzione alle promozioni verso il puro management."),
    ("GM", "Competenza manageriale generale",
     ["Voglio arrivare a dirigere un'intera organizzazione o un reparto.",
      "Mi attira la responsabilità dei risultati di un intero team.",
      "Preferisco integrare il lavoro degli altri piuttosto che essere specialista di una sola cosa."],
     "La motivano la responsabilità, l'integrazione e i risultati dell'organizzazione. Cerchi ruoli con un team e un "
     "budget. Attenzione ai ruoli da specialista isolato."),
    ("AU", "Autonomia / indipendenza",
     ["Voglio decidere io come, quando e dove lavorare.",
      "Le regole e le procedure rigide delle organizzazioni mi pesano.",
      "Rinuncerei alla sicurezza di un posto fisso per avere più libertà."],
     "Ha bisogno di controllare il proprio modo di lavorare. Cerchi freelance, consulenza, lavoro da remoto, obiettivi "
     "chiari con libertà nell'esecuzione. Attenzione al micromanagement."),
    ("SE", "Sicurezza / stabilità",
     ["La sicurezza del posto di lavoro e del reddito è molto importante per me.",
      "Preferisco un datore di lavoro stabile, anche se avanzo più lentamente.",
      "Mi rassicura sapere che cosa mi aspetta nei prossimi anni."],
     "La prevedibilità Le dà calma ed energia. Cerchi grandi datori di lavoro o il settore pubblico, contratti a "
     "tempo indeterminato, benefici chiari. Attenzione ai redditi variabili e alle start-up rischiose."),
    ("EC", "Creatività imprenditoriale",
     ["Sogno di creare qualcosa di completamente mio: un'azienda, un prodotto.",
      "Mi motiva trasformare un'idea in un'attività che funziona.",
      "Sono disposto/a a rischiare per costruire qualcosa di nuovo."],
     "Vuole creare qualcosa di Suo. Cerchi la fondazione di un'azienda, l'imprenditorialità interna, il lancio di "
     "prodotti. Attenzione ai ruoli in cui si limita a mantenere ciò che altri hanno creato."),
    ("SV", "Servizio / dedizione a una causa",
     ["Voglio che il mio lavoro contribuisca a una causa in cui credo.",
      "Sceglierei un posto meno pagato se aiutasse le persone o l'ambiente.",
      "Il senso di ciò che faccio conta più del titolo o del denaro."],
     "Contano il senso e l'impatto. Cerchi ONG, settore pubblico, sanità, istruzione, sostenibilità o aziende con una "
     "missione chiara. Attenzione agli ambienti orientati solo al profitto."),
    ("CH", "Sfida pura",
     ["Mi attirano i problemi che gli altri considerano impossibili.",
      "Mi annoio presto quando il lavoro diventa routine.",
      "La competizione e i grandi ostacoli mi danno energia."],
     "I problemi difficili Le danno energia. Cerchi progetti di trasformazione, consulenza, situazioni di crisi, "
     "obiettivi ambiziosi. Attenzione alla routine."),
    ("LS", "Stile di vita",
     ["Voglio una carriera che si adatti alla mia vita privata e alla mia famiglia, non il contrario.",
      "Rifiuterei un trasferimento o una promozione che squilibrasse la mia vita privata.",
      "Gli orari flessibili per me sono una condizione, non un bonus."],
     "La carriera deve integrarsi nella vita. Cerchi orari flessibili, tempo parziale, lavoro da remoto, datori di "
     "lavoro con una cultura dell'equilibrio. Attenzione alle culture del «sempre reperibili»."),
]

B5 = [  # Mini-IPIP (Donnellan et al., 2006), traduzione propria, ordine originale
    ("E", "+", "Spesso sono l'anima della festa."),
    ("A", "+", "Sono sensibile ai sentimenti degli altri."),
    ("C", "+", "Sbrigo subito le mie faccende."),
    ("N", "+", "Ho frequenti sbalzi d'umore."),
    ("O", "+", "Ho una fervida immaginazione."),
    ("E", "−", "Non parlo molto."),
    ("A", "−", "I problemi degli altri non mi interessano."),
    ("C", "−", "Spesso dimentico di rimettere le cose al loro posto."),
    ("N", "−", "Sono rilassato/a quasi sempre."),
    ("O", "−", "Le idee astratte non mi interessano."),
    ("E", "+", "Alle feste parlo con molte persone diverse."),
    ("A", "+", "Sento le emozioni degli altri."),
    ("C", "+", "Mi piace l'ordine."),
    ("N", "+", "Mi arrabbio facilmente."),
    ("O", "−", "Faccio fatica a capire le idee astratte."),
    ("E", "−", "Di solito resto in disparte."),
    ("A", "−", "Gli altri non mi interessano davvero."),
    ("C", "−", "Combino spesso pasticci."),
    ("N", "−", "Raramente mi sento giù."),
    ("O", "−", "Non ho una buona immaginazione."),
]
B5_NAME = {"E": "Estroversione", "A": "Gradevolezza", "C": "Coscienziosità", "N": "Nevroticismo",
           "O": "Intelletto / immaginazione"}

SDT = {
    "Autonomia": ["Potevo decidere in gran parte come organizzare il mio lavoro.",
                  "Sentivo di fare ciò che facevo per scelta, non per obbligo.",
                  "Le mie idee e opinioni venivano prese in considerazione."],
    "Competenza": ["Mi sentivo capace ed efficace in ciò che facevo.",
                   "Avevo l'occasione di imparare cose nuove e di crescere.",
                   "Ricevevo segnali chiari di fare un buon lavoro."],
    "Relazione": ["Mi sentivo parte di un team.",
                  "Al lavoro avevo persone di cui mi fidavo.",
                  "Tenevo ai miei colleghi e sentivo che anche loro tenevano a me."],
}

CTX = [
    ("Lavoro meglio da solo/a", "Lavoro meglio in team"),
    ("Compiti chiari e ben definiti", "Problemi aperti e ambigui"),
    ("Ritmo costante e prevedibile", "Ritmo serrato, con urgenze"),
    ("In ufficio o da casa", "Sul campo, in movimento"),
    ("Pochi contatti con i clienti", "Contatto quotidiano con i clienti"),
    ("Grande organizzazione strutturata", "Piccola organizzazione flessibile"),
    ("Specialista in profondità", "Generalista, molti temi"),
    ("Risultati a lungo termine", "Risultati rapidi e visibili"),
    ("Contributore individuale", "Responsabile di persone"),
    ("Stipendio fisso e prevedibile", "Reddito variabile, legato ai risultati"),
]

ADAPT = {
    "Preoccupazione (guardare avanti)": ["Penso a come sarà il mio lavoro tra cinque anni.",
                                         "Preparo per tempo i prossimi passi della mia carriera.",
                                         "So quali competenze saranno richieste nel mio settore."],
    "Controllo (decide Lei)": ["Prendo io le decisioni importanti sulla mia carriera.",
                               "Mi assumo la responsabilità del mio percorso professionale.",
                               "Resto fedele alle mie convinzioni quando decido."],
    "Curiosità (esplorare)": ["Esploro attivamente nuove opzioni professionali.",
                              "Cerco occasioni per imparare al di fuori del mio ruolo.",
                              "Chiedo agli altri come si lavora nei loro settori."],
    "Fiducia (può farcela)": ["Porto a termine i compiti anche quando sono difficili.",
                              "Imparo in fretta nuove competenze quando serve.",
                              "Trovo soluzioni quando le cose non vanno come previsto."],
}

OPEN = [
    ("Modello", "Chi ammirava da bambino/a o da adolescente (oltre ai Suoi genitori)? Che cosa ammirava esattamente?",
     "il sé ideale: le qualità che vuole incarnare"),
    ("Media preferiti", "Quali riviste, siti, canali o podcast segue volentieri? Che cosa La attira?",
     "gli ambienti e i tipi di problemi che La attirano"),
    ("Storia preferita", "Qual è la Sua storia preferita (libro, film, serie)? La racconti brevemente.",
     "il copione che potrebbe seguire per andare avanti"),
    ("Motto", "Ha un motto o un detto che La guida?", "il consiglio che dà a sé stesso/a"),
    ("Flow", "Quando ha perso l'ultima volta la cognizione del tempo lavorando a qualcosa? Che cosa stava facendo?",
     "un'attività con forte motivazione intrinseca"),
]

OCC = [
    ("Sviluppatore/trice software", "ICR"), ("Architetto/a IT / di soluzioni", "IEC"),
    ("Ingegnere/a DevOps / cloud", "RIC"), ("Data scientist", "ICA"), ("Data engineer", "CIR"),
    ("Specialista in sicurezza informatica", "CIE"), ("Amministratore/trice di sistemi e reti", "RCI"),
    ("Business analyst", "ICE"), ("Capo progetto IT", "ECI"), ("Product owner / product manager", "EIA"),
    ("Consulente IT", "EIC"), ("Scrum master / agile coach", "SEI"), ("Designer UX/UI", "AIE"),
    ("Redattore/trice tecnico/a", "AIC"), ("Formatore/trice IT per adulti", "SIE"),
    ("Insegnante di informatica", "SIA"), ("Auditor / responsabile qualità", "CIR"),
    ("Ingegnere/a elettrico/a", "IRC"), ("Ingegnere/a meccanico/a", "RIC"), ("Ingegnere/a civile", "RIC"),
    ("Ingegnere/a dell'automazione", "RIC"), ("Meccatronico/a", "RCI"), ("Elettricista", "RIC"),
    ("Consulente energetico/a", "IER"), ("Ingegnere/a ambientale", "IRS"), ("Laboratorista", "IRC"),
    ("Ricercatore/trice scientifico/a", "IAR"), ("Architetto/a", "AIR"), ("Grafico/a", "AER"),
    ("Fotografo/a / videomaker", "ARE"), ("Giornalista", "AES"), ("Traduttore/trice", "AIC"),
    ("Musicista", "AES"), ("Insegnante", "SAE"), ("Assistente sociale", "SEA"),
    ("Consulente di orientamento", "SAI"), ("Psicologo/a", "ISA"), ("Infermiere/a", "SIR"),
    ("Fisioterapista", "SRI"), ("Medico", "ISR"), ("Specialista HR / recruiter", "SEC"),
    ("Consulente di vendita", "ESC"), ("Key account manager", "ECS"),
    ("Imprenditore/trice / fondatore/trice", "EAI"), ("Responsabile marketing", "EAC"),
    ("Contabile / fiduciario/a", "CEI"), ("Controller finanziario", "CIE"),
    ("Impiegato/a amministrativo/a", "CES"), ("Logistico/a / supply chain", "CER"),
    ("Specialista alberghiero/a", "ESC"), ("Cuoco/a", "RAE"), ("Agente di polizia", "RES"),
    ("Giardiniere/a paesaggista", "RAC"), ("Falegname", "RAC"), ("Forestale", "RIS"), ("Pilota", "RIE"),
]

SC_LIKE = ["Per niente", "Poco", "Neutrale", "Molto", "Moltissimo"]
SC_CONF = ["Per niente sicuro/a: mai fatto", "Poco: provato, con fatica", "Abbastanza: con un po' d'aiuto",
           "Sicuro/a: fatto da solo/a", "Molto sicuro/a: gli altri mi chiedono aiuto"]
SC_TRUE = ["Per niente vero", "Poco vero", "In parte vero", "Per lo più vero", "Del tutto vero"]
SC_DESC = ["Per niente", "Poco", "In parte", "In gran parte", "Molto bene"]
SC_STR = ["Per niente", "Debole", "Moderato", "Forte", "Molto forte"]

n_int = 0
