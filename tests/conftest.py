import pytest
import src.shapes as shapes


@pytest.fixture
def rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(99, 100)