# DSCI-532_2024_3_world-happiness-tracker

## Welcome to our Dashboard 
### Purpose:
We aim to develop a dashboard that visually represents the global happiness score as well as the happiness scores of various countries and regions. This dashboard will be useful for educational purposes across multiple fields where the happiness score can prove to be beneficial. These fields include, but are not limited to, economics, sociology, and psychology.

We aim to integrate technology into the classroom, and we believe that with this dashboard, students will be able to learn about the world more efficiently while using an engaging tool.

### Usage information
Our World Happiness Tracker Dashboard is designed to make the analysis of global happiness accessible and interactive. With this tool, you can:  
•	Compare Happiness Scores: Select up to two countries to visualize and compare their happiness scores directly.  
•	Discover Trends: Use line and bar plots to explore changes in happiness scores over time.  
•	Interactive Visuals: Engage with our range of visualizations to gain deeper insights into what influences happiness around the world.  

### Demo
![Alt text](https://github.com/UBC-MDS/DSCI-532_2024_3_world-happiness-tracker/blob/main/img/demo.gif)  

### important links
See the Dashboard here: https://dsci-532-2024-3-world-happiness-tracker.onrender.com/  

If you see any problems with the dashboard, please follow this link and create a new issue: https://github.com/UBC-MDS/DSCI-532_2024_3_world-happiness-tracker/issues 

If you would like to make contributions please follow this link for more instructions: https://github.com/UBC-MDS/DSCI-532_2024_3_world-happiness-tracker/blob/main/CONTRIBUTING.md  

### Install and run the dashboard locally

#### Run the following in terminal

Clone the repo
```
git clone git@github.com:UBC-MDS/DSCI-532_2024_3_world-happiness-tracker.git
```

Step into the repo to create and activate the environment 
```
conda env create --file environment.yml
conda activate world-happiness-tracker-env
```

Get the dashboard
```
python src/app.py
```

After running click on the http output link in the terminal    
Link should look something similar to this: http://127.0.0.1:8050/
