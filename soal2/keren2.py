import shapefile

w = shapefile.Writer('soal2', shapeType=1)
w.shapeType

w.field('kolom1', 'B')
w.field('kolom2', 'B')

w.record('coba1', 'satu')
w.record('coba2', 'dua')

w.point(1,1)
w.point(2,2)

w.close()

