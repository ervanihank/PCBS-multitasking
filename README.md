### Multi-tasking Experiment

- Github Repository: [PCBS](https://github.com/ervanihank/PCBS-multitasking).
- The experiment is the replication of the original study:  [https://bmcpsychology.biomedcentral.com/articles/10.1186/2050-7283-1-18 ]
- The aim of the project: Creating a psychological experiment that compares the multi-tasking skills in men and women. 
- The experiment include a succession of trials in which the performance of women and men in a task-switching paradigm are tested. 
**In the shape task**, participants had to respond to the shape of imperative stimuli (diamonds and rectangles required a left and right response, respectively).
**In the filling task**, participants had to respond to the number of circles within the shape (two and three circles required a left and right response, respectively).

- Participants were informed which task to carry out based on the imperative stimulus location:
If the stimulus appeared in the upper half of the frame, labeled “shape”, they had to carry out the shape
task, and when it appeared in the bottomhalf of the frame, labeled “filling”, they had to carry out the filling task.

**The experiment consists of 3 blocks:** First two blocks were blocks with just one of the two tasks (pure blocks), and in the third block, the two tasks were randomly interleaved (mixed block).

In the mixed block, task-switch trials were those following a trial of the alternative task, and task-repeat trials were those following the same task.

Procedure:
When an imperative stimulus (one of the four figure shown in the Figure-a) appeared (they were chosen at random), participants had time pressure to respond. The imperative stimulus disappeared following a response or following the stated seconds in case no response was given. Incorrect responses (or failures to respond) were followed by a feedback. Then the new trial begin. Before starting to each block a new instruction is given.  

![Figure a](https://github.com/ervanihank/PCBS-multitasking/blob/master/picture.png)

The response time, accuracy, stimulus type and task type are recorded.


### What I would have done differently given more time

1- I would definietely run subjects and analyse their data. It would be really interesting to replicate the findings!
2- I would make the code cleaner: Especially the measure_reaction_time and save_data functions
3- I would make the code more flexible so that you can chance it easily
4- I would add a reminder of instructions into the feedback, which is done in the original experiment. But since it was painful to write any instruction by using pygame I couldnt find time to do it.
5- I would arrange my code so that it can record the task-switch and task-repeat trials automaticaly into the save file, so that hte analysis might be easier to conduct. 

Erva 12.05.2021

