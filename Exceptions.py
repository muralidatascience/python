try:
    fh=open("testfile1.txt","r")
    try:
        fh.write("This is my first Exceptional Handing Program!!!")
    finally:
        print "Everything is right"
        print "Vijay-Data Scientist"
        fh.close()
except IOError:
    print "Error: can\'t find file or read data"

print "Sai Teja - Data Scientist"
