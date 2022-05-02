import numpy as np
import matplotlib.pyplot as plt


def survey(ax, country_data, answer_categories):
	"""creates stacked horizontal bar chart
	   code from: https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html"""
	labels = list(country_data.keys())
	data = np.array(list(country_data.values()))
	data_cum = data.cumsum(axis=1)
	#does something to color intensity
	category_colors = plt.colormaps['tab20b'](np.linspace(0.15, 0.85, data.shape[1]))

	ax.invert_yaxis()
	ax.xaxis.set_visible(False)
	ax.set_xlim(0, np.sum(data, axis=1).max())

	for i, (colname, color) in enumerate(zip(answer_categories, category_colors)):
		widths = data[:, i]
		starts = data_cum[:, i] - widths
		rects = ax.barh(labels, widths, left=starts, height=0.5, label=colname, color=color)

		r, g, b, _ = color
		text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
		ax.bar_label(rects, label_type = 'center', color=text_color)

	ax.legend(ncol=len(answer_categories), bbox_to_anchor=(-0.005, -0.05), loc='center left', fontsize='12')


def data_by_gender(ax_nr, answer_categories, data_men, data_women, title):
	"""creates grouped horizontal bar chart"""
	y_pos = np.arange(len(answer_categories))
	width = 0.35

	rects1 = ax_nr.barh(y_pos - width/2, data_men, width, color='#393B79', label = 'Men')
	rects2 = ax_nr.barh(y_pos + width/2, data_women, width, color='#D6616B', label = 'Women')

	ax_nr.set_yticks(y_pos, labels = answer_categories)
	ax_nr.set_title(f'{title}')
	ax_nr.bar_label(rects1, padding=3)
	ax_nr.bar_label(rects2, padding=3)
	ax_nr.set_xticks([0, 50, 100])


def data_by_education(ax_nr, answer_categories, ed_02, ed_34, ed_58, title):
	"""creates grouped horizontal bar chart"""
	y_pos = np.arange(len(answer_categories))
	width = 0.2

	rects1 = ax_nr.barh(y_pos - width, ed_02, width, color='#9C9EDE', label = 'Lower secondary or less')
	rects2 = ax_nr.barh(y_pos, ed_34, width, color='#5254A3', label = 'Upper and post secondary')
	rects3 = ax_nr.barh(y_pos + width, ed_58, width, color='#393B79', label = 'Tertiary')

	ax_nr.set_yticks(y_pos, labels = answer_categories)
	ax_nr.set_title(f'{title}')
	ax_nr.bar_label(rects1, padding=3)
	ax_nr.bar_label(rects2, padding=3)
	ax_nr.bar_label(rects3, padding=3)
	ax_nr.set_xticks([0, 50, 100])
	

def data_by_age(ax_nr, answer_categories, y15_24, y25_34, y35_44, y45_54, y55_64, y65_more, title):
	"""creates grouped horizontal bar chart"""
	y_pos = np.arange(len(answer_categories))
	width = 0.12

	rects1 = ax_nr.barh(y_pos - width*2.5, y15_24, width, color = '#CEDB9C', label = 'y15_24')
	rects2 = ax_nr.barh(y_pos - width*1.5, y25_34, width, color = '#B4CF6A', label = 'y25_34')
	rects3 = ax_nr.barh(y_pos - width/2, y35_44, width, color = '#E7BA52', label = 'y35_44')
	rects4 = ax_nr.barh(y_pos + width/2, y45_54, width, color = '#BD9E39', label = 'y45_54')
	rects5 = ax_nr.barh(y_pos + width*1.5, y55_64, width, color = '#E7969C', label = 'y55_64')
	rects6 = ax_nr.barh(y_pos + width*2.5, y65_more, width, color ='#D6616B', label = 'y65_more')

	ax_nr.set_yticks(y_pos, labels = answer_categories)
	ax_nr.set_title(f'{title}')
	ax_nr.bar_label(rects1, padding=3)
	ax_nr.bar_label(rects2, padding=3)
	ax_nr.bar_label(rects3, padding=3)
	ax_nr.bar_label(rects4, padding=3)
	ax_nr.bar_label(rects5, padding=3)
	ax_nr.bar_label(rects6, padding=3)
	ax_nr.set_xticks([0, 50, 100])