# Salin daripada README
MEJA_TERJEMAHAN = '''False    Palsu                ڤلسو
None     Tiada                تياد
True     Benar                بنر
and      dan                  دان
as       sebagai              سباڬاي
assert   =                    =
async    =                    =
await    =                    =
break    putus                ڤوتوس
class    kelas                كلس
continue lanjut               لنجوت
def      fungsi               فوڠسي
del      hapus                هاڤوس
elif     =                    =
else     lain                 لاءين
except   kecuali              كچوالي
finally  akhirnya             اخيرڽ
for      untuk                ونتوق
from     dari                 دري
global   =                    =
if       jika                 جك
import   =                    =
in       dalam                دالم
is       ialah                اياله
lambda   =                    =
nonlocal =                    =
not      bukan                بوكن
or       atau                 اتاو
pass     =                    =
raise    =                    =
return   kembali              كمبالي
try      cuba                 چوبا
while    ketika               كتيك
with     dengan               دڠن
yield    =                    ='''

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
