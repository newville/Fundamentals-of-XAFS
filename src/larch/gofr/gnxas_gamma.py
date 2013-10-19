from Ifeffit import Ifeffit
from numpy import array,sqrt, exp, power
from scipy.special import gamma, gammaln
import time

iff = Ifeffit()
iff.ifeffit("set my.r = range(2,4,0.01)")
iff.ifeffit("show @arrays")

r = iff.get_array('my.r')

iff.ifeffit("set my.rho = my.r * my.r")

# iff.ifeffit("plot(my.r, my.rho)")

print r

def rho(r,r0, sigma2,k3):
    sigma = sqrt(sigma2)
    beta  = k3 / sigma2*sigma
    q     = 4 / (beta*beta)
    MAX = 20.
    if q > MAX: q=MAX
    if q < 2:   q=2
    if gammaln(q) > MAX:
        gammaq = MAX
    else:
        gammaq = max(1,min(MAX,gamma(q)))
    #print r0, sigma, beta, 4/(beta*beta), q, q-1, gammaln(q), gamma(q), gammaq

    pre = 2/ (sigma*abs(beta)*gammaq)

    fac =(q + 2*(r-r0)/(sigma*beta))

    return pre * power(fac,q-1) * exp(-fac)
   
rhox = rho(r,3.0, 0.3, 1.e-3)

print len(r), len(rhox)
print rhox
iff.put_array('my.rho', rhox)

iff.ifeffit("plot( my.r, my.rho, ymin=0,xmin=2.05,xmax=4.0)")





print 'done.'
for i in range(10): time.sleep(0.25)
