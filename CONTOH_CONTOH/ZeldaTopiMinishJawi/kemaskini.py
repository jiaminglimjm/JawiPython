#piton3
dari jawi_ke_tmc import *

import re
import json
import time
import os

pisah = str.split
sambung = str.join
ganti = str.replace

akhirdengan = str.endswith
muladengan = str.startswith
hurufkecil = str.lower
indeks = str.index

re.carisemua = re.findall
re.ganti = re.sub
re.padan = re.match
re.cari = re.search

# tidak kisah tentang perkataan dengan multi-penukaran
# menggunakan kurang drpd 1 saat
dengan buka('rumi-jawi.tsv', 'r') sebagai f:
    rumi_jawi_kamus = kamus(pisah(p,'\t') untuk p dalam pisah(f.read().strip(), '\n'))

dengan buka('perkataan_tambahan.tsv', 'r') sebagai f:
    untuk p dalam pisah(f.read().strip(), '\n'):
        p_rumi, p_jawi = pisah(p, '\t')
        rumi_jawi_kamus[p_rumi] = p_jawi

#rumi_jawi_kamus['dan'] = 'دان'

memulih_rumi = {
    '\u002c': '\u060c',  # ,
    '\u003b': '\u061b',  # ;
    '\u003f': '\u061f',  # ?
}

ganti_warna = {
    'blue': 'white',
    'red': 'white',
    'green': 'white',
    'yellow': 'white',
}

yangketidakdiketahui = []

fungsi memelihara_kawalan_depan(kenyataan):
    rentetan_depan = ''
    jangan_memelihara = ['color', 'symbol', 'player', 'key', 'var']
    ada = any # experimental
    jika ada(muladengan(kenyataan, '{' + katakunci) untuk katakunci dalam jangan_memelihara):
        kembali rentetan_depan, kenyataan
    ketika kenyataan[:1] == '{' dan bukan \
            ada(muladengan(kenyataan, '{' + katakunci) untuk katakunci dalam jangan_memelihara):
        i_kurung_tutup = indeks(kenyataan, '}')
        rentetan_depan += kenyataan[:i_kurung_tutup + 1]
        kenyataan = kenyataan[i_kurung_tutup + 1:]
    kembali rentetan_depan, kenyataan

fungsi dorong_bunyi_kedepan(baris):
    tambah_kedepan = ''
    untuk kk dalam re.carisemua('{[Ss]ound:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]}', baris):
        tambah_kedepan += kk
        baris = ganti(baris, kk, '')
    kembali tambah_kedepan + baris

fungsi terbalik_baris(baris):
    tanda_baca = dapat_id('،') + dapat_id('؛') + dapat_id('؟') + dapat_id('-') + \
                 [',', '.', '!', '-', ';', '?', '"', ':'] + \
                 ['{symbol:0b}'] # nota musik
    jawapan = []
    corak = '(' + sambung('|', ['\\' + tb untuk tb dalam tanda_baca]) + ')+$'
    untuk perkataan dalam pisah(baris, ' '):
        akhiran = re.cari(corak, perkataan)
        jika akhiran:
            perkataan = akhiran.group() + perkataan[:-len(akhiran.group())]
        jawapan.append(perkataan)
    kembali sambung(' ', terbalik(jawapan))

