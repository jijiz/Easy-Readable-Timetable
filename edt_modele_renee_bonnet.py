import edt
import couleurs

#######################################################
##########  DEBUT MODIFICATION  #######################
#######################################################
l_semaine = "Semaine QX"
l_classe = "Groupe X"
l_nom_prenom = "Renée BONNET"
l_coordo = "Mme LAUR"

d_semaine=[
    {'jour':'Lundi',
     'cours':[
            {  'debut':'8h20',
               'fin':'9h25',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'9h25',
               'fin':'10h20',
               'matiere':"??",
               'salle':"??",
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
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'11h35',
               'fin':'12h35',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'12h35',
               'fin':'13h25',
               'matiere':"Repas",
               'salle':"Self",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'13h25',
               'fin':'14h25',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'14h25',
               'fin':'15h20',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'15h20',
               'fin':'15h35',
               'matiere':"Pause",
               'salle':"",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'15h35',
               'fin':'16h35',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'16h35',
               'fin':'17h30',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            }
           ]
    },
    {'jour':'Mardi',
     'cours':[
            {  'debut':'8h20',
               'fin':'9h25',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'9h25',
               'fin':'10h20',
               'matiere':"??",
               'salle':"??",
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
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'11h35',
               'fin':'12h35',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'12h35',
               'fin':'13h25',
               'matiere':"Repas",
               'salle':"Self",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'13h25',
               'fin':'14h25',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'14h25',
               'fin':'15h20',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'15h20',
               'fin':'15h35',
               'matiere':"Pause",
               'salle':"",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'15h35',
               'fin':'16h35',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'16h35',
               'fin':'17h30',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            }
           ]
    },
    {'jour':'Mercredi',
     'cours':[
            {  'debut':'8h20',
               'fin':'9h25',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'9h25',
               'fin':'10h20',
               'matiere':"??",
               'salle':"??",
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
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'11h35',
               'fin':'12h35',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'12h35',
               'fin':'13h25',
               'matiere':"Repas",
               'salle':"Self",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'13h25',
               'fin':'14h25',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'14h25',
               'fin':'15h20',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'15h20',
               'fin':'15h35',
               'matiere':"Pause",
               'salle':"",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'15h35',
               'fin':'16h35',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'16h35',
               'fin':'17h30',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            }
           ]
    },
    {'jour':'Jeudi',
     'cours':[
            {  'debut':'8h20',
               'fin':'9h25',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'9h25',
               'fin':'10h20',
               'matiere':"??",
               'salle':"??",
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
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'11h35',
               'fin':'12h35',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'12h35',
               'fin':'13h25',
               'matiere':"Repas",
               'salle':"Self",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'13h25',
               'fin':'14h25',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'14h25',
               'fin':'15h20',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'15h20',
               'fin':'15h35',
               'matiere':"Pause",
               'salle':"",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'15h35',
               'fin':'16h35',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'16h35',
               'fin':'17h30',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            }
           ]
    },
    {'jour':'Vendredi',
     'cours':[
            {  'debut':'8h20',
               'fin':'9h25',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'9h25',
               'fin':'10h20',
               'matiere':"??",
               'salle':"??",
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
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'11h35',
               'fin':'12h35',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'12h35',
               'fin':'13h25',
               'matiere':"Repas",
               'salle':"Self",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'13h25',
               'fin':'14h25',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'14h25',
               'fin':'15h20',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'15h20',
               'fin':'15h35',
               'matiere':"Pause",
               'salle':"",
               'couleur':couleurs.bleu_ciel
            },
            {  'debut':'15h35',
               'fin':'16h35',
               'matiere':"??",
               'salle':"??",
               'couleur':couleurs.blanc
            },
            {  'debut':'16h35',
               'fin':'17h30',
               'matiere':"??",
               'salle':"??",
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