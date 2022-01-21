# WSDM 2022 TGP - AntGraph

[WSDM Cup Website link](https://www.wsdm-conference.org/2022/call-for-wsdm-cup-proposals/)

[Link to this challenge](https://www.dgl.ai/WSDM2022-Challenge/)

---

## Datasets
### Datasets A
- train_csvs/edges_train_A.csv
- train_csvs/node_features.csv
- train_csvs/edge_type_features.csv
- test_csvs/input_A_initial.csv

### Datasets B
- train_csvs/edges_train_B.csv
- test_csvs/input_B_initial.csv

## Usage

### Get LINE embedding

We use [LINE](https://github.com/tangjianpku/LINE) to generate a representation for the nodes of the constructed graph, and the heterogeneous edge information is temporarily discarded.

For dataset B, `src_id` and `dst_id` refer to different things, that is, they belong to heterogeneous nodes. Therefore, when constructing the LINE representation, we made a transformation for `dst_id` unification to distinguish between User and Item. It's `dst_id = dst_id + dst_offset`.

`graph_src_dst_id_by_all_edge_type_200_neg1-1_judge0.875.emb` and `dataset_b_graph_src_dst_id_by_all_edge_type2.emb` in the code are line embedding files.

#### Settings

**Dataset A**

```
Order: 1
Samples: 1000M
Negative: 1
Dimension: 200
Initial rho: 0.025000
----------------------
Number of edges: 54090536
Number of vertices: 19442
```

**Dataset B**

```
Order: 1
Samples: 1000M
Negative: 5
Dimension: 200
Initial rho: 0.025000
----------------------
Number of edges: 8278431
Number of vertices: 1304045
```

### All Pipeline

[AntGraph_solution.ipynb](./src/AntGraph_solution.ipynb)

## Dependencies

```
numpy==1.19.2
seaborn==0.11.2
lightgbm==3.1.1
xgboost==1.3.3
catboost==0.26.1
pandas==1.1.5
tqdm==4.62.2
scikit-learn==0.24.2
matplotlib==3.3.4
wandb==0.12.3
```
