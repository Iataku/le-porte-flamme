# Le Porte-Flamme — guide de publication

Ce dépôt contient le site du Porte-Flamme, construit avec **Hugo**. Tu n'as jamais besoin
de toucher au HTML ou au CSS pour publier : tu ajoutes juste un fichier texte, et le
site se reconstruit tout seul.

## Comment publier un nouvel article

1. Dans `content/articles/`, crée un **nouveau dossier** nommé par exemple
   `2026-09-03-mon-nouvel-article`
2. À l'intérieur, crée un fichier nommé exactement `index.md`
3. Ouvre `modele-article.md` (à la racine du projet), copie tout son contenu
   (à partir de la ligne `---`) et colle-le dans ton `index.md`
4. Remplace le contenu entre les `---` (l'en-tête) :

```yaml
---
title: "Le titre de ton article"
date: 2026-09-03
author: "Ton nom"
rubrique: "Politique"
readingTime: "6 min"
summary: "Une ou deux phrases qui donnent envie de lire l'article."
hero: false
---
```

   - `rubrique` doit être exactement l'une de : `National`, `International`, `Culture`, `Histoire`
   - `hero: true` si tu veux que cet article soit mis en avant en première page (laisse `false` pour tous les autres)

4. En dessous, écris ton article normalement, en Markdown :
   - `## Un sous-titre` pour une section
   - `**un mot**` pour le gras, `*un mot*` pour l'italique
   - `[un lien](https://exemple.fr)` pour un lien

5. Envoie ton dossier complet sur GitHub (voir plus bas). Le site se reconstruit et se publie
   automatiquement en 1 à 2 minutes.

## Insérer une image dans un article

1. Place ton fichier image (`.jpg`, `.png`...) **dans le même dossier** que
   le `index.md` de ton article — par exemple :
   ```
   content/articles/2026-09-03-mon-nouvel-article/
   ├── index.md
   └── ma-photo.jpg
   ```
2. Dans le texte de ton article, à l'endroit où tu veux que l'image apparaisse, écris :
   ```
   {{< image src="ma-photo.jpg" alt="Description pour les personnes malvoyantes" >}}
   ```
3. Pour ajouter une légende affichée sous l'image :
   ```
   {{< image src="ma-photo.jpg" alt="Description" caption="Ma légende" >}}
   ```
4. Pour changer la largeur d'affichage (400 pixels par défaut) :
   ```
   {{< image src="ma-photo.jpg" alt="Description" largeur="500" >}}
   ```

### La compression est automatique

Tu n'as **rien à faire toi-même** : à chaque publication, le site redimensionne
et recompresse automatiquement chaque image (qualité 82%, largeur choisie
ci-dessus). GitHub, de son côté, ne compresse jamais rien — c'est Hugo qui
s'en charge, pendant la construction du site.

Seule règle de bon sens : évite d'envoyer des photos brutes énormes (plusieurs
dizaines de Mo) — une photo de téléphone classique (quelques Mo) est amplement
suffisante, et garde ton dépôt GitHub léger.

Si le nom de fichier de l'image contient une faute de frappe, la publication
échoue avec un message clair indiquant quelle image est introuvable — comme
pour les rubriques, plutôt que de publier un article avec une image cassée.

## Envoyer ton article (et son image) sur GitHub

Le plus simple, sans rien installer : directement depuis le site github.com.

**Pour le texte de l'article :**
1. Va sur la page de ton dépôt
2. Ouvre le dossier `content/articles/`
3. Clique sur **Add file → Create new file**
4. Dans le champ du nom de fichier, tape le chemin complet :
   `nom-de-ton-dossier/index.md` (GitHub crée le dossier automatiquement)
5. Colle le contenu de ton article
6. En bas de page, clique sur **Commit changes**

**Pour une image :** une fois le dossier de l'article créé (étape précédente),
retourne dedans, clique sur **Add file → Upload files**, et glisse ton image.
Elle atterrit alors au bon endroit, à côté de `index.md`.

Suis la publication dans l'onglet **Actions** du dépôt (coche verte = article en ligne).

### Si tu te trompes de rubrique

Avant de publier, le site vérifie automatiquement que la `rubrique` de chaque
article existe bien parmi les quatre autorisées. Si tu écris par exemple
`rubrique: "Nationale"` au lieu de `"National"`, la publication **échoue
volontairement** (coche rouge dans Actions) avec un message qui te dit
exactement quoi corriger — plutôt que de publier un article invisible
sans que tu t'en rendes compte.

### Consulter les articles par rubrique

Chaque rubrique a sa propre page, listant tous ses articles :
`/rubriques/national/`, `/rubriques/international/`, `/rubriques/culture/`,
`/rubriques/histoire/`. Ce sont ces pages que le menu du haut affiche.

Pour ajouter une cinquième rubrique un jour : ajoute-la dans `hugo.toml`
(liste `rubriques`) ET crée un fichier correspondant dans
`content/rubriques/` (copie un des quatre existants et change le titre).

## Structure du projet

```
porte-flamme-hugo/
├── modele-article.md       ← à copier-coller pour rédiger un nouvel article
├── content/articles/       ← tes articles, un dossier par article (index.md + images)
├── content/rubriques/      ← une page par rubrique (ne pas modifier sauf ajout de rubrique)
├── static/css/style.css    ← le style visuel du site (CSS séparé du HTML)
├── static/images/          ← le logo et les images du site
├── layouts/                ← les gabarits HTML (structure des pages, ne pas modifier)
├── scripts/verifier_rubriques.py  ← vérifie les rubriques avant publication
├── archetypes/articles/     ← modèle utilisé par la commande "hugo new"
├── hugo.toml                ← configuration générale du site
└── .github/workflows/      ← publication automatique sur GitHub Pages
```

## Avant la première mise en ligne

Dans `hugo.toml`, remplace `TON-PSEUDO` et `NOM-DU-DEPOT` par ton nom d'utilisateur
GitHub et le nom réel du dépôt, sinon les images et les liens internes ne
fonctionneront pas correctement une fois le site publié.

## Tester en local avant de publier (si tu as Hugo installé)

```
hugo server -D
```

Puis ouvre `http://localhost:1313` dans ton navigateur. Pour créer un article
pré-rempli automatiquement :

```
hugo new content/articles/mon-nouvel-article
```

## Activer GitHub Pages (une seule fois)

Dans **Settings → Pages** de ton dépôt, choisis la source **GitHub Actions**
(pas "branch"). Le workflow fourni s'occupe ensuite de tout à chaque envoi.
