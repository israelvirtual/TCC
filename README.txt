README simplificado para os códigos e comuputações utilizados no TCC. Por gentileza, se orientar pelo fluxograma apresentado na parte de métodos:

Saliency Calculation and incorporation	
- Saliency calculation:
BMS360 (rodado em PC): https://github.com/Telecommunication-Telemedia-Assessment/GBVS360-BMS360-ProSal
CubePadding (rodado no servidor): http://aliensunmin.github.io/project/360saliency/

- Saliency incorporation:

É preciso a criação de duas pastas de entrada: uma com os vídeos referencia (VQA-ODV), uma os vídeos distorcidos (VQA-ODV-distorted) com os respectivos vídeos
É preciso a criação de quatro pastas de saída: uma para a inclusão de BM360 referência (VQA-ODV-Preprocess), uma para a inclusão de BM360 distocido (VQA-ODV-distorted-preprocess), uma para a inclusão de Cubepadding referência (VQA-ODV-CP-Preprocess), uma para a inclusão de BM360 distocido (VQA-ODV-CP-distorted-preprocess)
Criar pastas com os frames das saliencias: Saliencia para a BMS360 e CPSaliency para Cubepadding. Cada conjunto de frames deve estar numa pasta com o nome do vídeo

Depois rodar respectivos códigos abaixo no servidor. Os outputs são vídeos com saliências inclusas.
- incluiSaliencia para videos de referencia BMS360
- incluiSalienciadistorted para videos distorcidos BMS360
- incluiSalienciaCP para videos de referencia Cubepadding
- incluiSalienciaCPdistorted para videos distorcidos Cubepadding

QoE e Stats framework: Seguir trabalho de Saigg e Scholles conforme github. 
https://github.com/Scholles007/Framework-for-Objective-Visual-Quality-Assessment-FOVQA/blob/main/README.md

Há uma coluna no No meu caso, calculei os MOS dos videos conforme abaixo

import pandas as pd
import os
import glob

sh1 = pd.read_csv('/content/gdrive/MyDrive/TCC/Leva1MOS.csv')
sh2 = pd.read_csv('/content/gdrive/MyDrive/TCC/Leva2MOS.csv')
sheet1 = sh

g = []
for i in range(10):
  g.append(Tcc+ "/Group"+ str(i+1)+"_ScoreData")
for G in g:
  os.chdir(G)
  FileList = glob.glob('*.xlsx')
  #print(FileList)
  for filename in FileList:
    User = pd.read_excel(filename)
    for video in User["Video"].values:
      video2 = video.replace('.mp4', '')
      for value in sheet1['refFile'].values:
        if video2 == value:
          #print(video)
          sheet1["Mos"].loc[np.where(sheet1["refFile"] == video2)] +=  User["Raw"].loc[np.where(User["Video"] == video)].values
          sheet1["Count"].loc[np.where(sheet1["refFile"] == video2)] += 1
          print(sheet1["Mos"].loc[np.where(sheet1["refFile"] == video2)].values)
          print(sheet1["Count"].loc[np.where(sheet1["refFile"] == video2)])
          print(sheet1["Mos"].loc[np.where(sheet1["refFile"] == video2)].values)