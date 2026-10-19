# -*- coding: utf-8 -*-
# Jeu d'items français pour la Boussole de carrière. Même structure et même ordre que make_busola_pdf.py.
TYPES = ["R", "I", "A", "S", "E", "C"]
TYPE_NAME = {"R": "Réaliste", "I": "Investigateur", "A": "Artistique", "S": "Social", "E": "Entreprenant",
             "C": "Conventionnel"}
TYPE_DESC = {
    "R": "travailler de ses mains, avec des outils, des machines, dans la nature ; résultats concrets",
    "I": "analyser, rechercher, comprendre comment les choses fonctionnent",
    "A": "créer, s'exprimer, concevoir, travailler sans règles fixes",
    "S": "enseigner, soutenir, prendre soin des autres et les conseiller",
    "E": "convaincre, diriger, vendre, prendre des risques",
    "C": "structure, données, procédures, précision et contrôle",
}

INT = {
    "R": ["Réparer ou entretenir des équipements, des machines ou des appareils.",
          "Monter, raccorder et mettre en service une installation technique.",
          "Travailler avec des outils dans un atelier (bois, métal, électronique).",
          "Travailler en plein air : sur un chantier, en forêt ou dans une ferme.",
          "Conduire ou piloter des véhicules, des drones ou des engins.",
          "Construire quelque chose de physique à partir de zéro, selon un plan.",
          "Trouver pourquoi un appareil ne fonctionne pas et le réparer de vos mains.",
          "Prendre soin de plantes, d'animaux ou d'un terrain."],
    "I": ["Analyser des données pour trouver une tendance ou une cause cachée.",
          "Comprendre en profondeur le fonctionnement d'un système complexe.",
          "Mener des expériences et tester des hypothèses.",
          "Lire des études scientifiques ou techniques de votre domaine.",
          "Résoudre un problème logique difficile qui n'a pas encore de solution.",
          "Construire un modèle mathématique ou statistique.",
          "Rechercher la cause première d'une panne ou d'un incident.",
          "Apprendre seul(e) une nouvelle technologie ou théorie jusqu'à la maîtriser."],
    "A": ["Concevoir l'aspect visuel d'un produit, d'une application ou d'un espace.",
          "Écrire des textes, des histoires ou des articles.",
          "Composer, chanter ou produire de la musique.",
          "Photographier, filmer ou monter des vidéos.",
          "Inventer un concept ou une idée entièrement nouvelle.",
          "Jouer un rôle, présenter ou improviser devant un public.",
          "Travailler sans règles fixes, là où le style personnel compte.",
          "Dessiner, peindre ou créer des objets décoratifs."],
    "S": ["Expliquer quelque chose de compliqué à quelqu'un qui débute.",
          "Aider une personne à traverser une période difficile.",
          "Donner un cours ou animer un atelier.",
          "Prendre soin de personnes malades, âgées ou en situation de handicap.",
          "Servir de médiateur dans un conflit entre deux personnes.",
          "Être le mentor d'un(e) collègue plus jeune.",
          "Travailler sur un projet qui améliore la vie d'une communauté.",
          "Écouter et conseiller des personnes qui vous demandent conseil."],
    "E": ["Convaincre un client de choisir votre solution.",
          "Mener une équipe vers un objectif ambitieux.",
          "Lancer votre propre entreprise ou votre propre projet.",
          "Négocier un contrat, un prix ou un salaire.",
          "Présenter une idée à la direction pour obtenir un budget.",
          "Prendre des décisions rapides avec des informations incomplètes.",
          "Développer un réseau de contacts professionnels.",
          "Rivaliser pour des résultats mesurables (ventes, parts de marché)."],
    "C": ["Tenir un relevé exact des chiffres, des documents ou des stocks.",
          "Vérifier qu'un processus respecte les règles et les normes.",
          "Organiser des informations dans des tableaux, des bases de données ou des archives.",
          "Établir des budgets, des factures ou des rapports financiers.",
          "Suivre une procédure claire, étape par étape, sans erreur.",
          "Planifier des calendriers, des délais et des ressources.",
          "Contrôler la qualité d'un produit ou d'une documentation.",
          "Mettre de l'ordre dans un système chaotique de fichiers, de données ou de processus."],
}

