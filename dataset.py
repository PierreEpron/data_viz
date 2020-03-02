import sys, os
import pandas as pd

remu_path = 'data/remu.csv'
remu_categories = ['ligne_rectification', 'benef_categorie_code', 'benef_qualite_code', 'benef_pays_code', 
    'benef_titre_code', 'benef_specialite_code', 'benef_identifiant_type_code']

conv_path = 'data/conv.csv'
conv_categories = ['ligne_rectification', 'benef_categorie_code', 'benef_qualite_code', 'benef_pays_code', 
    'benef_titre_code', 'benef_specialite_code', 'benef_identifiant_type_code', 'conv_objet']

benef_path = 'data/clean/benef_clean.csv'
benef_categories = ['ligne_rectification', 'benef_categorie_code', 'benef_qualite_code', 'benef_pays_code', 
    'benef_titre_code', 'benef_specialite_code', 'benef_identifiant_type_code', 'semestre']


def load_benef():
    return load(benef_path, benef_categories)

def load_conv():
    return load(conv_path, conv_categories)

def load_remu():
    return load(remu_path, remu_categories)

def load(path, cats):
    df = pd.read_csv(path, sep=';', encoding='utf-8')
    for cat in cats:
        df[cat].astype('category')
    return df