#2) Write an R script to perform the following by Storing student data set in csv file.
#a) Check for invalid entries in marks, gender and name fields.
#b) If marks field is greater than 100 or lesser than 0, replace them with NA values.
#c) If gender column has 'f', replace with 'F'. Do similarly for male entries also. Otherwise, return NA.
#d) Name column should not have special characters, numbers. Check for this and omit through your code.
#e) Store student marks semester wise and calculate average.
#g) Do above operations with and without SQL queries in R.
name <- c("jo1","jovia","ab$c","abce","GHJ","S&2D")
m1 <- c(34,178,34,178,56,-45)
m2 <- c(56,189,34,155,78,65)
m3 <- c(94,78,68,23,78,-56)
#name <- as.character(name)
gender <- c('m','M','female','f','male','F')
ds = data.frame(name,m1,m2,m3,gender)
ds1 = data.frame(name,m1,m2,m3,gender)
invalid_name <- subset(ds,select=c("name"),subset=grepl("[^a-zA-Z]",name))
invalid_name
invalid_m1 <- subset(ds,select=c("m1"),subset=(m1>100|m1<0))
invalid_m2 <- subset(ds,select=c("m2"),subset=(m2>100|m2<0))
invalid_m3 <- subset(ds,select=c("m3"),subset=(m3>100|m3<0))
invalid_m1
invalid_m2
invalid_m3
invalid_gender <-subset(ds,select = c("gender"),subset = !(gender=="F"|gender=='M'))
invalid_gender
ds$m1[ds$m1>100|ds$m1<0]=0
ds$m2[ds$m2>100|ds$m2<0]=0
ds$m3[ds$m3>100|ds$m3<0]=0
ds$gender[ds$gender=='m'|ds$gender=='male']='M'
ds$gender[ds$gender=='f'|ds$gender=='female']='F'
ds$name = gsub("[^a-zA-Z]","",ds$name)
ds$avg = (ds$m1+ds$m2+ds$m3)/3
ds

library('sqldf')
t=sqldf('select m1 as invalid_m1 from ds1 where m1>100 OR m1<0 ')
t
for (i in t$invalid_m1)
{
  ds1$m1[ds1$m1==i]=0
}
t=sqldf('select m2 as invalid_m2 from ds1 where m2>100 OR m2<0 ')
t
for (i in t$invalid_m2)
{
  ds1$m2[ds1$m2==i]=0
}
t=sqldf('select m3 as invalid_m3 from ds1 where m3>100 OR m3<0 ')
t
for (i in t$invalid_m3)
{
  ds1$m3[ds1$m3==i]=0
}

sqldf('select gender from ds1 where gender!="F" and gender!="M" ')
t1 <-sqldf('select gender as in1 from ds1 where gender="f" or gender="female" ')
t1
t2 <-sqldf('select gender as in2 from ds1 where gender="m" or gender="male" ')
t2
ds1$gender <- as.character(ds1$gender)
for (i in t1$in1)
{
  ds1$gender[ds1$gender==i] = 'F'
}
for (i in t2$in2)
{
  ds1$gender[ds1$gender==i] = 'M'
}
ds1$name <- as.character(ds1$name)
t=sqldf('select name as invalid_name from ds1 where name like "%$%" UNION select name from ds1 where name like "%&%" ')
t
for (i in t$invalid_name)
{
ds1$name[ds1$name==i] = gsub("[^a-zA-Z]","",i)
}
ds1$avg = sqldf('select (m1+m2+m3)/3 as avg from ds1')
ds1

