JawiPython daripada CPython versi 3.11.0 alfa 1
===============================================

.. contents::

Cara Kompil & Guna
------------------

Untuk Unix, Linux, BSD, macOS, dan Cygwin::

    ./configure         # hanya untuk pertama kali
    make regen-pegen    # kemaskini parser
    make                # cipta fail binari

Ini akan membina fail binari Python dalam Bahasa Melayu sebagai ``python``. Ini TIDAK akan memasang python kepada sistem anda, hanya mencipta sebuah fail binari yang boleh dieksekusi.

Untuk mengetahui lebih lanjut tentang pengkompilan untuk MacOS dan Windows, sila lihat `github.com/python/cpython#build-instructions`_ Saya bukan pakar pengkompilan CPython, tetapi sudah pernah cuba kompil untuk Windows dan berhasil selepas mengikut arahan2 dalam pautan itu.

.. _github.com/python/cpython#build-instructions: https://github.com/python/cpython#build-instructions

`Aturcara contoh`_
.. image:: https://github.com/jiaminglimjm/JawiPython/ProjekEulerMasalah1.png
.. _Aturcara contoh: https://github.com/jiaminglimjm/JawiPython/blob/master/CONTOH_CONTOH/Projek Euler 1 - Angka kandungan 3 dan 5.ms.py

Untuk "syntax highlighting", saya buat sendiri sebenarnya dengan penyunting teks `xed`. Tapi masih belajar cara untuk membuatnya dalam vscode.



Terjemahan kata-kata kunci
--------------------------

======== ==================== ====================
Inggeris Bahasa Melayu (Rumi) Bahasa Melayu (Jawi)
======== ==================== ====================
False    Palsu                ڤلسو
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
if       jika                 جک
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
bytes                     =                           =
callable                  =                           =
chr                       =                           =
classmethod               =                           =
compile                   =                           =
complex                   =                           =
copyright                 hakcipta                    حقچيڤتا
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
format                    =                           =
frozenset                 =                           =
getattr                   =                           =
globals                   =                           =
hasattr                   =                           =
hash                      =                           =
help                      bantu                       بنتو
hex                       =                           =
id                        =                           =
input                     =                           =
int                       =                           =
isinstance                =                           =
issubclass                =                           =
iter                      =                           =
len                       =                           =
license                   =                           =
list                      senarai                     سناراي
locals                    =                           =
map                       =                           =
max                       =                           =
memoryview                =                           =
min                       =                           =
next                      =                           =
object                    =                           =
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
set                       =                           =
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
