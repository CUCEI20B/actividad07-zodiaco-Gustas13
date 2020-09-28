d = int(input())
m = int(input())

if m == 12:
    signo = "sagitario" if (d<21) else "capricornio"

elif m == 1:
    signo = "capricornio" if (d<20) else "acuario"

elif m == 2:
    signo = "acuario" if (d<19) else "piscis"

elif m == 3:
    signo = "piscis" if (d<21) else "aries"

elif m == 4:
    signo = "aries" if (d<20) else "tauro"

elif m == 5:
    signo = "tauro" if (d<21) else "geminis"

elif m == 6:
    signo = "geminis" if (d<21) else "cancer"

elif m == 7:
    signo = "cancer" if (d<23) else "leo"

elif m == 8:
    signo = "leo" if (d<23) else "virgo"

elif m == 9:
    signo = "virgo" if (d<23) else "libra"

elif m == 10:
    signo = "libra" if (d<23) else "escorpion"

elif m == 11:
    signo = "escorpion" if (d<21) else "sagitario"

print (signo)