def computepay(h, r):
    if h <= 40:
        return h*r
    else:
        return (r*1.5)*(h-40) + (r*40)


hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs, rate)
print("Pay", p)
