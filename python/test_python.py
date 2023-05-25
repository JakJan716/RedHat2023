import pytest

def obvodctverce(a):
    obvod = 4*a
    print(f"Obvod ctverce je: {obvod}")

def obsahctverce(a):
    obsah = a**2
    print(f"Obsah ctverce je: {obsah}")

def faktorial(a):
    faktorial = 1
    if int(a) >= 1:
        for i in range (1,a+1):
            faktorial = faktorial * i
    print(f"Faktorial čísla {a} vychází {faktorial}.")

@pytest.mark.parametrize(
"a, expected",
[(5, 20), (6, 24)]
)

def test_obvod_ctverce(a, expected):
    obvodctverce(a) == expected

@pytest.mark.parametrize(
"a, expected",
[(5, 25), (6, 36)]
)

def test_obsah_ctverce(a, expected):
    obsahctverce(a) == expected
    
@pytest.mark.parametrize(
"a, expected",
[(1, 1), (5, 120)]
)

def test_faktorial(a, expected):
    faktorial(a) == expected
    