import pytest
from lesson_04.урок.Calculator import Calcuator

def test_sum_possitive_num():
    calculator = Calcuator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_div_by_zero():
    calculator = Calcuator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)


#calculator = Calcuator()

#res = calculator.sum(4, 5)
#assert res == 9

#res = calculator.sum(5.6, 4.3) #Python посчитает сумму
#res = round(res, 1) #округлит ее до одного знака после запятой
#print(res) #напечатает сумму
#assert res == 9.9 #сравнит с предполагаемым значением

#numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
#res = calculator.avg(numbs)
#print(res)
#assert res == 5

#res = calculator.div(10, 0)
#assert res == None
