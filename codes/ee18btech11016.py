# License
'''
Code by Ganraj Borade
April 27,2020
Released under GNU GPL
'''

import control
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


#coefficents of open loop transfer function
num = [0,1,6,8]
den = [1,-3,10,0]

#Transfer function GH = num/den
G = control.tf(num,den) 

#plotting nyquist plot
control.nyquist(G)

plt.scatter(-1,0,s=60,color='r')
plt.annotate("   -1+0j",(-1,0))
plt.title('NYQUIST DIAGRAM of G(s)H(s)')
plt.axvline(x = 0.7873,ymax = 0.5,color='r',linestyle='--',linewidth=2)
plt.plot(0.7873,0,'o',color='r')
plt.text(0.7873,0, '({}, {})'.format(0.7873,0))

plt.axvline(x = -0.254,ymax = 0.5,color='r',linestyle='--',linewidth=2)
plt.plot(-0.254,0,'o',color='r')
plt.text(-0.254,0, '({}, {})'.format(-0.254,0))
plt.xlabel("${Re}\{G(j\omega)H(j\omega)\}$")
plt.ylabel("${Im}\{G(j\omega)H(j\omega)\}$")
plt.grid(color='k',linestyle='--',linewidth=1)
plt.show()


#if using termux
plt.savefig('./figs/ee18btech11016.pdf')
plt.savefig('./figs/ee18btech11016.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11016.pdf"))
#else
#plt.show()
