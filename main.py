words = {
    "лол": "что-то смешное",
    "кринж": "что-то стыдное",
    "изи": "легко",
    "агро": "злой",
    }
while True:
    word = input('Введите слово:').lower()
    if word in words:
        print(words[word])
    else:
        print('Слово не найдено')
