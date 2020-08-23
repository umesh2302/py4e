hours = input ("enter hours")
rate = input ("enter rate")
h1= float(hours)
r1 = float(rate)
def computepay (h,r):
    
    if h <= 40:
        pay = h*r
    else :
        pay = 40*r+ (h-40)*r*10.5
    return (pay)

print (compute)