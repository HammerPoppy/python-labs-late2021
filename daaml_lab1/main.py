import cv2
import numpy as np
import matplotlib.pyplot as plt


def roberts(grayImage):
    kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
    kernely = np.array([[0, -1], [1, 0]], dtype=int)
    x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
    y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)

    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)

    return cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


def prewitt(grayImage):
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
    x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
    y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)

    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)

    return cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


def sobel(grayImage):
    x = cv2.Sobel(grayImage, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(grayImage, cv2.CV_16S, 0, 1)
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)

    return cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


def laplace(grayImage):
    dst = cv2.Laplacian(grayImage, cv2.CV_16S, ksize=3)
    return cv2.convertScaleAbs(dst)


def canny(grayImage):
    return cv2.Canny(grayImage, 1, 1)


if __name__ == "__main__":
    img = cv2.imread('4.bmp')
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plt.subplot(231), plt.imshow(img_RGB), plt.title('original'), plt.axis('off')
    plt.subplot(232), plt.imshow(sobel(grayImage), cmap=plt.cm.gray), plt.title('Sobel'), plt.axis('off')
    plt.subplot(233), plt.imshow(prewitt(grayImage), cmap=plt.cm.gray), plt.title('Prewitt'), plt.axis('off')
    plt.subplot(234), plt.imshow(roberts(grayImage), cmap=plt.cm.gray), plt.title('Roberts'), plt.axis('off')
    plt.subplot(235), plt.imshow(laplace(grayImage), cmap=plt.cm.gray), plt.title('Laplace'), plt.axis('off')
    plt.subplot(236), plt.imshow(canny(grayImage), cmap=plt.cm.gray), plt.title('Canny ([1,1] thresholds)'), plt.axis('off')

    plt.show()
