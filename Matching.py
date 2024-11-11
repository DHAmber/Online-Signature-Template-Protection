Y='ascii'
X='%Y-%m-%d'
W=Exception
V=round
K=False
J='rb'
I=open
B=print
import pickle as D,Config as C,FinalTemplate as N,time as A
O=C.users
c=C.Genuine
d=C.Fake
with I(C.data_file_name,J)as E:P=D.load(E)
def extract_data(data,sign):
	A={}
	for B in C.keys:A[B]=data[B][sign-1]
	return A
def match(template,query):
	C=query;B=template;G=min(len(B),len(C));D=0;E=0;F=0
	for(A,H)in zip(B,C):
		if A==H:
			E+=1
			if A=='1':D+=1
		if A=='1':F+=1
	return E,D,F,G
S=['Template','User_Sign','Total_Bit','All_Matching_Bit','Total_Ones','Matching_One','MatchingPercent','Expected Results']
import pandas as T
from datetime import datetime as U
def matching_genuine():
	Z=[];d=U.now().strftime(X);e=f"Result\\{C.DB}\\Matching_({C.KeySize})_{d}_Genuine.csv"
	for D in O:
		f=f"Final_Template\\{C.DB}\\Template_{D}.txt";L=f"Template_{D}.txt"
		with I(f,J)as g:h=g.read().decode(Y)
		for E in c:
			try:F=A.time();B(f"Matching {L} to {E}");i=extract_data(P[D],E);G=A.time();B(f"Time to extract query data took {G-F:.2f} seconds");j=True;F=A.time();k=N.CreateQuery(D,i,j);G=A.time();B(f"Time to create query bit string took {G-F:.2f} seconds");F=A.time();a,M,H,b=match(h,k);G=A.time();B(f"Time to match bit strings took {G-F:.2f} seconds");l=V(M/H*100,2)if H>0 else .0;Z.append([L,f"USER{D}_{E}",b,a,H,M,l,'Match']);B("Processing complete..")
			except W as m:B(f"Error processing user {D}, gen {E}: {m}");continue
		n=T.DataFrame(data=Z,columns=S);n.to_csv(e,index=K)
def matching_fake():
	Z=[];c=U.now().strftime(X);e=f"Result\\{C.DB}\\Matching_({C.KeySize})_{c}_Fake.csv"
	for D in O:
		f=f"Final_Template\\{C.DB}\\Template_{D}.txt";L=f"Template_{D}.txt"
		with I(f,J)as g:h=g.read().decode(Y)
		for E in d:
			try:F=A.time();B(f"Matching {L} to {E}");i=extract_data(P[D],E);G=A.time();B(f"Time to extract query data took {G-F:.2f} seconds");j=K;F=A.time();k=N.CreateQuery(D,i,j);G=A.time();B(f"Time to create query bit string took {G-F:.2f} seconds");F=A.time();a,M,H,b=match(h,k);G=A.time();B(f"Time to match bit strings took {G-F:.2f} seconds");l=V(M/H*100,2)if H>0 else .0;Z.append([L,f"USER{D}_{E}",b,a,H,M,l,'Not Match']);B("Processing complete..")
			except W as m:B(f"Error processing user {D}, gen {E}: {m}");continue
		n=T.DataFrame(data=Z,columns=S);n.to_csv(e,index=K)
matching_genuine()
matching_fake()
