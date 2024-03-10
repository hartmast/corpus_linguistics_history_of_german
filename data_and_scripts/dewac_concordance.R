library(concordances)

d <- getWACKY("view_dewac_20240306183956.xml", tags = "column", XML = T)
d <- readLines("view_dewac_20240306183956.xml")
