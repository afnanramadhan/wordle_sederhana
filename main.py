import random



def ambil_kata():
    f = open("dataa.csv", "r")
    file = f.readlines()
    f.close()

    x = len(file)
    indeks  = random.randint(0,x-1)

    a = file[indeks]
    
    arr = []
    for i in a:
        if i!= "\n":
            arr.append(i)
    
    return arr

def input_kata():
    kata = input("Masukkan kata: ")
    arrKata = []
    while len(kata)!=5:
        print("Masukkan kata dengan 5 huruf")
        kata = input("Masukkan kata: ")
    for i in kata:
        arrKata.append(i)
    return arrKata

def validasi_menang(x,y,z):
    z = z
    if x==y:
        print("SELAMAT")
        z = 6
    return z

def array_to_str(x):
    temp = ""
    for i in x:
        temp+=i + "\t"
    return (temp)
def array_to_str2(x):
    temp = ""
    for i in x:
        temp+=i 
    return (temp)


def main(): 
    arr = ambil_kata()

    kesempatan = 0
    while kesempatan!=6:
        kata = input_kata()
        tempArr1 = []
        tempArr2 = []
        for i in range(5):
            if kata[i] == arr[i]:
                tempArr1.append(f"\033[0;32;40m{kata[i].upper()}")
                tempArr2.append(kata[i])
            elif kata[i] in arr:
                tempArr1.append(f"\033[0;33;40m{kata[i].upper()}")
                tempArr2.append(kata[i])
            else:
                tempArr1.append(f"\033[0;37;40m{kata[i].upper()}")
                tempArr2.append(kata[i])
        print(array_to_str(tempArr1)+"\033[0;37;40m")


        kesempatan+=1
        kesempatan = validasi_menang(array_to_str(tempArr2).upper(), array_to_str(arr).upper(), kesempatan)
    print("")
    print(array_to_str2(arr))
    
main()