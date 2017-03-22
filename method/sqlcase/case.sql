create table damage SELECT combinerbox,riqi,I2,T,PV FROM pingyuan.hlx where combinerbox='S18-NBA-HL02' AND riqi>='2016-05-01 00:00:00';
create table soiling SELECT combinerbox,riqi,I3,T,PV FROM pingyuan.hlx where combinerbox='S06-NBA-HL06' AND riqi>='2016-05-01 00:00:00';
create table shading SELECT combinerbox,riqi,I10,T,PV FROM pingyuan.hlx where combinerbox='S35-NBA-HL06' AND riqi>='2016-05-01 00:00:00';
create table normal SELECT combinerbox,riqi,I3,T,PV FROM pingyuan.hlx where combinerbox='S07-NBB-HL10' AND riqi>='2016-05-01 00:00:00';