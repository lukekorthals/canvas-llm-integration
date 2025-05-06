#R1
hist(sample(8:20, 40, replace = T) * 0.5)

#R2
df <- read.csv("https://raw.githubusercontent.com/hannesrosenbusch/PIPS_DATA/master/schiphol.csv")
plot(df$DATE, df$TAVG)

#R3
library(titanic, warn.conflicts = FALSE)
library(ggplot2, warn.conflicts = FALSE)
ggplot(titanic_train, aes(fill= factor(Survived, labels = c("dead", "alive")), x=Sex))+
  geom_bar() +
  labs(fill = "How did it go?")

#R4
#i like theme_bw(). seems basic

#R5 
plot(cars$speed, cars$dist, 
     main = "Car Speed vs Stopping Distance",
     xlab = "Speed (mph)", 
     ylab = "Stopping Distance (ft)", 
     pch = 19, 
     col = "darkred")
abline(lm(cars$dist ~ cars$speed), col = "blue", lwd = 2)
#added title
#added axis labels with units
#added regression line

#R6
library(ggplot2, warn.conflicts = FALSE)
library(dplyr, warn.conflicts = FALSE)
data.frame(ChickWeight) %>%
  group_by(Chick) %>%
  filter(Chick %in% c('1', '20', '5', '40', '19')) %>%
  summarise(max_weight = max(weight)) %>%
  mutate(chick = factor(Chick, levels=c('1', '20', '5', '40', '19'))) %>%
  ggplot() +
  geom_bar(aes(chick, max_weight), stat = "identity")

#R7
library(ggplot2, warn.conflicts = FALSE)
library(dplyr, warn.conflicts = FALSE)
data.frame(cars) %>%
  ggplot() +
  geom_point(aes(speed, dist)) +
  geom_smooth(aes(speed, dist))

#R8
library(ggplot2)
library(dplyr)
library(patchwork)
par(mfrow = c(2,2))
plot1 <- data.frame(ChickWeight) %>%
  filter(Chick %in% c('1', '20', '5', '40', '19')) %>%
  group_by(Chick) %>%
  summarise(max_weight = max(weight)) %>%
  mutate(chick = factor(Chick, levels=c('1', '20', '5', '40', '19'))) %>%
  ggplot() +
  geom_bar(aes(chick, max_weight), stat = "identity")

plot2 <- data.frame(ChickWeight) %>%
  filter(Chick %in% c('1', '20', '5', '40', '19')) %>%
  mutate(chick = factor(Chick, levels=c('1', '20', '5', '40', '19'))) %>%
  ggplot() +
  geom_line(aes(Time, weight, color = chick)) +
  labs(color = "chick")

plot1 + plot2


#R9
library(ggstatsplot)
ggbetweenstats(data = ToothGrowth, x = supp, y = len)


#R10
library(plotly)
df = read.csv("https://raw.githubusercontent.com/hannesrosenbusch/PIPS_DATA/master/body.csv")
plot_ly(df, x = ~TotalHeight, 
        y = ~HeadCircumference, 
        z = ~ShoulderToWaist, 
        opacity = 0.5,
        type="scatter3d", mode = "markers")

#R11 
#might need gifski package
library(cranlogs)
library(ggplot2)
library(gganimate)
downloads <- cran_downloads(c("ggplot2", "plotly"), from = "2013-08-21", to = "2025-01-01")
p <- ggplot(downloads, aes(date, count, color = package)) + 
  geom_line() +
  theme_bw() +
  labs(y = "Package Downloads", title = "Package popularity over time")+
  transition_reveal(date)
animate(p,  nframes = 100, fps = 10, width = 300, height = 300, end_pause = 70)
anim_save("package_downloads.gif", animation = last_animation())

#R12
library(quantmod)
getSymbols("AAPL", from = '2024-01-01',
           to = "2024-10-31",warnings = FALSE,
           auto.assign = TRUE)

chartSeries(AAPL)
#they made my phoneyy

#R13
library(tidyquant)
plotstock <- function(stocksym="AAPL", year = "2023", filename = "mystock.png"){
  
  my_data <- getSymbols(stocksym, from = paste0(year,'-01-01'),
                        to = paste0(year,'-12-31'),warnings = FALSE,
                        auto.assign = FALSE)
  png(filename)
  print(plot(my_data[,1]))
  dev.off()
}

plotstock("AMZN", "2015")

#R14
#i had unnecessary lines in task 13
# i used = instead of <- a bunch of times

#R15
#functions compares length of input string with some other string. 
#bad var names
#no comments
#only conditional return
#mix of assignment operators
#no indentation

#R16
matrix(1:9, 3, byrow = TRUE) * 1:3

#R17
#ctrl shift a or ctrl i


#R18
devtools::install_github("sctyner/memer")
library(memer)
library(dplyr)

meme_get("DistractedBf") %>% 
  meme_text_distbf("tidyverse", "new R users", "base R")

#Radv1
set.seed(42)
plot(rnorm(1000), rnorm(1000), axes = FALSE, xlab = "", ylab = "", main = "", frame.plot = FALSE)

#Radv2
# i like animals
cowsay::say("moo", "cow")

