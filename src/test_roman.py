import pytest

from src.roman import roman2arabic


@pytest.mark.parametrize(
    'roman, arabic',
    (
        ('I', 1),
        ('II', 2),
        ('III', 3),
        ('V', 5),
        ('X', 10),
        ('XV', 15),
        ('VI', 6),
        ('IV', 4),
        ('MCMLXXXV', 1985),
    ),
)
def test_roman_is_change_into_arabic(roman, arabic):
    assert roman2arabic(roman) == arabic
