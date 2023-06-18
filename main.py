def generateQuery():
    emailformat="email='testanalystsai+{0}@gmail.com'"
    finallist=""
    for i in range(71,131):
        if i<10:
            finallist=finallist +emailformat.format('0'+str(i))+" or "
        else:
            finallist = finallist + emailformat.format(str(i)) + " or "

    QueryList=open("ff.txt",'w')
    QueryList.writelines(finallist[0:len(finallist)-3].strip())
    QueryList.flush()
    QueryList.close()
    print(finallist[0:len(finallist)-3])
generateQuery()