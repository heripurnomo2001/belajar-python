#program untuk menghilangkan tanda baca pada sebuah teks
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

teks = str(input("Masukkan kalimat dengan tanda baca: "))

no_punct = ""
for char in teks:
    if char not in punctuations:
        no_punct = no_punct + char

print(no_punct)