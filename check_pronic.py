fist = int(input("Enter the fist num: "))
sec = int(input("Enter the sec num: "))
list =[]
test = []
flag = 0 


def check_pronic(no):
    for i in range(no):
        if i * (i + 1) == no:
           return True
        if i * (i + 1) > no:
            return False


for n in range(int(fist), int(sec)):
    

    if check_pronic(n):
        print(f'{n} is a Pronic number')
   
