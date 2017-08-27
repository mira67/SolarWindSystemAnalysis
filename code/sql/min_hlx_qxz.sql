CREATE TABLE hlx_qxz_min_all AS (
SELECT hlx.combinerbox,hlx.data_date, hlx.I1,hlx.I2,hlx.I3,hlx.I4,hlx.I5,hlx.I6,hlx.I7,hlx.I8,hlx.I9,hlx.I10,
hlx.I11,hlx.I12,hlx.I13,hlx.I14,hlx.I15,hlx.I16,hlx.T,hlx.PV,hlx.LS,
qxz.FS1, qxz.Fs2, qxz.Fs1m, qxz.Fs2m, qxz.Wv, qxz.Wd, qxz.Sd, qxz.T0 
FROM hlx
LEFT JOIN qxz ON hlx.data_date = qxz.data_date
)