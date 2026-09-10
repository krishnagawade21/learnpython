#initialize Weights
w1=0
w2=0
theta=2
Continue=1

#training data
X=[(1,1),(0,1),(1,0),(0,0)]
Y=[1,0,0,0]

for (x1,x2),y in zip(X,Y):
  w1=w1+x1*y
  w2=w2+x2*y

while Continue:

  attendance=float(input("\nEnter attendance percentage: "))
  assignment=int(input("Assignment submitted? (1=Yes, 0=No): "))

  x1=1 if attendance >= 75 else 0
  x2=assignment

  net=(x1*w1)+(x2*w2)

  if net >=theta:
    print("\nEligible For Internal Exam")
  else:
    print("\nNot Eligible For Internal Exam")

  Continue=int(input("\nDo you want to continue? (0=No 1=Yes): "))
