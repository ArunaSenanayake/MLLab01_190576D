# -*- coding: utf-8 -*-
"""190576D.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zgwG6uswWqHQxr3IeC5eT7aJP6MdfYt5
"""

import pandas
import numpy

l1 = "label_1"
l2 = "label_2"
l3 = "label_3"
l4 = "label_4"

labels = [l1,l2,l3,l4]
age_label = l2
features = [f'feature_{i}' for i in range(1,257)]

train_df = pandas.read_csv('train.csv')
train_df.head()

valid_df = pandas.read_csv('valid.csv')
valid_df.head()

test_df = pandas.read_csv('test.csv')
test_df.head()

train_df['label_4'].value_counts()

from sklearn.preprocessing import StandardScaler, RobustScaler

x_td = {}
x_vd = {}
y_td = {}
y_vd = {}
x_test = {}
y_test = {}

for target_label in labels:
  train_dataset = train_df[train_df['label_2'].notna()] if target_label == l2 else train_df
  valid_dataset = valid_df
  test_dataset = test_df

  scaler = RobustScaler()
  x_td[target_label] = pandas.DataFrame(scaler.fit_transform(train_dataset.drop(labels, axis=1)))
  y_td[target_label] = train_dataset[target_label]
  x_vd[target_label] = pandas.DataFrame(scaler.transform(valid_dataset.drop(labels, axis=1)))
  y_vd[target_label] = valid_dataset[target_label]
  x_test[target_label] = pandas.DataFrame(scaler.transform(test_dataset.drop(labels, axis=1)))
  y_test[target_label] = test_dataset[target_label]

y_td['label_1']

y_td['label_2']

from sklearn import svm

classifier = svm.SVC(kernel='linear')
classifier.fit(x_td[l1],y_td[l1])

from sklearn import metrics

y_pred = classifier.predict(x_vd[l1])

print(metrics.confusion_matrix(y_vd[l1],y_pred))
print(metrics.accuracy_score(y_vd[l1],y_pred))
print(metrics.precision_score(y_vd[l1],y_pred,average='weighted'))
print(metrics.recall_score(y_vd[l1],y_pred,average='weighted'))

from sklearn.feature_selection import SelectKBest, SelectPercentile, f_classif, mutual_info_classif

selector = SelectKBest(f_classif, k=130)
x_new = selector.fit_transform(x_td[l1],y_td[l1])
print("Shape:", x_new.shape)

classifier = svm.SVC(kernel='linear')
classifier.fit(x_new,y_td[l1])
y_pred2 = classifier.predict(selector.transform(x_vd[l1]))
print(metrics.confusion_matrix(y_vd[l1],y_pred2))
print(metrics.accuracy_score(y_vd[l1],y_pred2))
print(metrics.precision_score(y_vd[l1],y_pred2,average='weighted'))
print(metrics.recall_score(y_vd[l1],y_pred2,average='weighted'))

from sklearn.decomposition import PCA

pca = PCA(n_components=0.98, svd_solver='full')
pca.fit(x_td[l1])
x_train_trf = pandas.DataFrame(pca.transform(x_td[l1]))
x_valid_trf = pandas.DataFrame(pca.transform(x_vd[l1]))
print(x_train_trf.shape)
print(x_valid_trf.shape)

classifier = svm.SVC(kernel='linear')
classifier.fit(x_train_trf,y_td[l1])
y_pred2 = classifier.predict(x_valid_trf)
print(metrics.confusion_matrix(y_vd[l1],y_pred2))
print(metrics.accuracy_score(y_vd[l1],y_pred2))
print(metrics.precision_score(y_vd[l1],y_pred2,average='weighted'))
print(metrics.recall_score(y_vd[l1],y_pred2,average='weighted'))

classifier = svm.SVC(kernel='linear')
classifier.fit(x_td[l3],y_td[l3])

y_pred = classifier.predict(x_vd[l3])

print(metrics.confusion_matrix(y_vd[l3],y_pred))
print(metrics.accuracy_score(y_vd[l3],y_pred))
print(metrics.precision_score(y_vd[l3],y_pred,average='weighted'))
print(metrics.recall_score(y_vd[l3],y_pred,average='weighted'))

selector = SelectKBest(f_classif, k=90)
x_new = selector.fit_transform(x_td[l3],y_td[l3])
print("Shape:", x_new.shape)

classifier = svm.SVC(kernel='linear')
classifier.fit(x_new,y_td[l3])
y_pred2 = classifier.predict(selector.transform(x_vd[l3]))
print(metrics.confusion_matrix(y_vd[l3],y_pred2))
print(metrics.accuracy_score(y_vd[l3],y_pred2))
print(metrics.precision_score(y_vd[l3],y_pred2,average='weighted'))
print(metrics.recall_score(y_vd[l3],y_pred2,average='weighted'))

