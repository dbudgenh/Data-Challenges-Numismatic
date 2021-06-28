from typing import List
import matplotlib.pyplot as plt
import cv2

def plot_images(path_to_images:List[str], titles_for_images:List[str],rows:int, cols:int) -> None:
    fig = plt.figure(figsize=(5,5))
    images = []
    for img in path_to_images:
        images.append(cv2.imread(img))

    for index,img in enumerate(images):
        fig.add_subplot(rows,cols,index+1)
        plt.imshow(img)
        plt.axis('off')
        plt.title(titles_for_images[index])
    plt.show()