fungsi tambah_ruang(baris, ruang_baris=208-4):
    jika '{07:' dalam baris: # lompat ke dialog seterusnya
        kembali baris
    jika 'https' dalam baris atau 'jiaminglimjm' dalam baris:
        kembali baris
    jika '{player}' dalam baris:
        ruang_baris -= ڤنجڠ_نام
    jika '{var:1}' dalam baris:
        ruang_baris -= kira('20') # 18, harus dikhususkan untuk setiap dialog?
    ruang_tersisa = ruang_baris - kira(baris)
    kembali sambung('', dapat_id('رواڠ', int(0)) * (ruang_tersisa // 8)) + \
            sambung('', dapat_id('رواڠ', int(1)) * (ruang_tersisa % 8)) + baris




fungsi tukar_terbalik(perkataan):
    #cetak(tukar(perkataan))
    kembali sambung('', terbalik(tukar(perkataan)))

fungsi ganti_perkataan(objek_padanan):
    '''
    the * is for {color:___} placeholder
    '''
    padanan = objek_padanan.group(0)
    padanan_hk = hurufkecil(padanan)
    huruf_vokal = ['a', 'e', 'i', 'o', 'u']

    jika padanan_hk dalam memulih_rumi: # rentetan RE di paling bawah menunggalkan tanda baca
        kembali tukar_terbalik(memulih_rumi[padanan_hk])
    jika Palsu dan padanan dalam ganti_warna:
        kembali ganti_warna[padanan]
    jika len(padanan) == 2 dan re.padan('[0-9a-f][0-9a-f]', padanan_hk):
        kembali padanan

    jika padanan_hk dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan_hk])
    jikain akhirdengan(padanan_hk, 'lah') dan padanan_hk[:-3] dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan_hk[:-3]] + 'له')
    jikain akhirdengan(padanan_hk, 'kah') dan padanan_hk[:-3] dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan_hk[:-3]] + 'که')
    jikain akhirdengan(padanan_hk, 'kan') dan padanan_hk[:-3] dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan_hk[:-3]] + 'کن')
    jikain akhirdengan(padanan_hk, 'pun') dan padanan_hk[:-3] dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan_hk[:-3]] + 'ڤون')
    jikain akhirdengan(padanan_hk, 'nya') dan padanan_hk[:-3] dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan_hk[:-3]] + 'ڽ')
    jikain akhirdengan(padanan_hk, 'mu') dan padanan_hk[:-2] dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan_hk[:-2]] + 'مو')
    jikain akhirdengan(padanan_hk, 'ku') dan padanan_hk[:-2] dalam rumi_jawi_kamus:
        kembali tukar_terbalik(rumi_jawi_kamus[padanan_hk[:-2]] + 'کو')

    jikain (muladengan(padanan_hk, 'ke') atau muladengan(padanan_hk, 'di') atau muladengan(padanan_hk, 'se')) dan \
            padanan_hk[2:] dalam rumi_jawi_kamus:
        untuk hv dalam huruf_vokal:
            jika muladengan(padanan_hk, 'ke' + hv):
                kembali tukar_terbalik('کأ' + rumi_jawi_kamus[padanan_hk[2:]][1:])
            jikain muladengan(padanan_hk, 'di' + hv):
                kembali tukar_terbalik('دأ' + rumi_jawi_kamus[padanan_hk[2:]][1:])
            jikain muladengan(padanan_hk, 'se' + hv):
                kembali tukar_terbalik('سأ' + rumi_jawi_kamus[padanan_hk[2:]][1:])
        jika muladengan(padanan_hk, 'ke'):
            kembali tukar_terbalik('ک' + rumi_jawi_kamus[padanan_hk[2:]])
        jikain muladengan(padanan_hk, 'di'):
            kembali tukar_terbalik('د' + rumi_jawi_kamus[padanan_hk[2:]])
        jikain muladengan(padanan_hk, 'se'):
            kembali tukar_terbalik('س' + rumi_jawi_kamus[padanan_hk[2:]])

    jikain re.padan(r"([-\u0620-\u06ff\u0762\u200c]+)", padanan):
        kembali tukar_terbalik(padanan)
    lain:
        yangketidakdiketahui.append(padanan)
        kembali sambung('', tukar(padanan))



''' # contoh
ayat_ayat = [
    "marilah, kita \nbersama-sama hanya berookah kerana\nnyanyiannya!",
    "hanyalah kau?! {Symbol:0D} akhirnya\ntelahku {Color:White} lagi pula lagipula",
    "terimalah harta karun ini! menGGunakannya tekan achoo!! uak gonggong!",
]

dengan buka('output.txt', 'w') sebagai f:
    untuk ayat dalam ayat_ayat:
        f.tulis(re.ganti(r"([-a-z\u0620-\u06ff\u0762\u200c]+|[,;?\u060c\u061b\u061f])",
                ganti_perkataan,
                hurufkecil(ayat)) + '\n'
        )
'''

