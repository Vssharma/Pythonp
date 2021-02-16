list1=[1,4,6,8,9,12,10];
n=int(input("Enter the value of n:"));
i=0;
Finallist=[];
while i<n:
	max=0;
	for v in list1:
		if v> max:
			max=v;
	list1.remove(max);
	Finallist.append(max);
	i+=1;
 
print(max);
print(Finallist);