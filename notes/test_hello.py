from notes.hello import hello

def test_default():
    assert hello() == "hello, world"

def test_arguemnt():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"