# 21/11/2021 17:24 -18:51 (day1, just finished first prototype of jawi translation)
# [sudah diperbaiki day2] capitalization not preserved
# [sudah diperbaiki day2] symbol:xx may get translated if in dictionary....
# [sudah diperbaiki day2] game file size (space to shift to right) # how to fix: translations/USA.bin: translations/USA.json ; tools/tmc_strings/tmc_strings -p --source $< --dest $@ --size 0x70000
# "di" and "ke" remove space
# lewat"i"
# [sudah diperbaiki day1] some roda connection is wrong (FIXED 17:27), only for ف ڤ س ش ص ض cuz special case
# [sudah diperbaiki day2] ٢ also needs to be counted as non-connecting (note: change 2 and " to '٢')
# [sudah diperbaiki day2] adjust punctuation position (TOP PRIORITY FOR SECOND PROTOTYPE)
# [sudah diperbaiki day2] wau و and ro ر is size abit off (i think make ro taller by 2 pixels), especially for عنصور unsur. del دتتت height looks off in موريد murid, should be taller by one pixel (reading random sentences best way to judge a font)
# [sudah diperbaiki day2] ending with ب ت ث should be longer? and starting with them should be taller on the right side by one pixel
# [sudah diperbaiki day2] ha ه is too big
# color highlighting needs to be rearranged, choice options
# dimana-manapun, mau, remot, diatur, ke-5, tu je ye, pastikan, kurasa
# signboard spacing, all multispaces off
# \u0626, \u00e9
# extremely hard: align figurine names to the right
# all the other fonts (this would need other ppl pushing me to get done)
# some of the BM is very unnatural... maybe actually learn to translate first lol (reading in jawi makes me more critical of my translations hah)

# 22/11/2021 13:00 (day2, made lots of fixes from above)
# [sudah diperbaiki] "masalah" = "مسئله" by dealing with ئ
# OK, je, gitu, *menganggu*, wow
# deku
# question mark and zz mirror
# hamzah accent on alif, seekor, ke arah
# [sudah diperbaiki day3] "ruang" characters for fast and precise right-alignment spacing
# [sudah diperbaiki day3] OOF {Player} is variable length... can lessen damage by half, have padding and approximate name lengths, remove unecesary instances
# [sudah diperbaiki day3] OMW "memberiku", "memberitahu" came to bite me back HAHAH, i actually gotta fix it "memb" myself
# pastikan, selesaikan, i should just add kan to the end.
# TOP PRIORITY: Curly brackets mess up punctuation re-ordering "Lihat {color:red}peta{color:white}mu sahaja" becomes ليهت موڤيت سهاج
# [sudah diperbaiki day2] pure punctuations make program stuck on infinite loop (wow regular expressions are hard)
# special case for two-letter words which happen to be hexadecimal
# textbox glitch probably cuz of messing with text speed

# 23/11/2021 (day3, spacing and planning to release up to first boss)
# [sudah diperbaiki day3] add {key:_} widths maybe {choice:_} too?
# perfect jawi version up to first boss
# rearrange character ordering for most useful ones for naming
# [sudah diperbaiki day3] TOP PRIORITY: make sure positioning {04:10:0E} is at the beginning of text (OK, keep wtv curly brackets at the front fixed EXCEPT color, that one leave alone and deal with later)
# setup po file to json
# del د tunggal ada di 0x6A7260, alif (akhir kata) ا‍ di 0x6A6260

# 24/11/2021 (day4, thick pixel artt font)
# OK, 249 instances of {Player} so i can manually deal with each for jawi and import the rest from rumi
# still have to fix ta marbutah and qoh,
# stop blurring ur eyes omg i bet its a super unhealthy habit, cons of pixel art
# make alif (akhir kata) slant towards the right instead
# "(JAWI)" on title screen, dont need to turn those graphics into jawi tho, too much work and not even better

# 25/11/2021 (day5, todo before announcement on dragon force forum)
# [sudah, day5] in addition to {player}, have a list of exceptions also to exclude from importing from rumi (see how this grows first, if too big then only figure out how to deal with it)
# qoh ق  needs to be tweaked still, but surprisingly not bad for early scrapwork xD haha actually dont tweak it, it's like dorky and i like it
# teknik pedang chop removal
# handling two translations is pening kepala, abit overwhelming, need to either get used to it or improve
# ladang ternakan lon lon
# tiger scroll stamp 0x9252E0 and mirror tiger scroll
#
# TODO
# 1. warna teks
# 2. di-, ke-, se- prefixes and spacing             [fixed day6]
# 3. perfect dialog until big green chuchu
# 4. resolve naming abit off
# 5. writeup announcement and thank you for playing text for ketua minish
# 6. cengkerang -> cangkerang
# 7. variable values!!! choices!!

# 26/11/2021 (day6, all the difficult things to make everything join together)
# jawipython doesn't allow `0dan and 3atau` but allows `0and and 3or`
# jawipython `tiada` alias for `bukan`?
# Test cases for dealing with {}, 'ke ' and 'di ' will be remove space

