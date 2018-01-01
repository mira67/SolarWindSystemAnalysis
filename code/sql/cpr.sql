SELECT * FROM pingyuan.nbqday;

select riqi, avg(cpr) from pingyuan.nbqday group by riqi;

select riqi, avg(DayProduction*1000/(V*I)) as Yf from pingyuan.nbq group by riqi;

select riqi, sum(Dayproduction) as ACDly from pingyuan.nbq group by riqi