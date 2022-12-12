import numpy as np
import matplotlib.pyplot as plt

for i in range(1,4):
  Img = plt.imread('input'+str(i)+'.jpg')
  pxl = Img.shape[0]*Img.shape[1]
  mean = 1.0/pxl
  # Compute histogram
  his,bins = np.histogram(Img,np.array(range(0, 256)))
  
  thresh = 0
  value = 0
  for t in bins[1:-1]: 
      # Compute probabilities
      wb = np.sum(his[:t])*mean
      wf = np.sum(his[t:])*mean
      # Compute means
      mb = np.mean(his[:t])
      mf = np.mean(his[t:])
      # In-between class variance
      temp_value = wb*wf*(mb - mf)**2
      # Get the max variance
      if temp_value > value:
        value = temp_value
        thresh = t

  # Print Otsu threshold
  print(thresh)       
  
  Image = Img.copy()
  Image[Img < thresh] = 0
  Image[Img > thresh] = 255
  
  # Plot image after thresholding
  plt.imshow(Image,cmap='gray')
  plt.axis('off') 
  plt.savefig('image'+str(i)+'_Otsu.jpg')
  plt.show()