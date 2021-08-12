import edt
import couleurs

#######################################################
##########  DEBUT MODIFICATION  #######################
#######################################################
l_semaine = "Semaine Q1"
l_classe = "Groupe 1"
l_nom_prenom = "Julien Saccareau"
l_coordo = "Mme Laur"

d_semaine=[
    {'jour':'Lundi',
     'cours':[
            {  'debut':'8h20',
               'fin':'10h20',
               'matiere':"TP production",
               'salle':"Cuisine",
               'couleur':couleurs.blanc
            },
            {  'debut':'10h20',
               'fin':'10h35',
               'matiere':"Pause",
               'salle':"",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'10h35',
               'fin':'12h30',
               'matiere':"TP production",
               'salle':"Cuisine",
               'couleur':couleurs.blanc
            },
            {  'debut':'12h30',
               'fin':'13h20',
               'matiere':"Repas",
               'salle':"Self",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'13h20',
               'fin':'14h25',
               'matiere':"ULIS",
               'salle':"B06",
               'couleur':couleurs.gris_fonce
            },
            {  'debut':'14h25',
               'fin':'15h20',
               'matiere':"Français/Hist-Géo",
               'salle':"C01",
               'couleur':couleurs.blanc
            },
            {  'debut':'15h20',
               'fin':'15h35',
               'matiere':"Pause",
               'salle':"",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'15h35',
               'fin':'17h30',
               'matiere':"CAPCO",
               'salle':"B08",
               'couleur':couleurs.blanc
            }
           ]
    },
    {'jour':'Mardi',
     'cours':[
            {  'debut':'8h20',
               'fin':'12h50',
               'matiere':"ITEP",
               'salle':"",
               'couleur':couleurs.gris_clair
            },
            {  'debut':'12h50',
               'fin':'14h25',
               'matiere':"Savoir associés\n et Maths",
               'salle':"B03",
               'couleur':couleurs.blanc
            },
            {  'debut':'14h25',
               'fin':'15h20',
               'matiere':"Chef d'oeuvre",
               'salle':"CO1",
               'couleur':couleurs.blanc
            },
            {  'debut':'15h20',
               'fin':'15h35',
               'matiere':"Pause",
               'salle':"",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'15h35',
               'fin':'16h30',
               'matiere':"Chef d'oeuvre",
               'salle':"C01",
               'couleur':couleurs.blanc
            }
           ]
    },
    {'jour':'Mercredi',
     'cours':[
            {  'debut':'8h20',
               'fin':'8h50',
               'matiere':"ULIS (B06)",
               'salle':"",
               'couleur':couleurs.gris_fonce
            },
            {  'debut':'8h50',
               'fin':'9h50',
               'matiere':"PSE",
               'salle':"C01",
               'couleur':couleurs.blanc
            },
            {  'debut':'9h50',
               'fin':'10h50',
               'matiere':"TP Service",
               'salle':"BonAp'",
               'couleur':couleurs.blanc
            },
            {  'debut':'10h50',
               'fin':'11h35',
               'matiere':"Repas (Self)",
               'salle':"",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'11h35',
               'fin':'15h00',
               'matiere':"TP Service",
               'salle':"BonAp'",
               'couleur':couleurs.blanc
            }
           ]
    },
    {'jour':'Jeudi',
     'cours':[
            {  'debut':'8h20',
               'fin':'13h20',
               'matiere':"ITEP",
               'salle':"",
               'couleur':couleurs.gris_clair
            },
            {  'debut':'13h20',
               'fin':'14h25',
               'matiere':"ULIS",
               'salle':"B06",
               'couleur':couleurs.gris_fonce
            },
            {  'debut':'14h25',
               'fin':'15h20',
               'matiere':"Maths/Sciences",
               'salle':"C24",
               'couleur':couleurs.blanc
            },
            {  'debut':'15h20',
               'fin':'15h35',
               'matiere':"Pause",
               'salle':"",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'15h35',
               'fin':'16h30',
               'matiere':"Arts appliqués",
               'salle':"C16",
               'couleur':couleurs.blanc
            }
           ]
    },
    {'jour':'Vendredi',
     'cours':[
            {  'debut':'8h20',
               'fin':'9h25',
               'matiere':"Maths/Sciences",
               'salle':"C24",
               'couleur':couleurs.gris_clair
            },
            {  'debut':'9h25',
               'fin':'10h20',
               'matiere':"CAPCO",
               'salle':"B11",
               'couleur':couleurs.blanc
            },
            {  'debut':'10h20',
               'fin':'10h35',
               'matiere':"Pause",
               'salle':"",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'10h35',
               'fin':'11h35',
               'matiere':"EMC",
               'salle':"C01",
               'couleur':couleurs.blanc
            },
            {  'debut':'11h35',
               'fin':'13h20',
               'matiere':"Repas (Self)",
               'salle':"",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'13h20',
               'fin':'15h20',
               'matiere':"Savoir associés",
               'salle':"B09",
               'couleur':couleurs.blanc
            }
           ]
    }
]
#######################################################
############  FIN MODIFICATION  #######################
#######################################################

edt = edt.Edt()
edt.generate(d_semaine, l_semaine, l_classe, l_nom_prenom, l_coordo, couleurs.bleu_ciel, couleurs.gris_clair, couleurs.gris_fonce, couleurs.gris_semaine, couleurs.blanc)