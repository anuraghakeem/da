#7) Write an R script to Implement logistic regression and Predict sales-increase using
#advertisement data set stored in csv file. Find odds and log-odds values ofyour regression analysis.

survey<-read.csv("lab7_ip.csv",header = TRUE,sep = ",")
survey
survey$sales_increase <- gsub("Yes",1,survey$sales_increase)
survey$sales_increase <- gsub("No",0,survey$sales_increase)
survey$sales_increase <- as.integer(survey$sales_increase)
lr = glm ( sales_increase ~ budget ,data = survey , family = binomial,control = list(maxit = 5))
summary(lr)
summary (lr)$coef[ ,4]
#b0 <- summary ( glm.fits)$coef[ 1,4]
#b1 <- summary ( glm.fits)$coef[ 2,4]
probs = predict(lr,type="response")
probs

odds <- probs/(1-probs)
odds

log(odds)


