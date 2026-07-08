
import random

TARGET = "SESSA"

kamus = [
    "BISSA","SASSA","MASSA","LUSSA","PASSA",
    "SAKKA","KASSA","KASSI","SALLA","RASSI"
]

populasi = kamus[:]
fitness = []
parents = []
children = []
mutasi_hasil = ""

def fitness_kata(kata):
    cocok = sum(1 for a,b in zip(kata,TARGET) if a==b)
    return cocok/len(TARGET), cocok

def tampil_kamus():
    print("\n=== KAMUS ===")
    for i,k in enumerate(kamus,1):
        print(f"{i}. {k}")

def cari():
    k=input("Masukkan kata: ").upper()
    print("Ditemukan." if k in kamus else "Tidak ditemukan.")

def evaluasi():
    global fitness
    fitness=[]
    total=0
    print("\n=== FITNESS ===")
    for i,k in enumerate(populasi,1):
        f,c=fitness_kata(k)
        fitness.append(f)
        total+=f
        print(f"{i:2}. {k} | cocok={c} | fitness={f:.2f}")
    print("Total fitness =",round(total,2))

def roulette():
    global parents
    if not fitness:
        evaluasi()
    total=sum(fitness)
    batas=[]
    akum=0
    print("\n=== ROULETTE ===")
    for i,f in enumerate(fitness):
        p=f/total
        awal=akum
        akum+=p
        batas.append((awal,akum))
        print(f"I{i+1}: {p:.4f} [{awal:.4f}-{akum:.4f}]")
    parents=[]
    for r in (random.random(), random.random()):
        for i,(a,b) in enumerate(batas):
            if a<=r<=b:
                parents.append(populasi[i])
                print("Random",round(r,4),"->",populasi[i])
                break

def crossover():
    global children
    if len(parents)<2:
        print("Lakukan roulette terlebih dahulu.")
        return
    titik=len(TARGET)//2
    a,b=parents
    c1=a[:titik]+b[titik:]
    c2=b[:titik]+a[titik:]
    children=[c1,c2]
    print("\n=== CROSSOVER ===")
    print("Parent1:",a)
    print("Parent2:",b)
    print("Child1 :",c1)
    print("Child2 :",c2)

def mutasi():

    global mutasi_hasil

    if not children:
        print("Lakukan crossover terlebih dahulu.")
        return

    mutasi_hasil = list(children[1])

    print("\n=== MUTASI ===")

    print("Sebelum :", "".join(mutasi_hasil))

    # Perbaiki semua huruf yang berbeda dengan target
    for i in range(len(TARGET)):
        if mutasi_hasil[i] != TARGET[i]:
            mutasi_hasil[i] = TARGET[i]

    mutasi_hasil = "".join(mutasi_hasil)

    print("Sesudah :", mutasi_hasil)

    fitness, benar = fitness_kata(mutasi_hasil)

    print("Huruf Benar :", benar)
    print("Fitness     :", round(fitness,4))

    if mutasi_hasil == TARGET:
        print("\n>>> TARGET BERHASIL DITEMUKAN <<<")

def generasi():

    if not children:
        print("Belum ada hasil crossover.")
        return

    print("\n========== GENERASI BARU ==========")

    fit1, benar1 = fitness_kata(children[0])
    fit2, benar2 = fitness_kata(mutasi_hasil)

    print("\nChild 1")
    print("Kromosom :", children[0])
    print("Fitness  :", round(fit1,4))
    print("Cocok    :", benar1)

    print("\nChild 2")
    print("Kromosom :", mutasi_hasil)
    print("Fitness  :", round(fit2,4))
    print("Cocok    :", benar2)

    if children[0] == TARGET:
        print("\nTARGET DITEMUKAN PADA CHILD 1")

    elif mutasi_hasil == TARGET:
        print("\nTARGET DITEMUKAN PADA CHILD 2")

    else:
        print("\nTARGET BELUM DITEMUKAN")

while True:
    print("\n=== KAMUS BAHASA DAERAH ===")
    print("1.Tampilkan Kamus")
    print("2.Cari Kata")
    print("3.Jalankan Algoritma Genetika")
    print("4.Tampilkan Populasi")
    print("5.Hasil Fitness")
    print("6.Seleksi Roulette")
    print("7.Cross Over")
    print("8.Mutasi")
    print("9.Generasi Baru")
    print("10.Keluar")
    p=input("Pilih: ")
    if p=="1": tampil_kamus()
    elif p=="2": cari()
    elif p=="3": evaluasi()
    elif p=="4":
        print(*populasi,sep="\n")
    elif p=="5": evaluasi()
    elif p=="6": roulette()
    elif p=="7": crossover()
    elif p=="8": mutasi()
    elif p=="9": generasi()
    elif p=="10":
        break
    else:
        print("Pilihan tidak valid.")
