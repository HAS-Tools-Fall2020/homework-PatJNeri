Patrick Neri; 9/27/2020 Assignment #5

# Homework #5
*by Patrick Neri*

As we didn't have very much new information, I took some ideas of the previous weeks concepts. The major difficulty that I ran into was finding a quick way to summarize and call data, which I know comes with practice. What I ended up doing, since I didn't change my method very much, was to call last years flow values at the start of every week and average it with my previous predictions.

## Things I should do better
For the above line of thinking, obviously it would have worked better if I had taken the value of each week last year and averaged them, then compared that with my guesses, but I still found this difficult. Also, taking these week values, I can compare them to the average value over all the years we have data, and if last year was am outlier (not sure yet how you would want to define that), then you could default to an overall average for that week. Further still, I wanted to do multiple plots whereby you stack multiple year separated times on each other, to give a graphical image of if there has been massive variations of flow values for the dates in question.

1.   Column Names in order are: **agency_cd, site_no, datetime, flow, code, year, month, day**.
The index ranges from **0 to 11563** for my dataset. The data types in order are: **object, int64, object, float64, object, int32, int32, int32**.
2.   flow.min = 19.0; flow.mean = 346.33; flow.max = 63400; flow.std = 1412.466; flow.quartiles = 94.0, 158.0, 216.0;
3.   
| Month | Min | Mean | Max | STD | 25% | 50% | 75% |
| ----------- | ----------- || ----------- | ----------- || ----------- | ----------- |
| Jan | 158 | 706.32 | 63400 | 2749.15 | 202 | 219 | 292 |
| Feb | 136 | 925.25 | 61000 | 3348.82 | 201 | 244 | 631 |
| Mar | 97 | 941.73 | 30500 | 1645.80 | 179 | 387 | 1060 |
| Apr | 64 | 301.24 | 4690 | 548.14 | 112 | 142 | 214.5 |
| May | 46 | 105.44 | 546 | 50.77 | 77.97 | 92.95 | 118 |
| June | 22.1 | 65.99 | 481 | 28.96 | 49.22 | 60.5 | 77 |
| July | 19 | 95.57 | 1040 | 83.51 | 53 | 70.9 | 110 |
|Aug|29.6|164.57|5360|274.69|76.55|114.5|170.75|
|Sept|48.6|176.02|5590|290.05|90|122|173|
|Oct|69|146.16|1910|111.77|107|125|153|
|Nov|117|205.10|4600|235.67|156|175|199|
|Dec|155|337.09|28700|1097.28|191|204|228|

4.    **Lowest**
| # | Flow| Date |
| ---- | ---- | ---- |
|1|19.0|2012/7/1|
|2|20.1|2012/7/2|
|3|22.1|2012/6/30|
|4|22.5|2012/6/29|
|5|23.4|2021/7/3|

  **Highest**

  | # | Flow| Date |
| ---- | ---- | ---- |
|1|63400|1993/1/8|
|2|61000|1993/2/20|
|3|45500|1995/2/15|
|4|35600|2005/2/12|
|5|30500|1995/3/6|

5.   | Month | Min| Max |
| ---- | ---- | ---- |
|1|158 @ 2003|63400 @ 1993|
|2|136 @ 1991|61000 @ 1993|
|3|97 @ 1989|30500 @ 1995|
|4|64.9 @ 2018|4690 @ 1991|
|5|46 @ 2004|546 @ 1992|
|6|22.1 @ 2012|481 @ 1992|
|7|19 @ 2012|1040 @ 2006|
|8|29.6 @2019|5360 @ 1992|
|9|48.6 @ 2019|5590 @ 2004|
|10|69.9 @ 2012|1910 @ 2010|
|11|117 @ 2016|4600 @ 2004|
|12|155 @ 2012|28700 @ 2004|

6.   I found this difficult to achieve because I was unsure how to set upper and lower bounds in a conditional statement when pulling values from the data["flow"] column. Sorry!
