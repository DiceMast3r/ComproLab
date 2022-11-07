import matplotlib.pyplot as plt


def func(pct, allvals): # for autopct
    #absolute = int(pct/100.*np.sum(allvals))
    absolute = int(round(pct * sum(allvals) / 100.0)) # works better
    return "{:.1f}%\n({:d} THB)".format(pct, absolute)


def Convert_to_dict(lst): # convert list to dictionary
    dict = {}
    for i in lst:
        x = i.split(" ")
        dict[x[0]] = float(x[1])
    return dict


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal")) # create figure and axis

inp = input(
    "Enter in pair (category1 value1,category2 value2,...): ").strip().split(",") # get input
for i in range(len(inp)):  # this loop removes the spaces
    inp[i] = inp[i].strip()

data = [float(x.split()[-1]) for x in inp] # get data
category = [x.split()[0] for x in inp] # get category


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w")) # create pie chart

ax.legend(wedges, category,
          title="Categories",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1)) # create legend

plt.setp(autotexts, size=8, weight="bold") # set text size and weight

ax.set_title("Matplotlib pie: Money spent") # set title

print("List version:", inp)
print("Dictionary version:", Convert_to_dict(inp))
plt.show()
