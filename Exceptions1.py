try:
    fo = open("testfile.txt","r")
    try:
        fo.write("Vijay - Data Scientist")
    finally:
        print "I am closing this file !!!"
        fo.close()
except IOError:
    print "Error: can\'t find file or read data"
