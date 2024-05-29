
# IA Multi-Tâches

Ce projet implémente une IA multi-tâches capable d'exécuter diverses commandes sur votre système à partir de descriptions en langage naturel.

## Fonctionnalités

- Créer, lire et supprimer des fichiers
- Exécuter des commandes système
- Interpréter et exécuter des commandes en langage naturel

## Prérequis

- Python 3.x
- OpenAI API Key

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre_nom_utilisateur/ia-multi-taches.git
   cd ia-multi-taches
   ```

2. Installez les dépendances :
   ```bash
   pip install openai
   pip install flake8
   ```

3. Configurez votre clé API OpenAI dans `ai_multitask.py` :
   ```python
   openai.api_key = 'YOUR_API_KEY'
   ```

## Utilisation

Pour lancer l'IA multi-tâches, exécutez :
```bash
python ai_multitask.py
```

Entrez des commandes en langage naturel, par exemple :
- "Créer un nouveau fichier nommé 'test.txt' dans le dossier Documents"
- "Lire le fichier nommé 'test.txt'"
- "Supprimer le fichier nommé 'test.txt'"

Pour quitter, tapez "quitter" ou "exit".

## Contribution

Les contributions sont les bienvenues! Veuillez soumettre une pull request pour toute amélioration ou fonctionnalité supplémentaire.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
