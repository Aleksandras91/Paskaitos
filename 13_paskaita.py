# def division(a, b):
#     try:
#         print(a/b)
#         print(labas)
#     except ZeroDivisionError:
#         print("dalyba is nulio negalima")

# division(2, 2)
# division(2, 0)
# division(0, 2)
# division(6, 3)
print("")
# a = "12"

# my_int = int(a)

# print(my_int)
print("")
# a = 12

# my_int = int(a)

# print(my_int)

print("")
# a = ["14j", 3, True]

# try:
#     my_int1 = int(a)
# except ValueError:
#     print("reiksmes negalima paversti i sveikaji skaiciu")
# except TypeError:
#     print("reiksmes tipas yra neteisingas. tikimasi skaiciaus arba teksto")

# print(my_int1)
print("")

# a = "14j"

# try:
#     my_int1 = int(a)
# except ValueError:
#     print("reiksmes negalima paversti i sveikaji skaiciu")
# except TypeError:
#     print("reiksmes tipas yra neteisingas. tikimasi skaiciaus arba teksto")

# print(my_int1)
print("")

# a = ["14", 1]

# try:
#     my_int2 = int(a)
# except (ValueError, TypeError):
#     print("reiksmes negalima paversti i sveikaji skaiciu")

# print(my_int2)

# a = ["14", 1]

# try:
#     my_int2 = int(a)
# except (ValueError, TypeError) as x:
#     print(f"gautas erroras: {x.args}")


print("")

# "tekstas@tekstas.tekstas"

# email = input("iveskite emaila: ")

# try:
#     if "@" not in email:
#         raise AssertionError("emailo formatas neteisingas!")
    
#     split_email = email.split("@")
#     username = split_email[0]
#     domain = split_email[1]

#     if "." not in email:
#         raise AssertionError("emeilo formatas neteisingas!")
    
#     split_domain = domain.split(".")
#     website = split_domain[0]
#     extension = split_domain[1]
    
#     if len(username) == 0:  # or len(website) == 0 or len(extension) == 0:
#         raise AssertionError("emeilo formatas neteisingas")
    
#     if len(website) == 0:
#         raise AssertionError("emeilo formatas neteisingas")

#     if len(extension) == 0:
#         raise AssertionError("emeilo formatas neteisingas")

# except AssertionError as error:
#     print(f"kazkas negerai: {error}")

print("")

# a = 1
# b = 0

# try:
#     result = a / b
# except ZeroDivisionError:
#     print("negalima dalinti is nulio")
# else:
#     print(result)

print("")

a = 12
b = 6

try:
    result = a / b
except ZeroDivisionError:
    print("negalima dalinti is nulio")
else:
    print(f"rezultatas: {result}")
finally:
    print("ivyko")












# raise AssertionError("ivyko mano erroras")
