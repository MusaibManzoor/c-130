import csv
import pandas as pd
df = pd.read_csv("final.csv")

print(df.shape)

del df["hyperlink"]
del df["temp_planet_date "]
del df["temp_planet_mass"]
del df["pl_letter"]
del df["pl_name"]
del df["pl_controvflag"]
del df["pl_pnum"]
del df["pl_orbper"]
del df["pl_orbpererr1"]
del df["pl_orbpererr2"]
del df["pl_orbperlim"]
del df["pl_orbsmax"]
del df["plorbsmaxerr1"]
del df["pl_orbsmaxerr2"]
del df["pl_orbsmaxlim"]
del df["pl_orbeccen"]
del df["pl_orbeccenerr1"]
del df["pl_orbeccenerr2"]
del df["pl_orbeccenlim"]
del df["pl_orbinclerr1"]
del df["pl_orbinclerr2"]
del df["pl_orbincllim"]
del df["pl_bmassj"]
del df["pl_bmassjerr1"]
del df["pl_bmassjerr2"]
del df["pl_bmassjlim"]
del df["pl_bmassprov"]
del df["pl_radj"]
del df["pl_radjerr1"]
del df["pl_radjerr2"]
del df["pl_radjlim"]

print(df.shape)

#pl_denserr1 pl_denserr2 pl_denslim pl_ttvflag pl_kepflag pl_k2flag pl_nnotes ra dec st_dist st_disterr1 st_disterr2 st_distlim gaia_dist gaia_disterr1 gaia_disterr2 gaia_distlim st_optmag st_optmagerr st_optmaglim st_optband gaia_gmag gaia_gmagerr gaia_gmaglim st_tefferr1 st_tefferr2 st_tefflim st_masserr1 st_masserr2 st_masslim st_raderr1 st_raderr2
#st_radlim rowupdate pl_facility