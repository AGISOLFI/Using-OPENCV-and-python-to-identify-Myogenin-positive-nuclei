# Sirt-1 Influence on Myogenesis in Tissue Enginnered Skeletal Muscle

## Abstract

The Biomedical Engineering Research for Active military and Veterans (BRAVe) program at the University of Texas San Antonio inolves undergraduate students in a 10 week summer REU opportunity. In this time period, students complete research that is beneficial to and/or collabrative with the United States Armed Services. This repository was desgined for data quantification of the research of SIRT-1 overexpression influence on myogenesis in tissue engineered skeletal muscle.

[Learn more]()
   
## Problem
How can python code be utilized to determine the percentage of myogenin positive nuclei in fluorescent confocal microscopy images?

## Approach 
Using the OPENCV library, users can easily detect nuclei of interest. By separating the original code into 3 different color channels (blue, green, and red) the simple blob detector function built into OPENCV can be utilized to analyze DAPI stained nuclei (blue channel). A new channel is then created consisting of just the overlapping myogenin stain (red channel) and DAPI stain (blue channel). The simple blob detection function is applied once again to this new channel. User is prompted with figures of detected nuclei, the newly created overlap channel, and a figure of detected myogenin positive nuclei in order for the user to validate quantification. The user then is given the numerical count of total nuclei, myogenin positive nuclei, and the percentage of myogenin positive nuclei compared to the total nuclei count.

# Usage 
Open the file Myogenin Expressing Nuclei V5.py and change the file being read into img according to the name of your image of interest. Then simply run the program to receive quantification data.

# Acknowledgments
This research was supported, in part, by the National Science Foundation (EEC-1852560), and National Institutes of Health (5SC1DK122578)

This code was created for research use as part of the BRAVe program.  