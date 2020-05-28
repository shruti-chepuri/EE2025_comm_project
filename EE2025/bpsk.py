import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

def qfunc(x):
	return 0.5*mp.erfc(x/mp.sqrt(2))

snrlen = 10
#SNR values in dB
snrdb = np.linspace(0,9,10)
simlen = int(1e5)
#Simulated BER declaration
err = []
#Analytical BER declaration
ber = []


for i in range(0,snrlen):
	noise = np.random.normal(0,1,simlen)
	snr = 10**(0.1*snrdb[i])
	rx = mp.sqrt(snr) + noise
	#storing the index for the received symbol 
	#in error
	err_ind = np.where(rx <= 0)[0]
	#np.nonzero(rx < 0)
	#calculating the total number of errors
	err_n = len(err_ind)
	#calcuating the simulated BER
	err.append(err_n/float(simlen))
	#calculating the analytical BER
	ber.append(qfunc(mp.sqrt(snr)))
	
plt.semilogy(snrdb.T,ber,label='Analysis')
plt.semilogy(snrdb.T,err,'o',label='Sim')
plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
plt.ylabel('P_e')
plt.title('BPSK')
plt.legend()
plt.grid()
#if using termux
plt.savefig('./figs/bpsk_ber.pdf')
plt.savefig('./figs/bpsk_ber.eps')
subprocess.run(shlex.split("termux-open ./figs/bpsk_ber.pdf"))
#else
#plt.show()
