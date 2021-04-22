import matplotlib.pyplot as plt


# """
# This is an example of Scratter plot
# """

# stock_price = [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.45, 196.42, 200.32, 200.32, 200.85, 199.2, 199.2, 199.2, 199.46, 201.46, 197.54, 201.12, 203.12, 203.12, 203.12, 202.83, 202.83, 203.36, 206.83, 204.9, 204.9, 204.9, 204.4, 204.06]
# t = list(range(1, 31))
# plt.title('Opening Stock Prices')
# plt.xlabel('Days')
# plt.ylabel('$ USD')
# plt.plot(t, stock_price, marker='.', color='blue')
# plt.xticks([1, 8, 15, 22, 28]) 
# plt.show()

# """
# This is an example of Line plot
# """

# grades = ['A', 'B', 'C', 'D', 'E', 'F']
# students_count = [20, 30, 10, 5, 8, 2]
# plt.bar(grades, students_count, color=['green', 'gray', 'gray', 'gray', 'gray', 'red'])
# plt.title('Grades Bar Plot for Biology Class')
# plt.xlabel('Grade')
# plt.ylabel('Num Students')
# plt.bar(grades, students_count, color=['green', 'gray', 'gray', 'gray', 'gray', 'red'])
# plt.show()

# plt.title('Grades Bar Plot for Biology Class')
# plt.xlabel('Num Students')
# plt.ylabel('Grade')
# plt.barh(grades, students_count, color=['green', 'gray', 'gray', 'gray', 'gray', 'red'])
# plt.show()
# Plotting

# """
# This is an example of Pie plot
# """

# labels = ['Monica', 'Adrian', 'Jared']
# num = [230, 100, 98] # Note that this does not need to be percentages
# plt.pie(num, labels=labels, autopct='%.2f%%', colors=['lightblue', 'lightgreen', 'yellow'])
# plt.title('Voting Results: Club President', fontdict={'fontsize': 20})
# plt.show()
# plt.pie(num, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'yellow'])
# plt.show()

"""
This is an define function of HeatMap plot
"""

def heatmap(data, row_labels, col_labels, ax=None, cbar_kw={}, cbarlabel="", **kwargs):
    if not ax:
        ax = plt.gca()
    im = ax.imshow(data, **kwargs)
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")
    for edge, spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)
    return im, cbar
# import numpy as np
# data = np.array([
#     [30, 20, 10,],
#     [10, 40, 15],
#     [12, 10, 20]
# ])
# im, cbar = heatmap(data, ['Class-1', 'Class-2', 'Class-3'], ['A', 'B', 'C'], cmap='YlGn', cbarlabel='Number of Students')
# plt.show()
"""
This is define of Annotate HeatMap
"""
def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                    textcolors=["black", "white"],
                    threshold=None, **textkw):
    import matplotlib
    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

# """
# This is an example of Density plot
# """

import seaborn as sns
data = [90, 80, 50, 42, 89, 78, 34, 70, 67, 73, 74, 80, 60, 90, 90]
# sns.distplot(data)
# plt.show()

plt.title('Density Plot')
plt.xlabel('Score')
plt.ylabel('Density')
sns.histplot(data, kde=True, stat="density", linewidth=0)
plt.show()