# TODO
# 1. warna teks for prefix and suffix [day7]
# 2. perfect dialog until big green chuchu
# 3. resolve naming abit off
# 4. writeup announcement and thank you for playing text for ketua minish
# 5. variable values!!! choices!!

# 27/11/2021 (day7, fix ke- di- and -mu -ku colorings)
# red arrow dialog box move to left
# kaf ک is abit short, but lots of work to make longer
# [fixed day7 with regular expressions lol] apa!? mixed punctuations not rearranged correctly
# kecik interesting observation, ke-cik hahah

# 28/11/2021 (day 8, translations)
# should test and see if not having blue outline for thick font is ok or not...
# "cari untuk" is wrong??
# TODO
# 1. game over text
# 2. flip arrow icon
# 3. {key:__} spacings, L and R button for example is designed for ltr text
# 4. nun awal kata ن‍ is abit long



fungsi bukan_kecualian(perkataan):
    kembali bukan hurufkecil(perkataan) dalam ['deku', 'ketua', '!ketua']

fungsi jangan_warnai_akhir(warna, perkataan):
    tanda_baca = dapat_id('،') + dapat_id('؛') + dapat_id('؟') + dapat_id('-') + \
                 [',', '.', '!', '-', ';', '?', '"', ':'] + \
                 ['{symbol:0d}'] # nota musik
    corak = '(' + sambung('|', ['\\' + tb untuk tb dalam tanda_baca]) + ')*'
    rentetan_tandabaca = re.padan(corak, perkataan).group(0)
    perkataan = perkataan[len(rentetan_tandabaca):]
    perkataan_jawi = re.ganti(r"([-A-Za-z\u0620-\u06ff\u0762\u200c]+|[.!,;?\u060c\u061b\u061f])", ganti_perkataan, perkataan)
    cuba:
        jika (akhirdengan(hurufkecil(perkataan), 'mu') atau akhirdengan(hurufkecil(perkataan), 'ku')) dan bukan_kecualian(perkataan):
            akhiran = re.padan('{symbol:[0-9a-f][0-9a-f]}{symbol:[0-9a-f][0-9a-f]}', perkataan_jawi).group(0)
            #cetak('akhiran', warna, perkataan)
            #cetak('akhiran', akhiran)
            kembali rentetan_tandabaca + akhiran + warna + perkataan_jawi[len(akhiran):]
    kecuali: ...

    kembali rentetan_tandabaca + warna + perkataan_jawi

fungsi jangan_warnai_permulaan(warna, warna_sebelum, perkataan):
    perkataan_jawi = re.ganti(r"([-A-Za-z\u0620-\u06ff\u0762\u200c]+|[.!,;?\u060c\u061b\u061f])", ganti_perkataan, perkataan)

    jika (muladengan(hurufkecil(perkataan), 'ke') atau muladengan(hurufkecil(perkataan), 'di')) dan\
            hurufkecil(perkataan)[2:] dalam rumi_jawi_kamus dan bukan_kecualian(perkataan):
        mulaan = re.carisemua('{symbol:[0-9a-f][0-9a-f]}', perkataan_jawi)[-1]
        #cetak('mulaan', warna, warna_sebelum, perkataan)
        #cetak('mulaan', mulaan)
        kembali warna + perkataan_jawi[:-len(mulaan)] + warna_sebelum + mulaan

    kembali warna + perkataan_jawi

