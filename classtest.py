import cv2
import pyGridMatching
import pyVideoToFrames
import pyFrameSTemporal
import pyTargetFrame

frame1 = cv2.imread('OriginalFrames/frame41.jpg')
frame2 = cv2.imread('OriginalFrames/frame51.jpg')

obj = pyFrameSTemporal.temporal_S(frame1,frame2,2,2)

#spatial = obj.prevFrameS(frame1)
reg_pts = obj.matchedRegionPoints(frame1, frame2,0,2)
grid_temp = obj.Grid_S_temporal(frame1,frame2, 0,2)
frame_temp = obj.Frame_S_temporal(frame1, frame2)
#print(spatial)
print(reg_pts)
print(grid_temp)
print(frame_temp)
print(frame_temp.shape)
print(frame_temp[2][2][0], frame_temp[2][2][1])

#obj = pyGridMatching.frame(frame1,frame2)

#grid = obj.getGrid(frame2,2,2)
#H = grid.shape[0]
#W = grid.shape[1]
#M = 4
#N = 4


#for i in range(0,M):
    #for j in range(0,N):
        #grid = obj.getGrid(frame2, i, j)
        #matching_block_cor = obj.closestMatchingGrid(frame1, grid)
        #print(i*H,j*W)
        #print(matching_block_cor)
        #print(type(matching_block_cor))
