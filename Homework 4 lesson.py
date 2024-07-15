from Homework_3_lesson import zamena,textres,genernums,generpole,firslist

def test_zamena(): ### Цифра
    assert zamena(10)==" 10 "
    assert zamena(3)== "  3 "

def test_textres(): ### Список, Имя
    assert textres(generpole(firslist(),genernums()),"Loser") is None
    assert textres(generpole(firslist(),genernums()),"Winner") is None
    assert textres(generpole(firslist(),genernums()),"Gamer") is None

def test_genernums(): ###
    assert len(genernums())==15
    assert len(genernums())==15
    assert len(genernums())==15

def test_generpole(): ### Весь список, Все цифры
    assert generpole(firslist(),genernums())
    assert generpole(firslist(),genernums())
    assert generpole(firslist(),genernums())

def test_firslist(): ###
    assert len(firslist())==3
    assert len(firslist())==3
    assert len(firslist())==3
