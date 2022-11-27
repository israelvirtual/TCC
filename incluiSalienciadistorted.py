

import PIL.Image as Image      # https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=image.open#PIL.Image.open
import numpy as np
import skvideo.io              # http://www.scikit-video.org/stable/io.html
from pathlib import Path
  
workfolder = Path('')
saliency = Path("Saliencia")
video_path = Path("VQA-ODV-distorted")
saida_path = Path("VQA-ODV-distorted-preprocess")

for video in video_path.glob('*.mp4'):
 
  raiz = video.stem
  #print(raiz)
  partes = raiz.split('_')
  nome = partes[0]
  resolucao = partes[2]
  fps = partes[3][3:]
  root = nome + "_" + resolucao + "_fps" + fps

  output =  saida_path / (raiz + "_preprocess.mp4")
  salimage = saliency / root
  if not(salimage.exists()):
    print(str(raiz) + 'saliency not found')
    continue

  if output.exists():
    print(str(raiz) +'video_path found')
    continue


  vreader = skvideo.io.vreader(str(video), as_grey=True)
  writer = skvideo.io.FFmpegWriter(f'{output}',inputdict={'-r': fps}, outputdict={'-r': fps, '-pix_fmt': 'yuv420p','-crf':'0'})

  saliency_name_list = []
  for frame in range(1,500):
    saliency_name_list.append(f'salimage{frame:05d}.bmp')


  for frame, (frame_array, saliency_name) in enumerate(zip(vreader, saliency_name_list)):
    #if frame>30: break
    print(f'{raiz} - {frame}')
    # Ajusta o Shape do frame do vídeo
    height = frame_array.shape[1]
    width = frame_array.shape[2]
    frame_ref = frame_array.reshape((height, width)).astype('float32')

    # Abre a saliência, faz o upscale, normaliza e tira a raiz quadrada
    img_sal = Image.open(saliency/root/saliency_name).convert('L')
    img_sal = img_sal.resize((width, height))
    arr_sal = np.asarray(img_sal)
    arr_sal_norm = arr_sal / 255
    sqrt_arr_sal_norm = np.sqrt(arr_sal_norm)

    # Multiplica o frame do vídeo pela raiz da saliência normalizada
    video_weighed = frame_ref * sqrt_arr_sal_norm
    #video_weighed = np.round_(video_weighed)
    #print('video_weighed.shape=',video_weighed.shape)
    #print('frame_ref.shape=',frame_ref.shape)
    #print('sqrt_arr_sal_norm.shape=',sqrt_arr_sal_norm.shape)
    #break
    
    writer.writeFrame(video_weighed)

  writer.close()

  #writer = skvideo.io.FFmpegWriter(str(video_path.with_stem(video_path.stem + '_weighed')), outputdict={'crf':0})
