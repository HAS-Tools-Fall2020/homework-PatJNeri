# Homework #14
*by Patrick Neri*

## Grade
3/3 - nice work.

### Attempting to understand other humans: A Journey

So in this week we were tasked to find a paper with an open source code and try and replicate
the output of that code in a timely manner. In class I predicted that there would be 3 people
capable of doing it. I can now see why you were doubtful.

1. The first thing that I noticed is the span of papers written in other languages, or sometimes
in what seems like completely proprietary web based formats that to me seemed wholly unreadable.
It took me probably 20 minutes to find my first paper that actually used python, and it was a
really ugly format. I continued to search however, which is probably where I will differ from
some in the class who may have just tried with the first applicable paper since finding it in the first place is such a chore.

2. The paper I did end up finding, from a Nature publication, is very well organized. The paper was on the "Estimation of global tropical cyclone wind speed probabilities using the STORM dataset" by Bloemendaal et al. (2020). [Paper](https://www.nature.com/articles/s41597-020-00720-x#code-availability) They broke up the code into three different Github repos and had the dataset they used separate and downloadable as a ZIP. All of it was clearly labelled and the steps to get it working were well described in the various README docs. Here are the links to the three Githubs: [STORM-return-periods](https://github.com/NBloemendaal/STORM-return-periods) [STORM](https://github.com/NBloemendaal/STORM) [STORM-processing](https://github.com/NBloemendaal/STORM-preprocessing) AND this is the link to the data: [STORM dataset](https://doi.org/10.4121/uuid:82c1dc0d-5485-43d8-901a-ce7f26cda35d)

3.  Running the code. Huh. Well, first make sure that even if you don't immediately see why, if the code isn't too much, it may always serve as a helpful headstart to download all relevant content that is provided. So I got it to where based on all my testing the data that the code was calling was in the proper place for the code to find it, and indeed it would find the data. The issue that arose I think is 2 fold, and I may be wrong on this. The person who wrote this clearly had a better computer then mine, and also had more time for things to run. Their dataset files upon closer inspection are each Five Hundred Thousand rows and Thirteen columns, totaling in
at 6.5 million items. As it approaches the 20 minute mark of me watch my computer try and finish step 2 of 3 to get a graph outputted, I feel I was cheated. I'm gonna keep trying, but my hour is now up and I am sad. :(

4. What I have learned from this experience is 2 fold. 1, that research papers that deal with modelling of 10,000 years worth of information are hard to handle on a laptop, and 2, that you were very much right about this being a difficult issue to tackle. I actually found a paper
while looking that talked about how the information sharing during COVID has further demonstrated
that people are still really bad at writing code for other people. [See here](https://www.nature.com/articles/s41597-020-0524-5)
