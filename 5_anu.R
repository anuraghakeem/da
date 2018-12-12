ds=read.csv('sales1.csv')
ds

x1=mean(ds$TV)
x1
x2=mean(ds$Radio)
x2
y=mean(ds$Sales)
y

num1=sum((ds$TV-x1)*(ds$Sales-y))
den1=sum((ds$TV-x1)^2)
num2=sum((ds$Radio-x2)*(ds$Sales-y))
den2=sum((ds$TV-x2)^2)
b1=num1/den1
b2=num2/den2
b0 = y - (x1*b1) - (x2*b2)
ds$y_pred = b0 + (b1*ds$TV) + (b2*ds$Radio)

ds