fungsi atur_warna(kenyataan):
    terpisah = [pisah(baris,' ') untuk baris dalam pisah(kenyataan, '\n')]
    warna = '{color:white}'
    untuk i, baris dalam mengangkakan(terpisah):
        untuk j, perkataan dalam mengangkakan(terbalik(baris)):
            p = len(baris) - 1
            kunciwarna = re.carisemua('{color:[a-z]+}', perkataan)
            jika len(kunciwarna) == 2:
                perkataan = re.ganti('{color:[a-z]+}', '', perkataan)
                tanda_baca = dapat_id('،') + dapat_id('؛') + dapat_id('؟') + dapat_id('-') + \
                             [',', '.', '!', '-', ';', '?', '"', ':'] + \
                             ['{symbol:0d}'] # nota musik
                corak = '(' + sambung('|', ['\\' + tb untuk tb dalam tanda_baca]) + ')*'
                perkataan_tanpa_tandabaca_didepan = perkataan[len(re.padan(corak, perkataan).group(0)):]
                jika (muladengan(hurufkecil(perkataan_tanpa_tandabaca_didepan), 'ke') atau muladengan(hurufkecil(perkataan_tanpa_tandabaca_didepan), 'di')) dan\
                        hurufkecil(perkataan_tanpa_tandabaca_didepan)[2:] dalam rumi_jawi_kamus dan bukan_kecualian(perkataan):
                    perkataan_jawi = jangan_warnai_akhir(kunciwarna[0], perkataan)
                    mulaan = re.carisemua('{symbol:[0-9a-f][0-9a-f]}', perkataan_jawi)[-1]
                    terpisah[i][p-j] = perkataan_jawi[:-len(mulaan)] + kunciwarna[1] + mulaan
                    cetak('mulakhir', perkataan, kunciwarna, sep=' | ')
                lain:
                    terpisah[i][p-j] = jangan_warnai_akhir(kunciwarna[0], perkataan) + kunciwarna[1]
                warna = kunciwarna[1]
            jikain len(kunciwarna) == 1 dan bukan akhirdengan(perkataan, kunciwarna[0]):
                terpisah[i][p-j] = jangan_warnai_permulaan(kunciwarna[0], warna, re.ganti('{color:[a-z]+}', '', perkataan))
                warna = kunciwarna[0]
            jikain len(kunciwarna) == 1 dan akhirdengan(perkataan, kunciwarna[0]):
                terpisah[i][p-j] = jangan_warnai_akhir(warna, re.ganti('{color:[a-z]+}', '', perkataan))
                warna = kunciwarna[0]
            jikain len(kunciwarna) == 0:
                terpisah[i][p-j] = warna + re.ganti(r"([-A-Za-z\u0620-\u06ff\u0762\u200c]+|[.!,;?\u060c\u061b\u061f])", ganti_perkataan, re.ganti('{color:[a-z]+}', '', perkataan))


    kenyataan = sambung('\n', [re.ganti(r"([-A-Za-z\u0620-\u06ff\u0762\u200c]+|[.!,;?\u060c\u061b\u061f])", ganti_perkataan, sambung(' ', baris)) untuk baris dalam terpisah])
    kembali kenyataan

'''# CHEH around 100-200 instances of `startword{color:___}endword[punctuation]` only, can do manually also lah...
#rentetan asal                                      #rentetan harus                                 # rentetan lepas terbalik_baris()
Ke {Color:Green}pesta picori{Color:White}\n                                                         picori{Color:White} Ke{Color:Green}pesta
bersama-sama!\n                                                                                     !bersama-sama

DIA DI {Color:Green}PESTA{Color:White} SEKARANG!\n   !سکارڠ {Color:Green}ڤيستا{Color:White}دي د     !SEKARANG DI{Color:Green}PESTA{Color:White} DIA

Lihat {Color:Red}peta{Color:White}mu sahaja!\n                                                      !sahaja {Color:Red}peta{Color:White}mu Lihat

Jom kita pergi cari {Color:Red}Pedang\n         {Color:Red}ڤدڠ{Color:White} جوم کيت ڤرݢي چاري
Picori yang Patah{Color:White}!?\n              ؟!{Color:Red}ڤيکوري يڠ ڤاته{Color:White}


Lihat contoh ini!!

Suatu {Color:Blue}hari nanti\n                  {color:blue}هاري ننتي{color:white} سواتو            nanti {color:blue}hari Suatu\n
kita akan\n                                     {color:blue}کيت اکن{color:white}                    akan kita
membunuh kau{Color:White}...!!! hah!\n          !هه !!!...{color:blue}ممبونوه کاو{color:white}      !hah !!!...kau{color:white} membunuh
'''

# hanya menjawikan set dialog ini
ubah_set = [
    0, # status permainan
    2, # nama orang
    3, # berita pendekar
    4, # nama alat
    5, # anda mendapatkan ___
    6, # papan tanda
    7, # nama tempat
    8, # nama patung kecil
    9, # maklumat patung kecil
    11, # ezlo dialog
    12, # ezlo SELECT
    15, # intro
    16, # intro
    17, # pengenalan Ezlo
    27, # mutoh & kawan2
    28, # Ezlo selepas dapat unsur baru
    31, # minish pico ripico
    33, # Minish hutan
    34, # Ezlo dunia minish
    37, # pesta picori
]
ubah_set = senarai(julat(80)) # ada set 0 sampai 79