pca = PCA(n_components=0.9, svd_solver='full')
pca.fit(x_td[l3])
x_train_trf = pandas.DataFrame(pca.transform(x_td[l3]))
x_valid_trf = pandas.DataFrame(pca.transform(x_vd[l3]))
print(x_train_trf.shape)

classifier = svm.SVC(kernel='linear')
classifier.fit(x_train_trf,y_td[l3])
y_pred2 = classifier.predict(x_valid_trf)
print(metrics.confusion_matrix(y_vd[l3],y_pred2))
print(metrics.accuracy_score(y_vd[l3],y_pred2))
print(metrics.precision_score(y_vd[l3],y_pred2,average='weighted'))
print(metrics.recall_score(y_vd[l3],y_pred2,average='weighted'))

classifier = svm.SVC(kernel='linear')
classifier.fit(x_td[l1],y_td[l1])

y_pred = classifier.predict(x_test[l1])
pandas.DataFrame(y_pred).to_csv("l1_before.csv")

pca = PCA(n_components=0.98, svd_solver='full')
pca.fit(x_td[l1])
x_train_trf = pandas.DataFrame(pca.transform(x_td[l1]))
x_test_trf = pandas.DataFrame(pca.transform(x_test[l1]))
print(x_train_trf.shape)
print(x_test_trf.shape)

classifier = svm.SVC(kernel='linear')
classifier.fit(x_train_trf,y_td[l1])
y_pred2 = classifier.predict(x_test_trf)
pandas.DataFrame(y_pred2).to_csv("l1_after.csv")

x_test_trf.to_csv("fl1.csv")

classifier = svm.SVC(kernel='linear')
classifier.fit(x_td[l3],y_td[l3])

y_pred = classifier.predict(x_test[l3])
pandas.DataFrame(y_pred).to_csv("l3_before.csv")

selector = SelectPercentile(f_classif, percentile=10)
x_new = selector.fit_transform(x_td[l3],y_td[l3])
print(x_new.shape)

pandas.DataFrame(x_new).to_csv("fl3")

classifier = svm.SVC(kernel='linear')
classifier.fit(x_new,y_td[l3])
y_pred2 = classifier.predict(selector.transform(x_test[l3]))
pandas.DataFrame(y_pred2).to_csv("l3_after_sp.csv")

pca = PCA(n_components=0.9, svd_solver='full')
pca.fit(x_td[l3])
x_train_trf = pandas.DataFrame(pca.transform(x_td[l3]))
x_test_trf = pandas.DataFrame(pca.transform(x_test[l3]))
print(x_train_trf.shape)
print(x_test_trf.shape)

classifier = svm.SVC(kernel='linear')
classifier.fit(x_train_trf,y_td[l3])
y_pred2 = classifier.predict(x_test_trf)
pandas.DataFrame(y_pred2).to_csv("l3_after2.csv")

x_test_trf.to_csv("fl3.csv")

classifier = svm.SVC(kernel='linear')
classifier.fit(x_td[l2],y_td[l2])

y_pred = classifier.predict(x_test[l2])
pandas.DataFrame(y_pred).to_csv("l2_before.csv")

pca = PCA(n_components=0.99, svd_solver='full')
pca.fit(x_td[l2])
x_train_trf = pandas.DataFrame(pca.transform(x_td[l2]))
x_test_trf = pandas.DataFrame(pca.transform(x_test[l2]))
print(x_train_trf.shape)
print(x_test_trf.shape)

x_test_trf.to_csv("fl2_2.csv")

classifier = svm.SVC(kernel='linear')
classifier.fit(x_train_trf,y_td[l2])
y_pred2 = classifier.predict(x_test_trf)
pandas.DataFrame(y_pred2).to_csv("l2_after2.csv")

classifier = svm.SVC(kernel='linear', class_weight='balanced')
classifier.fit(x_td[l4],y_td[l4])

y_pred = classifier.predict(x_test[l4])
pandas.DataFrame(y_pred).to_csv("l4_before.csv")

pca = PCA(n_components=0.98, svd_solver='full')
pca.fit(x_td[l4])
x_train_trf = pandas.DataFrame(pca.transform(x_td[l4]))
x_test_trf = pandas.DataFrame(pca.transform(x_test[l4]))
print(x_train_trf.shape)
print(x_test_trf.shape)

x_test_trf.to_csv("fl4.csv")

classifier = svm.SVC(kernel='linear', class_weight='balanced')
classifier.fit(x_train_trf,y_td[l4])
y_pred2 = classifier.predict(x_test_trf)
pandas.DataFrame(y_pred2).to_csv("l4_after.csv")