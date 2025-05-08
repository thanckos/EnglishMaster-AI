import json

def load_grammar_lessons():
    with open("./grammar_lessons/tenses.json", "r") as f:
        tenses = json.load(f)
    with open("./grammar_lessons/vocabulary.json", "r") as f:
        vocabulary = json.load(f)
    return {"tenses": tenses, "vocabulary": vocabulary}

lessons = load_grammar_lessons()
print(lessons["tenses"]["lessons"][0]["title"])  # Affiche "Present Simple"
