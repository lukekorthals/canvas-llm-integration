
#R1
meryls_oscars <- 3
meryls_losses <- 18
best_actress <- "Meryl Streep"

if (best_actress == "Meryl Streep") {
  meryls_oscars <- meryls_oscars + 1
} else {
  meryls_losses <- meryls_losses + 1
}

#R2
box_hist <- function(vec) {
  if (runif(1) < 0.5) {
    boxplot(vec, main = "Boxplot", col = "lightblue")
  } else {
    hist(vec, main = "Histogram", col = "lightgreen", border = "white")
  }
}

#R3
# old function
box_hist <- function(vec) {
  if (runif(1) < 0.5) {
    boxplot(vec, main = "Boxplot", col = "lightblue")
  } else {
    hist(vec, main = "Histogram", col = "lightgreen", border = "white")
  }
}

# new function
box_hist <- function(vec) {
  if (runif(1) < 0.5) boxplot(vec) 
  else hist(vec)
}

#R4
# never prints "Boss blew of his bike...." as `predicted != actual` & `predicted == actual` covers all
# possible outcomes AND they come before `actual == "high wind"` in the if statement.
# Logical statements are always checked in order in if statements.

# improved code
predicted <- "rain"
actual <- "rain"
employee_salary <- 54000

if (actual == "sun") {
  print("Yay! Birthday moved outside!")
} else if (actual == "high wind") {
  print("Boss blew off his bike into a canal.")
} else if (predicted != actual) {
  employee_salary <- employee_salary - 500
} else if (predicted == actual) {
  employee_salary <- employee_salary + 500
} 

#R5
# It only uses the first element of these_numbers as the comparison in the
# if-statement
these_numbers <-  runif(100, min=-0.01, max=100)
they_are_negative <-  FALSE
if (any(these_numbers < 0)) {
  they_are_negative <- TRUE
}

#R6
curr_time = as.POSIXlt(Sys.time())
if (curr_time$hour >= 0 & curr_time$hour < 5) {
  print("Go to sleep!")
}

#R7
clinical_data <- read.csv("https://raw.githubusercontent.com/hannesrosenbusch/schiphol_class/master/Kaggle_Dataset_Mental_Disorders.csv")
clinical_data$Depletedness <- 0.5 * clinical_data$Sadness + 
  -0.8 * clinical_data$Euphoric + 
  0.3 * clinical_data$Exhausted

cutoff <- quantile(clinical_data$Depletedness, 0.9)
summary(clinical_data$Depletedness)

clinical_data$Outlying <- ifelse(clinical_data$Depletedness > cutoff, 
                                 TRUE, FALSE)


#R8
#loop 1
for (col_name in colnames(clinical_data)) {
  if (col_name == "Sexual.Activity") {
    print("Private information")
    next
  }
  print(paste(col_name, "is of type", class(clinical_data[[col_name]])))
}

#loop 2
for (i in 1:nrow(clinical_data)) {
  # Check conditions for postponing assessment
  if (clinical_data$Authority.Respect[i] == "NO" && clinical_data$Aggressive.Response[i] == "YES") {
    print("Assessment postponed")
    break
  }
  print(paste("Patient.Number", clinical_data$Patient.Number[i], "assessed successfully"))
}

#R9
set.seed(1)
co2_values = c()
while(length(co2_values) < 1000){
  sample = 121
  while(sample > 120){
    sample = rnorm(1, 100, 15)
  }
  co2_values = c(sample, co2_values)
}

library(ggplot2)
ggplot() + 
  geom_histogram(aes(co2_values)) + 
  theme_bw() + 
  labs(title = "1000 survivors")


#R10
weird_fibonacci <- c(0, 3)

for (i in 3:10) {
  next_element <- 3 * weird_fibonacci[i - 2] + weird_fibonacci[i - 1]
  weird_fibonacci <- c(weird_fibonacci, next_element)
}


#R11
# my game simulates die throws and sees whether all are same
# game name: dice
outcomes = c()
for(i in 1:1000){
  dice <- sample(1:6, 3, replace = TRUE)
  if(sd(dice) > 0) {
    outcomes = c(outcomes, -5)
  }else{
    outcomes = c(outcomes, 50)
  }
}
mean(outcomes)

#R12
these_numbers <- c(1, 3.1, 5.2, -1, 5.2)
# Good code below, note we changed "i" to these_numbers[i]
maximum <- numeric()
for (i in 1:length(these_numbers) ) {
  if (sum(these_numbers > these_numbers[i]) == 0) {  # Note the change here
    maximum <- c(maximum, these_numbers[i])
  }
}

#R13
end_time <- as.POSIXct("2040-01-01 00:00:00")

while (Sys.time() < end_time) {
  print(Sys.time())
  Sys.sleep(1800) # Sleep for 30 minutes
}

#R14
verhulst <- function(x, rate_in, cap) {
  rate_in * x * (cap - x) / cap  # Note that return is optional here
}

rabbits <- c(.001)
rate <- 2
capacity <- 1000

