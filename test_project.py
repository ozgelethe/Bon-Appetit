from project import countX,check_multiples,get_ing

def main():
    test_countX()
    test_check_multiples()
    test_get_ing()

def test_countX():
    assert countX([1, 1 , 1], 1) == 3
    assert countX([1, 6, 5, 15, 14, 15], 15) == 2
    assert countX(["egg", "egg", "sugar", "flour"], "flour") == 1
    assert countX(["cinnamon", "vinegar", "baking powder"], "apple") == 0

def test_check_multiples():
    assert check_multiples([1, 1, 1, 2, 3]) == [1, 2, 3]
    assert check_multiples(["egg", "egg", "sugar", "flour"]) == ["egg", "sugar", "flour"]
    assert check_multiples(["almond", "milk", "clove"]) == ["almond", "milk", "clove"]

def test_get_ing(monkeypatch):
    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr('builtins.input', lambda _: "Mark")

    # go about using input() like you normally would:
    i = input("What is your name?")
    assert i == "Mark"

if __name__ == "__main__":
    main()