CONF = {
    "R": ["Réparer un appareil électrique ou électronique.",
          "Utiliser des outils électriques en toute sécurité.",
          "Lire un plan technique et travailler d'après lui.",
          "Monter un meuble ou une installation simple sans instructions détaillées."],
    "I": ["Analyser un jeu de données et en tirer des conclusions correctes.",
          "Comprendre un article scientifique ou une documentation technique dense.",
          "Trouver la cause d'un problème complexe en éliminant systématiquement les hypothèses.",
          "Appliquer les statistiques ou les mathématiques à un problème réel."],
    "A": ["Créer un design visuel d'aspect professionnel.",
          "Écrire un texte qui capte l'attention.",
          "Avoir des idées originales quand les autres sont bloqués.",
          "Exprimer une idée par l'image, le son ou le mouvement."],
    "S": ["Enseigner quelque chose à un groupe pour que tout le monde comprenne.",
          "Calmer une personne contrariée.",
          "Percevoir ce que quelqu'un ressent sans qu'il ou elle le dise.",
          "Aider quelqu'un à atteindre un objectif personnel."],
    "E": ["Convaincre un groupe sceptique.",
          "Conduire une réunion jusqu'à une décision.",
          "Négocier un accord avantageux pour vous.",
          "Vendre un produit ou un service."],
    "C": ["Tenir un budget ou une comptabilité sans erreur.",
          "Créer un système de classement que d'autres utilisent aussi.",
          "Travailler avec des tableaux Excel complexes.",
          "Respecter des délais et des procédures stricts."],
}

ANCHORS = [
    ("TF", "Compétence technique / fonctionnelle",
     ["Je veux devenir un(e) expert(e) recherché(e) dans ma spécialité.",
      "Je me sens le plus épanoui(e) quand j'utilise mes compétences spécialisées à un haut niveau.",
      "Je refuserais une promotion qui me ferait sortir de mon domaine d'expertise."],
     "Votre identité professionnelle vient du fait d'être très bon(ne) dans un domaine. Cherchez des rôles d'expert "
     "et des filières techniques, pas seulement managériales. Méfiez-vous des promotions vers le management pur."),
    ("GM", "Management général",
     ["Je veux un jour diriger toute une organisation ou un département.",
      "La responsabilité des résultats de toute une équipe m'attire.",
      "Je préfère intégrer le travail des autres plutôt qu'être spécialiste d'une seule chose."],
     "Vous êtes motivé(e) par la responsabilité, l'intégration et les résultats de l'organisation. Cherchez des rôles "
     "avec une équipe et un budget. Méfiez-vous des rôles de spécialiste isolé."),
    ("AU", "Autonomie / indépendance",
     ["Je veux décider moi-même comment, quand et où je travaille.",
      "Les règles et procédures rigides des organisations me pèsent.",
      "Je renoncerais à la sécurité d'un poste fixe pour plus de liberté."],
     "Vous avez besoin de maîtriser votre façon de travailler. Cherchez le freelancing, le conseil, le télétravail, "
     "des objectifs clairs avec liberté d'exécution. Méfiez-vous du micromanagement."),
    ("SE", "Sécurité / stabilité",
     ["La sécurité de l'emploi et du revenu est très importante pour moi.",
      "Je préfère un employeur stable, même si j'avance plus lentement.",
      "Cela me rassure de savoir à quoi m'attendre dans les années à venir."],
     "La prévisibilité vous apporte calme et énergie. Cherchez de grands employeurs ou le secteur public, des "
     "contrats à durée indéterminée, des avantages clairs. Méfiez-vous des revenus variables et des start-up risquées."),
    ("EC", "Créativité entrepreneuriale",
     ["Je rêve de créer quelque chose d'entièrement à moi : une entreprise, un produit.",
      "Transformer une idée en une affaire qui fonctionne me motive.",
      "Je suis prêt(e) à prendre des risques pour construire quelque chose de nouveau."],
     "Vous voulez créer quelque chose à vous. Cherchez la création d'entreprise, l'intrapreneuriat, les lancements "
     "de produits. Méfiez-vous des rôles où vous ne faites qu'entretenir ce que d'autres ont créé."),
    ("SV", "Service / dévouement à une cause",
     ["Je veux que mon travail contribue à une cause en laquelle je crois.",
      "Je choisirais un poste moins bien payé s'il aidait les gens ou l'environnement.",
      "Le sens de ce que je fais compte plus que le titre ou l'argent."],
     "Le sens et l'impact comptent. Cherchez les ONG, le secteur public, la santé, l'éducation, la durabilité ou des "
     "entreprises à mission claire. Méfiez-vous des environnements uniquement orientés vers le profit."),
    ("CH", "Défi pur",
     ["Les problèmes que d'autres jugent impossibles m'attirent.",
      "Je m'ennuie vite quand le travail devient routinier.",
      "La compétition et les grands obstacles me donnent de l'énergie."],
     "Les problèmes difficiles vous donnent de l'énergie. Cherchez des projets de transformation, le conseil, les "
     "situations de crise, des objectifs ambitieux. Méfiez-vous de la routine."),
    ("LS", "Style de vie",
     ["Je veux une carrière qui s'adapte à ma vie personnelle et à ma famille, et non l'inverse.",
      "Je refuserais un déménagement ou une promotion qui déséquilibrerait ma vie privée.",
      "Des horaires flexibles sont pour moi une condition, pas un bonus."],
     "Votre carrière doit s'intégrer à votre vie. Cherchez des horaires flexibles, le temps partiel, le télétravail, "
     "des employeurs attachés à l'équilibre. Méfiez-vous des cultures de disponibilité permanente."),
]

