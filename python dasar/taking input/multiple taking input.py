# TAKING MULTIPLE INPUT

while True:
    try:
        x, y, z = map(int, input("Masukkan data x , y dan z : Format : 999  999 999 ").split())
        if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
            break
        else:
            print("Masukkan nilai integer yang valid untuk x, y, dan z ! ")
            
    except ValueError as e:
        print("Data yang anda masukkan bukan integer, tidak valid!")
        
        
