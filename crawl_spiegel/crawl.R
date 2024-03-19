library(stringi)
library(stringr)

d <- readLines("https __www.spiegel.de_.html")

# find all lines that contain spiegel.de
d1 <- grep("spiegel\\.de", d, 
           value = T)

strsplit(d1, ("(?=https://spiegel.de)"), d1[1], perl = T)

str_extract_all("The quick brown fox", "fox")
d2 <- gsub("\".*", "", unlist(str_extract_all(d, "https://www.spiegel.de.*")))
# writeLines(d2, "crawlthis.txt")

# read single page
tx <- readLines(d2[917])
tx1 <- grep("^<p>", tx, value = T)
tx1
