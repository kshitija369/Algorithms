
dataset = data.frame(v1 = as.numeric(), v2=as.numeric(), v3=as.numeric())

y = c(0,0,0,0,0,0,1,1,1,1,1,1)
dataset = rbind(dataset, c(1,2,0))
dataset = rbind(dataset, c(2,2,0))
dataset = rbind(dataset, c(2,2,0))
dataset = rbind(dataset, c(2,1,1))
dataset = rbind(dataset, c(0,2,1))
dataset = rbind(dataset, c(2,1,0))

dataset = rbind(dataset, c(0,1,2))
dataset = rbind(dataset, c(1,1,1))
dataset = rbind(dataset, c(1,0,0))
dataset = rbind(dataset, c(0,0,2))
dataset = rbind(dataset, c(1,0,2))
dataset = rbind(dataset, c(0,1,0))

# Calculate mean vector
m0 = colMeans(dataset[which(y==0),])
m1 = colMeans(dataset[which(y==1),])

print("Full Solution")
print("m0: ")
print(m0)

print("m1: ")
print(m1)

cal_var = function(x, m){
  x1 = matrix((x-m), nrow = 3, ncol = 1, byrow = TRUE)
  x2 = matrix((x-m), nrow = 1, ncol = 3, byrow = TRUE)
  return(x1%*%x2)
}

# log likelihood
cal_likelihood = function(x, m, var_){
  x1 = matrix((x-m), nrow = 1, ncol = 3, byrow = TRUE)
  x2 = matrix((x-m), nrow = 3, ncol = 1, byrow = TRUE)
  
  var_ = solve(var_)
  return(-(x1%*%var_%*%x2))
}

# Calculate variance
var0 = matrix(rep(0,3*3), nrow = 3, ncol = 3)
for(t in 1:6){
  var = cal_var(as.numeric(dataset[t,]), m0)
  var0 = var0 + var
}
var0 = var0 / 6

var1 = matrix(rep(0,3*3), nrow = 3, ncol = 3)
for(t in 7:12){
  var = cal_var(as.numeric(dataset[t,]), m1)
  var1 = var1 + var
}
var1 = var1 / 6

print("var0")
print(var0)

print("var1")
print(var1)

# Classify using log likelihood
# (1,2,1)
LL_C0 = cal_likelihood(c(1,2,1), m0, var0)

LL_C1 = cal_likelihood(c(1,2,1), m1, var1)

if(LL_C1 > LL_C0){
  print("(1,2,1): Class 1")
}else{
  print("(1,2,1): Class 0")  
}

# (0,0,1)
LL_C0 = cal_likelihood(c(0,0,1), m0, var0)

LL_C1 = cal_likelihood(c(0,0,1), m1, var1)

if(LL_C1 > LL_C0){
  print("(0,0,1): Class 1")
}else{
  print("(0,0,1): Class 0")  
}

### Nearest mean solution
print("")
print("Nearest mean Solution")
print("m0: ")
print(m0)

print("m1: ")
print(m1)

print("var0: ")
print(diag(var0))
print("var1: ")
print(diag(var1))

var0_nn = 0
for(t in 1:6){
  var = (as.numeric(dataset[t,]) - m0)^2
  var0_nn = var0_nn + var
}
var0_nn = var0_nn / 6

var1_nn = 0
for(t in 1:6){
  var = (as.numeric(dataset[t,]) - m1)^2
  var1_nn = var1_nn + var
}
var1_nn = var1_nn / 6

print("var0_nn: ")
print(var0_nn)
print("var1_nn: ")
print(var1_nn)

x = c(1,2,1)
print(paste("x", x))
LL_0 = -sum((x - m0)^2 / diag(var0))/2
LL_1 = -sum((x - m1)^2 / diag(var1))/2
print(paste("LL_0: " , LL_0 , "    LL_1: " , LL_1))
if(LL_1 > LL_0){
  print("(1,2,1): Class 1")
}else{
  print("(1,2,1): Class 0")  
}

x = c(0,0,1)
print(paste("x", x))

LL_0 = -sum((x - m0)^2 / diag(var0))/2
LL_1 = -sum((x - m1)^2 / diag(var1))/2

print(paste("LL_0: " , LL_0 , "    LL_1: " , LL_1))
if(LL_1 > LL_0){
  print("(0,0,1): Class 1")
}else{
  print("(0,0,1): Class 0")  
}


x = c(1,2,1)
print(paste("x", x))
LL_0 = -sum((x - m0)^2 / var0_nn)/2
LL_1 = -sum((x - m1)^2 / var1_nn)/2
print(paste("LL_0: " , LL_0 , "    LL_1: " , LL_1))
if(LL_1 > LL_0){
  print("(1,2,1): Class 1")
}else{
  print("(1,2,1): Class 0")  
}

x = c(0,0,1)
print(paste("x", x))

LL_0 = -sum((x - m0)^2 / var0_nn)/2
LL_1 = -sum((x - m1)^2 / var1_nn)/2

print(paste("LL_0: " , LL_0 , "    LL_1: " , LL_1))
if(LL_1 > LL_0){
  print("(0,0,1): Class 1")
}else{
  print("(0,0,1): Class 0")  
}


x = c(1,2,1)
print(paste("x", x))
LL_0 = -sum((x - m0)^2)
LL_1 = -sum((x - m1)^2)
print(paste("LL_0: " , LL_0 , "    LL_1: " , LL_1))
if(LL_1 > LL_0){
  print("(1,2,1): Class 1")
}else{
  print("(1,2,1): Class 0")  
}

x = c(0,0,1)
print(paste("x", x))

LL_0 = -sum((x - m0)^2)
LL_1 = -sum((x - m1)^2)

print(paste("LL_0: " , LL_0 , "    LL_1: " , LL_1))
if(LL_1 > LL_0){
  print("(0,0,1): Class 1")
}else{
  print("(0,0,1): Class 0")  
}