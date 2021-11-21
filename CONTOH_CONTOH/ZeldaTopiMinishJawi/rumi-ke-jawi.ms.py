#piton3
dari jawi_ke_tmc import *

import re
import json

pisah = str.split
sambung = str.join

akhirdengan = str.endswith
muladengan = str.startswith
hurufkecil = str.lower

# tidak kisah tentang perkataan dengan multi-penukaran
# menggunakan kurang drpd 1 saat
dengan buka('rumi-jawi.tsv', 'r') sebagai f:
    rumi_jawi_kamus = kamus(pisah(p,'\t') untuk p dalam pisah(f.read().strip(), '\n'))

dengan buka('perkataan_tambahan.tsv', 'r') sebagai f:
    untuk p dalam pisah(f.read().strip(), '\n'):
        p_rumi, p_jawi = pisah(p, '\t')
        rumi_jawi_kamus[p_rumi] = p_jawi

rumi_jawi_kamus['dan'] = 'دان'

memulih_rumi = {
  '\u002c': '\u060c',  # ,
  '\u003b': '\u061b',  # ;
  '\u003f': '\u061f',  # ?
}

yangketidakdiketahui = []

fungsi tukar_terbalik(perkataan):
    #cetak(tukar(perkataan))
    kembali sambung('', terbalik(tukar(perkataan)))

fungsi ganti_perkataan(objek_padanan):
    padanan = hurufkecil(objek_padanan.group(0))
    jika padanan dalam memulih_rumi:
        kembali tukar_terbalik(memulih_rumi[padanan])
    jika padanan dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan])
    elif akhirdengan(padanan, 'lah') dan padanan[:-3] dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan[:-3]] + 'له')
    elif akhirdengan(padanan, 'kah') dan padanan[:-3] dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan[:-3]] + 'که')
    elif akhirdengan(padanan, 'nya') dan padanan[:-3] dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan[:-3]] + 'ڽ')
    elif akhirdengan(padanan, 'mu') dan padanan[:-2] dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan[:-2]] + 'مو')
    elif akhirdengan(padanan, 'ku') dan padanan[:-2] dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan[:-2]] + 'کو')
    lain:
        yangketidakdiketahui.append(padanan)
        kembali padanan

''' # contoh
ayat_ayat = [
    "marilah, kita \nbersama-sama hanya berookah kerana\nnyanyiannya!",
    "hanyalah kau?! {Symbol:0D} akhirnya\ntelahku {Color:White} lagi pula lagipula",
    "terimalah harta karun ini! menGGunakannya tekan achoo!! uak gonggong!",
]

dengan buka('output.txt', 'w') sebagai f:
    untuk ayat dalam ayat_ayat:
        f.tulis(re.sub(r"([-a-z\u0620-\u06ff\u0762\u200c]+|[,;?\u060c\u061b\u061f])",
                ganti_perkataan,
                hurufkecil(ayat)) + '\n'
        )
'''

dengan buka('BahasaMelayu.json', 'r') sebagai f:
    k_ms = json.loads(f.read())

# 21/11/2021 17:24 -18:51 (just finished first prototype of jawi translation)
# capitalization not preserved
# symbol:xx may get translated if in dictionary....
# punctuation order
# game file size (space to shift to right)
# "di" and "ke" remove space
# lewat"i"
# some roda connection is wrong (FIXED 17:27), only for ف ڤ س ش ص ض cuz special case
# ٢ also needs to be counted as non-connecting (note: change 2 and " to '٢')
# adjust punctuation position (TOP PRIORITY FOR SECOND PROTOTYPE)
# wau و and ro ر is size abit off (i think make ro taller by 2 pixels), especially for عنصور unsur. del دتتت height looks off in موريد murid, should be taller by one pixel (reading random sentences best way to judge a font)
# ending with ب ت ث should be longer? and starting with them should be taller on the right side by one pixel
# ha ه is too big
# color highlighting needs to be rearranged, choice options
# dimana-manapun, mau, remot, diatur, ke-5, tu je ye, pastikan, kurasa
# signboard spacing, all multispaces off
# \u0626, \u00e9
# extremely hard: align figurine names to the right
# all the other fonts (this would need other ppl pushing me to get done)
# some of the BM is very unnatural... maybe actually learn to translate first lol

untuk n dalam julat(len(k_ms)):
    untuk i, sertaan dalam mengangkakan(k_ms[n]):
        kenyataan = re.sub(r"([-a-z\u0620-\u06ff\u0762\u200c]+|[,;?\u060c\u061b\u061f])",
                            ganti_perkataan,
                            hurufkecil(sertaan))
        k_ms[n][i] = sambung('\n', [sambung(' ', terbalik(pisah(baris))) untuk baris dalam pisah(kenyataan, '\n')])

dengan buka('JawiContoh_5_3.json', 'w') sebagai f:
    f.write(json.dumps(k_ms, indent=4))

#untuk x dalam set(yangketidakdiketahui):
#    cetak(x, yangketidakdiketahui.count(x))

bukan_dalam_kamus = [(yangketidakdiketahui.count(x), x) untuk x dalam set(yangketidakdiketahui)]

untuk b, p dalam terbalik(susun(bukan_dalam_kamus)):
    cetak(b, p)
















    #
