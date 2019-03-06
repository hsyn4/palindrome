liste = ()
sayi = (input("palindrome : "))
liste = list(sayi)
print(liste)
stack = liste
for i in range(int(len(stack))):

    control1 = stack.pop(0)
    # print(control1)

    control2 = stack.pop()
    # print(control2)
    if control1 != control2:
        print("not palindrome")
        break
    elif len(stack) <= 1:
        print("it is palindrome!")
        break


