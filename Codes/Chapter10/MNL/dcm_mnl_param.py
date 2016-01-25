# This file has automatically been generated
# biogeme 2.4 [Dim 1 nov 2015 18:08:12 EST]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Sun Jan 24 18:20:17 2016</p>
#
Z_price = Beta('Z_price',-3.44861,-10,10,0,'Z price' )

B_refund = Beta('B_refund',-0.617234,-3,3,0,'refund' )

B_comp = Beta('B_comp',-0.673158,-3,3,0,'compartment' )

C_price = Beta('C_price',-3.13244,-10,10,0,'C price' )

Y_price = Beta('Y_price',-4.91588,-10,10,0,'Y price' )

ASC = Beta('ASC',0,-10,10,1,'ASC' )

V_price = Beta('V_price',-5.52783,-10,10,0,'V price' )


## Code for the sensitivity analysis
names = ['B_comp','B_refund','C_price','V_price','Y_price','Z_price']
values = [[0.203085,0.0287736,-0.283255,-0.114033,-0.132506,-0.308403],[0.0287736,0.0172849,-0.0752662,-0.0771587,-0.0864283,-0.0705853],[-0.283255,-0.0752662,0.49642,0.335965,0.376385,0.507871],[-0.114033,-0.0771587,0.335965,0.390022,0.420183,0.315098],[-0.132506,-0.0864283,0.376385,0.420183,0.461041,0.353013],[-0.308403,-0.0705853,0.507871,0.315098,0.353013,0.531725]]
vc = bioMatrix(6,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