# menjelaskan set dialog mana dan bagaimana dia berbeza daripada dialog biasa
ruang_set = {
    0 : Palsu, # status permainan
    1 : Palsu, # penghargaan
    2 : [(97, (0, 149))], # nama dalam halaman gabungan kinstone
    4 : [(134, (117, 125))], # gulungan harimau, dll
    7 : Palsu, # nama tempat
    8 : [(135, (0, 138))], # nama patung kecil
    9 : Palsu, # penjelasan patung kecil
    10: Palsu,
    15: Palsu, # intro
    46: Palsu, # tidak digunakan? nama & harga
}

mengurufkecil = [
    '{Color',
    '{Sound',
    '{Choice',
    '{Player',
    '{Var',
    '{Key',
    '{Symbol',

    ':White}',
    ':Red}',
    ':Green}',
    ':Blue}',
    ':Yellow}',

    ':A}',
    ':B}',
    ':Left}',
    ':Right}',
    ':DUp}',
    ':DDown}',
    ':DLeft}',
    ':DRight}',
    ':Dpad}',
    ':Select}',
    ':Start}',
]

tetap_guna_dari_versi_jawi = [
    (0,5), (0,7), (0,8), (0,11), # game pak
    (0,13), # aktifkan mod tidur
    (0,16), # simpan, jgn simpan
    (0,17), # terus main, keluar

    (37,5), # zelda, bukankah ada pertandingan lawan pedang?
    (37, 12), # selamat datang ke Hyrule setiap seratus tahun.
    (37, 13), # tukang cerita tua: agar -> supaya
    (37, 15), # Kamu rasa saya akan nampak picori jika saya menjadi anak yang baik?
    (37, 17), # terri (beedle), buah-buahan
    (37, 19), # topi kerucut merah, sangattt kecil
    (37, 22), # seorang misteri yang berpakaian serba hitam
    (37, 25), # poemun, tepat waktunya
    (37,28), # spacing, beliau sebenarynya ahli pedang terbaik di pernah ada di hyrule

    (4,117), # gulungan harimau - serangan berputar
    (4,122), # gulungan harimau - serangan berputar hebat

    (5,24), # kepingan hati 1, mengumpulkan
    (5,53), # menerima pedang picori yang patah
    (5,91), # kacang celoteh, memahami bahasa minish
    (5,62), # mendapatkan cengkerang
    (5,63), # mendapatkan cengkerang
    (5,64), # mendapatkan unsur tanah, adalah sumber dari mana semua makhluk hidup
    (5,118), # mendapatkan cengkerang
    (5,110), # mendapatkan cengkerang

    (6,2), # tanda baca sebelum hutan minish
    (6,7), # tanda baca pertama
    (6,11), # tanda baca di ladang lon lon
    (6,14), # tanda baca di padang utara hyrule

    (11,50), # ezlo kuil deepwood, tekan R untuk tarik tuas
    (11, 52), # ezlo kuil deepwood, Itu tidak besar;
    (12,2), # ezlo random, periksa sekitarmu
    (12,8), # ezlo jangan merenung, merayau!
    (12,18), # ezlo, mendapatkan unsur tanah
    (12,19), # ezlo, ketua minish ingin kita kembali
    (12,136), # ezlo, ala lima minit sahaja

    (15,3), # picori muncul membawa pedang dan kuasa cahaya

    (16,68), # vaati, mmmm ah hah hah hah هههههههه
    (16,73), # ?!? kosong? gerombolan, apa maknanya, hmm

    (16,81), # smith picori? tidak banyak, tahu apa yang dikatakan dalam cerita dongeng sahaja
    (16,83), # menteri tengaro, a-apa? dengan segera!
    (16,97), # hamba nurse, insyaallah
    (17,1), # ezlo, tolong! tolooonggg!
    (17,9), # ezlo, terima aniaya
    (17,14), # ezlo, ... ... saya pun berusaha menghancurkan satu kutukan vaati
    (17,18), # ezlo naik atas nah, menggeliang-geliut, wawasanku SELECT
    (34,3), # selamat datang ke dunia melalui mata minish
    (17,50), # ketua minish, empat unsur hablur pergabungan pedang picori peta
    (17,51), # ketua minish, unsur tanah
    (17,53), # ketua minish, terima kasih bermain demo :)

    (27,5), # tentera, makhluk anek dan vaati
    (27,35), # pekerja tukang kayu, entah dari mana

    (31,22), # fesuta, kacang celoteh
    (31,24), # fesuta, makhluk2 buas telah menetap di situ.
    (33,21), # minish, wisatawan yang menemukan kinstone dan beruntung
    (33,31), # minish untuk meruta, tinggal di gunung;
    (33,32), # minish untuk meruta, tinggal di gunung;
    (33,34), # ketua ricopi picoco
    (33,37), # minish, melawan mahluk2 dan mengambil unsur tanah?
    (33,47), # minish, makhluk hijau BESAR

]

