import wikipediaapi

# Ustal szczegółowy user-agent
USER_AGENT = "x-scrapper (https://github.com/hvbcix; roszyk.hubert@gmail.com)"

# Inicjalizacja obiektu Wikipedia z user-agent
wiki_languages = {
    'pl': wikipediaapi.Wikipedia(language='pl', user_agent=USER_AGENT),
    'en': wikipediaapi.Wikipedia(language='en', user_agent=USER_AGENT),
    'de': wikipediaapi.Wikipedia(language='de', user_agent=USER_AGENT),
    'fr': wikipediaapi.Wikipedia(language='fr', user_agent=USER_AGENT)
}

term = "Napoleon Bonaparte"  # Wyszukiwany termin
articles = {}

# Pobieranie artykułów
for lang, wiki in wiki_languages.items():
    page = wiki.page(term)
    if page.exists():
        articles[lang] = page.text
    else:
        articles[lang] = ""

# Wyświetlenie fragmentu artykułów
for lang, text in articles.items():
    print(f"Język: {lang}, Długość tekstu: {len(text)}")
    print(text[:500])  # Wyświetlenie pierwszych 500 znaków
