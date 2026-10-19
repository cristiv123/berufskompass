# -*- coding: utf-8 -*-
# English item set for Career Compass. Same structure and order as make_busola_pdf.py.
TYPES = ["R", "I", "A", "S", "E", "C"]
TYPE_NAME = {"R": "Realistic", "I": "Investigative", "A": "Artistic", "S": "Social", "E": "Enterprising",
             "C": "Conventional"}
TYPE_DESC = {
    "R": "working with your hands, tools, machines, nature; concrete results",
    "I": "analysing, researching, understanding how things work",
    "A": "creating, expressing yourself, design, working without fixed rules",
    "S": "teaching, supporting, caring for and advising people",
    "E": "persuading, leading, selling, taking risks",
    "C": "structure, data, procedures, accuracy and control",
}

INT = {
    "R": ["Repair or maintain equipment, machines or appliances.",
          "Install, connect and commission a technical system.",
          "Work with tools in a workshop (wood, metal, electronics).",
          "Work outdoors: on a building site, in a forest or on a farm.",
          "Drive or operate vehicles, drones or machinery.",
          "Build something physical from scratch, following a plan.",
          "Find out why a device isn't working and fix it with your own hands.",
          "Look after plants, animals or land."],
    "I": ["Analyse data to find a trend or a hidden cause.",
          "Understand in depth how a complex system works.",
          "Run experiments and test hypotheses.",
          "Read scientific or technical studies in your field.",
          "Solve a hard logical problem that has no known solution yet.",
          "Build a mathematical or statistical model.",
          "Investigate the root cause of a failure or an incident.",
          "Teach yourself a new technology or theory until you master it."],
    "A": ["Design the look of a product, an app or a space.",
          "Write texts, stories or articles.",
          "Compose, sing or produce music.",
          "Take photos, film or edit video.",
          "Invent a completely new concept or idea.",
          "Act, present or improvise in front of an audience.",
          "Work without fixed rules, where personal style matters.",
          "Draw, paint or make decorative objects."],
    "S": ["Explain something complicated to someone who is just starting out.",
          "Help someone through a difficult period.",
          "Teach a course or run a workshop.",
          "Care for people who are ill, elderly or living with a disability.",
          "Mediate a conflict between two people.",
          "Mentor a younger colleague.",
          "Work on a project that improves life in a community.",
          "Listen to and advise people who ask for your advice."],
    "E": ["Convince a client to choose your solution.",
          "Lead a team towards an ambitious goal.",
          "Start your own business or project.",
          "Negotiate a contract, a price or a salary.",
          "Pitch an idea to management to get a budget.",
          "Make quick decisions with incomplete information.",
          "Build a network of professional contacts.",
          "Compete for measurable results (sales, market share)."],
    "C": ["Keep accurate records of figures, documents or stock.",
          "Check whether a process follows rules and standards.",
          "Organise information in spreadsheets, databases or archives.",
          "Prepare budgets, invoices or financial reports.",
          "Follow a clear procedure step by step, without mistakes.",
          "Plan schedules, deadlines and resources.",
          "Check the quality of a product or a piece of documentation.",
          "Bring order to a chaotic system of files, data or processes."],
}

CONF = {
    "R": ["Repair an electrical or electronic device.",
          "Use power tools safely.",
          "Read a technical drawing and work from it.",
          "Assemble furniture or a simple installation without detailed instructions."],
    "I": ["Analyse a data set and draw correct conclusions.",
          "Understand a scientific article or dense technical documentation.",
          "Find the cause of a complex problem by systematically ruling out hypotheses.",
          "Apply statistics or mathematics to a real problem."],
    "A": ["Create a visual design that looks professional.",
          "Write a text that grabs attention.",
          "Come up with original ideas when others are stuck.",
          "Express an idea through image, sound or movement."],
    "S": ["Teach a group something so that everyone understands.",
          "Calm down someone who is upset.",
          "Sense what someone feels without them telling you.",
          "Support someone in reaching a personal goal."],
    "E": ["Win over a sceptical group.",
          "Steer a meeting to a decision.",
          "Negotiate a good deal for yourself.",
          "Sell a product or a service."],
    "C": ["Keep a budget or records without errors.",
          "Create an organising system that others also use.",
          "Work with complex Excel spreadsheets.",
          "Meet strict deadlines and procedures."],
}

