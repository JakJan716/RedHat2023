import pytest

def obvodctverce(a):
    obvod = 4*a
    print(f"Obvod ctverce je: {obvod}")

@pytest.mark.parametrize(
"a, expected",
[(5, 20), (6, 24)],
)

def test_obvod_ctverce(a):
    obvodctverce(obsah) == expected