jika __name__ == '__main__':
    dengan buka('BahasaMelayu.json', 'r') sebagai f: # fail ini sama dengan versi rumi
        k_ms = json.loads(f.read())
    dengan buka('UbahsuaianJawi.json', 'r') sebagai f: # fail ini khusus untuk kenyataan jawi istimewa
        k_tetapjawi = json.loads(f.read())

    untuk n dalam julat(len(k_ms)):
        untuk i, kenyataan dalam mengangkakan(k_ms[n]):

            jika '{player}' dalam hurufkecil(kenyataan) atau (n, i) dalam tetap_guna_dari_versi_jawi:
                kenyataan = k_tetapjawi[n][i]

            untuk kk dalam mengurufkecil:
                kenyataan = ganti(kenyataan, kk, hurufkecil(kk))
            untuk r dalam [' ', '\n', '{color:white}', '{color:blue}', '{color:red}', '{color:green}']:
                untuk kk dalam ['di ', 'ke ', 'Di ', 'Ke ', 'DI ', 'KE ']:
                    kenyataan = ganti(kenyataan, r + kk, r + kk[:-1])
                    jika kenyataan[:3] == kk:
                        kenyataan = kk[:-1] + kenyataan[3:]
            untuk nombor_bilang dalam pisah('100,1,2,3,4,5,6,7,8,9', ','):
                kenyataan = ganti(kenyataan, 'ke-'+nombor_bilang, nombor_bilang+'-ke')

            jika n dalam ubah_set:
                rentetan_depan, kenyataan = memelihara_kawalan_depan(kenyataan)
                kenyataan = sambung('\n', [dorong_bunyi_kedepan(baris) untuk baris dalam pisah(kenyataan, '\n')])
                kenyataan = sambung('\n', [terbalik_baris(baris) untuk baris dalam pisah(kenyataan, '\n')])
                jika '{color:' dalam kenyataan:
                    kenyataan = atur_warna(kenyataan)
                lain:
                    kenyataan = sambung('\n', [re.ganti(r"([-A-Za-z\u0620-\u06ff\u0762\u200c]+|[.!,;?\u060c\u061b\u061f])",
                                                      ganti_perkataan, baris)
                                               untuk baris dalam pisah(kenyataan, '\n')])
                jika n bukan dalam ruang_set:
                    kenyataan = sambung('\n', [tambah_ruang(baris) untuk baris dalam pisah(kenyataan, '\n')])
                jikain bukan ruang_set[n] == Palsu:
                    untuk berapa_piksel, julat_dialog dalam ruang_set[n]:
                        jika i dalam julat(*julat_dialog):
                            kenyataan = sambung('\n',
                                [tambah_ruang(baris, berapa_piksel) untuk baris dalam pisah(kenyataan, '\n')]
                            )
                k_ms[n][i] = rentetan_depan + kenyataan
            lain:
                k_ms[n][i] = f'{n}-{i}'

    nama_fail_json = time.strftime('./Arkib/fail_teks_json/%Y%m%d_%H%M%S_TMCTeksJawi.json')
    dengan buka(nama_fail_json, 'w') sebagai f:
        f.write(json.dumps(k_ms, indent=4))

    #untuk x dalam set(yangketidakdiketahui):
    #    cetak(x, yangketidakdiketahui.count(x))
    '''
    bukan_dalam_kamus = [(yangketidakdiketahui.count(x), x) untuk x dalam set(yangketidakdiketahui)]

    untuk b, p dalam terbalik(susun(bukan_dalam_kamus)):
        cetak(b, p)
    '''

    os.system('git add .; git commit -m "auto-kompil"')
    os.system(f'cp {nama_fail_json} ./tmc/translations/USA.json')
    os.system('rm ./tmc/translations/USA.bin')
    os.system('cd ./tmc; make -s -j1')
    os.system('mgba-qt ./tmc/tmc.gba > /dev/null 2>&1 &')







    #
