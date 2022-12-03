# c style formating

print("%d" % 432)
print("%d %d" % (432, 345))
print("%f" %(432.123))
print("%f %f" % (432.123, 10.3))
print("%f" %432.123456)
print("%f" %432.12345651)
print("%s" % "geekyshows")
print("%s %s" % ("hello" , "geekyshows"))
print("%d %s" %(432, "geekyshows"))

print("%(nm)s %(ag)d" %{'ag':432, 'nm': "geekyshows"})

print("%d" %(432))

print("% d" % 432)
print("%+d" % 432)

# precision type

print("%8d" % 432)
print("%08d" % 432)
print("%.3f" % 432.123)
print("%.2f" % 432.123)
print("%.2f" % 432.128)
print("%9.2f" % 432.128)
print("%09.2f" % 432.123)
print("%9.2f" % 4388453232.124)