# 2021-Even-BDA-HA01
Estimate the Probability of success in a deal show. One experiment consists of following.–A contestant is presented with three doors.–Behind one of them is a valuable prize.–After contestant chooses a door, host opens one of the other two doors (not the one containing the prize)–The contestant is then given the choice to switch to the other unopened door.–Assume that contestance switches to other door.•Input–i/p 1: number of mapped instances–i/p 2: number of tries•Output–o/p: average of all mapper outputs
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

hdfs dfs -put reducer.py /user

hdfs dfs -put mapper.py /user

hdfs dfs -chmod go+wx /user/mapper.py

hdfs dfs -chmod go+wx /user/reducer.py

hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /user/inputfile.txt -output /output
The output will be saved in /output

hdfs dfs -cat /output/part-00000

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

references
https://github.com/Overdrivr/monty-hall-problem

http://www.science.smith.edu/dftwiki/index.php/Map-Reduce_Examples

https://github.com/maleckicoa/Monty-Haul/blob/master/Monty%20Haul.ipynb
