# Salin daripada README
MEJA_TERJEMAHAN = '''ArithmeticError           =                           =
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
#False                     Palsu                       ڤلسو
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
#None                      Tiada                       تياد
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
#True                      Benar                       بنر
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
credits                   penghargaan                 ڤڠهرڬاءن
delattr                   =                           =
dict                      kamus                       قاموس
dir                       =                           =
divmod                    =                           =
enumerate                 mengangkakan                مڠڠكاكن
eval                      =                           =
exec                      jalan                       جالن
exit                      keluar                      كلوار
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
int                       =                           اينتيڬر
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
open                      buka                        بوك
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
zip                       =                           ='''

s = 'import builtins\n\n'

untuk garis dalam pisah(MEJA_TERJEMAHAN, '\n'):
    inggeris, rumi, jawi = pisah(garis)
    jika inggeris[0] != '#':
        jika bukan rumi == '=':
            s += f'builtins.{rumi} = {inggeris}\n'
        jika bukan jawi == '=':
            s += f'builtins.{jawi} = {inggeris}\n'

dengan buka('../Lib/terjemahan.py', 'w') sebagai f:
    f.tulis(s)

#cetak(tatabahasa)