for (time in 2:50) {
  rabbits[time] <- verhulst(rabbits[time - 1], rate, capacity)
}

plot(rabbits, type='l', xlab='time', bty='n')


#R15
an_array <- array(NA, dim=c(4, 50, 3))
for (i in 1:length(an_array[1, , 1])) {
  an_array[, i, ] <- rnorm(n = 12, mean = i, sd = 1) #fill with that index as mean
}

#R16
# my 3d array from R15
an_array <- array(NA, dim=c(4, 50, 3))
for (i in 1:length(an_array[1, , 1])) {
  an_array[, i, ] <- rnorm(n = 12, mean = i, sd = 1) #fill with that index as mean
}

# calculating minimum value
min_matrix <- apply(an_array, 1, min)

#R17
# a) it is NULL as no case matches the string "shoe"
# b) it can either be "perch" or "carp", the latter because empty argument
#    assignments in `switch()` default to the next defined argument


#R18
# By setting pos = 1 rm() removes the provided object from the global environment and 
# not the local context of the function. Therefore the function removes itself.

#R19
p_values <- sapply(t_tests, function(test) test$p.value)

#R20
bugged_function = function(inpt){
  if (!is.numeric(inpt)){
    warning("Why no numbers?")
  }
  print(rep(inpt, each = 3))
  return(as.character(inpt))
}
# call `debug()` on it
debug(bugged_function)
# execute the function
bugged_function(1:3)
# undebug the function
undebug(bugged_function)


#R21
special <- function(x) {
  if (is.vector(x) != TRUE) {
    stop("Input for `special` has to be a vector")
  }
  spec <- numeric()
  for (i in 1:length(x)) {
    if (any(x[i] == spec) == FALSE) {
      spec <- c(spec, x[i])
    }
  }
  if (length(x) == length(spec)) {
    warning("All values are special!")
  }
  return(spec)
}

my_vec <- sample(100, 50, replace = TRUE)
special(my_vec) # Visual comparison
unique(my_vec)  # Visual comparison
# check, has to be TRUE if all values are indeed the same
all(unique(my_vec) == special(my_vec))  
special(data.frame(c(1, 2, 2)))     # The error message works
special(c(1, 3, 5, 6, 8))             # warning works
special(sample(5, 10, replace = TRUE)) # doesn't give warning when it shouldn't

#R22 
quicksortof <- function(to_sort) {
  to_sort <- c(max(to_sort),to_sort,min(to_sort))
  print("I tried my best to quicksort!")
  return(to_sort)
}

#R23
# All this function really does is return a vector of strings ("blue", " green")
# If grass is defined as something else in the global environment, then it will
# return a list with whatever grass is in the second element.

# The value of grass will stay green in the global environment.
# Even though grass is defined locally in the function later as "blue"

#R24 
# The function does not work when sourced because the global variable grass does 
# not exist.

# my fixed function inside the new .R file
colorit <- function(color_me, grass_me) {
  grass_me <- "green"
  color_me <- "blue"
  colorful_items = c(color_me, grass_me)
  return(colorful_items)
}

#R25 
# A recursive function that calculates the factorial of a given number (integer)
get_factorial <- function(n){
  if(n == 0) {
    return(1)
  } else {
    return(n * get_factorial(n - 1))
  }
}

#Radv1 
# Load the word list
five_letter_words <- readLines("https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt")  # Ensure the file is in the working directory


# Function to simulate monkey typing random 5-letter sequences
simulate_monkey_typing <- function() {
  alphabet <- c(letters, " ")  # Letters + space
  typed_sequence <- ""
  count <- 0
  
  # Keep typing until a valid 5-letter word is formed
  while (TRUE) {
    count <- count + 1
    # Generate a 5-letter sequence
    sequence <- paste(sample(alphabet, 5, replace = TRUE), collapse = "")
    # Check if the sequence is a valid 5-letter word
    if (sequence %in% five_letter_words) {
      return(count)  # Return the number of sequences typed before a valid word
    }
  }
}

# Run the simulation 100 times
set.seed(42)  # For reproducibility
results <- replicate(100, simulate_monkey_typing())

# Summarize the results
mean_sequences <- mean(results)
sd_sequences <- sd(results)

cat("Mean number of sequences:", mean_sequences, "\n")
cat("Standard deviation:", sd_sequences, "\n")

# Plotting the results
library(ggplot2)

# Convert results to a data frame
results_df <- data.frame(sequences = results)

# Create a boxplot to show the spread
ggplot(results_df, aes(y = sequences)) +
  geom_boxplot(fill = "lightblue", color = "black") +
  labs(title = "Boxplot of Sequences Before Valid Word",
       y = "Number of Sequences") +
  theme_minimal() +
  theme(text = element_text(size = 12))


#Radv2
# I created a package to add a gap to the y axis of a ggplot
devtools::install_github("lukekorthals/gg-ygap")
pradv2 = cars %>%
  ggplot(aes(x=dist, y=speed)) +
  geom_point() +
  theme_classic()
# add the break
ggygap::gg.y_gap(pradv2, 4, max(cars$speed), 1)

