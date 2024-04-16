# World Happiness Tracker App

## Welcome

Welcome to the World Happiness Tracker App!

On this page, you can learn more details about our dashboard. Please click on one of the links below to jump to one of the sections or just scroll through the page.

- [Purpose](#purpose)
- [For Users](#for-users)
- [For Developers and Those Interested to Run the App Locally](#for-developers-and-those-interested-to-run-the-app-locally)

## Purpose

We aim to develop a dashboard that visually represents the global happiness score as well as the happiness scores of various countries and regions. This dashboard will be useful for educational purposes across multiple fields where the happiness score can prove to be beneficial. These fields include, but are not limited to, economics, sociology, and psychology.

We aim to integrate technology into the classroom, and we believe that with this dashboard, students will be able to learn about the world more efficiently while using an engaging tool.

## For Users

Our World Happiness Tracker App is designed to make the analysis of global happiness accessible and interactive. We believe that this is important since it can improve the quality of education for those in the social sciences who seek to learn about this topic. With this tool, you can:

- Compare Happiness Scores: Select up to two countries to visualize and compare their happiness scores directly.  
- Discover Trends: Use line and bar plots to explore changes in happiness scores over time.  
- Interactive Visuals: Engage with our range of visualizations to gain deeper insights into what influences happiness around the world.  

### Demo
![Alt text](https://github.com/UBC-MDS/DSCI-532_2024_3_world-happiness-tracker/blob/main/img/demo.gif)  

### Important Links
See the dashboard here: <https://dsci-532-2024-3-world-happiness-tracker.onrender.com/>.  

To get support, please create a new issue [here](<https://github.com/UBC-MDS/DSCI-532_2024_3_world-happiness-tracker/issues>).


## For Developers and Those Interested to Run the App Locally

### To Run the App Locally

Please follow the following the instructions:

1. Please clone the repo by running the following command in your terminal:

```bash
git clone git@github.com:UBC-MDS/DSCI-532_2024_3_world-happiness-tracker.git
```

2. Step into the repository you have just cloned to create and activate the conda environment:

```bash
conda env create --file environment.yml
conda activate world-happiness-tracker-env
```

3. To run the dashsboard:

    i. First, go into the `src` directory by running `cd src` from the root of the repository.
    ii. From the `src` directory, run the following command to start the app:

```bash
python app.py
```

4. Click on the http output link in the terminal. The link should look something similar to this: `http://127.0.0.1:8050/`.

### To Contribute to Our Project

If you would like to make contributions, please see our [`CONTRIBUTING.md`](<https://github.com/UBC-MDS/DSCI-532_2024_3_world-happiness-tracker/blob/main/CONTRIBUTING.md>) for more details.
