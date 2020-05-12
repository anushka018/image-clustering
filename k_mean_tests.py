from k_means import *
from image_utils import *
#Anushka Angamuthu


if __name__ == "__main__":
    file = input("image file> ")
    image = read_ppm(file)

    print(compute_dist((255,0,255),(255,255,0))) #360.62
    print(compute_dist((255, 255, 255), (255, 255, 255)))  # 0

    print(compute_avg([(99, 28, 90), (0, 0, 0), (255, 255, 0), (255, 255, 255), (34, 56, 89)]))  # (128,118,86)
    print(compute_avg([(128, 54, 98), (0, 255, 0), (255, 255, 0), (255, 0, 255), (0, 56, 62)]))  # (127,124,83)

    # print(initial_guess(3)) #rand but list with 3 tuples that are pixel values
    print(initial_guess(7))  # rand but list with 7 tuples that are pixel values

    print(compute_avg([(255, 0, 0), (255, 255, 0)])) #(255, 127, 0)
    print(compute_avg([(0, 255, 255), (255, 255, 255)])) #(127, 255, 255)
    print(compute_avg([(0, 0, 255), (0, 0, 0)])) #(0, 0, 127)

    k = 3
    test_image = [ [(255 , 0 , 0) , (255 , 255 , 0)] , [(0 , 255 , 255) , (255 , 255 , 255)] ,[(0 , 0 , 255) , (0 , 0 , 0)] ]
    i = initial_guess(k)
    print(i)  # random list of colors of length k
    assignments = get_assignments_ls(test_image, [(172, 7, 60), (127, 173, 211), (6, 246, 0)])
    print(assignments)  # [[0,2], [1,1], [1,0]]
    print(update_means_list(test_image, assignments,k))  # [(127,0,0), (85,170,255),(255,255,0)]
    print(k_means(test_image,k))  # tuple with means & assignments list or lists

