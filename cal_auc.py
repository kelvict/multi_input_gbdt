#!/user/bin/env python
#coding=utf-8
# Author: Zhiheng Zhang (405630376@qq.com)
#
import pandas as pd
from sklearn.metrics import roc_auc_score
import sys

def cal_auc(pred_path):
	df = pd.read_csv(pred_path, header=None, sep=' ')
	labels = df.iloc[:, 0].values
	labels = [l==1 for l in labels]

	preds = df.iloc[:, 1].values
	preds = [p>0 for p in preds]
	roc_auc_score(labels, preds)

if __name__ == "__main__":
	cal_auc(sys.argv[1])