# Get the y combinator companies with filter options

This project reversere engineered the ycombinator.com API for your usage. You can set the filter options on your own and just extract the companies. The idea of the project is to give everyone the opportunity to identify current innovation trends, do Data Science on the dataset and come up with better start-up ideas. Have fun and get valuable insights.

### Decide whether you want the export as a json or csv file, while inserting csv or json into the *export_type* variable

### enter the path for the export into the *file_path* variable

## insert the following filters as a string as they are published at ycombinator.com. Seperate them by a comma. ["S21", "S20"]

### if all you want all batches insert nothing. If you want one of the following specific batches, S21, W21, S20, W20, S19, W19, S18, W18, S17, W17, IK12, S16, W16, S15, W15, S14, W14, S13, W13,S12, W12, S11, W11, S10, W10, S09, W09, S08, W08, S07, W07, S06, W06, S05, enter them at the *batch* variable as string

### if all you want all industries insert nothing. Filtering for certain industries choose between B2B Software, Services, Education, Consumer, Healthcare, Real Estate, Construction, Financial Technology, Industrials or Government. Please insert them as a string at the *industries* variable.

### Filter after different status with the following Active, Public, Acquired & Inactive Status. If all you want all companies regardless the status let the *filter* variable empty. 


### if all you want all (anywhere) insert nothing. If you want specific choose between, North America, Asia, Europe, Africa, Central America, South America, Oceanic and insert them as a string into the *regions* variable.

## Just clone the repository and run the script with your filter settings, enjoy!
