clear all
n=1000; % grid size
t=[1:n]/n; % so plot the process on t in [0,1]
h=0.97;
covar=@(s,t)(5*(abs(s).^(2*h)-abs(t-s).^(2*h)+abs(t).^(2*h)));
for i=1:n
    for j=1:n
        Sig(i,j)=covar(t(i),t(j));
    end
end
A=chol(Sig,'lower');
X=A*randn(n,1); % using Alg. in the slides
plot(t,X)