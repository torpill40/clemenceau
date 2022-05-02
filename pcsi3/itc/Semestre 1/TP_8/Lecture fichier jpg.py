import matplotlib. pyplot as plt  # import de la bibliothèque

image=plt.imread("Gullfoss.jpg")  # ouverture de l'image Gullfoss.jpg et affectation à la variable image

plt.imshow(image)
#plt.axis('off')    # masque les axes
plt.show()  # affichage de l'image