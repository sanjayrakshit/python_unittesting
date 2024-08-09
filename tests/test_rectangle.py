

def test_area(rectangle):
    assert rectangle.area() == 10*20


def test_perimeter(rectangle):
    assert rectangle.perimeter() == 2 * (10+20)


def test_not_equal(rectangle, weird_rectangle):
    assert rectangle != weird_rectangle