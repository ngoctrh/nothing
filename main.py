import cv2
import numpy as np
from scipy import spatial
import time, random

#read image
def read_image(path):
    return cv2.imread(path)
#data X[a,b,c,d,e] a,b,c = r,g,b d,e = position		
def create_data(img):
    h,w = img.shape[:2]
    dataX = []
    for i in range(h):
        for j in range(w):
            temp = np.concatenate((img[i,j],[i,j]))
            dataX.append(temp)
    return dataX

#calculator distance from 1 point to the clus center
def getDistance(x, xi):
    return np.linalg.norm(np.array(x)-np.array(xi))

#return list index of point neighbour of x in distance <= window 
def neighbourhood_points(point_tree, x, window):
    return point_tree.query_ball_point(x, window)

def create_neighbour(points):
	return spatial.cKDTree(points,balanced_tree=False)


#meanshift
def meanshift(X):
    
    window = 166
    flag = True
    clus = []
    
    while len(X) > 0:
        #print(len(X))
        if flag:
            #choose random 1 data point
            current_mean = random.randint(0,len(X)-1)
            #libs return tree for later
            point_tree = create_neighbour(X)
            #print(point_tree)
            x = X[current_mean]
        #label of point neighbour has distance < lookdistance
        
        ind_neighbours = neighbourhood_points(point_tree, x, window)
        #print('indddddd',ind_neighbours)
        #calculator center position
        sum = 0
        for ind in ind_neighbours:
            sum = sum + X[ind]
        center = sum/len(ind_neighbours)
        #print('sumn',type(sum))
        #print('center',center)
        #thay màu tất cả hàng xóm = center
        if getDistance(x, center) ==0:
            temp = []
            ind_neighbours.sort(reverse=True)
            for i in ind_neighbours:
                temp.append(X.pop(i)) #xóa label
            temp.append(center)
            clus.append(temp)
            flag = True
        else:
            flag = False
            x = center
    return clus

def main():
    img = read_image('quyt.jpg')
    print(img.shape)
    #create data points
    dataPoints = create_data(img)
    print('Len data points:',len(dataPoints))
    start = time.time()
    #excute meanshift
    clus = meanshift(dataPoints)
    #print(clus)
    print("Time to segment", time.time() - start)
    #copy from image to segment
    segmented_image = img.copy()
  #  h,w,_ = segmented_image.shape
      # for each clus founding in meanshift, 
    for c in clus:
        for ind in range(len(c)):
            i = c[ind][3]	
            j = c[ind][4]
            segmented_image[int(i),int(j)] = c[-1][:3]
    print("Number cluster: ", len(clus))
    cv2.imshow('Normal',img)
    cv2.imshow("segment2", segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
