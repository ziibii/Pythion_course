# my_list = ["Zane", 1, 2, 4.5, "četri"]
# print(my_list)
#
# print("Zane" in my_list)

# 1.a Vidējā vērtība
# Uzrakstīt programmu, kas liek lietotājam ievadīt skaitļus(float).
# Programma pēc katra ievada rāda visu ievadīto skaitļu vidējo vērtību.
# PS. 1a var iztikt bez lists
# 1.b Programma rāda gan skaitļu vidējo vērtību, gan VISUS ievadītos skaitļus
# PS Iziešana no programmas ir ievadot "q"
# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.
# sum = 0
# num_list = []
#
# while True:
#     num = (input("Ievadiet, lūdzu, skaitli "))
#     if num == "q":
#         break
#     num = float(num)
#     num_list.append(num)
#     num_list.sort()
#     sum = sum + num
#     print(f"Rinda {num_list}")
#     print(f"Vidējais: {sum/len(num_list)}")
#     if len(num_list) > 2:
#         print(f"TOP 3 {num_list[-3:]}")
#         print(f"BOTTOM 3 {num_list[0:3]}")
#     print("_______________________________________________")


# 2. Kubu tabula
# Lietotājs ievada sākumu (veselu skaitli) un beigu skaitli.
# Izvads ir ievadītie skaitļi un to kubi
# Piemēram: ievads 2 un 5 (divi ievadi)
# Izvads
# 2 kubā: 8
# 3 kubā: 27
# 4 kubā: 64
# 5 kubā: 125
# Visi kubi: [8,27,64,125]
# PS teoretiski varētu iztikt bez list, bet ar list būs ērtāk

# my_list = []
# cube_list = []
# while True:
#     start_num = int(input("Lūdzu, ievadiet veselu skaitli "))
#     end_num = int(input("Lūdzu, ievadiet veselu skaitli, kas lielāks vai vienāds par iepriekšējo "))
#     if start_num > end_num:
#         print("Mēģiniet vēlreiz!")
#     else:
#         for item in range(start_num,end_num):
#             my_list.append(item)
#             cubic = pow(item, 3)
#             cube_list.append(cubic)
#             print(f"{item} kubā {cubic}")
#         print(f"Visi kubi {cube_list}")
#         break


# 3. Apgrieztie vārdi
# Lietotājs ievada teikumu.
# Izvadam visus teikuma vārdus apgrieztā formā.
# Alus kauss -> Sula ssuak
# PS Te varētu noderēt split un join operācijas.

# sentence = input("Ievadiet, lūdzu, teikumu ")
# sentence_split = sentence.split()
# rev_list = []
# for item in sentence_split:
#     rev = (item[::-1])
#     rev_list.append(rev)
# rev_sentence = " ".join([str(elem) for elem in rev_list])
# print(F"{sentence.capitalize()} --> {rev_sentence.capitalize()}


my_list = [11,12,13,14,15]

my_list.pop()

result = my_list.pop()

my_list.append(16)

print(result)









