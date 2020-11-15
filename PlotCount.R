
library(reshape2)
library(tidyverse)
library(ggplot2)

QFOnum = 13
ReptileNum= 18
LizardNum=4
VsnakeNum=12
NonvenomousNum=2
total = QFOnum + ReptileNum+ LizardNum+ VsnakeNum + NonvenomousNum
#read in data
FamilyCounts= as.data.frame(read.csv("E:/work/hons/SnakeVenom-Feb20/Analysis/FamilyCountsV5/totalCountsV2.txt",header = FALSE, sep = "\t"))
#rename colomuns
names(FamilyCounts)[1] <- "Family"
names(FamilyCounts)[2] <- "Total"
names(FamilyCounts)[3] <- "Venomous"
names(FamilyCounts)[4] <- "Non_venomous"
names(FamilyCounts)[5] <- "Lizard"
names(FamilyCounts)[6] <- "QFO"
summary(FamilyCounts)
#remove total for plotting
withoutTotal<-subset(FamilyCounts,select= -c(Total))
#calculate difference in QFO and reptile
averageCounts <- withoutTotal
averageCounts$Venomous <- averageCounts$Venomous/VsnakeNum
averageCounts$Non_venomous <- (averageCounts$Non_venomous)/NonvenomousNum
averageCounts$Lizard <- averageCounts$Lizard/LizardNum
averageCounts$QFO <- averageCounts$QFO/QFOnum
averageCounts$diff= averageCounts$Venomous-averageCounts$QFO
summary(averageCounts)


summary(FamilyCounts$Total)/31
summary(FamilyCounts$Venomous)/12
summary(FamilyCounts$`Non_venomous`)/2
summary(FamilyCounts$Lizard)/4
summary(FamilyCounts$QFO)/13

#order
averageCounts <- averageCounts %>% arrange(diff)
#t.test(averageCounts$Reptile,averageCounts$QFO)
withoutTotal.m =0
#Melt together for multi plot
FamilyCounts.m <- melt(FamilyCounts,id.vars='Family', measure.vars=c('Total','Venomous','QFO',"Non_venomous","Lizard"))
withoutTotal.m <- melt(withoutTotalSort,id.vars='Family', measure.vars=c('Venomous','QFO',"Non_venomous","Lizard"))
averageCounts.m <- melt(averageCounts,id.vars='Family', measure.vars=c('Venomous','QFO',"Non_venomous","Lizard"))
total <- merge(averageCounts.m,averageCounts,by="Family")

#plot boxplot
p <- ggplot(FamilyCounts.m) +
  geom_boxplot(aes(x=variable, y=value,))+ 
  #geom_boxplot(width=1) +
  #ylim(15000, 28000)+
  #xlim(-1,1)+
  #theme(axis.text.x= element_text(size = 0))+
  labs(x="Protein dataset", y = "Number of protiens in a family")
  #geom_text(label=FamilyCounts.m$Family,hjust = 0,size = 3.5, nudge_x = 0.1)+
  #geom_dotplot(aes(x=variable, y=value),binaxis='y',binwidth = 1, stackdir='center', dotsize=15)
p
#plot dot plot
X <- ggplot(FamilyCounts.m)+
  geom_dotplot(aes(x=Family, y=value, color = variable),binaxis='y',binwidth = 1, stackdir='center', dotsize=20)+
  theme(axis.text.x= element_text(angle = 90, size = 5))

X
#plot ordered do plot 
y <- ggplot(FamilyCounts.m)+
  geom_dotplot(aes(x=reorder(Family,diff), y=value, color = variable),binaxis='y',binwidth = 1, stackdir='center', dotsize=2)+
  theme(axis.text.x= element_text(angle = 90, size = 5,vjust = 0.2, hjust = 0.95))+
  labs(x="Protien family", y = "Average number of protiens", color ="Protien set")

y  
#dot plot with axis flipped
flip <- ggplot(total)+
  geom_point(aes(y=reorder(Family,diff), x=value, shape = variable, color = variable))+
  theme(axis.text.y= element_text(angle = 0, size = 7,vjust = 0.2, hjust = 0.95))+
  theme(axis.text.x= element_text(angle = 0, size = 7,vjust = 0.2, hjust = 0.95))+
  labs(y="Protien family", x = "Average number of protiens per species", color ="Protien set", shape = "Protien set")

flip 
flip <- ggplot(total)+
  geom_point(aes(y=reorder(Family,diff), x=value,  colour = variable, shape = variable))+
  theme(axis.text.y= element_text(angle = 0, size = 7,vjust = 0.2, hjust = 0.95))+
  labs(y="Protien family", x = "Average number of protiens per group ", color ="Protien set", shape = "Protien set")

flip 

y <- ggplot(total)+
  geom_dotplot(aes(x=reorder(Family,diff), y=value, color = variable),binaxis='y',binwidth = 1, stackdir='center', dotsize=2)+
  theme(axis.text.x= element_text(angle = 90, size = 5,vjust = 0.2, hjust = 0.95))+
  labs(x="Protien family", y = "Average number of protiens", color ="Protien set")
  #coord_flip()
y  

