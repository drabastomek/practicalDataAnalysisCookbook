# This file has automatically been generated
# biogeme 2.4 [Dim 1 nov 2015 18:08:12 EST]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sun Jan 24 23:33:36 2016</p>
#
C_price = Beta('C_price',-7.29885,-10,10,0,'C price' )

B_refund = Beta('B_refund',-0.718748,-3,3,0,'refund' )

B_comp = Beta('B_comp',3.52571,-10,10,0,'compartment' )

V_price = Beta('V_price',-5.07495,-10,10,0,'V price' )

Y_price = Beta('Y_price',-4.40754,-10,10,0,'Y price' )

Z_price = Beta('Z_price',-8.70638,-10,10,0,'Z price' )

ASC = Beta('ASC',0,-10,10,1,'ASC' )


## Code for the sensitivity analysis
names = ['B_comp','B_refund','C_price','V_price','Y_price','Z_price']
values = [[1.71083,-0.0398667,-1.67587,0.190499,0.209566,-2.13821],[-0.0398667,0.0188657,-0.00717013,-0.083915,-0.0941582,0.0155518],[-1.67587,-0.00717013,1.76813,0.0330621,0.0365816,2.18927],[0.190499,-0.083915,0.0330621,0.418485,0.452985,-0.0676863],[0.209566,-0.0941582,0.0365816,0.452985,0.498726,-0.0766095],[-2.13821,0.0155518,2.18927,-0.0676863,-0.0766095,2.74714]]
vc = bioMatrix(6,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
