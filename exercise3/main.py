from boyer_moore import BoyerMoore
from knuth_morris_pratt import KnuthMorrisPratt
from rabin_karp import RabinKarp
import timeit

def main():
    bm = BoyerMoore()
    display_time(bm)

    kmp = KnuthMorrisPratt()
    display_time(kmp)

    rk = RabinKarp()
    display_time(rk)

    print("""На основі отриманих даних, алгоритм Boyer-Moore показав найкращу швидкість у всіх випадках.
Для кожного тесту:
Пошук існуючого рядка в статтях 1 і 2 – Boyer-Moore виконувався швидше за Knuth-Morris-Pratt і Rabin-Karp.
Пошук неіснуючого рядка також був найшвидшим у Boyer-Moore.
          
Загальний час виконання всіх тестів:
Boyer-Moore – 6.40 секунд
Knuth-Morris-Pratt – 68.72 секунд
Rabin-Karp – 189.12 секунд

Таким чином, Boyer-Moore є найефективнішим алгоритмом для пошуку рядків у тексті. 
Якщо потрібно швидко знаходити підрядки, варто використовувати саме його.""")

def display_time(algorithm):
    with open(r"exercise3\source\article1.txt", "r", encoding="utf-8") as file:
        article1 = file.read()

    with open(r"exercise3\source\article2.txt", "r", encoding="utf-8") as file:
        article2 = file.read()

    line_from_article1 = "Інтерполяційний пошук використовується для пошуку елементів у відсортованому масиві. "\
                        "Він корисний для рівномірно розподілених у структурі даних. "\
                        "При рівномірно розподілених даних місцезнаходження елемента визначається точніше. "\
                        "Тут і розкривається відміна алгоритму від бінарного пошуку, де потрібно знайти елемент у середині масиву."\
                        " Для пошуку елементів у масиві алгоритм використовує формули інтерполяції." 


    line_from_article2 = "Експерименти проводилися на комп’ютері з процесором AMD Ryzen 5 3600 та 32 Гб оперативної пам’яті. "\
                        "Для формування рекомендацій було використано колаборативну фільтрацію. "\
                        "З метою моделювання рекомендаційної системи розроблено програмну імітаційну модель, "\
                        "в якій було виділено три основні сутності – агент, сесія та предмет"
    
    print(f"{algorithm.name}: для 10000 виконянь")
    time_bm_existing_line_article1 = timeit.timeit(lambda: algorithm.search(article1, line_from_article1), number=10000)
    print("Час пошуку існуючого рядка в статті 1: ", time_bm_existing_line_article1)

    time_bm_existing_line_article2 = timeit.timeit(lambda: algorithm.search(article2, line_from_article2), number=10000)
    print("Час пошуку існуючого рядка в статті 2: ", time_bm_existing_line_article2)

    time_bm_not_existing_line_article1 = timeit.timeit(lambda: algorithm.search(article1, line_from_article2), number=10000)
    print("Час пошуку не існуючого рядка в статті 1: ", time_bm_not_existing_line_article1)

    time_bm_not_existing_line_article2 = timeit.timeit(lambda: algorithm.search(article2, line_from_article1), number=10000)
    print("Час пошуку не існуючого рядка в статті 2: ", time_bm_not_existing_line_article2)


if __name__ == '__main__':
    main()