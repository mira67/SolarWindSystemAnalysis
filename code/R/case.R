library(RMySQL)

pingyuan_con = dbConnect(dbDriver("MySQL"), dbname = "pingyuan", host = "128.138.189.159", user = "liuqi", password="1234")

query = function(sql, con = pingyuan_con) {
  fetch(dbSendQuery(con, sql), n = 1e8)
}

#pingyuan<-odbcConnect("mysql",uid="liuqi",pwd = "1234")
#sqlTables(pingyuan)
#dam<-sqlFetch(pingyuan,"damage")
# soi<-sqlFetch(pingyuan,"soiling")
# hot<-sqlFetch(pingyuan,"hotspot")
# sha<-sqlFetch(pingyuan, "shading")
# nor<-sqlFetch(pingyuan, "normal")

dam = query("SELECT * FROM damage")
soi = query("SELECT * FROM soiling")
hot = query("SELECT * FROM hotspot")
sha = query("SELECT * FROM shading")
nor = query("SELECT * FROM normal")

plot(dam$I2,ylim=c(0,9),xlab = "timestamp (minute)",ylab = "I",
     main = "Current varies with time in a damaging string",type = "p",cex=0.1,col="red")
plot(soi$I3,ylim=c(0,9),xlab = "timestamp (minute)",ylab = "I",
     main = "Current varies with time in a soiling string",type = "p",cex=0.1,col="red")
plot(hot$I3,ylim=c(0,9),xlab = "timestamp (minute)",ylab = "I",
     main = "Current varies with time in a hotspot string",type = "p",cex=0.1,col="red")
plot(sha$I10,ylim=c(0,9),xlab = "timestamp (minute)",ylab = "I",
     main = "Current varies with time in a shading string",type = "p",cex=0.1,col="red")
plot(nor$I3,ylim=c(0,9),xlab = "timestamp (minute)",ylab = "I",
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

plot(dam$T,xlab = "timestamp (minute)",ylab = "T",
     main = "T varies with time in a damaging string",type = "p",cex=0.1,col="red")
plot(soi$T,xlab = "timestamp (minute)",ylab = "T",
     main = "T varies with time in a soiling string",type = "p",cex=0.1,col="red")
plot(hot$T,xlab = "timestamp (minute)",ylab = "T",
     main = "T varies with time in a hotspot string",type = "p",cex=0.1,col="red")
plot(sha$T,xlab = "timestamp (minute)",ylab = "T",
     main = "T varies with time in a shading string",type = "p",cex=0.1,col="red")
plot(nor$T,xlab = "timestamp (minute)",ylab = "T",
     main = "T varies with time in a normal string",type = "p",cex=0.1,col="red")

dam_full = query("SELECT data_date, combinerbox, I2 FROM pingyuan.hlx WHERE combinerbox = 'S18-NBA-HL02';")
plot(dam_full$I2,xlab = "timestamp (minute)",ylab = "current",
     main = "current varies with time in a damage string",type = "p",cex=0.1,col="red")

write.table(dam_full, file = "NYC-2016-May-79.csv", sep = ",", col.names = NA,
            qmethod = "escape")



