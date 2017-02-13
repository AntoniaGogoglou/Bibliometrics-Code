library(sde)
library(nloptr)
mu=0.0015*10; sigma=0.045*sqrt(10); P0=47.72; T = 10/360  ## 10 days, T is default st in years
nt=10000; n=10
#############Generate nt trajectories
dt=T/n; t=seq(0, T, by=dt)
X=matrix(rep(0,length(t)*nt), nrow=nt)
for (i in 1:nt) {X[i,]= GBM(x=P0,r=mu,sigma=sigma,T=T,N=n)}
##Plot
ymax=max(X); ymin=min(X) #bounds for simulated prices
plot(t,X[1,],t='l',ylim=c(ymin, ymax), col=1,
     ylab="Price P(t)",xlab="time t",xaxt='n')
axis(1, at=t, labels=c(1:11))
DataPath<-"/home/anto/Desktop/bro/StockPrices.txt"
for(i in 2:nt){lines(t,X[i,], t='l',ylim=c(ymin, ymax),col=i)}
write.table(X[, 11], DataPath, sep="\t") 
#result<-c(0)
#f3<-function(n,S=X[1,1:10]) t(S)%*%n-t(n)%*%n
#for(i in 1:10000) {S<-X[i,1:10]
#n<-c(3,2,4,5,1,7,18,12,3,1)
#temp1<-f3(n,as.vector(S))
#result=c(result,temp1)
#}


#for(i in 1) {
#  InitialHold=50000
#  x0<-c(5000,5000,5000,5000,5000,5000,5000,5000,5000,5000)
#  low<-c(0,0,0,0,0,0,0,0,0,0)
#  up<-c(InitialHold,InitialHold,InitialHold,InitialHold,InitialHold,InitialHold,InitialHold,InitialHold,InitialHold,InitialHold)
#  #up<-c(InitialHold*10,InitialHold*10,InitialHold*10,InitialHold*10,InitialHold*10,InitialHold*10,InitialHold*10,InitialHold*10,InitialHold*10,InitialHold*10)
#  hh<-function(n,X0=InitialHold) sum(n)-X0
#  te1<-hh(low)
#  te2<-hh(up)
#  ff<-function(n,S=X[i,1:10],X0=InitialHold) X0*S[1]+(1/2)*0.025*X0+(1/2)*X0^2-t(S)%*%n+(1-1/2)*t(n)%*%n
#  res<-isres(x0=x0,fn=ff,lower=low,upper=up,heq=hh,maxeval=100000)
#}


