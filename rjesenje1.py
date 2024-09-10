import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tifffile import imread, imwrite

# Ucitavanje tiff datoteke
image_data = imread('./response_bands.tiff')

# Nakon provjere broja kanala i provjere web linkova utvrdjeno je da je crveno 4. kanal, nir je 8. kanal
# te swir 11. kanal. Sto kod 0-based indexa daje 3,7,10 kao treci index u slicingu
red = image_data[:,:,3]*10000
nir = image_data[:,:,7]*10000
swir = image_data[:,:,10]*10000

# Izracun indexa, numpy se bavi dijeljenjem sa 0, te dodjeljuje NaN tim vrijednostima.
# S obzirom da nije navedeno kako postupiti s tim slucajevima ostavljeno je nan
# U slucaju da treba ukljuciti nan vrijednosti kao nulte vrijednosti postoji mnogo opcija i za to
ndvi = (nir-red)/ (nir+red)
ndmi = (nir-swir)/ (nir+swir)

# Shodno prethodnom komentaru, nan vrijednosti izbacene su iz racunanja prosjecne vrijednosti
# Također pretpostavljeno je da se traži aritmetička sredina
ndvi_avg = np.nanmean(ndvi)
ndmi_avg = np.nanmean(ndmi)

# Spremanje .tiff datoteka za tražene indexe
imwrite('ndvi.tiff', ndvi)
imwrite('ndmi.tiff', ndmi)

# Printanje u konzolu trazenih prosjecnih vrijednosti za indexe, te broj kanala satelitske snimke
# Pretpostavka je da se trazi broj kanala orginalne tiff datoteke
print(',\n\n')
print(f'Prosjecna vrijednost NDVI indexa iznosi {ndvi_avg:.3f}\n')
print(f'Prosjecna vrijednost NDMI indexa iznosi {ndmi_avg:.3f}\n')
print(f'Satelitska snimka sadrzi {image_data.shape[2]} kanala\n')