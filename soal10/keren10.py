import shapefile

w = shapefile.Writer('soal12')
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("coba1","satu")

w.poly([[
    [1,1],
    [4,6],
    [7,1]
]])

w.close()