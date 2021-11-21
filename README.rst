JawiPython daripada CPython versi 3.11.0 alfa 1
===============================================

.. contents::

Cara Kompil & Guna
------------------

Untuk Unix, Linux, BSD, macOS, dan Cygwin::

    ./configure         # hanya untuk pertama kali
    make regen-pegen    # kemaskini parser
    make                # cipta fail binari

Ini akan membina fail binari ``python``. Ini TIDAK akan memasang python kepada sistem anda. Ia hanya mencipta sebuah fail binari yang boleh mengeksekusi fail python yang ditulis dalam Bahasa Inggeris, Bahasa Melayu (Rumi) atau Jawi.

Untuk mengetahui lebih lanjut tentang pengkompilan untuk MacOS dan Windows, sila lihat `github.com/python/cpython#build-instructions`_. Saya pernah cuba kompil untuk Windows dengan mengikut arahan2 dalam pautan itu, tapi itu untuk versi 3.9 lah, entah kalau sudah berubah, tapi saya rasa stepsnya masih sama...

.. _github.com/python/cpython#build-instructions: https://github.com/python/cpython#build-instructions

.. image:: https://raw.githubusercontent.com/jiaminglimjm/JawiPython/master/CONTOH_CONTOH/ProjekEulerMasalah1_RUMI.png

.. image:: https://raw.githubusercontent.com/jiaminglimjm/JawiPython/master/CONTOH_CONTOH/ProjekEulerMasalah1_JAWI.png

`Fail contoh di sini`_

.. _Fail contoh di sini: https://github.com/jiaminglimjm/JawiPython/blob/master/CONTOH_CONTOH/ProjekEuler001-AngkaKandungan3dan5.ms.py

Kalau ada kesilapan di bawah, sila memberitahu saya dekat "github issues" atau emel. Saya masih belajar bahasa melayu, dan projek ini adalah salah satu cara saya melalukannya.

Terjemahan kata-kata kunci
--------------------------

======== ==================== ====================
Inggeris Bahasa Melayu (Rumi) Bahasa Melayu (Jawi)
======== ==================== ====================
False    Palsu                ڤلسو
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
yield    =                    =
======== ==================== ====================

Terjemahan fungsi piawai
------------------------

========================= =========================== ===========================
        Inggeris              Bahasa Melayu (Rumi)        Bahasa Melayu (Jawi)
========================= =========================== ===========================
ArithmeticError           =                           =
AssertionError            =                           =
AttributeError            =                           =
BaseException             =                           =
BlockingIOError           =                           =
BrokenPipeError           =                           =
BufferError               =                           =
BytesWarning              =                           =
ChildProcessError         =                           =
ConnectionAbortedError    =                           =
ConnectionError           =                           =
ConnectionRefusedError    =                           =
ConnectionResetError      =                           =
DeprecationWarning        =                           =
EOFError                  =                           =
Ellipsis                  =                           =
EnvironmentError          =                           =
Exception                 =                           =
False                     Palsu                       ڤلسو
FileExistsError           =                           =
FileNotFoundError         =                           =
FloatingPointError        =                           =
FutureWarning             =                           =
GeneratorExit             =                           =
IOError                   =                           =
ImportError               =                           =
ImportWarning             =                           =
IndentationError          =                           =
IndexError                =                           =
InterruptedError          =                           =
IsADirectoryError         =                           =
KeyError                  =                           =
KeyboardInterrupt         =                           =
LookupError               =                           =
MemoryError               =                           =
ModuleNotFoundError       =                           =
NameError                 =                           =
None                      Tiada                       تياد
NotADirectoryError        =                           =
NotImplemented            =                           =
NotImplementedError       =                           =
OSError                   =                           =
OverflowError             =                           =
PendingDeprecationWarning =                           =
PermissionError           =                           =
ProcessLookupError        =                           =
RecursionError            =                           =
ReferenceError            =                           =
ResourceWarning           =                           =
RuntimeError              =                           =
RuntimeWarning            =                           =
StopAsyncIteration        =                           =
StopIteration             =                           =
SyntaxError               =                           =
SyntaxWarning             =                           =
SystemError               =                           =
SystemExit                =                           =
TabError                  =                           =
TimeoutError              =                           =
True                      Benar                       بنر
TypeError                 =                           =
UnboundLocalError         =                           =
UnicodeDecodeError        =                           =
UnicodeEncodeError        =                           =
UnicodeError              =                           =
UnicodeTranslateError     =                           =
UnicodeWarning            =                           =
UserWarning               =                           =
ValueError                =                           =
Warning                   =                           =
ZeroDivisionError         =                           =
_                         =                           =
__build_class__           =                           =
__debug__                 =                           =
__doc__                   =                           =
__import__                =                           =
__loader__                =                           =
__name__                  __nama__                    __نام__
__package__               =                           =
__spec__                  =                           =
abs                       =                           =
all                       semua                       سموا
any                       =                           =
ascii                     =                           =
bin                       =                           =
bool                      =                           =
breakpoint                =                           =
bytearray                 =                           =
bytes                     bait                        باءيت
callable                  =                           =
chr                       =                           =
classmethod               =                           =
compile                   =                           =
complex                   kompleks                    =
copyright                 hakcipta                    =
credits                   penghargaan                 ڤڠهرݢاءن
delattr                   =                           =
dict                      kamus                       قاموس
dir                       =                           =
divmod                    =                           =
enumerate                 mengangkakan                مڠڠکاکن
eval                      =                           =
exec                      jalan                       جالن
exit                      keluar                      کلوار
filter                    =                           =
float                     =                           =
format                    =                           فورمت
frozenset                 =                           =
getattr                   =                           =
globals                   =                           =
hasattr                   =                           =
hash                      =                           =
help                      bantu                       بنتو
hex                       =                           =
id                        =                           =
input                     =                           اينڤوت
int                       =                           اينتيݢر
isinstance                =                           =
issubclass                =                           =
iter                      =                           =
len                       =                           =
license                   =                           =
list                      senarai                     سناراي
locals                    =                           =
map                       =                           =
max                       =                           مکسيموم
memoryview                =                           =
min                       =                           مينيموم
next                      =                           =
object                    objek                       اوبجيک
oct                       =                           =
open                      buka                        بوک
ord                       =                           =
pow                       =                           =
print                     cetak                       چيتق
property                  =                           =
quit                      =                           =
range                     julat                       جولت
repr                      =                           =
reversed                  terbalik                    ترباليق
round                     bundar                      بوندر
set                       =                           سيت
setattr                   =                           =
slice                     =                           =
sorted                    susun                       سوسون
staticmethod              =                           =
str                       rentetan                    رينتيتن
sum                       tambah                      تمبه
super                     =                           =
tuple                     =                           =
type                      tipe                        تيڤى
vars                      =                           =
zip                       =                           =
========================= =========================== ===========================
