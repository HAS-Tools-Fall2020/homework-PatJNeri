Patrick Neri; 9/13/2020 Assignment #3

# Homework #3
*by Patrick Neri*

---------
# Grade

2/3 - Really great job on the analysis and the forecast. I subtracted 1 point because you didn't answer the four questions in the assignment. Next time just make sure you include your answers to those too. 

---

### Approach
In this weeks homework, we were allowed to introduce base levels of python coding into
our method. When looking at the original code that we were provided, I noticed a few areas where my approach was flawed.

### Flaws
One major difficulty I realized was the ability to accurately visualize the large amount of data. When I had previously looked at graph displays, my sectioning of the data was unable to represent the true variety of values that were achieved. Looking at the min and max of the data set quickly drove that home.

The other major flaw that I found was although my first approximation on the average of the overall dataset was relatively accurate, it factored in the major outliers in the data, which although occurring frequently, are very misleading in getting an accurate prediction of what an average days reading may be.

### Solutions
The first thing was to narrow down what a better average day prediction may be by cutting down on the outliers. To do this, I created a new list which grabbed all the data points that were below the total flow data's average.

Doing this and looking at the length of the new list shows that over **87%** of days are below this average. Even more so, finding the mean of this new list produced a value of around 114 with a STD of 67. This gave me a new average to make variations to.

The other way I adjusted my strategy was to just find the data from the previous year, and looking at that data, pick some weeks that seemed more likely, historically speaking, to be a part of the 13% of days who went above this average.

## Summary
This strategy produced results that seem to be more consistent with previous data, but at the end of the day they are still just better informed guesses.

### Potential Improvement
One easy way I could improve the results is by first comparing each year overall and seeing if any noticeable trends occur. Then, depending on the results of that analysis, either take the averages of the days in question for each previous year and make that the guess, or make some kind of linear regression model or presumed statistical occurrence.  
