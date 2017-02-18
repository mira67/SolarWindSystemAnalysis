library("RODBC")
pingyuan<-odbcConnect("mysql",uid="root",pwd = "123456")
sqlTables(pingyuan)
dam<-sqlFetch(pingyuan,"damage")
plot(dam$I2,ylim=c(0,8.79),xlab = "timestamp (minute)",ylab = "I",main = "Current varies with time in damaging string",type = "p",cex=0.1)
soi<-sqlFetch(pingyuan,"soiling")
hot<-sqlFetch(pingyuan,"hotspot")
sha<-sqlFetch(pingyuan, "shading")
nor<-sqlFetch(pingyuan, "normal")
plot(dam$I2,ylim=c(0,8.79),xlab = "timestamp (minute)",ylab = "I",
     main = "Current varies with time in a damaging string",type = "p",cex=0.1,col="red")
plot(soi$I3,ylim=c(0,8.79),xlab = "timestamp (minute)",ylab = "I",
     main = "Current varies with time in a soiling string",type = "p",cex=0.1,col="red")
plot(hot$I3,ylim=c(0,8.79),xlab = "timestamp (minute)",ylab = "I",
     main = "Current varies with time in a hotspot string",type = "p",cex=0.1,col="red")
plot(sha$I10,ylim=c(0,8.79),xlab = "timestamp (minute)",ylab = "I",
     main = "Current varies with time in a shading string",type = "p",cex=0.1,col="red")
plot(nor$I3,ylim=c(0,8.79),xlab = "timestamp (minute)",ylab = "I",
     main = "Current varies with time in a normal string",type = "p",cex=0.1,col="red")
points(soi$I3,col="green",cex=0.1)
points(hot$I3,col="blue",cex =0.1)
points(sha$I10,col="cyan",cex=0.1)
points(nor$I3,co1="black",cex=0.1)
text.legend=c("damaging","soiling","hotspot","shading","normal")
col2<-c("red","green","blue","cyan","black")
legend("topleft",inset=c(-0.45,0),legend=text.legend,col = c(col,col2),pch=16)
plot(dam$PV,xlab = "timestamp (minute)",ylab = "v",
     main = "Voltage varies with time in a damaging string",type = "p",cex=0.1,col="red")
plot(soi$PV,xlab = "timestamp (minute)",ylab = "v",
     main = "Voltage varies with time in a soiling string",type = "p",cex=0.1,col="red")
plot(hot$PV,xlab = "timestamp (minute)",ylab = "v",
     main = "Voltage varies with time in a hotspot string",type = "p",cex=0.1,col="red")
plot(sha$PV,xlab = "timestamp (minute)",ylab = "v",
     main = "Voltage varies with time in a shading string",type = "p",cex=0.1,col="red")
plot(nor$PV,xlab = "timestamp (minute)",ylab = "v",
     main = "Voltage varies with time in a normal string",type = "p",cex=0.1,col="red")

