from image_utils import *
# Anushka Angamuthu


def k_means(image, k):
    """
    Performs a complete k means computation by creating a random initial means list & an assignments list of list
    based on that initial list. The function continues to update the means list and assignments list of lists until the
    assignments list of lists does not change.
    :param image: The image data, should be a width x height list-of-lists with each element
            being a 3-tuple of red,green,blue values each of which should be between 0 and 255.
    :param k: an integer representing the number of colors the image will be clustered into.
    :return: a 2-tuple, the first position of which contains the means
    list, and the second contains the assignments list-of-lists.
    """
    means_ls = initial_guess(k)
    assignments_ls = get_assignments_ls(image, means_ls)
    for i in range(len(image)):
        means_ls = update_means_list(image, assignments_ls, k)
        assignments_ls = get_assignments_ls(image, means_ls)
    return means_ls, assignments_ls


def initial_guess(k):
    """
    Creates a random initial guess means list based on the number of colors the image will be clustered into.
    :param k: an integer representing the number of colors the image will be clustered into.
    :return: a random initial means list.
    """
    means_list = []
    for num in range(k):
        rand_pix = random_color()
        means_list.append(rand_pix)
    return means_list


def get_assignments_ls(image, means):
    """
    Computes/updates the assignments list of lists by finding the index of the closest mean to a given pixel.
    :param image: The image data, should be a width x height list-of-lists with each element
            being a 3-tuple of red,green,blue values each of which should be between 0 and 255.
    :param means: The current means list.
    :return: a new assignments list-of-lists.
    """
    assignments = [[[] for i in range(len(image[0]))] for j in range(len(image))]
    for a in range(len(image[0])):
        for b in range(len(image)):
            idx = 0
            min_dist = compute_dist(image[b][a], means[0])
            for i in range(len(means)):
                d = compute_dist(image[b][a], means[i])
                if d < min_dist:
                    min_dist = d
                    idx = i
            assignments[b][a] = idx
    return assignments


def update_means_list(image, assignments, k):
    """
    Updates the means list by finding the average color of all the pixels assigned to a
    given cluster.
    :param image: The image data, should be a width x height list-of-lists with each element
            being a 3-tuple of red,green,blue values each of which should be between 0 and 255.
    :param assignments: The current assignments list-of-lists.
    :param k: an integer representing the number of colors the image will be clustered into.
    :return: a new means list.
    """
    means = []
    for i in range(k):
        colors = []
        for j in range(len(assignments)):
            for k in range(len(assignments[0])):
                if assignments[j][k] == i:
                    colors.append(image[j][k])
        if len(colors) == 0:
            means.append((0, 0, 0))
        else:
            avg = compute_avg(colors)
            means.append(avg)
    return means


def compute_dist(c1,c2):
    """
    Computes the Euclidean distance between two colors, treating the colors as 3d points.
    :param c1: a tuple containing the red, green, and blue values of a single pixel.
    :param c2: a tuple containing the red, green, and blue values of a single pixel.
    :return: a float that represents the distance between c1 and c2.
    """
    x = (c1[0]-c2[0])**2
    y = (c1[1]-c2[1])**2
    z = (c1[2]-c2[2])**2
    result = (x + y + z) ** 0.5
    return result


def compute_avg(ls_colors):
    """
    Finds the average color in a list of colors, computed using the mathematical average of the red, green, and blue
    color components of the pixel.
    :param ls_colors: a list containing tuples that represent a pixel with red, green, and blue color components.
    :return: an integer representing the average color in the list in ls_colors.
    """
    sum_r = 0
    sum_g = 0
    sum_b = 0
    for i in ls_colors:
        sum_r += i[0]
        sum_g += i[1]
        sum_b += i[2]
    r_avg = (sum_r/(len(ls_colors)))
    g_avg = (sum_g/(len(ls_colors)))
    b_avg = (sum_b/(len(ls_colors)))
    avg = int(r_avg), int(g_avg), int(b_avg)
    return avg





