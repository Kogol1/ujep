arr = []
vrchol = -1

print("Zadej velikost pole")
lenght = int(input())

arr = [None] * lenght

def mujinput1(func):
    if(func == "push"):
        push()
    if(func == "pop"):
        pop()
    else:
        print("špatné zadání")
        aCoTed()

def push():
    global vrchol
    if(vrchol + 1 < len(arr)):
        print("napiš číslo")
        value = int(input())
        arr[vrchol + 1] = value
        vrchol = vrchol + 1
        print(vrchol, arr)
        print("\n...........................")
        aCoTed()
    else:
        print("Je to plný")
        aCoTed()


def pop():
    global vrchol
    if(vrchol > -1):
        print(arr[vrchol])
        vrchol -= 1
    else:
        print("zásobník je prázdný")
    aCoTed()


def end():
    print("\n...........................")
    print("Konečné pole je:")
    print(arr)
    print("\n...........................")

def aCoTed():
    print("napiš funkci 'push', 'pop', 'end'")
    func = input()
    mujinput1(func)

aCoTed()

