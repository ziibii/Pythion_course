# with open("Veidenbaums.txt", encoding = "utf-8") as fstream:
#     lines = fstream.readlines()
#
# for line in lines:
#     print(f"{line[-2]} pēdējais burts")
#     break

# 1a -> uzrakstam funkciju file_line_len(fpath), kas atgriež rindiņu skaitu failā
# pārbaudam file_line_len("veidenbaums.txt") -> vajadzētu būt 971
# iespējams jums veidenbaums.txt nebūs tajā pašā mapē, tad lietojam relatīvo ceļu uz failu

# def file_line_len(fpath):
#     return len(open(fpath, encoding = "utf-8").readlines()) #iesaka likt with priekšā
#
# print(file_line_len("veidenbaums.txt"))
#
# # 1b -> uzrakstam funkciju get_poem_lines(fpath), kas atgriež list ar tikai tām rindiņām kurās ir dzeja.
# # Tātad mums nederēs rindiņas bez teksta un nederēs dzejoļu virksraksti.
# # PS vēlams izmantot encoding = "utf-8"a
#
# def get_poem_lines(fpath):
#     new_poem = []
#     for line in open(fpath, encoding = "utf-8").readlines():
#         if len(line.strip()) == 0:
#             pass
#         elif line[-2] == "*":
#             pass
#         else:
#             new_poem.append(line)
#     return new_poem
#
# print(get_poem_lines("Veidenbaums.txt"))

# 1c -> uzrakstam funkciju save_lines(destpath, lines)
# Šī funkcija noglabās destpath faila ceļā(tātad fails vai fails ar ceļu), visas lines

def save_lines(destpath, lines):
    new_poem = open(destpath, "w+", encoding = "utf-8")
    old_poem = open("Veidenbaums.txt", "r", encoding = "utf-8")
    for line in old_poem:
        new_poem.writelines(line)
    new_poem.close()
    old_poem.close()
    return new_poem

print(save_lines("new_poem.txt", 5))

# test











