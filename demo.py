i=1

while i<=150:
    print "Count at :",i
    if i == 150/2:
        print "half way through, almost there"
    i+=1

print "this is now an acceptable amount"
i-=1
print "the amount now is",i
print "now we will subtract 50 from",i
print i,"- 50"
i-=50
print "the amount now is",i
print "now we will count backwards from",i
while i>=0:
    print "Count at :",i
    if i == 50:
        print "half way through, almost there"
    i-=1