colnames(averageCounts)
averageCounts$ratio
ratio <- ggplot(averageCounts)+
  geom_dotplot(aes(y=reorder(Family,ratio), x=ratio, shape=factor(ifelse(ratio == 2.5,1,2))),binaxis='y',binwidth = 1.5, stackdir='center', dotsize=.5)+
  theme(axis.text.y= element_text(angle = 0, size = 5,vjust = 0.2, hjust = 0.95))+
  labs(y="Protien family", x = "log2 Ratio of average number \n of QFO to Reptile proteins \n per group", color ="Protien set")+
  xlim(-1.5,2.5)+
  scale_shape_manual(values=c(3, 16, 17))
  

ratio

summary((FamilyCounts$Total))


s <- read.csv("E:/work/hons/SnakeVenom-Feb20/Analysis/2020-07-30.SpeciesCounts/speciesCounts.csv")
species = c("ANOCA","BOACO","CROVV","DEIAC","DOPGR","HYDCUR","NAJNA","NOTSC","OPHHA","PANGU","POGVI","PROFL","PROMU","PSETE","PYTBI","THAEL","THASI","VARKO","BOVIN","CANLF","CHICK","DANRE","GORGO","HUMAN","LEPOC","MONDO","MOUSE","ORYLA","PANTR","RAT","XENTR")
names
speciesNums <- s[,seq(2, ncol(s), 2)]
ggplot(data = melt(speciesNums), aes(y=variable, x=value)) + geom_boxplot(aes(fill=variable))



scaffs <-  read.csv("E:/work/hons/SnakeVenom-Feb20/Analysis/2020-07-27.ScaffoldCountV2/joinedSummary.txt", header = FALSE)
Snakes = c("PSETE","CROVV","HYDCUR","NOTSC","NAJNA","BOACO")
scaffs.m <- melt(scaffs)  #the function melt reshapes it from wide to long
scaffs.m$rowid <- Snakes

scaffs.g <- scaffs.m %>% group_by(rowid, value)
  

ggplot(scaffs.m)+ 
  #geom_boxplot(aes(x=rowid, y=value))+
  geom_dotplot(aes(x=rowid, y=value),binaxis='y',binwidth = 1, stackdir='center', dotsize=.1)+
  ylim(0,10)

ggplot(scaffs.m, aes(x=rowid, y=value))+
  geom_bar(stat="identity", position=position_dodge())


p <- ggplot(FamilyCounts.m) +
  geom_boxplot(aes(x=variable, y=value,))+ 
  #geom_boxplot(width=1) +
  #ylim(15000, 28000)+
  #xlim(-1,1)+
  #theme(axis.text.x= element_text(size = 0))+
  labs(x="Protein dataset", y = "Number of protiens in a family")
#geom_text(label=FamilyCounts.m$Family,hjust = 0,size = 3.5, nudge_x = 0.1)+
#geom_dotplot(aes(x=variable, y=value),binaxis='y',binwidth = 1, stackdir='center', dotsize=15)
p
       


barData <-  read.table("E:/work/hons/SnakeVenom-Feb20/Analysis/2020-07-27.ScaffoldCountV2/2020-08-03.SummaryBoxData.txt", header = TRUE)
names(barData)[2] <-1
names(barData)[3] <-2
names(barData)[4] <-3
names(barData)[5] <-4
names(barData)[6] <-5
names(barData)[7] <-6
names(barData)[8] <-7
names(barData)[9] <-8
names(barData)[10] <-9
cbbPalette <- c("#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00")
barData.m <- melt(barData)
#barData.m$variable<-as.numeric(levels(barData.m$variable))[barData.m$variable]
ggplot(barData.m, aes(x=variable, y=value,color=Species, fill=Species))+
  geom_bar(stat="identity", position=position_dodge(),)+
  labs(x="Number of homologs on scaffold", y = "Number of occurances")
  



subFamily<- read.csv("E:/work/hons/SnakeVenom-Feb20/Analysis/FamilyCountsV5/2020-10-04.Q90392.count.Families.csv", header = TRUE)


ggplot(subFamily, aes(x=Size, y=reorder(Family,order)))+
  geom_bar(stat="identity", position=position_dodge(),)+
  theme(axis.text.y= element_text(angle = 0, size = 7,vjust = 0.2, hjust = 0.95))+
  labs(x="Number of members", y = "Subfamily")




averageCounts.m <- melt(averageCounts,id.vars='Family', measure.vars=c('Venomous','QFO'))
total <- merge(averageCounts.m,averageCounts,by="Family")


flip <- ggplot(total)+
  geom_point(aes(y=reorder(Family,diff), x=value,  colour = variable, shape = variable))+
  theme(axis.text.y= element_text(angle = 0, size = 7,vjust = 0.2, hjust = 0.95))+
  labs(y="Protien family", x = "Average number of proteins per species ", color ="Protein set", shape = "Protein set")

flip 



subFamily<- read.csv("E:/work/hons/SnakeVenom-Feb20/Analysis/FamilyCountsV5/2020-11-08.PLA2.count.Families.csv", header = TRUE)
ggplot(subFamily, aes(x=Size, y=reorder(Family,order)))+
  geom_bar(stat="identity", position=position_dodge(),)+
  labs(x="Number of members", y = "Subfamily")


