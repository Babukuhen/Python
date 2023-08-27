import cv2 as cv

# Original Image
img = cv.imread('images\input.jpg')
cv.imshow('Input Image', img)

# Grayscale Image (1)
gray_img = cv.imread('images\input.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Grayscale Image 1', gray_img)

# Grayscale Image (2)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image 2', gray_img)

# YUV Image
yuv_img = cv.cvtColor(img, cv.COLOR_BGR2YUV)
cv.imshow('YUV Image', yuv_img)
cv.imshow('Y Channel', yuv_img[:, :, 0])
cv.imshow('U Channel', yuv_img[:, :, 1])
cv.imshow('V Channel', yuv_img[:, :, 2])

# HSV Image
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV Image', hsv_img)
cv.imshow('H Channel', hsv_img[:, :, 0])
cv.imshow('S Channel', hsv_img[:, :, 1])
cv.imshow('V Channel', hsv_img[:, :, 2])

cv.waitKey()