#!/usr/bin/env python3
"""
Vérifie que chaque article utilise une rubrique valide avant publication.
=========================================================================
Pourquoi ce script ? Sans lui, un article avec une faute de frappe dans
sa rubrique (ex: "Nationale" au lieu de "National") ne provoque AUCUNE
erreur visible : il disparaît juste silencieusement du site, sans
apparaître nulle part. C'est le pire des scénarios.

Ce script fait donc échouer volontairement la publication si un article
a une rubrique introuvable, avec un message clair pour corriger vite.

Utilisation : python3 scripts/verifier_rubriques.py
Code de sortie 0 = tout est valide. Code de sortie 1 = erreur trouvée.
"""

import os
import re
import sys
import glob
import difflib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HUGO_TOML = os.path.join(ROOT, "hugo.toml")
ARTICLES_DIR = os.path.join(ROOT, "content", "articles")


def lire_rubriques_autorisees():
    """Extrait la liste des rubriques valides depuis hugo.toml."""
    with open(HUGO_TOML, "r", encoding="utf-8") as f:
        contenu = f.read()

    match = re.search(r'rubriques\s*=\s*\[(.*?)\]', contenu, re.DOTALL)
    if not match:
        print("ERREUR : impossible de trouver la liste 'rubriques' dans hugo.toml")
        sys.exit(1)

    valeurs = re.findall(r'"([^"]+)"', match.group(1))
    if not valeurs:
        print("ERREUR : la liste 'rubriques' dans hugo.toml semble vide")
        sys.exit(1)
    return valeurs


def lire_rubrique_article(chemin_fichier):
    """Extrait la valeur du champ 'rubrique:' dans l'en-tête d'un article."""
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        contenu = f.read()

    if not contenu.startswith("---"):
        return None

    parts = contenu.split("---", 2)
    if len(parts) < 3:
        return None

    entete = parts[1]
    match = re.search(r'^\s*rubrique\s*:\s*"?([^"\n]+?)"?\s*$', entete, re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip()


def verifier():
    rubriques_valides = lire_rubriques_autorisees()
    fichiers = sorted(glob.glob(os.path.join(ARTICLES_DIR, "*.md")))

    erreurs = []

    for chemin in fichiers:
        nom_fichier = os.path.basename(chemin)
        rubrique = lire_rubrique_article(chemin)

        if rubrique is None:
            erreurs.append(
                f"  • {nom_fichier}\n"
                f"    Aucun champ 'rubrique:' trouvé dans l'en-tête de l'article."
            )
            continue

        if rubrique not in rubriques_valides:
            suggestions = difflib.get_close_matches(rubrique, rubriques_valides, n=1, cutoff=0.4)
            if suggestions:
                conseil = f"Voulais-tu écrire \"{suggestions[0]}\" ?"
            else:
                conseil = f"Rubriques valides : {', '.join(rubriques_valides)}"
            erreurs.append(
                f"  • {nom_fichier}\n"
                f"    Rubrique \"{rubrique}\" introuvable. {conseil}"
            )

    if erreurs:
        print("=" * 70)
        print("ÉCHEC — un ou plusieurs articles ont une rubrique invalide")
        print("=" * 70)
        print()
        print("\n\n".join(erreurs))
        print()
        print(f"Rubriques disponibles : {', '.join(rubriques_valides)}")
        print()
        print("Corrige le(s) champ(s) 'rubrique:' ci-dessus, puis renvoie le fichier.")
        print("Le site n'a PAS été publié pour éviter qu'un article reste invisible.")
        sys.exit(1)

    print(f"OK — {len(fichiers)} article(s) vérifié(s), toutes les rubriques sont valides.")
    sys.exit(0)


if __name__ == "__main__":
    verifier()
