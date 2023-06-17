# WSDM 2022 TGP - AntGraph

Source code for "[An Effective Graph Learning based Approach for Temporal Link Prediction: The First Place of WSDM Cup 2022](https://arxiv.org/abs/2203.01820)"

## WSDM Cup 2022

[WSDM Cup Website link](https://www.wsdm-conference.org/2022/call-for-wsdm-cup-proposals/)

[Link to this challenge](https://www.dgl.ai/WSDM2022-Challenge/)


## Datasets

### Datasets A
- train_csvs/edges_train_A.csv
- train_csvs/node_features.csv
- train_csvs/edge_type_features.csv
- test_csvs/input_A_initial.csv
- test_csvs/input_A.csv
- test_csvs/input_A_final.csv

### Datasets B
- train_csvs/edges_train_B.csv
- test_csvs/input_B_initial.csv
- test_csvs/input_B.csv
- test_csvs/input_B_final.csv



## Usage

### 1. Get LINE embedding

We use [LINE](https://github.com/tangjianpku/LINE) to generate a representation for the nodes of the constructed graph, and the heterogeneous edge information is temporarily discarded.

For dataset B, `src_id` and `dst_id` refer to different things, that is, they belong to heterogeneous nodes. Therefore, when constructing the LINE representation, we made a transformation for `dst_id` unification to distinguish between User and Item. It's `dst_id = dst_id + dst_offset`.

`dataset_A_graph_src_dst_id.emb` and `dataset_B_graph_src_dst_id.emb` in the code are line embedding files.



**Quick guide**

Download the `*.emb` from [this link (OneDrive)](https://dreamwingscn-my.sharepoint.com/:f:/g/personal/i_dreamwings_cn/ErnCSpB0lUFPhlBUZ7uOTXoBcBiTYi2ZFMBHCKmI21Q2iA?e=FCS8JE) and place it in the `./embs` folder.



#### 1.1. build input data for LINE

```bash
cd src
python ./generate_for_line_emb.py --dataset A
python ./generate_for_line_emb.py --dataset B
```



#### 1.2. generate LINE embedding

The `-threads 64` can be changed according to the actual situation.

We use the **linux** version of the program to generate the embeddings.

##### Dataset A

```bash
cd src/LINE-master/(linux or windows)

./line -train ../../../embs/dataset_A_graph_src_dst_id.txt -output ../../../embs/dataset_A_graph_src_dst_id.emb -size 200 -order 1 -negative 1 -samples 1000 -threads 64
```

Settings

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



##### Dataset B

```bash
cd src/LINE-master/(linux or windows)

./line -train ../../../embs/dataset_B_graph_src_dst_id.txt -output ../../../embs/dataset_B_graph_src_dst_id.emb -size 200 -order 1 -negative 5 -samples 1000 -threads 64
```

Settings

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



### 2. All Pipeline

[AntGraph_solution.ipynb](./src/AntGraph_solution.ipynb)



## Dependencies

```
numpy==1.21.0
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

## References

Please cite this repository using the following reference:

```
@article{zhao2022effective,
  title={An Effective Graph Learning based Approach for Temporal Link Prediction: The First Place of WSDM Cup 2022},
  author={Zhao, Qian and Yang, Shuo and Hu, Binbin and Zhang, Zhiqiang and Wang, Yakun and Chen, Yusong and Zhou, Jun and Shi, Chuan},
  journal={arXiv preprint arXiv:2203.01820},
  year={2022}
}
```
