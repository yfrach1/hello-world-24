def make_sequence(lst):
    """ py string"""
    lst=lst
    index=0
    def all_filter(f=None):
        return (tuple(filter(f,lst)))

    def return_filter(f):
        t=(all_filter(f))
        
        def next():
            nonlocal index,t
            if (index )==len(t):
                index=0
            print (t[index])
            index+=1
    
        def reverse():
            nonlocal index,t
            if (index-1)==-1:
                index=len(t)
            index-=1
            print (t[index])
        return {'next':next,'reverse':reverse}

    def reverse():
        l=[]
        for i in range (len(lst)-1,-1,-1):
            l+=[lst[i]]
        return tuple(l)
    
    def extend(add):
        nonlocal lst
        l=[]
        for i in range (len(lst)):
            l+=[lst[i]]
        for i in range (len(add)):
            l+=[add[i]]
        lst=l
        return tuple(lst)

    def clear():
        nonlocal lst
        lst=()
        return lst
    return {'all_filter':all_filter,'return_filter':return_filter,'reverse':reverse,'extend':extend,'clear':clear}

