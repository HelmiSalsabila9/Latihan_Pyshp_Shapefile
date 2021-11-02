import shapefile

w = shapefile.Writer('soal1')
w.shapeType

w.field('kolom1', 'A')
w.field('kolom2', 'A')

w.record('coba1', 'satu')
w.record('coba2', 'dua')

w.point(1,1)
w.point(2,2)

w.close()
