# -*- coding: utf-8 -*-

import flask
import random

app = flask.Flask(__name__) # Création de l'application

@app.route('/') # O
def index():    
    return flask.render_template("index.html")

@app.route('/regles') 
def regles():
    # Les fonctions de ce type (qui ne contiennent que return flask.render_template())
    # renvoient des pages html du dossier templates. 
    return flask.render_template("regles.html")

@app.route('/intro') 
def introduction():
    return flask.render_template("intro.html")

@app.route('/maison')
def maison():
    return flask.render_template("maison.html")

@app.route('/maison/interieur')
def intr():
    return flask.render_template("interieur.html")

@app.route('/maison/interieur/cuisine')
def cuisine():
    return flask.render_template("cuisine.html")

@app.route('/maison/interieur/bain')
def bain():
    return flask.render_template("bain.html")

@app.route('/maison/interieur/bureau')
def bureau():
    return flask.render_template("bureau.html")

@app.route('/papa', methods = ['POST'])
def papa():
    # Les fonctions de ce type (qui récupèrent des résultats de formulaires et les comparent avec des valeurs)
    # permettent de vérifier que le joueur à choisit le bon chemin ou qu'il a entré un mot de passe valide.
    resultat = flask.request.form

    if resultat.get("papa") == "question":
        return flask.render_template("questions.html")
    else:
        return flask.render_template("livres.html")
    
@app.route('/questions', methods = ['POST'])
def question():
    resultat = flask.request.form

    if resultat.get("q") == "totoro":
        return flask.render_template("qtotoro.html")
    else:
        return flask.render_template("qforet.html")
    
@app.route('/livres', methods = ['POST'])
def livre():
    resultat = flask.request.form

    if resultat.get("livre") == "plantes":
        return flask.render_template("lplantes.html")
    
    elif resultat.get("livre") == "legendes":
        return flask.render_template("llegendes.html")
    
    else:
        return flask.render_template("lhistoire.html")
    
@app.route('/maison/exterieur')
def extr():
    return flask.render_template("exterieur.html")

@app.route('/maison/exterieur/suite', methods = ['POST'])
def suivre():
    resultat = flask.request.form
    
    if resultat.get("suivre") == "oui":
        return flask.render_template("mei.html")
    else:
        return flask.render_template("endroits.html")

@app.route('/maison/exterieur/riz')
def riz():
    return flask.render_template("rizieres.html")

@app.route('/maison/exterieur/pompe')
def pompeau():
    return flask.render_template("pompe-eau.html")

@app.route('/maison/exterieur/pompe/fin')
def fin2():
    return flask.render_template("pompefin.html")

@app.route('/maison/exterieur/linge', methods = ['POST'])
def linge():
    resultat = flask.request.form
    
    if resultat.get("linge") == "accroupir":
        return flask.render_template("esprits.html")
    else:
        return flask.render_template("etendoirs.html")
    
@app.route('/rejoindre')
def rejoindre():
    return flask.render_template("rejoindre.html")

@app.route('/poursuite')
def poursuite():
    return flask.render_template("poursuite.html")

@app.route('/poursuite/suite', methods = ['POST'])
def noisette():
    resultat = flask.request.form
    
    if resultat.get("chemin") == "on" and resultat.get("noisette") =="on":
        return flask.render_template("noisettes.html")
    elif resultat.get("chemin") == "on":
        return flask.render_template("transparent.html")
    else:
        return flask.render_template("fatigue.html")
    
@app.route('/foret/arbre', methods = ['POST'])
def rendre():
    resultat = flask.request.form
    
    if resultat.get("rendre") == "noisettes":
        return flask.render_template("guide.html")
    else:
        return flask.render_template("noisetier.html")

@app.route('/foret')
def foret():
    return flask.render_template("foret.html")

@app.route('/foret/centre')
def centref():
    return flask.render_template("centref.html")

@app.route('/foret/plante', methods = ['POST'])
def plante():
    resultat = flask.request.form
    
    if resultat.get("plante") == "bambous"  or resultat.get("plante") == "bambou" :
        return flask.render_template("bambou.html")
    else:
        return flask.render_template("autrep.html", plante=resultat.get("plante"))

@app.route('/foret/guide', methods = ['POST'])
def guide():
    resultat = flask.request.form
    
    if resultat.get("guide") == "tonari no totoro":
        return flask.render_template("compris.html")
    else:
        return flask.render_template("confus.html")

@app.route('/foret/arbreroi')
def arbreroi():
    return flask.render_template("arbreroi.html")

@app.route('/foret/arbreroi/suite', methods = ['POST'])
def offrande():
    resultat = flask.request.form
    
    if resultat.get("offrande") == "fleche":
        return flask.render_template("chute.html")
    else:
        return flask.render_template("echec.html")
        
@app.route('/totoro')
def totoro():
    return flask.render_template('totoro.html')
    
@app.route('/foret/pin')
def pin():
    return flask.render_template("pin.html")

@app.route('/foret/pin/fin')
def finpin():
    return flask.render_template("pinfin.html")
    
app.run() 