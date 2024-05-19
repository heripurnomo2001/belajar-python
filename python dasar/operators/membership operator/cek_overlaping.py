# Cek Overlaping

# Buat fungsi 
def overlaping(list1, list2):
    c = 0
    d = 0
    for i in list1:
        c += 1
    for j in list2:
        d += 1
    for i in range(0, c):
        for j in range(0, d):
            if(list1[i] == list2[j]):
                    return 1
    return 0



# Driver Code
list1 = ['duku', 'mangga', 'jambu', 'salak']
list2 = ['rambutan', 'salak', 'durian', 'sawo', 'mangga']
if overlaping(list1, list2):
    print("overlaping")
else:
    print("not overlaping")
 

