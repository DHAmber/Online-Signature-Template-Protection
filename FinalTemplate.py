_B='total_acceleration'
_A='path_velocity'
import numpy as np,math,Config,Utilty
taps=[15,14,5,4]
def compute_dim_vals(data,dim):A=math.ceil(np.max(data));B=math.floor(np.min(data));C=math.ceil((A-B)/dim);return dim,C
def get_index(value,val,dim):A=math.floor(value/val);return min(A,dim-1)
def CreateFinalTemplate(user,data,savedKey=True):
        A=data;E=A['X'];I=A['Y'];i=A['Az'];J=A['Al'];K=A['P'];L=A[_A];M=A[_B];N,T=compute_dim_vals(E,200);O,U=compute_dim_vals(I,100);P,V=compute_dim_vals(J,10);Q,W=compute_dim_vals(K,10);R,X=compute_dim_vals(L,10);S,Y=compute_dim_vals(M,10);C=np.zeros((N,O,P,Q,R,S),dtype=str);C[C=='']='0'
        for B in range(E.size):Z=get_index(E[B],T,N);a=get_index(I[B],U,O);b=get_index(J[B],V,P);c=get_index(K[B],W,Q);d=get_index(L[B],X,R);e=get_index(M[B],Y,S);C[Z][a][b][c][d][e]='1'
        F=C.flatten();G=np.flatnonzero(F)
        if G.size>0:f=G[0];g=G[-1]+1;D=F[f:g]
        else:D=F
        if savedKey:H=Utilty.read_LFSR_Key(user)
        else:h=Utilty.generate_random_number();H=Utilty.lfsr(h,taps,Config.KeySize)
        H='';D=''.join(D);return str(H)+str(D)
def CreateQuery(user,data,savedKey=True):
        A=data;E=A['X'];I=A['Y'];J=A['Al'];K=A['P'];L=A[_A];M=A[_B];N,T=compute_dim_vals(E,200);O,U=compute_dim_vals(I,100);P,V=compute_dim_vals(J,10);Q,W=compute_dim_vals(K,10);R,X=compute_dim_vals(L,10);S,Y=compute_dim_vals(M,10);C=np.zeros((N,O,P,Q,R,S),dtype=str);C[C=='']='0'
        for B in range(E.size):Z=get_index(E[B],T,N);a=get_index(I[B],U,O);b=get_index(J[B],V,P);c=get_index(K[B],W,Q);d=get_index(L[B],X,R);e=get_index(M[B],Y,S);C[Z][a][b][c][d][e]='1'
        F=C.flatten();G=np.flatnonzero(F)
        if G.size>0:f=G[0];g=G[-1]+1;D=F[f:g]
        else:D=F
        if savedKey:H=Utilty.read_LFSR_Key(user)
        else:h=Utilty.generate_random_number();H=Utilty.lfsr(h,taps,Config.KeySize)
        H='';D=''.join(D);return str(H)+str(D)
