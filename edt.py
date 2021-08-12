from PIL import Image, ImageDraw, ImageFont
import datetime   
    
page_hauteur = 1357
page_largeur = 1920
largeur_colonne = page_largeur/5
padding_heure = 20
largeur_heure = 70
largeur_bloc = 250

entete_y = 5
semaine_x = 110
classe_x = 400
nom_prenom_x = 850
coordo_x = 1300

jour_y = 110
jour_hauteur = 50

y_debut_blocs_cours = 175
hauteur_journee = 1100
px_secondes = (9*60*60)/hauteur_journee

fnt_heure = ImageFont.truetype("arial.ttf", 25)
fnt_matiere_salle = ImageFont.truetype("arial.ttf", 27)
fnt_matiere_salle_gras = ImageFont.truetype("arialbd.ttf", 27)

# set general font
fnt = ImageFont.truetype("arial.ttf", 40)

# create an image
out = Image.new("RGB", (page_largeur, page_hauteur), (255, 255, 255))

# drawing context
d = ImageDraw.Draw(out)
class Edt:
    def __init__(self):
        d_semaine = []
        l_semaine = ""
        l_classe = ""
        l_nom_prenom = ""
        l_coordo = ""

    def semaine(self):
        d.text((semaine_x,entete_y), self.l_semaine, font=fnt, fill=(0, 0, 0), stroke_width=1)
        
    def classe(self):
        d.text((classe_x,entete_y), self.l_classe, font=fnt, fill=(0, 0, 0), stroke_width=1)
        
    def nom_prenom(self):
        d.text((nom_prenom_x,entete_y), self.l_nom_prenom, font=fnt, fill=(0, 0, 0), stroke_width=1)
        
    def coordo(self):
        d.text((coordo_x,entete_y), "Coordinatrice : "+self.l_coordo, font=fnt, fill=(0, 0, 0), stroke_width=1)

    def entete(self):
        #d.rectangle([0, 5, page_largeur-10, 55], outline=1, width=1)
        self.semaine()
        self.classe()
        self.nom_prenom()
        self.coordo()
        
        
    def bloc_jour(self, jour):
        x0 = self.bloc_to_x(jour)
        y0 = jour_y
        x1 = x0+largeur_bloc
        y1 = jour_y+jour_hauteur
        d.rectangle([x0, y0, x1, y1], fill=(0, 0, 0), outline=None, width=1)
        d.text((x0+largeur_bloc/2, y0+jour_hauteur/2), jour, font=fnt, fill=(255, 255, 255), stroke_width=1, anchor="mm")
        
        
        
    def hauteur_bloc_heure_cours(self, debut, fin):
        heure_debut_obj = datetime.datetime.strptime(debut, '%Hh%M')
        heure_fin_obj = datetime.datetime.strptime(fin, '%Hh%M')
        duree_cours = heure_fin_obj - heure_debut_obj
        return duree_cours.total_seconds()/px_secondes
        
    def bloc_heure_cours(self, offset_y, jour, debut, fin = "", matiere = "", salle = "", couleur = (0,0,0)):
        offset_Pause = 0
        hauteur_bloc = self.hauteur_bloc_heure_cours(debut, fin)
        if hauteur_bloc < 30:
            hauteur_bloc = 40

        y0 = y_debut_blocs_cours+offset_y
        y1 = y0+hauteur_bloc
        x0 = self.bloc_to_x(jour)
        x1 = x0+largeur_bloc
        
        # Rectangle
        d.rectangle([x0, y0, x1, y1], fill=couleur, outline=1, width=1)
        
        # Texte matiere 
        f_font = fnt_matiere_salle
        if "Pause" in matiere or "Repas" in matiere:
            f_font = fnt_matiere_salle_gras
            
        if matiere == "Pause" or salle == "":
            d.text((x0+largeur_bloc/2, y1-hauteur_bloc/2), matiere , font=f_font, fill=(0, 0, 0), stroke_width=0, anchor="mm", align ="center")
        else:
            
            # Texte salle 
            if "\n" in matiere:
                d.text((x0+largeur_bloc/2, y1-hauteur_bloc/2-25), matiere , font=f_font, fill=(0, 0, 0), stroke_width=0, anchor="mm", align ="center")
                d.text((x0+largeur_bloc/2, y1-hauteur_bloc/2+25), "("+salle+")" , font=f_font, fill=(0, 0, 0), stroke_width=0, anchor="mm")
            else:
                d.text((x0+largeur_bloc/2, y1-hauteur_bloc/2-20), matiere , font=f_font, fill=(0, 0, 0), stroke_width=0, anchor="mm", align ="center")
                d.text((x0+largeur_bloc/2, y1-hauteur_bloc/2+20), "("+salle+")" , font=f_font, fill=(0, 0, 0), stroke_width=0, anchor="mm")
        
        # Heure
        d.text((x0-15, y0), debut, font=fnt_heure, fill=(0,0,0), stroke_width=0, anchor="rm")
        d.line([x0, y0, x0-10, y0], fill =(0, 0, 0), width = 0)
        d.text((x0-15, y1), fin, font=fnt_heure, fill=(0,0,0), stroke_width=0, anchor="rm")
        d.line([x0, y1, x0-10, y1], fill =(0, 0, 0), width = 0)
        
        return hauteur_bloc

    def jour_to_int(self, jour):
        switcher = {
            'Lundi': 0,
            'Mardi': 1,
            'Mercredi': 2,
            'Jeudi': 3,
            'Vendredi': 4,
        }
        return switcher.get(jour, -1)

    def heure_to_x(self, jour):
        return self.jour_to_int(jour)*largeur_colonne + padding_heure + 15
        
    def bloc_to_x(self, jour):
        return self.heure_to_x(jour) + largeur_heure

    def bloc_to_y(self):
        return 200

    def bloc_jours(self):
        jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
        for jour in jours:
            self.bloc_jour(jour)
            
    def blocs_cours(self):
        
        
        for jours in self.d_semaine:
            s_jour = jours['jour']
            a_cours = jours['cours']
            offset = 0
            for cours in a_cours:
                offset = offset + self.bloc_heure_cours(offset_y = offset, jour=s_jour, debut=cours['debut'], fin=cours['fin'], matiere = cours['matiere'], salle=cours['salle'], couleur=cours['couleur'])

    def generate(self, d_semaine, l_semaine, l_classe, l_nom_prenom, l_coordo, bleu_ciel, gris_clair, gris_fonce, gris_semaine, blanc):
        self.d_semaine = d_semaine
        self.l_semaine = l_semaine
        self.l_classe = l_classe
        self.l_nom_prenom = l_nom_prenom
        self.l_coordo = l_coordo
        self.bleu_ciel = bleu_ciel
        self.gris_clair = gris_clair
        self.gris_fonce = gris_fonce
        self.gris_semaine = gris_semaine
        self.blanc = blanc
        
        self.entete()

        self.bloc_jours()

        #offset = bloc_heure_cours(offset_y = 0, jour='Lundi', debut="8h20", fin="10h00", matiere = "Mathématiques", salle="CO1")
        self.blocs_cours()
        # save image
        out.save("c:\\edt\\"+self.l_nom_prenom+".png")
        
        