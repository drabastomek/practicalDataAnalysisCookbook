# This file has automatically been generated
# biogeme 2.4 [Dim 1 nov 2015 18:08:12 EST]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sun Jan 24 18:54:38 2016</p>
#
Y_price = Beta('Y_price',-4.91592,-10,10,0,'Y price' )

B_ref = Beta('B_ref',-0.617855,-3,3,0,'refund' )

B_ref_S = Beta('B_ref_S',0.0496741,-3,3,0,'refund (std)' )

B_comp = Beta('B_comp',-0.673125,-3,3,0,'compartment' )

Z_price = Beta('Z_price',-3.44868,-10,10,0,'Z price' )

V_price = Beta('V_price',-5.52788,-10,10,0,'V price' )

ASC = Beta('ASC',0,-10,10,1,'ASC' )

C_price = Beta('C_price',-3.13251,-10,10,0,'C price' )


## Code for the sensitivity analysis
names = ['B_comp','B_ref','B_ref_S','C_price','V_price','Y_price','Z_price']
values = [[0.203088,0.0287656,0.000339562,-0.283261,-0.114036,-0.13251,-0.308409],[0.0287656,0.0172895,-0.000185804,-0.0752577,-0.0771543,-0.0864231,-0.0705735],[0.000339562,-0.000185804,0.00903728,-0.000415341,-0.000260393,-0.000305981,-0.000538544],[-0.283261,-0.0752577,-0.000415341,0.496431,0.335975,0.376396,0.507883],[-0.114036,-0.0771543,-0.000260393,0.335975,0.390033,0.420194,0.315107],[-0.13251,-0.0864231,-0.000305981,0.376396,0.420194,0.461053,0.353023],[-0.308409,-0.0705735,-0.000538544,0.507883,0.315107,0.353023,0.531736]]
vc = bioMatrix(7,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
