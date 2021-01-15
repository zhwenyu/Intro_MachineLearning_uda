#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print "number of persons", len(enron_data)
# for i in enron_data:
#     print len(enron_data[i])
#     break 

# num_poi = 0
num_quant = 0
for person_i in enron_data:
    # if enron_data[person_i]["poi"] == 1:
    #     num_poi += 1 
    # if "JAMES" in person_i: 
    #     print person_i, enron_data[person_i]['total_stock_value']
    # if "COLWELL" in person_i:
    #     print person_i, enron_data[person_i]['from_this_person_to_poi']
    # if "SKILLING" in person_i:
    #     print person_i, enron_data[person_i]['exercised_stock_options']
    # if "LAY" in person_i or "SKILLING" in person_i or "FASTOW" in person_i:
    #     print person_i, enron_data[person_i]['total_payments'] 
    if enron_data[person_i]['email_address'] != 'NaN':
        num_quant += 1

# print "num_poi", num_poi
print "num_quant", num_quant
