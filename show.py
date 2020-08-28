import cv2


def view_result():
    startIndex = 40
    image = cv2.imread('F:/database/OTB2015/OTB100/Dog1/img/{0:04d}.jpg'.format(startIndex))

    x1, y1, w1, h1 = [150, 108, 50, 33]  # gt
    x2, y2, w2, h2 = [147.692, 104.116, 51.017, 36.012]  # siamfc
    x3, y3, w3, h3 = [146.402, 107.001, 54.478, 38.455]  # dcanet
    x4, y4, w4, h4 = [148.0, 106.0, 54.0, 38.0]  # muster

    color1 = (255, 0, 0)
    color2 = (0, 255, 0)
    color3 = (0, 0, 255)
    color4 = (0, 255, 255)
    # Line thickness of 2 px
    thickness = 2
    out = cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), color1, thickness)
    # cv2.rectangle(image,(x2, y2), (x2+w2, y2+h2),color2, thickness)
    # cv2.rectangle(image,(x3, y3), (x3+w3, y3+h3),color3, thickness)
    # out=cv2.rectangle(image, (x4, y4), (x4 + w4, y4 + h4),color4, thickness)

    # cv2.imwrite("Basketball{0:04d}.jpg".format(startIndex), out)  # 将画过矩形框的图片保存到当前文件夹

    cv2.imshow("draw_0", out)  # 显示画过矩形框的图片

    cv2.waitKey(0)


# def get_coordinate(res):
#     return int(res[0]), int(res[1]), int(res[2]), int(res[3])


if __name__ == '__main__':
    view_result()