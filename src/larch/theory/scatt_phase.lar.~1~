# gnuplot file to make figures for gas absorption coefs

feo  = read_ascii('fe_o.dat')
fefe = read_ascii('fe_fe.dat')
fepb = read_ascii('fe_pb.dat')

xlabel=r'$k \rm\, (\AA^{-1})$'
ylabel=r'$\delta(k)$'

opts = dict(linewidth=3, xmax=20)
s = 0

plot(feo.k,   feo.phase+s*feo.k, zorder=10, # ymin=-11, ymax=11,
	      new=True, xlabel=xlabel, ylabel=ylabel, **opts)
plot(fefe.k, fefe.phase+s*fefe.k, zorder= 9,  **opts)
plot(fepb.k, fepb.phase+s*fepb.k, zorder= 8, **opts)


plot_text(' Fe  ',  7.0 , -14.0)
plot_text(' O   ', 10.0 , -13.0)
plot_text(' Pb  ',  12.0 , -7.0)


