def persegi():
    print("menghitung luas persegi")
    panjang =int(input("masukkan nilai panjang: "))
    lebar =int(input("masukkan nilai lebar: "))
    luas =(panjang*lebar)
    print("luas persegi adalah:",luas,"cm")

persegi()

def lingkaran():
    print("menghitung luas lingkaran")
    phi =float(input("masukkan nilai phi: "))
    r =int(input("masukkan nilai r: "))
    luas =(phi*r*r)
    print("luas lingkaran adalah:",luas,"cm")

lingkaran()

def segitiga():
    print("menghitung luas segitiga")
    alas =int(input("masukkan nilai alas: "))
    tinggi =int(input("masukkan nilai tinggi: "))
    luas =(alas*tinggi/2)
    print("luas segitiga adalah:",luas,"cm")

segitiga()
