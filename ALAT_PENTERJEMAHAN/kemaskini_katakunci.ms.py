# Salin daripada README
MEJA_TERJEMAHAN = '''False    Palsu                ڤلسو
None     Tiada                تياد
True     Benar                بنر
and      dan                  دان
as       sebagai              سباݢاي
assert   =                    =
async    =                    =
await    =                    =
break    putus                ڤوتوس
class    kelas                کلس
continue lanjut               لنجوت
def      fungsi               فوڠسي
del      hapus                هاڤوس
elif     jikain               جکاءين
else     lain                 لاءين
except   kecuali              کچوالي
finally  akhirnya             اخيرڽ
for      untuk                اونتوق
from     dari                 دري
global   =                    ݢلوبل
if       jika                 جک
import   =                    ايمڤورت
in       dalam                دالم
is       ialah                اياله
lambda   =                    =
nonlocal =                    =
not      bukan                بوکن
or       atau                 اتاو
pass     =                    =
raise    =                    =
return   kembali              کمبالي
try      cuba                 چوبا
while    ketika               کتيک
with     dengan               دڠن
yield    =                    ='''

pisah = str.split
ganti = str.replace

dengan buka('../Grammar/python.en.gram', 'r') sebagai f:
    tatabahasa = f.baca()

untuk garis dalam pisah(MEJA_TERJEMAHAN, '\n'):
    inggeris, rumi, jawi = pisah(garis)
    jika bukan (rumi == '=' atau jawi == '='):
        tatabahasa = ganti(tatabahasa, "a='%s'" % inggeris, "|||+|||=%s" % inggeris)
        tatabahasa = ganti(tatabahasa, "'%s'" % inggeris, "('%s'|'%s'|'%s')" % (inggeris, jawi, rumi))
        tatabahasa = ganti(tatabahasa, "|||+|||=%s" % inggeris, "a='%s'" % inggeris,)

dengan buka('../Grammar/python.gram', 'w') sebagai f:
    f.tulis(tatabahasa)

#cetak(tatabahasa)
