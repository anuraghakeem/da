#6)Create the credit data set with the following columns:
#.name,age, cards (number of credit cards),
#.education (years of education),
#.income (in thousands of dollars),
#.limit (credit limit), and
#.rating (credit rating
#*balance
#.gender, student (student status)
#.status (marital status), and
#.ethnicity (Caucasian, African American or Asian)
#a) Predict balance of each person using his/her income and using column whether he/she is student
#or not using regression analysis.
#b) predict balance of each person using his/her gender using regression analysis.
#c) predict balance of each person using his/her ethnicity using regression analysis.

ds <- read.csv('credit.csv')
ds
ds$student = gsub('yes',1,ds$student)
ds$student = gsub('no',0,ds$student)
ds$ethnicity = gsub('caucasian',1,ds$ethnicity)
ds$ethnicity = gsub('American',-1,ds$ethnicity)
ds$ethnicity = gsub('African',0,ds$ethnicity)
ds$gender = gsub('f',1,ds$gender)
ds$gender = gsub('m',0,ds$gender)
ds

# balance = b0 + b1*student + b2*income
x1 = mean(as.integer(ds$student))
x2 = mean(ds$income)
y = mean(ds$balance)
num1 = sum(((as.integer(ds$student))-x1)*(ds$balance-y))
deno1= sum(((as.integer(ds$student))-x1)^2)
b1 = num1/deno1
num2 = sum((ds$income-x2)*(ds$balance-y))
deno2= sum((ds$income-x2)^2)
b2 = num2/deno2
b0 = y - b1*x1 - b2*x2
ds$balance_pred_1= b0 + b1*(as.integer(ds$student)) + b2*ds$income
ds

# balance = b0 + b1*gender
x = mean(as.integer(ds$gender))
y = mean(ds$balance)
num = sum(((as.integer(ds$gender))-x1)*(ds$balance-y))
deno= sum(((as.integer(ds$gender))-x1)^2)
b1 = num/deno
b0 = y - b1*x
ds$balance_pred_2= b0 + b1*(as.integer(ds$gender))
ds

# balance = b0 + b1*ethnicity
x = mean(as.integer(ds$ethnicity))
y = mean(ds$balance)
num = sum(((as.integer(ds$ethnicity))-x1)*(ds$balance-y))
deno= sum(((as.integer(ds$ethnicity))-x1)^2)
b1 = num/deno
b0 = y - b1*x
ds$balance_pred_3= b0 + b1*(as.integer(ds$ethnicity))
ds

