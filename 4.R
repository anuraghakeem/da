#4) Write an R script to implement KNN algorithm for predicting whether the customer will pay
#the loan amount or not. Store the input attributes age, loan_amount,gender,student_status and paid
#status in csv file.
age <- c(12,56,34,98,22)
loan_amount <- c(400,56000,60000,34000,23456)
gender<- c('f','f','m','m','f')
student_status <- c(1,0,0,0,1)
paid <- c(1,0,0,0,1)
ds <- data.frame(age,loan_amount,gender,student_status,paid)
ds$dist= sqrt((ds$loan_amount-5000)^2+(ds$paid-1)^2)
k=3
y<- head(ds[order(ds$dist),],k)
y
library('plyr')
freqy <- count(y,'paid')
freqy
ypred = freqy$paid[freqy$freq==max(freqy$freq)]
ypred
