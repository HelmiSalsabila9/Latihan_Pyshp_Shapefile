import shapefile

w = shapefile.Writer('soal4', shapefile.POINTM)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek", "satu")
w.record("ngok", "dua")

w.pointm(1,1)
w.pointm(2,2)

w.close()