# U.S. Bureau of Labor Statistics API Interactor
## Purpose
The purpose of this package is to facilitate a user's interaction with the U.S. Bureau of Labor Statistics API in connection with their personal location and interests, and summarize and visualize the results in a Pandas Dataframe and PyPlot line plot.

## Pre-requisities
The following Python packages must be installed before using the module:

- pandas 
- requests
- json
- ip2geotools
- python-dotenv
- os
- matplotlib

## Set-up
The module works with V2 of the U.S. Bureau of Labor Statistics API, which requires a personal API key. A blank .env file is provided with a place to insert your API key, which you can sign up for (here)[https://data.bls.gov/registrationEngine/].

## What Works and What Doesn't
Currently, our module has the ability collect a user's interest, location, relevant series according to their interest, and execute requests to the BLS API, handle the most common errors, and do a basic visualization of a series. We are still figuring out how to make sure
the functions can all work together since we have been working on them separately and figuring out how we want to handle visualizing and summarizing multiple series of interest (do we want to visualize all of them or just one?). 

