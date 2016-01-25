# This file has automatically been generated
# biogeme 2.4 [Dim 1 nov 2015 18:08:12 EST]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sun Jan 24 18:21:29 2016</p>
#
C_price = Beta('C_price',-6.72393,-10,10,0,'C price' )

B_refund = Beta('B_refund',-0.72318,-3,3,0,'refund' )

B_comp = Beta('B_comp',3,-3,3,0,'compartment' )

V_price = Beta('V_price',-5.05523,-10,10,0,'V price' )

Y_price = Beta('Y_price',-4.38749,-10,10,0,'Y price' )

Z_price = Beta('Z_price',-8.01591,-10,10,0,'Z price' )

ASC = Beta('ASC',0,-10,10,1,'ASC' )


## Code for the sensitivity analysis
names = ['B_comp','B_refund','C_price','V_price','Y_price','Z_price']
values = [[2.75431e-30,4.17794e-17,-2.89676e-16,-3.63094e-16,-3.9347e-16,-2.42312e-16],[4.12315e-17,0.0183747,-0.0478975,-0.0815499,-0.0915569,-0.0351632],[-2.3331e-16,-0.0478975,0.132913,0.227617,0.250606,0.0981703],[-2.1132e-16,-0.0815499,0.227617,0.40712,0.440473,0.17462],[-3.55558e-16,-0.0915569,0.250606,0.440473,0.484957,0.189947],[-6.07756e-17,-0.0351632,0.0981703,0.17462,0.189947,0.0765937]]
vc = bioMatrix(6,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
