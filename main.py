from typing import List


# OPTIUNEA 1 \/ \/ \/
def citire_lista():
    lst = []
    given_string = input("Dati elementele separate prin virgula: ")
    number_as_string = given_string.split(",")
    for x in number_as_string:
        lst.append(int(x))
    return lst
# OPTIUNEA 1 /\ /\ /\


# OPTIUNEA 2 \/ \/ \/
def is_found(lst: List[int], find_this: int, position: int) -> bool:
    """
    Determina daca un numar citit de la tastatura se afla in lista pe pozitia citita del a tastatura
    :param lst: lista care contine numere intregi
    :param find_this: numarul intreg care trebuie gasit
    :return:
    """
    for i in range(position, len(lst)):
        if lst[i] == find_this:
            return True
    return False


def test_is_found():
    assert is_found([2, 32, 122, 12, 1456], 12, 3) is True
    assert is_found([2, 32, 122, 12, 1456], 12, 4) is False
    assert is_found([2, 32, 122, 12, 1456], 42, 1) is False
    assert is_found([], 3, 1) is False
    assert is_found([4, 8, 6, 3, 2, 1], 2, 2) is True
# OPTIUNEA 2 /\ /\ /\


# OPTIUNEA 3 \/ \/ \/
# OPTIUNEA 3 /\ /\ /\


# OPTIUNEA 4 \/ \/ \/
# OPTIUNEA 4 /\ /\ /\


# OPTIUNEA 5 \/ \/ \/
# OPTIUNEA 5 /\ /\ /\


def print_menu():
    print("1. Citire lista.")
    print("2. Determina si afiseaza daca un numar citit de la tastatura"
          "se regaseste un lista incepand de la o anumita pozitie citita de la"
          "tastatura.")
    print("3. !NU UITA SA MODIFICI!")
    print("4. !NU UITA SA MODIFICI!")
    print("5. !NU UITA SA MODIFICI!")
    print("A. Afisare lista")
    print("6. Iesire")


def main():
    lst = []
    should_run = True
    while should_run:
        print_menu()
        optiune = input("Selectati optiunea: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            find_this = int(input("Numarul citit de la tastatura: "))
            position = int(input("Pozitia = "))
            if is_found(lst, find_this, position) is True:
                print("DA")
            else:
                print("NU")
        elif optiune == "3":
            pass
        elif optiune == "4":
            pass
        elif optiune == "5":
            pass
        elif optiune == "A":
            print(lst)
        elif optiune == "6":
            should_run = False
        else:
            print("Optiune gresita! Reincercati!")


if __name__ == "__main__":
    test_is_found()
    main()
