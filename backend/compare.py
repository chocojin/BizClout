import math

def comp(bizCat, influCat):
    bizCat.replace(" & ","/")
    influCat.replace(" & ", "/")
    bizCat.split("/");
    influCat=s.split("/");

    list(set(bizCat))
    list(set(influCat))

    diffSet=list(set(bisCat)-set(influCat))

    return len(diffSet)

valList=[]
influList=[]

for i in range (influ_num):
    channel= ""
    bizCat=""
    influCat""
    val=comp(bizCat, influCat)
    valList.append(val)
    influList.append(channel)

valList, influList = (list(x) for x in zip(*sorted(zip(valList, influList))))
return influList

