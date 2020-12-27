def sort(List):
    cnt =0
    for i in range(len(List)):
        for j in range(len(List)-1):
            if List[j]> List[j +1]:
                List[j], List[j +1]= List[j +1], List[j]
                cnt +=1
                if cnt ==0:
                    break

x =[5,9,10,8,2,1,6,3,4,7]
sort(x)
print(x)