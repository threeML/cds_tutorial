from threeML import *
from threeML.utils.OGIP.response import OGIPResponse
from threeML.utils.photometry import PhotometericObservation
# The filter library takes a while to load so you must import it explicitly.
from threeML.utils.photometry import get_photometric_filter_library

import numpy as np

np.random.seed(12345)




threeML_filter_library = get_photometric_filter_library()
# generates the example data for the tutorial

rsp = OGIPResponse("c_data/acis.rmf", "c_data/acis.arf")


update_logging_level("INFO")

bb =  Blackbody(K=2.,kT = 1.)


bkg = Powerlaw(K=1e2 ,index=-1.2) + Gaussian(F=1e2, mu=0.75, sigma=.1) + Gaussian(F=1e2, mu=5, sigma=.1)

xx = rsp.monte_carlo_energies


gen = DispersionSpectrumLike.from_function('gen',source_function=bb, response= rsp, background_function=bkg, scale_factor=1e-2)
gen.write_pha("c_data/obs", overwrite=True)




src =  Powerlaw(K=1.e-2, index = -2., piv=5) + Gaussian(F=3e-2, mu=6.4, sigma=.1)


bkg = Powerlaw(K=1e1,index=-1.5, piv=5) + Gaussian(F=1.5e1, mu=3., sigma=.2)

xx = rsp.monte_carlo_energies


gen = DispersionSpectrumLike.from_function('gen',source_function=src, response= rsp, background_function=bkg, scale_factor=1e-2)
gen.write_pha("c_data/obs_bkg_demo", overwrite=True)



# joint fits


plaw = Broken_powerlaw(alpha=-1.5,
                       beta=-2,
                       K=1.e0)

plaw.xb.bounds = (None, None)
plaw.xb=1.
ps = PointSource("demo", 0,0, spectral_shape=plaw)


model = Model(ps)


grond_filters = threeML_filter_library.LaSilla.GROND

grond_observation = PhotometericObservation.from_kwargs(g=(21.5,0.02),
                                                        r=(22.,0.03),
                                                        i=(21.8, 0.01),
                                                        z=(21.2, 0.01),
                                                        J=(19.6, 0.1),
                                                        H=(18.6, 0.01),
                                                        K=(18.0, 0.1))


photo = PhotometryLike("GROND",observation=grond_observation,filters=grond_filters)

photo.set_model(model)

p2 = photo.get_simulated_dataset()

p2._observation.to_hdf5("joint_data/grond_data.h5", overwrite=True)

src =  plaw


bkg = Powerlaw(K=1e1,index=-1.2, piv=5)

gen = DispersionSpectrumLike.from_function('gen',
                                           source_function=src,
                                           response= rsp,
                                           background_function=bkg,
                                          scale_factor=.01
                                          
                                          
                                          )


gen.write_pha("joint_data/obs_demo", overwrite=True)
