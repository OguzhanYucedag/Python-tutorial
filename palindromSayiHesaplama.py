pSayı = 0
pToplam = 0
pBasamak = [0,0,0,0,0,0,0]#pBasamak =[0,1,2,3]
sayıyaKadar = int(input("Kaçıncı sayıya kadar palindrom sayıları saysın ve hesaplasın..:"))
for i in range(1,sayıyaKadar +1):
    x = str(i)
    if x == x[::-1]:
        pSayı += 1#pSayı=pSayı+1#pSayı++
        pToplam += int(x)#pToplam =pToplam+1
        pBasamak[len(x)-1] += 1#12=>'12'
        
        #print(len(x))
        
    
    
    
    

print("Palindrom sayı adedi :", pSayı)
print("Palindrom sayıların toplamı:",pToplam)
print("Palindrom Hangi Basamakta kaç tane var :", pBasamak)




