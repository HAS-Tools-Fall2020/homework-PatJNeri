Patrick Neri HW8 Code Review

## Homework #8

#### Greetings!!
This is a file to help navigate my program.

So email me if you have any other questions:
 **pjneri@email.arizona.edu**

 Feel free to run all of the script, and steal my plotting function of the months for the
 past 30 years. It is rather interesting!

In order to get the proper 16 week prediction, make the adjustment of the text file in ln 66 to 'streamflow_week1'
If you wish to get the more accurate 2 week prediction, utilize a more recent streamflow dataset.
Things to change:
ln 91 : You can look at any specific month over the past 30 years, starting at 1991 till 2020. It's interesting to see what months saw more flow then others.
ln 129, 130 : Adjust the training dates for model 1
ln 156, 157 : Adjust the xlim to match the dates chosen in ln 129, 130
ln 213, 220, 227 : Make sure that the date is large enough to show all relevant data.
ln 231 : Adjust to chosen relevant dates for model 2 (Recommend 2020 only)

 ### Make sure to run the stream flow from 1989-1-1 to align the dates properly!!

 Again, reach out if things don't work.

 1. So I noted that 2020 is just different in the scheme of things, and so I made a Linear Autoregression model based on 2020 data.
 2. I did end up using my model for the values. In the long run, at this point every year we begin to see an uptick in flow spikes. This type of model in the long run is unable to get an accurate number, but I felt I would leave it up to math this week instead of guessing.
 3. The peer evaluation pointed out how I can improve the aspects of my ReadMe documents. In terms of my script, we came up with some things in terms of graphs I could add, such as the final plot.
 4. I am definitely most proud of my large plot in cell 9. Although I haven't quite resolved the x labels, I love how it clearly indicates the differences of this period year from year.
