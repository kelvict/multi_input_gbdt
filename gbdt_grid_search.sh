#!/usr/bin/env bash

for n_tree in 5 10 20 50; do
	for depth in 4 6 8; do
		./gbdt -t ${n_tree} -d ${depth} -s 12 \
		te.gbdt.dense te.gbdt.sparse tr.gbdt.dense tr.gbdt.sparse \
		te.gbdt.out_${n_tree}_${depth} tr.gbdt.out_${n_tree}_${depth}\
		te.gbdt.pred_${n_tree}_${depth} tr.gbdt.pred_${n_tree}_${depth}
	done
done
