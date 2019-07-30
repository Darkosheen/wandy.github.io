import os
import shutil





path = "C:/Users/WR/Desktop/wanderson/imagens/" #caminho das imagens
dst = "C:/Users/WR/Desktop/wanderson" #caminho para salvar as imagens para
dst = input("caminho: ")
lista  = os.listdir(path)
fp = open('C:/Users/WR/Desktop/wanderson/excel.txt', 'r')
line = fp.readline()
cnt = 0
i = 0
while line:
   print("Linha: "+ line.strip() + " imagens: " + lista[cnt])
   for i in lista:
      if line.strip() +".jpg" == i:
         shutil.copy(path + i, dst)
         print("Foi")
  
   line = fp.readline()
   cnt += 1
fp.close()

