# # EXERCİSE 1
# def is_odd(n):
#     if n % 2 == 1:
#         return True
# #     else :
#         return False


# EXERCİSE 2
# def if_leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
#
#
# print(if_leap_year(2000))
#
# # EXERCİSE 3
# def print_triangular_number(n):
#     toplam = 0
#     for i in range(1, n + 1):
#         toplam = toplam + i
#         print(i,toplam)


# EXERCİSE 4
# def if_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#
#     return True
#
# # EXERCİSE 5
# def reverse_string(s):
#     sonuc = ""
#     for harf in s:
#         sonuc = sonuc + harf
#     return sonuc


# # EXERCİSE 6
# def remove_all(to_remove, text):
#     if to_remove=="":
#         return text
#     result = ""
#     i = 0
#     while i < len(text):
#         if text[i: i + len(to_remove) ] == to_remove]==
# to_remove:
#         i = i+ len(to_remove)
#
#         else:
#           result = result + text[i:]
#           i = i + 1
#     return result


# EXERCİSE 7
#
# def substitule(message, key):
#     alphabet =  "abcçdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#     for ch  in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result += ch + result
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else :
#             result = result + key[index].lower()
#     return result
#
# key = "ertyuıopğüasdfghjklşizxcvbnmö"
#
# print(len(key))
# print (substitule("hello world", key))


# EXERCİSE 8

def remove_dups(text):
    new_text = ""
    for char in text:
        if char in new_text:
            pass
        else:
            new_text += char
    return new_text

print(remove_dups("avangardistiom"))
