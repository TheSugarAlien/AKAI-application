#Kod działa dla języka polskiegoi angielskiego, dla reszty języków wystarczyłoby zmodyfikować ifa z literami specyficznymi dla danego języka

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

polish_letters = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']

word_counter = {}
for sentence in sentences:
    sentence = sentence.lower()
    words = sentence.split(' ')
    for word in words:
        if (ord(word[-1]) < 97 or ord(word[-1]) > 122) and word[-1] not in polish_letters:
            word = word[:-1]
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] += 1

sorted_word_counter_desc = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)

print("1.", sorted_word_counter_desc[0][0], "-", sorted_word_counter_desc[0][1])
print("2.", sorted_word_counter_desc[1][0], "-", sorted_word_counter_desc[1][1])
print("3.", sorted_word_counter_desc[2][0], "-", sorted_word_counter_desc[2][1])


