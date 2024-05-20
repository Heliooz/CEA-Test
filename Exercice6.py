import wikipedia
import spacy
import pandas as pd

import itertools

from sklearn.metrics import accuracy_score, f1_score, recall_score

# Récupération des data wikipedia de la page Marie Curie
page = wikipedia.page("MarieCurie").content.split("\n")
page = [item.split(".") for item in page]
page = [sentence for paragraph in page for sentence in paragraph if sentence != ""]

# On load les modèles spacy

nlp_sm = spacy.load("en_core_web_sm")
nlp_md = spacy.load("en_core_web_md")
nlp_lg = spacy.load("en_core_web_lg")

## Fonction permettant d'appliquer le modèle de NER sur les données extraites, de faire des statistiques puis de retourner un dataset pour comparaison
def extract_data(doc, model, label):

    # On applique le model sur les phrases de la page wikipedia
    doc = [model(sentence) for sentence in page]

    values = []

    # Pour chaque phrase, on récupère et stocke les entités dans un dictionnaire
    for idx, sentence in enumerate(doc):
        for ent in sentence.ents:
            values.append({"entity_value": ent.text, "sentence_number": idx, f"entity_label_{label}" : ent.label_})

    # On créé un dataframe à partir du dictionnaire
    values = pd.DataFrame(values)

    # On affiche les 5 valeurs les plus présentes parmis les entités et leurs occurences
    print(values[f"entity_label_{label}"].value_counts()[0:5])
    print(values[f"entity_value"].value_counts()[0:5])

    occurences = {}


    # Pour chaque phrases, on créé un combinaison des entités afin de decompter les coocurrences d'entités 
    for value in values["sentence_number"].unique():
        current = values[values["sentence_number"] == value][f"entity_label_{label}"].sort_values().to_list()
        combinations = list(itertools.combinations(current, 2))
        for combination in combinations:
            if(combination in list(occurences.keys())): occurences[combination] += 1
            else : occurences[combination] = 1

    print(sorted(occurences.items(), key=lambda item: item[1], reverse=True)[0:5])
    return values

df_sm = extract_data(page, nlp_sm, "small")
df_md = extract_data(page, nlp_md, "medium")
df_lg = extract_data(page, nlp_lg, "large")

print(df_sm.shape, df_md.shape, df_lg.shape)

# On fusionne nos resultats sur un dataset de référence -> spacy_large

df_general = df_sm.merge(df_md, how="outer", on=["entity_value", "sentence_number"])
df_general = df_general.merge(df_lg, how="right", on=["entity_value", "sentence_number"])

df_general = df_general.fillna("NULL")

# On calcule les différentes métriques de comparaisons puis on les print 

print("Spacy Small / Spacy Medium")

print("Accuracy score : ",
accuracy_score(df_general["entity_label_large"], df_general["entity_label_small"]), "/",
accuracy_score(df_general["entity_label_large"], df_general["entity_label_medium"]))

print("F1 score : ",
f1_score(df_general["entity_label_large"], df_general["entity_label_small"], average="weighted"), "/",
f1_score(df_general["entity_label_large"], df_general["entity_label_medium"], average="weighted"))

print("Recall score : ",
recall_score(df_general["entity_label_large"], df_general["entity_label_small"], average="weighted", zero_division=0), "/",
recall_score(df_general["entity_label_large"], df_general["entity_label_medium"], average="weighted", zero_division=0))