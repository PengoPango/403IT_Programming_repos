print("Let's form a band")


band = []
while len(band) < 4:
    print("Pick an instrument:")
    instrument = input()

    if instrument in band:
        print ("This instrument is already in the band")
    else:
        band.append(instrument)
print("your band includes:")
print(band)
