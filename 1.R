##  Write an R script to perform the following:
#a) Store students' USN,6 subjects' CIE marks and SEE marks in three vectors
#b) Find total of CIE and SEE for each student in each subject
#c) Find student grades in each subject
#d) Find the topper's name in each subject
#e) Store students' details in CSV file and perform the above operations.
#f) Perform the above operations using SQL queries in R.

name <- c('jo','jovia','abc')
cie1 <- c(34,78,78)
see1 <- c(56,89,90)
cie2 <- c(34,78,45)
see2 <- c(56,89,34)
cie3 <- c(94,78,68)
see3 <- c(96,39,40)
total1 <- cie1*0.5 + see1*0.5
total2 <- cie2*0.5 + see2*0.5
total3 <- cie3*0.5 + see3*0.5
total1
total2
total3
f <- function(total)
{
  grade <- c()
for(i in 1:length(total))
{
  if(total[i]>=90)
    grade[i]= 'A'
  else if(total[i]>=75)
    grade[i]='B'
  else if(total[i]>=60)
    grade[i]='C'
  else if(total[i]>=40)
    grade[i]='D'
  else
    grade[i]='F'
}
  print("marks: ")
  grade
}
f(total1)
f(total2)
f(total3)
maxi1 = which(total1=max(total1))
print(maxi1)
print(name[maxi1])
maxi2 = which(total1=max(total1))
print(maxi2)
print(name[maxi2])
maxi3 = which(total1=max(total1))
print(maxi3)
print(name[maxi3])

ds <- read.csv("stud.csv")
name <- ds$name
cie1 <- ds$cie1
see1 <- ds$see1
cie2 <- ds$cie2
see2 <- ds$see2
cie3 <- ds$cie3
see3 <- ds$see3
total1 <- cie1*0.5 + see1*0.5
total2 <- cie2*0.5 + see2*0.5
total3 <- cie3*0.5 + see3*0.5
total1
total2
total3
f <- function(total)
{
  grade <- c()
  for(i in 1:length(total))
  {
    if(total[i]>=90)
      grade[i]= 'A'
    else if(total[i]>=75)
      grade[i]='B'
    else if(total[i]>=60)
      grade[i]='C'
    else if(total[i]>=40)
      grade[i]='D'
    else
      grade[i]='F'
  }
  print("marks")
  grade
}
f(total1)
f(total2)
f(total3)
maxi1 = which(total1==max(total1))
print(maxi1)
print(name[maxi1])
maxi2 = which(total2==max(total2))
print(maxi2)
print(name[maxi2])
maxi3 = which(total3==max(total3))
print(maxi3)
print(name[maxi3])




ds <- read.csv("stud.csv")
library('sqldf')
t=sqldf("SELECT cie1*0.5 + see1*0.5 as total1 FROM ds ")
ds=transform(ds,total1=t$total1)
t=sqldf("SELECT cie2*0.5 + see2*0.5 as total2 FROM ds ")
ds=transform(ds,total2=t$total2)
t=sqldf("SELECT cie3*0.5 + see3*0.5 as total3 FROM ds ")
ds=transform(ds,total3=t$total3)
t=sqldf('Select CASE WHEN total1>=90 THEN "S"

         WHEN total1>=75 THEN "A"

         WHEN total1>=65 THEN "B"

         WHEN total1>=60 THEN "C"

         WHEN total1>=50 THEN "D"

         WHEN total1>=40 THEN "E"

         ELSE "F"

         END AS grade1 from ds')
ds=transform(ds,grade1=t$grade1)
t=sqldf('Select CASE WHEN total2>=90 THEN "S"

         WHEN total1>=75 THEN "A"

         WHEN total1>=65 THEN "B"

         WHEN total1>=60 THEN "C"

         WHEN total1>=50 THEN "D"

         WHEN total1>=40 THEN "E"

         ELSE "F"

         END AS grade2 from ds')
ds=transform(ds,grade2=t$grade2)
t=sqldf('Select CASE WHEN total3>=90 THEN "S"

         WHEN total1>=75 THEN "A"

         WHEN total1>=65 THEN "B"

         WHEN total1>=60 THEN "C"

         WHEN total1>=50 THEN "D"

         WHEN total1>=40 THEN "E"

         ELSE "F"

         END AS grade3 from ds')

ds=transform(ds,grade3=t$grade3)
ds
sqldf('Select name,max(total1) from ds')
sqldf('Select name,max(total2) from ds')
sqldf('Select name,max(total3) from ds')