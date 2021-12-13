# Import Packages
import time
import os
import glob
import cv2
import random
import argparse
import numpy as np
from scipy.spatial import distance as dist

# Variables
width,height,channel = 480,320,3

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--video_src', type=str, required=True)

# Parse the argument
args = parser.parse_args()

# Function to find similarity between 2 images
def compare_images(image_1,image_2):
    image_1 = cv2.cvtColor(image_1,cv2.COLOR_BGR2RGB)
    image_2 = cv2.cvtColor(image_2,cv2.COLOR_BGR2RGB)
    hist_1 = cv2.calcHist([image_1],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
    hist_1_normalized = cv2.normalize(hist_1,hist_1).flatten()
    hist_2 = cv2.calcHist([image_2],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
    hist_2_normalized = cv2.normalize(hist_2,hist_2).flatten()
    dist = cv2.compareHist(hist_1_normalized,hist_2_normalized,cv2.HISTCMP_CORREL)
    return dist

# Function to generate summary clusters
def video_clustering(video_src):
    count = 0
    id = 0
    clip_len = 0
    flag = False
    video_cluster_dict = {}
    prev_image = 255*np.ones((width,height,channel),np.uint8)
    vidcap = cv2.VideoCapture(video_src)

    while(True):
        #vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*50))
        sucess, image = vidcap.read()

        if(not sucess):
            video_cluster_dict[id] = [start_time,int(milliseconds),start_frame,frame_count,video_src,clip_len]
            break

        frame_count = "frame"+"%d"%count
        image = cv2.resize(image,(width,height),interpolation=cv2.INTER_AREA)
        milliseconds = vidcap.get(cv2.CAP_PROP_POS_MSEC)
        if(count==0):
            video_cluster_dict[0] = ["START_TIME","END_TIME","START_TIME","END_FRAME",video_src.upper(),"VIDEO_LEN"]
            start_frame = frame_count
            start_time = int(milliseconds)
        
        # Compare Images
        dist = compare_images(prev_image,image)

        if(dist<0.8):
            end_time = int(milliseconds)
            if(clip_len>10):
                print("ID : ",id," - ",frame_count)
                video_cluster_dict[id] = [start_time,end_time,start_frame,frame_count,video_src,clip_len]
                id += 1
            start_frame = frame_count
            start_time = int(milliseconds)
            flag = True
            clip_len = 0 
        else:
            clip_len += 1
        prev_image = image
        count += 1
    vidcap.release()
    return video_cluster_dict

def generate_summary(index):
    list_idx = list(index.keys())[1:]
    video_src = index[0][4]
    video_name = video_src.split(".")[0]
    video_sum = cv2.VideoWriter(video_name+"_summary.mp4",0x7634706d,60,(width,height))
    vidcap = cv2.VideoCapture(video_src)
    if(len(list_idx)==0):
        print("Video is too short for summary")

    for id in list_idx:
        print("ID : ",id)
        cluster_list = index[id]
        if(cluster_list[5]<60):
            cluster_start_frame = cluster_list[0]
            cluster_end_frame = cluster_list[1]
        else:
            cluster_start_frame = int((cluster_list[0] + cluster_list[1])/2) - 30
            cluster_end_frame = int((cluster_list[0] + cluster_list[1])/2) + 30
        vidcap.set(cv2.CAP_PROP_POS_MSEC,cluster_start_frame)
        video_len = cluster_end_frame-cluster_start_frame
        for i in range(0,video_len):
            sucess,image = vidcap.read()
            if sucess:
                image = cv2.resize(image,(width,height),interpolation=cv2.INTER_AREA)
                video_sum.write(image)
            else:
                print("Error while writing image")
                break

    vidcap.release()
    video_sum.release()
    cv2.destroyAllWindows()
    return

# To Run without web app
# Uncomment the below lines and type "python3 summary.py --video_src=VIDEOPATH"

video_src = args.video_src
index = video_clustering(video_src)
print(index)
generate_summary(index)