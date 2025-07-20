# Detection&TraductionLangueAPI

API de détection et traduction de langue.

## Endpoints principaux

- POST `/detect` : détecter la langue d'un texte
- POST `/translate` : traduire un texte

### Exemple de body JSON pour /detect
```
{
  "text": "Bonjour, comment ça va ?"
}
```

### Réponse /detect
```
{
  "lang": "fr"
}
```

### Exemple de body JSON pour /translate
```
{
  "text": "Bonjour, comment ça va ?",
  "target": "en"
}
```

### Réponse /translate
```
{
  "translated": "Hello, how are you?"
}
```

## Lancer en local

```bash
uvicorn main:app --reload
``` 