import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Script Tombol Tambahan Untuk Newbie')
print(b+'\t             Hasil Karya')
print('\t           Sandi Pirmansyah')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] nyobaan Heula Kanu Properti..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Sabar Heula Bel !')
sleep(1)
print(b+'\n[!] Keur Nyetel Ulang..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Sabar Heula Bel !')
sleep(1)
print(b+'\n[!] Nyeting Ulang Heula..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully !! ^^'+c+'\n\nhubungi Pembuat Script Sandi Pirmansyah Mun Aya Nu ek Ditanyakeun Kanu Wa 085316267169 Chat Hungkul Montong Nelepon Bisi Di Block :*\n\n')


# Ngan Saukur Nambah Tombol
# Sandi Pirmansyah
