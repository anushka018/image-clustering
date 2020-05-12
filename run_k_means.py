from image_utils import *
from k_means import *
# Anushka Angamuthu


if __name__ == "__main__":
    file = input("please enter a image filename to run the k-means clustering algorithm on:")
    k = int(input("please enter a value for k, the number of colors you would like to cluster the image into:"))
    output = (input("what would you like to name the file that contains the clustered image? (end name with .ppm)"))
    image = read_ppm(file)
    result = k_means(image, k)
    for mean in range(len(result[0])):
        for j in range(len(result[1])):
            for k in range(len(result[1][0])):
                if (result[1])[j][k] == mean:
                    (image[j][k]) = result[0][mean]
    save_ppm(output, image)
