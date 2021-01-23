Loan prediction
-
The goal of this project is to predict if a loan acquired by Fannie Mae will go into foreclosure or not.

Fannie Mae buys loans from lenders to try to incentive them to issue more loans.

Fannie Mae publishes [here](https://capitalmarkets.fanniemae.com/credit-risk-transfer/single-family-credit-risk-transfer/fannie-mae-single-family-loan-performance-data) data for the loans that it has acquired and how they perform through time.

This project was done following a [tutorial](https://www.dataquest.io/blog/data-science-portfolio-machine-learning/) from Dataquest.

In 2020, Fannie Mae modified the way they publish their data. To avoid having to make too many modifications to the tutorial project, the [old dataset](https://rapidsai.github.io/demos/datasets/mortgage-data) was used.

Installation
-
### Download the data
* Clone this repo.
* Go to the folder: `cd loan-prediction`.
* Create a `data` directory: `mkdir data`.
* Go to the `data` directory: `cd data`.
* Get the data:
	* Manually:
	    * Download the 2000-2015 dataset [here](https://rapidsai.github.io/demos/datasets/mortgage-data).
	    * Extract the files from `2012 Q1` through `2015 Q1`.
	    * Remove the `.tar` file.
	    * Move the files to the `data` directory.
	* Or run the download script: `python download_data.py`.
* Go back to the `loan-prediction` directory: `cd ..`

### Install the requirements
* Install the requirements: `pip install -r requirements.txt`.
* **perhaps change to `venv`?**

Usage
-
* Create a directory for the processed datasets: `mkdir processed`
* Combine the `Acquisition` and `Performance` datasets: `python assemble.py`:
	* This will create two files in the `processed` directory: `Acquisition.txt` and `Performance.txt`.
* Generate the training data: `python annotate.py`:
	* This will use `Acquisition.txt` and `Performance.txt` to create training data.
	* It will create a file `train.csv` with this data.
* Run cross-validation on the training set, and print the associated error metrics: `python predict.py`.