B5 = [  # Mini-IPIP (Donnellan et al., 2006), traduction propre, ordre original
    ("E", "+", "Je suis souvent l'âme de la fête."),
    ("A", "+", "Je suis sensible aux sentiments des autres."),
    ("C", "+", "Je fais mes tâches tout de suite."),
    ("N", "+", "J'ai souvent des sautes d'humeur."),
    ("O", "+", "J'ai une imagination débordante."),
    ("E", "−", "Je ne parle pas beaucoup."),
    ("A", "−", "Les problèmes des autres ne m'intéressent pas."),
    ("C", "−", "J'oublie souvent de remettre les choses à leur place."),
    ("N", "−", "Je suis détendu(e) la plupart du temps."),
    ("O", "−", "Les idées abstraites ne m'intéressent pas."),
    ("E", "+", "En soirée, je parle à beaucoup de gens différents."),
    ("A", "+", "Je ressens les émotions des autres."),
    ("C", "+", "J'aime l'ordre."),
    ("N", "+", "Je me fâche facilement."),
    ("O", "−", "J'ai du mal à comprendre les idées abstraites."),
    ("E", "−", "Je reste en retrait."),
    ("A", "−", "Les autres ne m'intéressent pas vraiment."),
    ("C", "−", "Je mets souvent la pagaille."),
    ("N", "−", "Je me sens rarement déprimé(e)."),
    ("O", "−", "Je n'ai pas beaucoup d'imagination."),
]
B5_NAME = {"E": "Extraversion", "A": "Agréabilité", "C": "Conscienciosité", "N": "Névrosisme",
           "O": "Intellect / imagination"}

SDT = {
    "Autonomie": ["Je pouvais décider en grande partie comment organiser mon travail.",
                  "J'avais le sentiment de faire ce que je faisais par choix, et non par obligation.",
                  "Mes idées et mes opinions étaient prises en compte."],
    "Compétence": ["Je me sentais capable et efficace dans ce que je faisais.",
                   "J'avais l'occasion d'apprendre de nouvelles choses et de progresser.",
                   "Je recevais des signaux clairs que je faisais du bon travail."],
    "Appartenance": ["Je me sentais membre d'une équipe.",
                     "J'avais au travail des personnes en qui j'avais confiance.",
                     "Je tenais à mes collègues et je sentais que je comptais aussi pour eux."],
}

CTX = [
    ("Je travaille mieux seul(e)", "Je travaille mieux en équipe"),
    ("Tâches claires et bien définies", "Problèmes ouverts et ambigus"),
    ("Rythme régulier et prévisible", "Rythme soutenu, avec des urgences"),
    ("Au bureau ou à domicile", "Sur le terrain, en déplacement"),
    ("Peu de contact avec les clients", "Contact quotidien avec les clients"),
    ("Grande organisation structurée", "Petite organisation flexible"),
    ("Spécialiste en profondeur", "Généraliste, nombreux sujets"),
    ("Résultats à long terme", "Résultats rapides et visibles"),
    ("Contributeur individuel", "Responsable d'équipe"),
    ("Salaire fixe et prévisible", "Revenu variable, lié à la performance"),
]

ADAPT = {
    "Préoccupation (regarder devant)": ["Je réfléchis à ce que sera mon travail dans cinq ans.",
                                        "Je prépare à temps les prochaines étapes de ma carrière.",
                                        "Je sais quelles compétences seront demandées dans mon domaine."],
    "Contrôle (vous décidez)": ["Je prends moi-même les décisions importantes concernant ma carrière.",
                                "J'assume la responsabilité de mon parcours professionnel.",
                                "Je reste fidèle à mes convictions quand je décide."],
    "Curiosité (explorer)": ["J'explore activement de nouvelles options professionnelles.",
                             "Je cherche des occasions d'apprendre en dehors de mon rôle.",
                             "Je demande aux autres comment on travaille dans leur domaine."],
    "Confiance (vous pouvez)": ["Je mène les tâches à bien même quand elles sont difficiles.",
                                "J'apprends vite de nouvelles compétences quand c'est nécessaire.",
                                "Je trouve des solutions quand les choses ne se passent pas comme prévu."],
}

