import pandas as pd

df=pd.read_csv("all_labels.csv")
df.drop('width', axis = 1, inplace = True)
df.drop('height', axis = 1, inplace = True)
df.rename(columns={'class':'label','filename':'image'}, inplace=True)
df.reindex(columns=['image','xmin','ymin','xmax','ymax','label'])
#df.astype({'image': int, 'label': numpy.float64})

df.to_csv("Annotations-export.csv", index=False)


