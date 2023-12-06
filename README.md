# Cryptography
These are the lab assignments performed during the course of cryptography
# Lab 1-2
1. Програмно реалізувати матричний шифр  з  стовпцевим і рядковим ключами (див. слайд №12 лекції №2)
2. Програмно реалізувати  шифр Віженера для української мови

Заскрінити результат шифрування і розшифрування на тестовому прикладі
# Lab 4
1. Реалізувати у вигляді функції gcdex(a,b) ітераційний розширений алгоритм Евкліда пошуку трійки (d,x,y), де ax+by = d. Протестити на прикладі  a= 612 і b=342.

2. Реалізувати у вигляді функції inverse_element(a,n) пошук розв'язку рівняння ax=1 (mod n), тобто знаходження мультиплікативноо оберненого елемента a^(-1) по модулю n, використовуючи gcdex(a,b).  Протестити на прикладі  a = 5 і  n=18.

3. Реалізувати у вигляді функції phi(m) обчислення значення функції Ейлера для заданого m (https://en.wikipedia.org/wiki/Euler%27s_totient_function)

4. Реалізувати у вигляді функції inverse_element_2(a,p) знаходження мультиплікативного оберненого елемента a^(-1) по модулю числа n, використовуючи інший спосіб (теорему Ейлера або малу теорему Ферма у випадку простого числа n=p). Протестити на прикладі  a= 5 і  n=18.

Протестувати роботу функцій та заскрінити.

# Lab 5
Реалізувати у вигляді функцій mul02 і mul03 множення довільного байту на елементи (байти) 02 і 03 над полем Галуа GF (2^8) за модулем m(x) = x^8 + x^4 + x^3 + x + 1, використавши методику зсуву бітів і операцію ХОR (малюнки 2-4)
Протестувати на прикладах: D4 * 02 = B3, BF * 03 = DA
Зауваження:
1) 02 = x, 03 = x + 1
2) Множення на 03 зводиться до множення на 02:   BF * 03 = BF * (02+01) = BF * 02 + BF.

# Lab 7
Завдання 1. 1) запрограмувати тест простоти Міллера — Рабіна:
Вхідні дані: n>3, непарне натуральне число, яке потрібно перевірити на простоту; k - кількість раундів.
Вихідні дані:  Чи є n складеним або простим числом. Якщо просте, то з якою ймовірністю воно просте

Завдання 2
Реалізувати навчальну криптографічну систему з відкритим ключем RSA:
1) прості числа p i q згенерувати програмно (порядку 512 біт кожне), використавши тест простоти Міллера — Рабіна
2) згенерувати відкритий і закритий ключі для шифрування та розшифрування. Для пошуку закритого ключа скористатись розширеним алгоритмом Евкліда.
3) Завантажити скріни виконання програми (шифрування і розшифрування)

# Lab 8
Реалізувати програмно обмін ключами по протоколу Діффі-Хелмана

P.S. Згенерувати p за допомогою тесту Рабіна - Міллера, а g вибрати рандомно за умови, що воно є первісним коренем за модулем p (або генератором групи мультиплікативної групи Z_p).

# Lab 9
Реалізувати програмно шифрування і дешифрування повідомлення вказаним алгоритмом Ель-Гамаля
Протестувати

P.S. Згенерувати p за допомогою тесту Рабіна - Міллера, а g вибрати рандомно за умови, що воно є первісним коренем за модулем p.
