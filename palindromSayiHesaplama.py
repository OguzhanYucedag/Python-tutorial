pSayı = 0
pToplam = 0
pBasamak = [0,0,0,0,0,0,0]
sayıyaKadar = int(input("Kaçıncı sayıya kadar palindrom sayıları saysın ve hesaplasın..:"))
for i in range(1,sayıyaKadar +1):
    x = str(i)
    if x == x[::-1]:
        pSayı += 1
        pToplam += int(x)
        pBasamak[len(x)-1] += 1
        print("***")
    
    
    

print("Palindrom sayı adedi :", pSayı)
print("Palindrom sayıların toplamı:",pToplam)
print("Palindrom Hangi Basamakta kaç tane var :", pBasamak)




