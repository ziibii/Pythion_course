# 1. Lielais rezultāts
# Uzrakstiet funkciju add_mult, kurai nepieciešami trīs parametri/argumenti
# Atgriež rezultātu, kas ir 2 mazāko argumentu summa reizināta ar lielāko argumenta vērtību.
# PS Uzskatīsim, ka funkcijai vienmēr tiks padoti skaitliski parametri, varam tipus nepārbaudīt.
# Iespējami dažādi risinājumi, piemēram ar list struktūru varētu būt tīri eleganti.
# Piemērs add_mult(2,5,4) -> atgriezīs (2+4)*5 = 30

# my_list = []
#
# i = 1
# while i < 4:
#     num = int(input("Enter a number: "))
#     my_list.append(num)
#     i = i + 1
#
# def add_mult(my_list):
#     sorted_list = sorted(my_list)
#     resault = (sorted_list[0] + sorted_list[1]) * sorted_list[2]
#     print(f"Iegūtā summa {resault} --> ({sorted_list[0]} + {sorted_list[1]}) * {sorted_list[2]}")
#     return resault
#
# add_mult(my_list)


# uzrakstiet funkciju is_palindrome(text)
# kas atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm.
# PS no sākuma varat sākt ar viena vārda risinājumu, bet pilns risinājums ignorēs atstarpes(whitespace) un lielos/mazos burtus
# is_palindrome("Alus ari ira      sula") -> True
#
# #
# my_text = input("Enter some text: ")
#
# my_list = my_text.lower().split()
# new_list = []
#
# def is_palindrome(text):
#     for elem in my_list:
#         new_list.append(elem[::-1])
#     rev_list = new_list[::-1]
#     resault = my_list == rev_list
#     print(f"Resault is {resault}")
#     return resault
#
# is_palindrome(my_list)


# 3. Pilsēta
# Pilsētā ir zināms skaits iedzīvotāju p0
# Katru gadu nāk klāt procentuāls skaits perc
# Katru gadu nāk klāt(vai aizbrauc) arī zināms skaits delta
# Mums ir jāzina, kad(ja vispār) pilsēta sasniegs iedzīvotāju skaitu p
# Uzrakstiet funkciju get_city_year(p0, perc, delta, p) kas atgriež gadus (pilnus) kad p tiks sasniegts.
# Ja p nevar sasniegt, tad atgriežam -1
# Piemērs:
# get_city_year(1000,2,50,1200) -> 3
# 1000 + 1000 * 0.02 + 50 => 1070 pēc 1.gada
# 1070 + 1070 * 0.02 + 50 => 1141 pēc 2.gada
# 1141 + 1141 * 0.02 + 50 => 1213 pēc 3.gada
# PS. Ievērojam, ka padodam perc kā procentu kas jāpārvērš decimāl skaitlī.
# Pārbaudam, vai strādā ar sekojošiem parametriem:
# get_city_year(1000, 2, -50, 5000) -> -1 # samērā aktuāla problēma
# get_city_year(1500, 5, 100, 5000) -> 15
# get_city_year(1500000, 2.5, 10000, 2000000) -> 10

# p0 = int(input("Enter population: "))
# perc = int(input("Enter population growth in a year in %: "))
# delta = int(input("Enter how many are leaving in a year: "))
# p = int(input("Enter population that needs to achieved: "))
#
# def get_city_year(p0, perc, delta, p):
#     prec_dec = prec / 100
#     pop = 0
#     year = 0
#     while p <= pop:
#         year = year + 1
#         pop = (pop + p0 * prec_dec) - delta
#         if pop >= p:
#             print(f"Sasniegs pēc {year} gadiem")
#             break
#         else:
#             print(f"{year}. gadā --> pop")

# def calc(a,b=5,c=10):
#     return a+b+c

# print(calc(5))
# print(calc(10,20))
# print(calc(1,2,3))
# print(calc(5) + calc(10,20) + calc(1,2,3))

# 3.udevums - mājas risinājums
# p0 - iedzīvotaju skaits
# prec - % katru gadu nāk klāt
# delta - nāk klāt vai aizbrauc
# p - vēlamais iedzīvotāju skaits

# def get_city_year(p0, perc, delta, p):
#     prec_2 = perc/100
#     p0_par = p0
#     i = 0
#     while p > p0:
#         i = i + 1
#         p0 = p0 + p0 * prec_2 + delta
#         # print(f"{i}. gads -> {p0}")
#         if p0 <= p0_par:
#             print(-1)
#             break
#     if p <= p0:
#         print(i)
#
# get_city_year(1000, 2, -50, 5000)
# get_city_year(1500, 5, 100, 5000)
# get_city_year(1500000, 2.5, 10000, 2000000)

