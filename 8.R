#VIF is used to estimate multicollinearity.If VIF>10 the variable is highly collinear wrt other predictors

#8)Write an R script to find Variance Inflation Factor and high leverage points of advertisement
#dataset which is stored in CSV file. Check for collinearity in advertisement data.

sales<-c(100,200,300,400,300)

radio<-c(3000,400,600,800,900)
tv<-c(10,20,30,40,50)
newspaper<-c(450,340,320,890,876)

survey<-data.frame(sales,radio,tv,newspaper)
survey

model<-lm(sales~radio+tv+newspaper,data=survey)
summary(model)

library(HH)
vif(model)

###### If parkavi tells you cant use function do like this
####### To find VIF for newspaper
model1<-lm(newspaper~radio+tv,survey)
summary(model1)

#Use R square value from summary of model1 
1/(1-0.7932)
4.83559

####### To find VIF for radio
model2<-lm(radio~newspaper+tv,survey)
summary(model2)

#Use R square value from summary of model2 
1/(1-0.6468)
2.831

####Similarly do for tv also if you want



##################  High leverage points
# We will do for radio

#findComp1<-function(x){
# return((x-xbar)*(x-xbar))
#}

xbar<-mean(radio)

#deno<-sapply(radio,findComp1)
denominator<-sum((radio-xbar)^2)

n<-length(radio)
n

#findComp2<-function(x){
#  return((1/n)+((x-xbar)*(x-xbar)/denominator))
#}

#high_val<-sapply(radio,findComp2)
high_val = ((1/n)+((radio-xbar)*(radio-xbar)/sum((radio-xbar)^2)))
high_val

#If high_val if greater than (p+1)/n , (p is 1 here because we use only radio)it is a high leverage point
print('High leverage points are ')
for(i in 1:n)
{
  if(high_val[i]>(2/n))
    print(radio[i])
}


###################Collinearity using correlation matrix
cor(survey)

#If value is close to 1 then they are correlated Eg: TV and newspaper