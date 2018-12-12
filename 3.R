#3)Write an R script to predict the sales increase in the number of units using linear regression.
#Store the input in csv file with the following fields media_used_for_advertisement,media_name,
#sales_no_of_units_increased. Plot predictor value against response value.

ds = read.csv("sales.csv")
ds
x=mean(ds$no_of_units)
y=mean(ds$sales)
num = sum((ds$no_of_units-x)*(ds$sales-y))
deno = sum((ds$no_of_units-x)^2)
b1=num/deno
b0 = y- x*b1
ds$ypred =  b0 + b1*ds$no_of_units
ds$error = (ds$sales - ds$ypred)
ds
rss <- sum(ds$error^2)
rss
tss <- sum((ds$sales - y)^2)
tss
r2 <- 1-rss/tss 
r2
rse <- sqrt(rss/(length(ds$sales)-2))
rse
se.b0 <- (rse^2)*(1/length(ds$sales)+(x^2/deno))
se.b0
se.b1<- (rse^2)/deno
se.b1
plot(x=ds$no_of_units,y=ds$sales,col='red',type='l')
lines(x=ds$no_of_units,y=ds$ypred,col='blue')



