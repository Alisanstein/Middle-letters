def mid(string):
    lis = list(string)
    
    if len(lis)%2 == 0:
        return ""
    
    else: 
        return lis[int(((len(lis)+1)/2)-1)]