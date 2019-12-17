
# coding: utf-8



# importing dependencies 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
import sys 
   
# creating data 
mean_01 = np.array([0.0, 0.0]) 
cov_01 = np.array([[1, 0.3], [0.3, 1]]) 
dist_01 = np.random.multivariate_normal(mean_01, cov_01, 10) 
   
mean_02 = np.array([6.0, 7.0]) 
cov_02 = np.array([[1.5, 0.3], [0.3, 1]]) 
dist_02 = np.random.multivariate_normal(mean_02, cov_02, 10) 
   
mean_03 = np.array([7.0, -5.0]) 
cov_03 = np.array([[1.2, 0.5], [0.5, 1,3]]) 
dist_03 = np.random.multivariate_normal(mean_03, cov_01, 10) 
   
mean_04 = np.array([2.0, -7.0]) 
cov_04 = np.array([[1.2, 0.5], [0.5, 1,3]]) 
dist_04 = np.random.multivariate_normal(mean_04, cov_01, 10) 
   
data = np.vstack((dist_01, dist_02, dist_03, dist_04)) 
np.random.shuffle(data) 


           
# function to compute euclidean distance 
def distance(p1, p2): 
    return np.sum((p1 - p2)**2) 
   
# initialisation algorithm 
def initialize(data, no_of_clusters): 
    ''' 
    intialized the centroids for K-means++ 
    inputs: 
        data - numpy array of data points having shape (200, 2) 
          
    '''
    ## initialize the centroids list and add 
    ## a randomly selected data point to the list 
    centroids = [] 
    centroids.append(data[np.random.randint( 
            data.shape[0]), :].tolist())
    temp_data=data.tolist()
    temp_data.append('dummy')
    
   
    ## compute remaining no_of_clusters - 1 centroids 
    for c_id in range(no_of_clusters-1): 
          
        ## initialize a list to store distances of data 
        ## points from nearest centroid 
        dist = [] 
        for i in range(data.shape[0]):
            if [data[i,:].tolist()]*len(centroids)!=centroids:
                temp_sum=1
                for j in range(c_id+1):
                    #dist.append(distance(data[i,:],centroids[c_id]))
                    temp_sum *= distance(data[i,:],centroids[j])
                dist.append(temp_sum)
            else:
                dist.append(0)
        pdf=(dist/sum(dist)).tolist()
        pdf.append(0)
        next_centroid = np.random.choice(temp_data,p=pdf)
        centroids.append(next_centroid)
    return centroids 

def classify_a_point(point, groups, k):
    index=-1
    dist=[]
    for i in range(len(groups)):
        for j in range(len(groups[i])):
            dist.append((distance(point,groups[i][j]),i))
    if len(dist)>k:
        dist=sorted(dist)[:k]
    else:
        dist=sorted(dist)
    #calculating frequencies of different groups
    freq=[0]*len(groups)
    #use if loops for no_of_clusters times 
    for e in dist:
        if e[1]==0:
            freq[0]+=1
        if e[1]==1:
            freq[1]+=1
        if e[1]==2:
            freq[2]+=1
        if e[1]==3:
            freq[3]+=1
    index = freq.index(max(freq))
    return index

def cluster(data, no_of_clusters, k, max_iterations):
    groups=initialize(data, no_of_clusters)
    #print('groups are',groups)
    groups=[[element] for element in groups]
    #print('groups converted as follows', groups)
    #plot_clusters(groups)
    #plt.show()
    for n in range(max_iterations):
        for i in range(data.shape[0]):
            group_no = classify_a_point(data[i,:], groups,k)
            #print('point chosen: ', data[i,:], 'classified in group no. :', group_no)
            print('data point is: ', data[i,:])
            print('initialized point is: ',groups[group_no][0] )
            if groups[group_no][0].all()!=data[i,:].all():  #to prevent the initialized points from gettind re-added
                groups[group_no].append(data[i,:])
            #plot_clusters(groups)
            #plt.show()
    return groups

def plot_clusters(groups):
    #colors = cm.rainbow(np.linspace(0, 1, len(groups)))
    plt.scatter(*zip(*groups[0]),[6], 'r')
    plt.scatter(*zip(*groups[1]),[6], 'b')
    plt.scatter(*zip(*groups[2]),[6], 'g')
    plt.scatter(*zip(*groups[3]),[6], 'c')
    plt.show()   



l=initialize(data,4)
colors = cm.rainbow(np.linspace(0, 1, len(l)))
#cluster(data,4,5,1)
plt.scatter(*zip(*data),[6],'r')
for i in range(len(l)):
    plt.scatter(l[i][0],l[i][1],[6],color=colors)
plt.show()




    
    
        
    
    
    
    



