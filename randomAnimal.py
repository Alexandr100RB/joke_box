import random

words = '''аист акула бабуин баран барсук бобр бык варан верблюд волк вомбат воробей ворон выдра
голубь гусь додо дятел енот ехидна еж жаба жираф журавль заяц зебра землеройка зяблик
игуана кабан казуар кайман какаду кальмар камбала канарейка каракатица карп кенгуру
киви кит лама ламантин ласка ласточка лебедь лев лемур ленивец леопард лиса лягушка
мотылек муравьед муравей мангуст медведь морж муха мышь медуза нарвал носорог орел омар олень овцебык
осьминог орел осел оса овца опоссум обезьяна паук пескарь пингвин пиранья попугай
пчела рысь рыба росомаха страус сурок стрекоза сорока сова снегирь сокол собака слон
слон скорпион скворец скат сельдь свинья сурикат скунс слизень светлячок тюлень тукан тигр
трясогуска термит тетерев тунец тритон тарантул таракан тля утконос уж устрица улитка угорь фазан фламинго
форель хорек хомяк хамелеон цапля цесарка цикада черепаха червь чайка шимпанзе шиншилла
щука эму ящерица ястреб як ягуар'''.split()
# split разбивает строку и делает список


# получаем случайное слово из списка
def getRandomAnimal():
    return random.choice(words)
