import random

jokes = ['''
Заходят два дракона в бар. Один говорит другому:
— Что-то здесь жарковато.
А тот отвечает:
— А ты рот свой закрой.
''', '''
Купил мужчина шляпу, а она ему как раз.
''', '''
— Скажите, а это ваш "Ягуар" стоит около выхода?
— Да.
— Я допью?
''', '''
Заходит как-то давление в один бар в один бар.
''', '''
Библиотекарша чихнула, и её сопля попала в книгу рекордов Гиннеса
''', '''
Заходит чукча в магазин телевизоров и говорит:
- У вас естя цветные телевизоры?
Продавец ему отвечает:
- Есть.
- Дайте мене тогда зеленый
''', '''
На распродаже человеческих органов нaчалась давка и я еле успел унести нoги.
''', '''
Научил попугая говорить "Спасибо". Он был благодарен.
''', '''
Пришёл мужик в магазин:
— Нарежьте мне колбасы 100г, только 50 справа налево, а 50 слева направо.
— Хорошо, а вы что полицейский?
— Да, а как вы догадались?
— Вы в форме.
''', '''
Молвил богатырь: — Выходи, чудище поганое! И ответило чудище поганое: — Извините, но мне только через две остановки выходить.
''', '''
— Василий Иванович, белые идут!
— А как же красные?
— А красные вас полнят.
''', '''
Первый человек, гуляя по райскому саду, обратился к Богу:
— Боже, а дашь мне имя?
— А дам.
''']

def getRandomJoke(jokes):
    return (random.choice(jokes))