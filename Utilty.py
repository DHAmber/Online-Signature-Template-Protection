import numpy as np
import math as m
import random
import pandas as pd

import Config

IsNormalised=True

def readFile(filepath):
    with open (filepath, 'r+') as f:
        return f.readlines()

def _extractFeature(data):
    x = []          #0 index
    y = []          #1 index
    time_stamp=[]   #2 index
    bs=[]           #3 index
    Azimuth=[]      #4 index
    Altitude=[]     #5 index
    p = []          #6 index

    for lines in data:
        s=lines.split()
        if(len(s)==7):
            x.append(s[0])
            y.append(s[1])
            time_stamp.append(s[2])
            bs.append(s[3])
            Azimuth.append(s[4])
            Altitude.append(s[5])
            p.append((s[6]))
        elif len(s)==6:
            x.append(s[0])
            y.append(s[1])
            time_stamp.append(s[2])
            #bs.append(s[3])
            Azimuth.append(s[3])
            Altitude.append(s[4])
            p.append((s[5]))

    return normalised(x),normalised(y),time_stamp,bs,normalised(Azimuth),normalised(Altitude),normalised(p)        #x,y,p,time_stamp

def normalised(input_ar):
    Ar = np.array(input_ar, dtype=float)
    if IsNormalised:
        maxx = np.max(Ar)
        minx = np.min(Ar)
        Xg = Ar.sum() / len(input_ar)
        newAr = np.array((Ar - Xg) / (maxx - minx))
    else:
        return Ar
    return newAr

def getFeatures(path,IsNumpy):
    data=readFile(path)
    X,Y,T,B,Az,Al,P=_extractFeature(data)
    Tm=np.diff(np.array(T,dtype=int))
    Tm=np.insert(Tm,0,0)
    if IsNumpy:
        return np.array(X,dtype=np.float32),np.array(Y,dtype=np.float32),Tm,np.array(B),np.array(Az,dtype=np.float32),np.array(Al,dtype=np.float32),np.array(P,dtype=np.float32)
    else:
        return X,Y,Tm.tolist(),B,Az,Al,P

def getCombineFerture(path,IsNumpy):
    X,Y,T,B,Az,Al,P=getFeatures(path, True)
    Ar=np.column_stack((X,Y,T,B,Az,Al,P))
    if IsNumpy:
        return Ar
    else:
        return Ar.tolist()

def CustomFeature(x, y):
    path_tangent_angle = []
    path_velocity = []
    log_curvature_radius = []
    total_acceleration = []

    for i, j in zip(x, y):
        if i != 0:
            r = float(j) / float(i)
        else:
            r = 0
        path_tangent_angle.append(np.arctan(r))

    for i, j in zip(x, y):
        path_velocity.append(m.sqrt(i ** 2 + j ** 2))

    for i, j in zip(path_velocity, path_tangent_angle):
        if abs(j)==0:
            log_curvature_radius.append(0)
        else:
            log_curvature_radius.append(m.log(abs(i) / abs(j)))

    for i, j in zip(path_velocity, path_tangent_angle):
        total_acceleration.append(m.sqrt((i ** 2 + (i * j) ** 2)))

    return path_tangent_angle, path_velocity, log_curvature_radius, total_acceleration

def get_all_features(path,IsNumpy):
    X,Y,Tm,B,Az,Al,P=getFeatures(path,IsNumpy)
    path_tangent_angle, path_velocity, log_curvature_radius, total_acceleration=CustomFeature(X,Y)
    return X,Y,Tm,B,Az,Al,P,path_tangent_angle, path_velocity, log_curvature_radius, total_acceleration

def lfsr(seed, taps, n_bits):
    lfsr = seed
    output = []
    for _ in range(n_bits):
        bit = sum((lfsr >> tap) & 1 for tap in taps) % 2  # Calculate the new bit from the taps
        output.append(str(bit))
        lfsr = (lfsr >> 1) | (bit << (len(bin(seed)) - 3))  # Shift right and insert new bit in MSB

    return ''.join(output)

def generate_random_number():
    return (random.randint(33333, 99999))

def read_LFSR_Key(user):
    df = pd.read_csv(Config.key_file_name)
    df = df[df["User"] == user]
    return df.iloc[0][1]