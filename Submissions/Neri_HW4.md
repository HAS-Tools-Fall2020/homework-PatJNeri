Patrick Neri; 9/20/2020 Assignment #4

# Homework #4
*by Patrick Neri*

___
### Grade
3/3 - nice job, we will be getting to plotting soon don't worry. Also you can use an atom plugin to add images to your markdown. instructions are included in next weeks assignment. 
___


## In this week
### We utilized histograms to see more frequent values and trends.
This showed more visibly what I saw previously, and allowed the picture to display what my eyeballs and numbers could not.
The difficulties with using the data in this way were also very clear. A lack of obvious signal as to when the data was from prevented any kind of
noticing in trends over time. Instead, this method suggests, unfairly, of a uniformity to the history and ongoing changes in the conditions producing these values.
### Things to improve.
Finding a way to use graphical functions to clarify trends over time would help. Also figuring out how to properly add a .jpg to a markdown so I can do my homework would be helpful.
Better yet, find a better way to divide the data into week subsets so that more accurate time specific statistics can be preformed.
1.  This week played into the previous observations that I made last week. When looking at a histogram of the total dataset, it is clear that outliers make the mean, when taken over a large scale, very misleading.
    Looking at the quantile makes it more clear, as 90% of the stream flow data is less then 479.8, yet the mean is very close at 346.1. I found the % chance a value in a month went above its historical mean, and
    based my guess off of that, and what appeared to be the most common value in the histogram.
2.  The variable flow_data is a **2D array** made up of the data taken from our chosen site. It is made up of **4 1D arrays, 3 of which are integers (year, month, day) and one of float (flow data)**.
    The dimensions are **4 columns and 11572 rows** (for the dataset I used), with a total size of **46288**.
3.  Not sure if you are asking for each of my values for this or what, but for my week 1 prediction of 59, there were 899 times it was higher, or 96% of the time. I still picked this due to a low 0.5 quartile and
    recent low amount values. For week 2 and a guess of 84, there were 764 times, or 81%. I went higher due to it being close to October, where we see higher values more frequently, but still low because drought?
4.  Up until 2000, out of 360 days, 328 of them were above my guess of 84 (91%) and for 59 all of them were higher (100%). After 2010, for my 84 guess there were 236 times (78.6%), and for my 59 guess there were
    288 times (96%). For both of these, it does make me consider raising the values. However within the last 2 months low values overall have occurred, making me fine with it.
5. The second half clearly has a more defined common low flow value, around 85, where as the first half is more varied with values that don't have a clearly obvious most common value.
