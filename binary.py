import matplotlib.pyplot as plt

#Load Image 1
Img=plt.imread('input1.jpg')

# Plot Histogram
plt.hist(Img, density = True)  
plt.xlabel('Data')
plt.ylabel('Probability')
plt.savefig('hist_image1.jpg')
plt.show()

# Thresholding with T=70
T =70
Image1 = Img.copy()
Image1[Img > T] = 255
Image1[Img < T] = 0
plt.imshow(Image1,cmap='gray') 
plt.axis('off')
plt.savefig('image1_T80.jpg')
plt.show()

# Thresholding with T=100
T =100
Image1 = Img.copy()
Image1[Img > T] = 255
Image1[Img < T] = 0
plt.imshow(Image1,cmap='gray') 
plt.axis('off')
plt.savefig('image1_T115.jpg')
plt.show()

# Thresholding with T=150  
T =150
Image1 = Img.copy()
Image1[Img > T] = 255
Image1[Img < T] = 0
plt.imshow(Image1,cmap='gray') 
plt.axis('off')
plt.savefig('image1_T150.jpg')
plt.show()  


# Load Image 2
Img2=plt.imread('input2.jpg')

# Plot Histogram
plt.hist(Img2, density = True, bins=10)  
plt.xlabel('Data')
plt.ylabel('Probability')
plt.savefig('hist_image2.jpg')
plt.show()

# Thresholding with T=100
T =100
Image2 = Img2.copy()
Image2[Img2 > T] = 255
Image2[Img2 < T] = 0
plt.imshow(Image2,cmap='gray') 
plt.axis('off')
plt.savefig('image2_T100.jpg')
plt.show()

# Thresholding with T=150
T =150
Image2 = Img2.copy()
Image2[Img2 > T] = 255
Image2[Img2 < T] = 0
plt.imshow(Image2,cmap='gray') 
plt.axis('off')
plt.savefig('image2_T150.jpg')
plt.show()
   
# Thresholding with T=200   
T =200
Image2 = Img2.copy()
Image2[Img2 > T] = 255
Image2[Img2 < T] = 0
plt.imshow(Image2,cmap='gray') 
plt.axis('off')
plt.savefig('image2_T200.jpg')
plt.show()  


# Load Image 3
Img3=plt.imread('input3.jpg')

# Plot Histogram
plt.hist(Img3, density = True, bins=10)  
plt.xlabel('Data')
plt.ylabel('Probability')
plt.savefig('hist_image3.jpg')
plt.show()

# Thresholding with T=100
T =100
Image3 = Img3.copy()
Image3[Img3 > T] = 255
Image3[Img3 < T] = 0
plt.imshow(Image3,cmap='gray') 
plt.axis('off')
plt.savefig('image3_T100.jpg')
plt.show()

# Thresholding with T=150
T =150
Image3 = Img3.copy()
Image3[Img3 > T] = 255
Image3[Img3 < T] = 0
plt.imshow(Image3,cmap='gray') 
plt.axis('off')
plt.savefig('image3_T150.jpg')
plt.show()
   
# Thresholding with T=200   
T =200
Image3 = Img3.copy()
Image3[Img3 > T] = 255
Image3[Img3 < T] = 0
plt.imshow(Image3,cmap='gray') 
plt.axis('off')
plt.savefig('image3_T200.jpg')
plt.show()  