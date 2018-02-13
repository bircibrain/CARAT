# CARAT

Welcome to the github repository for the CARAT project. Here you will find scripts and documentation to help you process and analyze fMRI data.

Here is a list of the documentation that is available:

1. **Creating timing files**  
There are two ways to create timing files. You can use user-defined variables (the default) or you can pull the timing straight from the raw eyetracker output (good for spot-checking). Timing files are necessary to run the preprocessing and first-level statistical analysis.
	1. **[User-Defined Variables](./Timing/UserDefinedTimings.md)**  
This section will tell you how to create timing files from the user-defined variables contained in the CARAT ExperimentBuilder scripts.
	2. **[Raw Output](./Timing/RawEDFTimings)**  
This section will tell you how to create timing files from raw EDF (eyetracker) output. 
3. **[Checking Timing Files](./Timing/SpotChecks)**  
From time to time, it is important to make sure that the two methods for extracting timing line up. This will ensure that the user-defined variables are working as expected. This section will explain how to check for that.
4. **[Preprocessing](./Preprocessing/)**  
Preprocessing takes your raw imaging data (DICOM format) and timing information and creates subject-level statistical maps that can be used for the second-level analysis. Here, you will learn how to gather/organize your data, how to generate preprocessing scripts, and how to run the preprocessing scripts.
5. **[Optimization](./optimization/)**  
Optimization refers to organizing your experimental stimuli so that you have the most power to estimate each condition. This folder contains information and scripts to optimize SPR and SPONT.



Contact information: Kayleigh Ryherd, [kayleigh.ryherd@uconn.edu](mailto:kayleigh.ryherd@uconn.edu)