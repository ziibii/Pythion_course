# # print("Hello world!")
# # print("Zane")
# # a = "Zane"
# #
# # print(a)
# # b=len(a)
# # print(b)
# # print(a[3])
# # print(a[::-1]) #apgriezts
# # a=a.replace("a", "āāā")
# # print(a)
# # print(a.index("e"))
# # print(a.find("e"))
# # print(a.count("ā"))
#
# # Juceklis
# #
# # Lietotājs ievada vārdu.
# #
# # Tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu un papildu teksu pamatīgs juceklis vai ne pirmais lietotāja burts?
# #
# # Valdis -> Sidlav, pamatigs juceklis vai ne V?
#
# # name = (input("Ievadiet savu vārdu "))
# # rev_name = name[::-1]
# # cap_name = rev_name.capitalize()
# # print(name + " -> " + cap_name + ", pamatīgs juceklis vai ne?")
#
# # Uzrakstīt programmu teksta simbola atpazīšanai
# #
# # Lietotājs(pirmais spēlētājs) ievada tekstu.
# #
# # Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt
# #
# # Lietotājs(tātad otrs spēlētājs) ievada simbolu.
# #
# # Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
# #
# # Kartupeļu lauks -> ********* *****
# #
# # ievada a -> *a****** *a***
# #
# # Principā tas ir labs iesākums karātavu spēlei.
# #
# # name = input("Ievadiet, lūdzu, savu vārdu ")
# # name_star = " "
# #
# # for c in name:
# #     if c == " ":
# #         name_star = name_star + " "
# #     else:
# #         name_star = name_star + "*"
# #
# # print(name_star)
# #
# # # char = input("Ievadiet mināmo burtu ")
# # # for c in name:
# # #     if c == char:
# #
# #
# #
# # # name_len = len(name)+1
# # name_shif = " "
# # character = input("Ievadiet mināmo burtu ")
# # if name.count(character):
# #     for c in name:
# #         if c == character:
# #             name_shif = name_shif + character
# #         elif c == " ":
# #             name_shif = name_shif + " "
# #         else:
# #             name_shif = name_shif + "*"
# # else:
# #     print("nav uzminēts")
# # print(name_shif)
#
# # Uzrakstīt programmu teksta pārveidošanai
# # Saglabā lietotāja ievadu
# # Izdrukā ievadīto tekstu bez izmaiņām
# # Izņēmums: ja ievadā ir vārdi nav .... slikts, TAD izvadā nav ... slikts posms jānomaina uz ir labs
# # Laiks nav slikts -> Laiks ir labs
# # Auto nav jauns -> Auto nav jauns
# # Tas biezpiens nav nemaz tik slikts -> Tas biezpiens ir labs
# # Droši vien noderēs find (vai index, vai pat rfind), tāpat arī in operātors var noderēt. Tāpat slice sintakse būs noderīga.
# # Ja uzdevums risinās raiti, tad varam uzlabot un meklēt gan nav ... slikts -> ir labs, gan nav ... slikta -> ir laba
#
# text = input("Ievadiet apgalvojuma teikumu ")
# print(text.find("nav"))
#
#
#
#
#