ANCHORS = [
    ("TF", "Technical / functional competence",
     ["I want to become a sought-after expert in my specialism.",
      "I feel most fulfilled when I use my specialist skills at a high level.",
      "I would turn down a promotion that took me out of my area of expertise."],
     "Your professional identity comes from being very good at one field. Look for expert roles and technical career "
     "paths, not only management ones. Be wary of promotions into pure management."),
    ("GM", "General managerial competence",
     ["I want to end up running a whole organisation or department.",
      "I am drawn to responsibility for the results of an entire team.",
      "I would rather integrate other people's work than specialise in one thing."],
     "You are motivated by responsibility, integration and organisational results. Look for roles with a team and a "
     "budget. Be wary of isolated specialist roles."),
    ("AU", "Autonomy / independence",
     ["I want to decide for myself how, when and where I work.",
      "Rigid organisational rules and procedures weigh on me.",
      "I would give up the security of a permanent job for more freedom."],
     "You need control over how you work. Look for freelancing, consulting, remote work, clear goals with freedom in "
     "execution. Be wary of micromanagement."),
    ("SE", "Security / stability",
     ["Job and income security are very important to me.",
      "I prefer a stable employer, even if I progress more slowly.",
      "It reassures me to know what to expect in the coming years."],
     "Predictability gives you calm and energy. Look for large or public employers, permanent contracts, clear "
     "benefits. Be wary of variable pay and risky start-ups."),
    ("EC", "Entrepreneurial creativity",
     ["I dream of creating something entirely my own: a company, a product.",
      "I am motivated by turning an idea into a business that works.",
      "I am willing to take risks to build something new."],
     "You want to create something of your own. Look for founding a company, intrapreneurship, product launches. Be "
     "wary of roles where you only maintain what others have built."),
    ("SV", "Service / dedication to a cause",
     ["I want my work to contribute to a cause I believe in.",
      "I would choose a lower-paid job if it helped people or the environment.",
      "The meaning of what I do matters more than title or money."],
     "Meaning and impact matter. Look for NGOs, the public sector, health, education, sustainability or "
     "mission-driven companies. Be wary of purely profit-driven environments."),
    ("CH", "Pure challenge",
     ["I am drawn to problems that others consider impossible.",
      "I get bored quickly when work becomes routine.",
      "Competition and big obstacles give me energy."],
     "Hard problems energise you. Look for transformation projects, consulting, crisis situations, ambitious targets. "
     "Be wary of routine."),
    ("LS", "Lifestyle",
     ["I want a career that fits my personal life and family, not the other way round.",
      "I would turn down a move or promotion that would unbalance my private life.",
      "Flexible working hours are a condition for me, not a bonus."],
     "Your career has to fit into your life. Look for flexible hours, part-time, remote work, employers with a "
     "culture of balance. Be wary of always-on cultures."),
]

B5 = [  # Mini-IPIP, Donnellan et al. (2006), original public-domain IPIP wording
    ("E", "+", "I am the life of the party."),
    ("A", "+", "I sympathize with others' feelings."),
    ("C", "+", "I get chores done right away."),
    ("N", "+", "I have frequent mood swings."),
    ("O", "+", "I have a vivid imagination."),
    ("E", "−", "I don't talk a lot."),
    ("A", "−", "I am not interested in other people's problems."),
    ("C", "−", "I often forget to put things back in their proper place."),
    ("N", "−", "I am relaxed most of the time."),
    ("O", "−", "I am not interested in abstract ideas."),
    ("E", "+", "I talk to a lot of different people at parties."),
    ("A", "+", "I feel others' emotions."),
    ("C", "+", "I like order."),
    ("N", "+", "I get upset easily."),
    ("O", "−", "I have difficulty understanding abstract ideas."),
    ("E", "−", "I keep in the background."),
    ("A", "−", "I am not really interested in others."),
    ("C", "−", "I make a mess of things."),
    ("N", "−", "I seldom feel blue."),
    ("O", "−", "I do not have a good imagination."),
]
B5_NAME = {"E": "Extraversion", "A": "Agreeableness", "C": "Conscientiousness", "N": "Neuroticism",
           "O": "Intellect / imagination"}

SDT = {
    "Autonomy": ["I could largely decide how to organise my work.",
                 "I felt I did what I did because I chose to, not because I had to.",
                 "My ideas and opinions were taken into account."],
    "Competence": ["I felt capable and effective in what I did.",
                   "I had the chance to learn new things and grow.",
                   "I received clear signals that I was doing a good job."],
    "Relatedness": ["I felt part of a team.",
                    "I had people at work whom I trusted.",
                    "I cared about my colleagues and felt they cared about me too."],
}

