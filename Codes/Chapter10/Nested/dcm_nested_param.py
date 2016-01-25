# This file has automatically been generated
# biogeme 2.4 [Dim 1 nov 2015 18:08:12 EST]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sun Jan 24 19:53:32 2016</p>
#
Y_price = Beta('Y_price',-4.91591,-10,10,0,'Y price' )

B_refund = Beta('B_refund',-0.617229,-3,3,0,'refund' )

B_comp = Beta('B_comp',-0.673168,-3,3,0,'compartment' )

C_price = Beta('C_price',-3.13244,-10,10,0,'C price' )

Z_price = Beta('Z_price',-3.44861,-10,10,0,'Z price' )

ASC = Beta('ASC',0,-10,10,1,'ASC' )

V_price = Beta('V_price',-5.52786,-10,10,0,'V price' )

biz_mu = Beta('biz_mu',1,0,1,0,'biz_mu' )

eco_mu = Beta('eco_mu',1,0,1,0,'eco_mu' )


## Code for the sensitivity analysis
names = ['B_comp','B_refund','C_price','V_price','Y_price','Z_price','biz_mu','eco_mu']
values = [[0.203083,0.0287736,-0.283254,-0.114033,-0.132507,-0.308402,-7.62397e-17,-1.8382e-16],[0.0287736,0.017285,-0.0752663,-0.0771588,-0.0864285,-0.0705854,-1.41739e-17,-2.56464e-17],[-0.283254,-0.0752663,0.496419,0.335966,0.376386,0.50787,7.067e-17,2.79608e-16],[-0.114033,-0.0771588,0.335966,0.390023,0.420183,0.315098,-4.56135e-17,6.47934e-17],[-0.132507,-0.0864285,0.376386,0.420183,0.461041,0.353014,-2.15692e-17,6.9419e-17],[-0.308402,-0.0705854,0.50787,0.315098,0.353014,0.531723,3.11877e-17,3.68244e-16],[8.90442e-17,1.33953e-18,-1.43419e-16,3.96453e-18,-1.25366e-17,-1.75499e-16,3.26262e-30,-4.7884e-30],[-1.82881e-16,-3.54759e-17,2.18362e-16,8.62532e-17,8.73277e-17,2.79234e-16,-1.43343e-30,1.31202e-30]]
vc = bioMatrix(8,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
