import shapefile

w = shapefile.Writer('soal9')
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("coba1","satu")
w.record("coba2","dua")


w.poly([[
    [1,3],
    [5,3],
    [5,2],
    [1,2],
    [1,3]
]])

w.poly([[
    [1,6],
    [5,6],
    [5,9],
    [1,9],
    [1,6]
]])


w.close()