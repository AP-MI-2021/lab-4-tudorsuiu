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
    :param position: pozitia de unde se incepe cautarea lui find_this
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
def sum_of_all_even(lst: List[int]) -> int:
    """
    Determina suma tuturor numerelor intregi pare din lista
    :param lst: lista care contine numere intregi
    :return: suma tuturor numerelor intregi pare din lista
    """
    total = 0
    for number_from_list in lst:
        if number_from_list % 2 == 0:
            total = total + number_from_list
    return total


def test_sum_of_all_even():
    assert sum_of_all_even([2, 3, 122, 12, 1456]) == 1592
    assert sum_of_all_even([0]) == 0
    assert sum_of_all_even([2, 3, 12, 5, 9]) == 14
    assert sum_of_all_even([23, 13, 3, 57, 19]) == 0
# OPTIUNEA 3 /\ /\ /\


# OPTIUNEA 4 \/ \/ \/
def find_all_even_from_list(lst: List[int]) -> List[int]:
    """
    Determina toate elementele pare dintr-o lista
    :param lst: lista care contine numere intregi
    :return: o lista care contine toate numerele pare gasite in lst, fara ca
             acestea sa se repete
    """
    result = []
    for number_from_list in lst:
        if number_from_list % 2 == 0 and is_found(result, number_from_list, 0) is False:
            result.append(number_from_list)
    return result


def test_find_all_even_from_list():
    assert find_all_even_from_list([23, 12, 3, 52, 12]) == [12, 52]
    assert find_all_even_from_list([12, 3, 12, 12, 7, 12, 3, 3]) == [12]
    assert find_all_even_from_list([]) == []
    assert find_all_even_from_list([2, 32, 122, 12, 1456]) == [2, 32, 122, 12, 1456]

# OPTIUNEA 4 /\ /\ /\


# OPTIUNEA 5 \/ \/ \/
def tuple_element_is_a_sum_of_elements(lst: List[int], element: int) -> tuple:
    """
    Determina daca un element dat poate se poate obtine prin adunarea oricaror
    doua elemente din lista
    :param lst:
    :param element:
    :return: tupla cu cele doua elemente din lista care adunate au ca rezultat
             elementul dat, tupla goala in caz contrar
    """
    for st in range(len(lst)):
        for dr in range(len(lst)):
            if st != dr and element == lst[st] + lst[dr] and lst[st] != element and lst[dr] != element:
                return lst[st], lst[dr]
    return ()


def test_tuple_element_is_a_sum_of_elements():
    assert tuple_element_is_a_sum_of_elements([4, 8, 6, 3, 2, 1], 3) == (2, 1)
    assert tuple_element_is_a_sum_of_elements([4, 8, 6, 3, 2, 1], 4) == (3, 1)
    assert tuple_element_is_a_sum_of_elements([4, 8, 6, 3, 2, 1], 8) == (6, 2)
    assert tuple_element_is_a_sum_of_elements([4, 8, 6, 3, 2, 1], 6) == (4, 2)
    assert tuple_element_is_a_sum_of_elements([1, 2, 3, 4, 5, 6, 7], 15) == ()


def replace_with_sum_of_elements(lst: List[int]) -> List[int]:
    """
    Determina daca elementele din lista pot fi scrise ca suma de doua valori
    preluate din lista
    :param lst: lista care contine numere intregi
    :return: lista formata din tupluri si numere intregi
    """
    result = lst[:]
    for i in range(len(lst)):
        if tuple_element_is_a_sum_of_elements(lst, lst[i]) != ():
            result[i] = tuple_element_is_a_sum_of_elements(lst, lst[i])
    return result


def test_replace_with_sum_of_elements():
    assert replace_with_sum_of_elements([4, 8, 6, 3, 2, 1]) == [(3, 1), (6, 2), (4, 2), (2, 1), 2, 1]
    assert replace_with_sum_of_elements([1, 2, 3, 4, 5]) == [1, 2, (1, 2), (1, 3), (1, 4)]
    assert replace_with_sum_of_elements([21, 30, 42, 53, 0, 123]) == [21, 30, 42, 53, 0, 123]
# OPTIUNEA 5 /\ /\ /\


def print_menu():
    print("1. Citire lista.")
    print("2. Determina si afiseaza daca un numar citit de la tastatura"
          "se regaseste un lista incepand de la o anumita pozitie citita de la"
          "tastatura.")
    print("3. Determina si afiseaza suma tuturor numerelor intregi pare din lista.")
    print("4. Determina si afiseaza toate numerele din lista care sunt pare. Daca "
          "se repeta un numar, acesta va aparea in lista razultat doar o singura "
          "data.")
    print("5. Determina si afiseaza lista obtinuta prin inlocuirea fiecarui numar "
          "cu un tuplu format din doua numere de pe pozitii distincte din lista "
          "care adunate dau acel numar, daca se poate.")
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
            print(sum_of_all_even(lst))
        elif optiune == "4":
            print(find_all_even_from_list(lst))
        elif optiune == "5":
            print(replace_with_sum_of_elements(lst))
        elif optiune == "A":
            print(lst)
        elif optiune == "6":
            should_run = False
        else:
            print("Optiune gresita! Reincercati!")


if __name__ == "__main__":
    test_is_found()
    test_sum_of_all_even()
    test_find_all_even_from_list()
    test_tuple_element_is_a_sum_of_elements()
    test_replace_with_sum_of_elements()
    main()
