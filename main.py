import random

def guess(x):
    random_number =random.randint(1,x)
    guess=0
    while guess!= random_number:
        guess=int(input(f'Bir sayı tahmin et (0 ile {x+1} arasında) : '))
        if guess < random_number:
            print ('Tekrar dene!! Küçük sayı girdin.')
        elif guess > random_number:
            print('Tekrar dene !! Büyük sayı girdin. ')
    
    print(f'Tebrikler {random_number} sayısını doğru tahmin ettin.')


guess(10)