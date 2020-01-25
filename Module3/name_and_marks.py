res=input()
l1=res.split(",")
l2=[int(i) for i in l1[1:]]
print(l1[0],"obtained",sum(l2[0:-3]),"out of","500 in theory and",sum(l2[-3:]),"""marks out of 90 in practical and
successfully passed the exam with""","{0:.2f}".format((sum(l2[0:-3])+sum(l2[-3:]))/590*100),"% in aggregate.Many congrulations to",l1[0],".")
