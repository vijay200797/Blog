lst =["Ram", "Avtar", "","Sumit", "ABC"]

def chkStr(words):
    if words:
        return True
    else:
        return False

li =list(filter(chkStr,lst))
print(li)