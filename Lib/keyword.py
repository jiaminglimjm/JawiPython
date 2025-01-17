"""Keywords (from "Grammar/python.gram")

This file is automatically generated; please don't muck it up!

To update the symbols in this file, 'cd' to the top directory of
the python source tree and run:

    PYTHONPATH=Tools/peg_generator python3 -m pegen.keywordgen \
        Grammar/python.gram \
        Grammar/Tokens \
        Lib/keyword.py

Alternatively, you can run 'make regen-keyword'.
"""

__all__ = ["iskeyword", "issoftkeyword", "kwlist", "softkwlist"]

kwlist = [
    'Benar',
    'False',
    'None',
    'Palsu',
    'Tiada',
    'True',
    'akhirnya',
    'and',
    'as',
    'assert',
    'async',
    'atau',
    'await',
    'break',
    'bukan',
    'class',
    'continue',
    'cuba',
    'dalam',
    'dan',
    'dari',
    'def',
    'del',
    'dengan',
    'elif',
    'else',
    'except',
    'finally',
    'for',
    'from',
    'fungsi',
    'global',
    'hapus',
    'ialah',
    'if',
    'import',
    'in',
    'is',
    'jika',
    'jikain',
    'kecuali',
    'kelas',
    'kembali',
    'ketika',
    'lain',
    'lambda',
    'lanjut',
    'nonlocal',
    'not',
    'or',
    'pass',
    'putus',
    'raise',
    'return',
    'sebagai',
    'try',
    'untuk',
    'while',
    'with',
    'yield',
    'اتاو',
    'اخيرڽ',
    'اونتوق',
    'اياله',
    'بنر',
    'بوکن',
    'تياد',
    'جک',
    'جکاءين',
    'دالم',
    'دان',
    'دري',
    'دڠن',
    'سباݢاي',
    'فوڠسي',
    'لاءين',
    'لنجوت',
    'هاڤوس',
    'چوبا',
    'ڤلسو',
    'ڤوتوس',
    'کتيک',
    'کلس',
    'کمبالي',
    'کچوالي'
]

softkwlist = [
    '_',
    'case',
    'match'
]

iskeyword = frozenset(kwlist).__contains__
issoftkeyword = frozenset(softkwlist).__contains__
