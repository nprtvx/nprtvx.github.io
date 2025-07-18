






number: int = 8

def change_number(numb: int) -> int:
    if numb:
        global number
        number = numb
    return

print(number)
change_number(4)
print(number)

try:
    change_number()
except Exception as exc:
    print(exc, "missing_argument")
print(number)





# eof