CTX = [
    ("I work best alone", "I work best in a team"),
    ("Clear, well-defined tasks", "Open, ambiguous problems"),
    ("Steady, predictable pace", "Fast pace with urgent deadlines"),
    ("In the office or at home", "In the field, on the move"),
    ("Little contact with clients", "Daily contact with clients"),
    ("Large, structured organisation", "Small, flexible organisation"),
    ("Specialist in depth", "Generalist across many topics"),
    ("Long-term results", "Quick, visible results"),
    ("Individual contributor", "Leader of people"),
    ("Fixed, predictable salary", "Variable, performance-based income"),
]

ADAPT = {
    "Concern (looking ahead)": ["I think about what my work will look like in five years.",
                                "I prepare my next career steps in good time.",
                                "I know which skills will be in demand in my field."],
    "Control (you decide)": ["I make the important decisions about my career myself.",
                             "I take responsibility for my professional path.",
                             "I stay true to my convictions when I decide."],
    "Curiosity (you explore)": ["I actively explore new career options.",
                                "I look for chances to learn outside my role.",
                                "I ask others how work is done in their fields."],
    "Confidence (you can)": ["I finish tasks even when they are hard.",
                             "I learn new skills quickly when needed.",
                             "I find solutions when things don't go to plan."],
}

OPEN = [
    ("Role model", "Whom did you admire as a child or teenager (other than your parents)? What exactly did you admire?",
     "the ideal self: qualities you want to embody"),
    ("Favourite media", "Which magazines, websites, channels or podcasts do you enjoy following? What attracts you to "
     "them?", "the settings and kinds of problems that attract you"),
    ("Favourite story", "What is your favourite story (book, film, series)? Tell it briefly.",
     "the script you could follow to move forward"),
    ("Motto", "Do you have a motto or saying that guides you?", "the advice you give yourself"),
    ("Flow", "When did you last lose track of time while working on something? What were you doing?",
     "an activity with strong intrinsic motivation"),
]

OCC = [
    ("Software developer", "ICR"), ("IT / solution architect", "IEC"), ("DevOps / cloud engineer", "RIC"),
    ("Data scientist", "ICA"), ("Data engineer", "CIR"), ("IT security specialist", "CIE"),
    ("Systems / network administrator", "RCI"), ("Business analyst", "ICE"), ("IT project manager", "ECI"),
    ("Product owner / product manager", "EIA"), ("IT consultant", "EIC"), ("Scrum master / agile coach", "SEI"),
    ("UX/UI designer", "AIE"), ("Technical writer", "AIC"), ("IT trainer for adults", "SIE"),
    ("Computer science teacher", "SIA"), ("Quality auditor / manager", "CIR"), ("Electrical engineer", "IRC"),
    ("Mechanical engineer", "RIC"), ("Civil engineer", "RIC"), ("Automation engineer", "RIC"),
    ("Mechatronics technician", "RCI"), ("Electrician", "RIC"), ("Energy consultant", "IER"),
    ("Environmental engineer", "IRS"), ("Laboratory technician", "IRC"), ("Research scientist", "IAR"),
    ("Architect", "AIR"), ("Graphic designer", "AER"), ("Photographer / videographer", "ARE"),
    ("Journalist", "AES"), ("Translator", "AIC"), ("Musician", "AES"), ("Teacher", "SAE"),
    ("Social worker", "SEA"), ("Career counsellor", "SAI"), ("Psychologist", "ISA"), ("Nurse", "SIR"),
    ("Physiotherapist", "SRI"), ("Physician", "ISR"), ("HR specialist / recruiter", "SEC"),
    ("Sales consultant", "ESC"), ("Key account manager", "ECS"), ("Entrepreneur / founder", "EAI"),
    ("Marketing manager", "EAC"), ("Accountant / fiduciary", "CEI"), ("Financial controller", "CIE"),
    ("Administrative clerk", "CES"), ("Logistics / supply chain specialist", "CER"),
    ("Hospitality specialist", "ESC"), ("Cook / chef", "RAE"), ("Police officer", "RES"),
    ("Landscape gardener", "RAC"), ("Carpenter / joiner", "RAC"), ("Forester", "RIS"), ("Pilot", "RIE"),
]

SC_LIKE = ["Not at all", "A little", "Neutral", "Quite a lot", "Very much"]
SC_CONF = ["Not at all: never done it", "A little: tried, with difficulty", "Moderately: with some help",
           "Confident: done it on my own", "Very confident: others ask me for help"]
SC_TRUE = ["Not at all true", "Slightly true", "Partly true", "Mostly true", "Completely true"]
SC_DESC = ["Not at all", "A little", "Partly", "Largely", "Very well"]
SC_STR = ["Not at all", "Weak", "Moderate", "Strong", "Very strong"]

n_int = 0
