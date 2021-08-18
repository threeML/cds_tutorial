from threeML import *
from threeML.utils.OGIP.response import OGIPResponse

# generates the example data for the tutorial

rsp = OGIPResponse("c_data/asic.rmf", "c_data/asic.arf")


update_logging_level("INFO")

bb =  Blackbody(K=1.5,kT = 1.)


bkg = Powerlaw(K=2,index=-1.5) + Gaussian(F=.5, mu=0.75, sigma=.1) + Gaussian(F=.3, mu=5, sigma=.1)

xx = rsp.monte_carlo_energies


gen = DispersionSpectrumLike.from_function('gen',source_function=bb, response= rsp, background_function=bkg)
gen.write_pha("c_data/obs", overwrite=True)