OPEN = [
    ("Modèle", "Qui admiriez-vous enfant ou adolescent(e) (en dehors de vos parents) ? Qu'admiriez-vous exactement ?",
     "le soi idéal : les qualités que vous voulez incarner"),
    ("Médias préférés", "Quels magazines, sites, chaînes ou podcasts suivez-vous avec plaisir ? Qu'est-ce qui vous y "
     "attire ?", "les environnements et les types de problèmes qui vous attirent"),
    ("Histoire préférée", "Quelle est votre histoire préférée (livre, film, série) ? Racontez-la brièvement.",
     "le scénario que vous pourriez suivre pour avancer"),
    ("Devise", "Avez-vous une devise ou un dicton qui vous guide ?", "le conseil que vous vous donnez"),
    ("Flow", "Quand avez-vous oublié le temps pour la dernière fois en travaillant sur quelque chose ? Que "
     "faisiez-vous ?", "une activité à forte motivation intrinsèque"),
]

OCC = [
    ("Développeur/euse de logiciels", "ICR"), ("Architecte IT / de solutions", "IEC"),
    ("Ingénieur(e) DevOps / cloud", "RIC"), ("Data scientist", "ICA"), ("Ingénieur(e) de données", "CIR"),
    ("Spécialiste en sécurité informatique", "CIE"), ("Administrateur/trice systèmes et réseaux", "RCI"),
    ("Analyste métier (business analyst)", "ICE"), ("Chef(fe) de projet informatique", "ECI"),
    ("Product owner / chef(fe) de produit", "EIA"), ("Consultant(e) IT", "EIC"),
    ("Scrum master / coach agile", "SEI"), ("Designer UX/UI", "AIE"), ("Rédacteur/trice technique", "AIC"),
    ("Formateur/trice IT pour adultes", "SIE"), ("Enseignant(e) d'informatique", "SIA"),
    ("Auditeur/trice / responsable qualité", "CIR"), ("Ingénieur(e) en électricité", "IRC"),
    ("Ingénieur(e) en mécanique", "RIC"), ("Ingénieur(e) civil(e)", "RIC"),
    ("Ingénieur(e) en automatisation", "RIC"), ("Mécatronicien(ne)", "RCI"), ("Électricien(ne)", "RIC"),
    ("Conseiller/ère en énergie", "IER"), ("Ingénieur(e) en environnement", "IRS"), ("Laborantin(e)", "IRC"),
    ("Chercheur/euse scientifique", "IAR"), ("Architecte", "AIR"), ("Graphiste", "AER"),
    ("Photographe / vidéaste", "ARE"), ("Journaliste", "AES"), ("Traducteur/trice", "AIC"),
    ("Musicien(ne)", "AES"), ("Enseignant(e)", "SAE"), ("Travailleur/euse social(e)", "SEA"),
    ("Conseiller/ère en orientation", "SAI"), ("Psychologue", "ISA"), ("Infirmier/ère", "SIR"),
    ("Physiothérapeute", "SRI"), ("Médecin", "ISR"), ("Spécialiste RH / recruteur/euse", "SEC"),
    ("Conseiller/ère de vente", "ESC"), ("Key account manager", "ECS"),
    ("Entrepreneur/euse / fondateur/trice", "EAI"), ("Responsable marketing", "EAC"),
    ("Comptable / fiduciaire", "CEI"), ("Contrôleur/euse de gestion", "CIE"),
    ("Employé(e) administratif/ve", "CES"), ("Logisticien(ne) / supply chain", "CER"),
    ("Spécialiste en hôtellerie", "ESC"), ("Cuisinier/ère", "RAE"), ("Policier/ère", "RES"),
    ("Paysagiste", "RAC"), ("Menuisier/ère", "RAC"), ("Forestier/ère", "RIS"), ("Pilote", "RIE"),
]

SC_LIKE = ["Pas du tout", "Un peu", "Neutre", "Beaucoup", "Énormément"]
SC_CONF = ["Pas du tout sûr(e): jamais fait", "Un peu: essayé, avec difficulté", "Moyennement: avec un peu d'aide",
           "Sûr(e): fait seul(e)", "Très sûr(e): on me demande de l'aide"]
SC_TRUE = ["Pas du tout vrai", "Un peu vrai", "En partie vrai", "Plutôt vrai", "Tout à fait vrai"]
SC_DESC = ["Pas du tout", "Un peu", "En partie", "Largement", "Très bien"]
SC_STR = ["Pas du tout", "Faible", "Moyen", "Fort", "Très fort"]

n_int = 0
