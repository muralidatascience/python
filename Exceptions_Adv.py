def someFunction(level):
    print level
    if level<2:
        try:
            raise ValueError('Invalid level to start the game')
        except Exception,arg:
            print 'Error:',arg
        
    
