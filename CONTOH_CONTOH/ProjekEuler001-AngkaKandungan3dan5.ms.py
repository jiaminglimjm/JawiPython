# https://projecteuler.net/problem=1
jawapan = 0

untuk n dalam julat(1000):
    jika n % 3 == 0:
        jawapan += n
    jika n % 5 == 0:
        jawapan += n
    jika n % 15 == 0:
        jawapan -= n

cetak(jawapan)
