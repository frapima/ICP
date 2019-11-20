# COMPUTATIONAL INFRASTRUCTURES FOR MASSIVE DATA PROCESSING (ICP)

## Presentation

Working with massive data requires the use of computational infrastructures specifically designed for them. These infrastructures differ from traditional infrastructures in several respects. First fo all, it is necessary to combine the computing power of many computers, building what is known as a computer cluster. On the other hand, it is necessary to use programming paradigms that can take advantage of the computing power of the cluster but in a simple way for the developer in charge of implementing the programs for the analysis of massive data. Both aspects can be developed using cloud provider services. This course shows some of the most important technologies that allow to deploy infrastructures for massive data processing. 

## Contextualization

The course of Computer Infrastructures for Mass Data Processing is a compulsory course of 6 ECTS credits, taught in the first semester of the Master's Degree in Engineering and Data Science in UNED's University.

## Installation

For every project, you can create an isolated conda environment. The first thing you have to do is:
- Go to the conda web page, download and install conda.
- Place on the environment folder of the project you want to run and write the following command in your command line:
    - `conda create env -f environment.yml --prefix .`
- Now, it would depend on the project, some of them are `jupter notebook`, and others are `docker-compose up -d`. See instructions in the instructions file of each project.
