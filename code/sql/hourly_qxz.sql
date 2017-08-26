CREATE TABLE qxz_hour AS(

SELECT DATE(data_date) as d_date, HOUR(data_date) as the_hour, AVG(Fs1m) as Fs1m, AVG(Fs2m) as Fs2m, AVG(Wv) as Wv, AVG(Wd) as Wd, AVG(Sd) AS Sd
,AVG(T0) as T
  FROM qxz   
  GROUP BY d_date, the_hour
)