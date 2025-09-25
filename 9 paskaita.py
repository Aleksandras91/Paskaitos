def addition(a, b): 
    return a + b

def addition2(a, b, c):
    return a + b + c

def addition(*args):
    result = sum(args)
    return result 

print(addition()) #()
print(addition(1)) #(1,)
print(addition(1, 6, 1))


def multiplication(a, b, c, *args, d=1, e=2, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"args: {args}")
    for arguments in args:
        print(arguments)
    print(f"d: {d}")
    print(f"e: {e}")
    print(f"kwargs: {kwargs}")
    for arguments in kwargs:
        print(arguments.split())


multiplication(1, 2, 3, "nebutinas", 1, 2, 3, d=5, e=6, q=3, j=9, t=4)


def division(**kwargs):
    print(kwargs)

division( a=8, b=7)

print((lambda x, y: x + y)(2, 3))


def words_lenght(words):
    return len(words)

words = ["bananas", "obuolys", "citrina", "apple"]

sorted_words = sorted(words, key=words_lenght)

print(sorted_words)


def words_lenght(words):
    return len(words)

words = ["bananas", "obuolys", "citrina", "apple"]

sorted_words = sorted(words, key=lambda words: len(words))

print(sorted_words)

