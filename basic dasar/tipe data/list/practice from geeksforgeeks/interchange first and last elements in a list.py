# interchange first and last elements in a list

'''
Program untuk menukar element pertama dengan element
terakahir pada sebuah list
'''

# Buat function misalnya swabList
def swapList(List1):

    # Proses swab
    temp = List1[0]
    List1[0] = List1[len(List1)-1]
    List1[len(List1)-1] = temp
    
    return List1


# Panggil function
List1 = [1,5,7,8,99]

print("List1 Original is: ", List1)

List1 = swapList(List1)

print("List1 Swap Result is: ", List1)
