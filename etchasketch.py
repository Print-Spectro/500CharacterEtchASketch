from pygame import *
r=800
S=999
s=display.set_mode((S,r))
R=50
c="grey"
t=600
o=100
s.fill("red")
[draw.circle(s,c,(i,r-R),R) for i in (R,S-R)]
draw.rect(s,c,Rect(o,o,r,t))
w=0.1
while True:
    k=key.get_pressed()
    S=w if k[K_s] and t<700 else -w if k[K_w] and t>o else 0
    t+=S
    R=w if k[K_d] and r<900 else -w if k[K_a] and r>o else 0
    r+=R 
    ([quit() if e.type==QUIT else... for e in event.get()], draw.rect(s,"black",Rect(r,t,2,2)), display.update())