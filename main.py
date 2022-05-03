import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.gridspec import GridSpec
import charts

def get_column_indexes(country):
	"""Gets index for column in the 1st row"""
	c_index = clean_data[0].index(country)
	return c_index


with open('data.tsv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter='\t')
	
	#create variable holding all data to loop over multiple types,
	#since csv.reader can loop only once
	data = list(csv_reader)

	#remove trailing spaces and special characters from data
	clean_data = []
	for row in data:
		row = [col.replace(':', '') for col in row]
		row = [col.replace(' u', '') 
		for col in row]
		row = [col.strip() for col in row]
		clean_data.append(row)

	#get indexes for the necessary columns
	country_1 = get_column_indexes('LV')
	country_2 = get_column_indexes('LT')
	country_3 = get_column_indexes('EE')
	EU27 = get_column_indexes('EU27_2020')

	#set names for selected countries
	c1 = 'Latvia'
	c2 = 'Lithuania'
	c3 = 'Estonia'

	#get totals for each country
	answer_categories = ['1-3x a week', '4-6x a week', 'Once a day or more', 'Never or occasionaly']
	country_data = {} #dict is requared to create horizontal stacked bar chart
	c1_all = []
	c2_all = []
	c3_all = []
	eu27_all = []
	for row in clean_data:
		if 't,total,total' in row[0].lower():
			c1_all.append(float(row[country_1]))
			c2_all.append(float(row[country_2]))
			c3_all.append(float(row[country_3]))
			eu27_all.append(float(row[EU27]))
	# first 3 dict keys need to be changes acording to the chosen countries
	# here data are selected for LV, LT and EST
	country_data.update({f'{c1}': c1_all}) 
	country_data.update({f'{c2}': c2_all})
	country_data.update({f'{c3}': c3_all})
	country_data.update({'EU_27': eu27_all})

	#get data by gender for each country 
	men_c1, women_c1 = [], []
	men_c2, women_c2 = [], []
	men_c3, women_c3 = [], []
	men_eu27, women_eu27 = [], []
	for row in clean_data:
		if 'm,total,total' in row[0].lower():
			men_c1.append(float(row[country_1]))
			men_c2.append(float(row[country_2]))
			men_c3.append(float(row[country_3]))
			men_eu27.append(float(row[EU27]))
		elif 'f,total,total' in row[0].lower():
			women_c1.append(float(row[country_1]))
			women_c2.append(float(row[country_2]))
			women_c3.append(float(row[country_3]))
			women_eu27.append(float(row[EU27]))

	#get data by education for each country
	ed_02_c1, ed_34_c1, ed_58_c1 = [], [], []
	ed_02_c2, ed_34_c2, ed_58_c2 = [], [], []
	ed_02_c3, ed_34_c3, ed_58_c3 = [], [], []
	ed_02_eu27, ed_34_eu27, ed_58_eu27 = [], [], []
	for row in clean_data:
		if 't,total,ed0-2' in row[0].lower():
			ed_02_c1.append(float(row[country_1]))
			ed_02_c2.append(float(row[country_2]))
			ed_02_c3.append(float(row[country_3]))
			ed_02_eu27.append(float(row[EU27]))
		elif 't,total,ed3_4' in row[0].lower():
			ed_34_c1.append(float(row[country_1]))
			ed_34_c2.append(float(row[country_2]))
			ed_34_c3.append(float(row[country_3]))
			ed_34_eu27.append(float(row[EU27]))
		elif 't,total,ed5-8' in row[0].lower():
			ed_58_c1.append(float(row[country_1]))
			ed_58_c2.append(float(row[country_2]))
			ed_58_c3.append(float(row[country_3]))
			ed_58_eu27.append(float(row[EU27]))

	#get data by age for each country
	y15_24c1, y25_34c1, y35_44c1, y45_54c1, y55_64c1, y65_morec1 = [], [], [], [], [], []
	y15_24c2, y25_34c2, y35_44c2, y45_54c2, y55_64c2, y65_morec2 = [], [], [], [], [], []
	y15_24c3, y25_34c3, y35_44c3, y45_54c3, y55_64c3, y65_morec3 = [], [], [], [], [], []
	y15_24eu27, y25_34eu27, y35_44eu27, y45_54eu27, y55_64eu27, y65_moreeu27 = [], [], [], [], [], []
	for row in clean_data:
		if 't,y15-24,total' in row[0].lower():
			y15_24c1.append(float(row[country_1]))
			y15_24c2.append(float(row[country_2]))
			y15_24c3.append(float(row[country_3]))
			y15_24eu27.append(float(row[EU27]))
		elif 't,y25-34,total' in row[0].lower():
			y25_34c1.append(float(row[country_1]))
			y25_34c2.append(float(row[country_2]))
			y25_34c3.append(float(row[country_3]))
			y25_34eu27.append(float(row[EU27]))
		elif 't,y35-44,total' in row[0].lower():
			y35_44c1.append(float(row[country_1]))
			y35_44c2.append(float(row[country_2]))
			y35_44c3.append(float(row[country_3]))
			y35_44eu27.append(float(row[EU27]))
		elif 't,y45-54,total' in row[0].lower():
			y45_54c1.append(float(row[country_1]))
			y45_54c2.append(float(row[country_2]))
			y45_54c3.append(float(row[country_3]))
			y45_54eu27.append(float(row[EU27]))
		elif 't,y55-64,total' in row[0].lower():
			y55_64c1.append(float(row[country_1]))
			y55_64c2.append(float(row[country_2]))
			y55_64c3.append(float(row[country_3]))
			y55_64eu27.append(float(row[EU27]))
		elif 't,y_ge65,total' in row[0].lower():
			y65_morec1.append(float(row[country_1]))
			y65_morec2.append(float(row[country_2]))
			y65_morec3.append(float(row[country_3]))
			y65_moreeu27.append(float(row[EU27]))

#common formatting settings for the charts
title_font = {'fontname': 'Calibri',
			  'color': '#333230',
			  'weight': 'bold',
			  'size': 18,
			 }

subtitle_font = {'fontname': 'Calibri',
				 'color': '#333230',
			     'weight': 'normal',
				 'size': 14,
				}

y_font = {'fontname': 'Calibri',
		  'color': '#333230',
		  'weight': 'bold',
		  'size': 12,
		 }

gs = GridSpec(nrows=1, ncols=4)

#plotting the 1st chart
fig, ax = plt.subplots(figsize=(11, 6))
charts.survey(ax, country_data, answer_categories)

#formatting the 1st chart
plt.title("Sugar Drink Consumption", y=1.1, fontdict=title_font)
fig.text(s='Frequency of consumption, %', x=0.5, y=0.93, fontdict=subtitle_font, ha='center', va='center')
plt.ylabel('', fontdict=y_font)


#plotting the 2nd chart
fig = plt.figure(figsize = (13, 8)) 

plot1 = fig.add_subplot(gs[0, 0])
plot2 = fig.add_subplot(gs[0, 1], sharey=plot1)
plot3 = fig.add_subplot(gs[0, 2], sharey=plot1)
plot4 = fig.add_subplot(gs[0, 3], sharey=plot1)
charts.data_by_gender(plot1, answer_categories, men_c1, women_c1, f"{c1}")
charts.data_by_gender(plot2, answer_categories, men_c2, women_c2, f"{c2}")
charts.data_by_gender(plot3, answer_categories, men_c3, women_c3, f"{c3}")
charts.data_by_gender(plot4, answer_categories, men_eu27, women_eu27, "EU27")

#formatting the 2nd chart
plt.setp(plot2.get_yticklabels(), visible=False)
plt.setp(plot3.get_yticklabels(), visible=False)
plt.setp(plot4.get_yticklabels(), visible=False)
plt.suptitle("Sugar Drink Consumption by Gender", fontname='Calibri', fontsize=18, fontweight='bold', color='#333230' )
fig.text(s='Frequency of consumption, %', x=0.5, y=0.93, fontdict=subtitle_font, ha='center', va='center')
handles, labels = plot4.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower left', bbox_to_anchor=(0.12, -0.01), ncol=3, fontsize=12)


#plotting data for the 3rd chart
fig = plt.figure(figsize = (13, 8))
plot1 = fig.add_subplot(gs[0, 0])
plot2 = fig.add_subplot(gs[0, 1], sharey=plot1)
plot3 = fig.add_subplot(gs[0, 2], sharey=plot1)
plot4 = fig.add_subplot(gs[0, 3], sharey=plot1)
charts.data_by_education(plot1, answer_categories, ed_02_c1, ed_34_c1, ed_58_c1, f"{c1}" )
charts.data_by_education(plot2, answer_categories, ed_02_c2, ed_34_c2, ed_58_c2, f"{c2}" )
charts.data_by_education(plot3, answer_categories, ed_02_c3, ed_34_c3, ed_58_c3, f"{c3}" )
charts.data_by_education(plot4, answer_categories, ed_02_eu27, ed_34_eu27, ed_58_eu27, "EU27" )

#formatting the 3rd chart
plt.setp(plot2.get_yticklabels(), visible=False)
plt.setp(plot3.get_yticklabels(), visible=False)
plt.setp(plot4.get_yticklabels(), visible=False)
fig.suptitle('Sugar Drink Consumption by Education', fontname='Calibri', fontsize=18, fontweight='bold', color='#333230')
fig.text(s='Frequency of consumption, %', x=0.5, y=0.93, fontdict=subtitle_font, ha='center', va='center')
handles, labels = plot4.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower left', bbox_to_anchor=(0.12, -0.01), ncol=3, fontsize=12)


#plotting the 4th chart
fig = plt.figure(figsize=(13, 8))
plot1 = fig.add_subplot(gs[0, 0], sharey=plot1)
plot2 = fig.add_subplot(gs[0, 1], sharey=plot1)
plot3 = fig.add_subplot(gs[0, 2], sharey=plot1)
plot4 = fig.add_subplot(gs[0, 3], sharey=plot1)
charts.data_by_age(plot1, answer_categories, y15_24c1, y25_34c1, y35_44c1, y45_54c1, y55_64c1, y65_morec1, f'{c1}')
charts.data_by_age(plot2, answer_categories, y15_24c2, y25_34c2, y35_44c2, y45_54c2, y55_64c2, y65_morec2, f'{c2}')
charts.data_by_age(plot3, answer_categories, y15_24c3, y25_34c3, y35_44c3, y45_54c3, y55_64c3, y65_morec3, f'{c3}')
charts.data_by_age(plot4, answer_categories, y15_24eu27, y25_34eu27, y35_44eu27, y45_54eu27, y55_64eu27, y65_moreeu27, 'EU27')

#formating the 4th chart
plt.setp(plot2.get_yticklabels(), visible=False)
plt.setp(plot3.get_yticklabels(), visible=False)
plt.setp(plot4.get_yticklabels(), visible=False)

handles, labels = plot4.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower left', bbox_to_anchor=(0.12, -0.01), ncol=6, fontsize=12)
fig.suptitle('Sugar Drink Consumption by Age', fontname='Calibri', fontsize=18, fontweight='bold', color='#333230')
fig.text(s='Frequency of consumption, %', x=0.5, y=0.93, fontdict=subtitle_font, ha='center', va='center') 

plt.show()



