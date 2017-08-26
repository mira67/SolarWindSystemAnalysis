CREATE TABLE nbq_s01_NBA_hour AS(

SELECT nbqno, DATE(data_date) as d_date, HOUR(data_date) as the_hour, AVG(p) as ap, AVG(I) as aI, AVG(V) as aV, AVG(xiaolv) as a_r
  FROM nbq    
  WHERE nbqno = 'S01-NBA'
  GROUP BY nbqno, d_date, the_hour
)