class Parent:
    parentAttr=100
    def __init__(self):
        print "Calling parent Constructor"
    def parentMethod(self):
        print "Calling parent Method"
    def setAttr(self,attr):
        Parent.parentAttr=attr
    def getAttr(self):
        print "Parent Attribute -",Parent.parentAttr


class Child(Parent):
    def __init__(self):
        print "Calling child Constructor"
    def childMethod(self):
        print "Calling child Method"
