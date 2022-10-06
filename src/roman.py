"""
Write a function roman2arabic
that takes a Roman numeral as an input
and returns a corresponding decimal numeral.
"""

# TDD - Test Driven Development
# 1. No production code without a failing test
# 2. Only as much test code to make the test fail
# 3. Only as much production code to make the test pass

# TDD = Red - Green - Refactor

ROMAN = 'IVXLCDM'
ARABIC = (1, 5, 10, 50, 100, 500, 1000)
ROMAN_ARABIC_MAP = dict(zip(ROMAN, ARABIC))


def get_current_roman(i, previous):
    value = ROMAN_ARABIC_MAP.get(i)
    return -value if value < previous else value


def roman2arabic(roman):
    previous = 0
    arabic = 0
    for i in roman[::-1]:
        value = get_current_roman(i, previous)
        arabic += value
        previous = abs(value)
    return arabic

# TDD PROS:
# - instant feedback
# - good coverage
# - critical mindset
# - support finding meaningful edge cases
# - more focus
# - iterative - break big problem into smaller ones
# - supports refactoring
# - more fun
# - get to see failing test and get to see that the test passes

# TDD CONS:
# - same person is writing tests and code
# - slow ???
# - depends on case e.g. more difficult in some circumstances e.g. with framework

