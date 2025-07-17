






number: int = 8

def changeNumber(number: int) -> int:
    if number:
        global number as numb
        numb = number
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