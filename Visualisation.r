library(ggplot2)
library(dplyr)
library(ggthemes)

df = read.csv('newnumberones.csv')

df2 = mutate(df, DATE= as.Date(DATE, format= "%d/%m/%Y"))

ggplot(df2, aes(x=DATE,y=SONG.LENGTH.SECONDS)) +
  theme_solarized() +
  geom_point(alpha=0.1) +
  geom_smooth(colour="steelblue",size=1.5) +
  ylim(98,400) +
  labs(x="Date",y="Song Duration in Seconds",title ="Song Duration of every Number 1 UK Single 1951-2020")
