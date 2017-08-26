CREATE TABLE nbq_qxz_hour AS (
SELECT nbq_s01_nba_hour.nbqno, nbq_s01_nba_hour.d_date, nbq_s01_nba_hour.the_hour, nbq_s01_nba_hour.aP, nbq_s01_nba_hour.aI, nbq_s01_nba_hour.aV,
nbq_s01_nba_hour.a_r, qxz_hour.Fs1m, qxz_hour.Fs2m, qxz_hour.Wv, qxz_hour.Wd, qxz_hour.Sd, qxz_hour.T 
FROM nbq_s01_nba_hour
LEFT JOIN qxz_hour ON nbq_s01_nba_hour.d_date = qxz_hour.d_date AND nbq_s01_nba_hour.the_hour = qxz_hour.the_hour
)