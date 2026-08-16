# Le Porte-Flamme — guide de publication

Ce dépôt contient le site du Porte-Flamme, construit avec **Hugo**. Tu n'as jamais besoin
de toucher au HTML ou au CSS pour publier : tu ajoutes juste un fichier texte, et le
site se reconstruit tout seul.

## Comment publier un nouvel article

1. Va dans le dossier `content/articles/`
2. Copie un fichier existant (par exemple `2026-08-16-financiarisation-logement.md`)
   et renomme la copie, par exemple : `2026-09-03-mon-nouvel-article.md`
3. Ouvre-le et remplace l'en-tête entre les `---` :

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

   - `rubrique` doit être exactement l'une de : `Politique`, `International`, `Société`, `Culture`, `Histoire`
   - `hero: true` si tu veux que cet article soit mis en avant en première page (laisse `false` pour tous les autres)

4. En dessous, écris ton article normalement, en Markdown :
   - `## Un sous-titre` pour une section
   - `**un mot**` pour le gras, `*un mot*` pour l'italique
   - `[un lien](https://exemple.fr)` pour un lien

5. Envoie ton fichier sur GitHub (voir plus bas). Le site se reconstruit et se publie
   automatiquement en 1 à 2 minutes.

## Envoyer ton fichier sur GitHub

Le plus simple, sans rien installer : directement depuis le site github.com.

1. Va sur la page de ton dépôt
2. Ouvre le dossier `content/articles/`
3. Clique sur **Add file → Create new file**
4. Colle le contenu de ton article, donne-lui un nom qui se termine par `.md`
5. En bas de page, clique sur **Commit changes**

Suis la publication dans l'onglet **Actions** du dépôt (coche verte = article en ligne).

## Structure du projet

```
porte-flamme-hugo/
├── content/articles/       ← tes articles, un fichier .md par article
├── static/css/style.css    ← le style visuel du site (CSS séparé du HTML)
├── static/images/          ← le logo et les images du site
├── layouts/                ← les gabarits HTML (structure des pages, ne pas modifier)
├── archetypes/articles.md  ← modèle utilisé par la commande "hugo new"
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
hugo new content/articles/mon-nouvel-article.md
```

## Activer GitHub Pages (une seule fois)

Dans **Settings → Pages** de ton dépôt, choisis la source **GitHub Actions**
(pas "branch"). Le workflow fourni s'occupe ensuite de tout à chaque envoi.
