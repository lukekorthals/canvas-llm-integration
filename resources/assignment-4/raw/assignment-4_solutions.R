#R1
library(data.table)
library(dplyr)
df1 <- fread("https://raw.githubusercontent.com/hannesrosenbusch/PIPS_DATA/refs/heads/master/A.csv") %>% 
  filter(rowSums(is.na(.)) <= 15)
df2 <- fread("https://raw.githubusercontent.com/hannesrosenbusch/PIPS_DATA/refs/heads/master/B.csv")
boxplot(df2$funniness_rating~ df2$stimulus, 
        las = 2, xlab = NULL,
        main = "funniness of stimuli")

#R2
df = plyr::rbind.fill(list(df1, df2)) %>%
  mutate(age = ifelse(is.na(age), mean(age, na.rm = TRUE), age)) %>%
  group_by(userid) %>%
  filter(length(unique(funniness_rating)) != 1) %>% 
  ungroup()

library(ggplot2)
library(ggside)
ggplot(df, aes(age, funniness_rating)) +
  geom_smooth(method = "lm", formula = 'y ~ x') +
  geom_xsidedensity(aes(y   = after_stat(density)))

rm(list = c("df1", "df2"))

#R3
library(dplyr)
library(tidyr)
library(corrplot)
moods = df %>% 
  group_by(userid) %>% 
  slice(1) %>% 
  ungroup() %>%
  select(starts_with("mood_")) %>%
  rename_all(~gsub("mood_", "", .)) %>%
  select(order(cor(.)[,"upset"]))
  
cor(moods) %>%
  corrplot()

#R4
library(randomNames)
set.seed(1)
randos = randomNames(nrow(moods), sample.with.replacement = F)

moods = moods %>%
  mutate(userid = randos)  %>%
  pivot_longer(-userid, names_to = "mood", values_to = "score")

mood_percentile = function(participant_id, df = df){
  if(! participant_id %in% df$userid){
    stop("didnt find id in column user_id")
    }
  
   temp = df %>%
     group_by(mood) %>%
     mutate(perc = 100* ecdf(score)(score)) %>%
     ungroup() %>%
     filter(userid == participant_id) %>%
     filter(perc == max(perc))

  return(paste(participant_id, "scores the highest on mood: ", temp$mood, " ( percentile:", temp$perc, ")" ))
}

mood_percentile("al-Farrah, Ali", moods)

#R5
library(DataExplorer)
create_report(df, y = "funniness_rating")

#R6
#no example solution provided

#R7
#no example solution provided

#R8
#no example solution provided

#Radv1
#no example solution provided