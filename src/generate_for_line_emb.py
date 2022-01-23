"""
为 LINE embedding 生成提供输入文件
"""

import pandas as pd
import numpy as np
import argparse


def get_args():
    ### Argument and global variables
    parser = argparse.ArgumentParser('Base')
    parser.add_argument('--dataset',
                        type=str,
                        choices=["A", "B"],
                        default='A',
                        help='Dataset name')

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)
    return args


if __name__ == '__main__':
    dataset = get_args().dataset
    print(f'Build input data for LINE (Dataset {dataset})')

    if dataset == 'A':
        # 由于 Dataset A 头尾节点类型一致，id 也一致，因此不必区分
        # 使用无向图建模
        dst_offset = 0
        use_directed_graph = False
    else:
        # Dataset B 头尾分别是 User 与 Item
        # 在同质图情况下，需对 dst id 做偏移以区分两者
        # 以有向图建模
        dst_offset = 791332
        use_directed_graph = True

    names = ['src_id', 'dst_id', 'edge_type', 'timestamp']
    if dataset == 'B':
        names.append('edge_feat')
    edge_csvs = pd.read_csv(f'../train_csvs/edges_train_{dataset}.csv',
                            header=None,
                            names=names).drop(columns=[
                                'timestamp', 'edge_feat', 'edge_type'
                            ],
                                              errors='ignore')

    edge_csvs['dst_id'] += dst_offset

    if not use_directed_graph:
        edge_csvs = pd.DataFrame(np.concatenate(
            [edge_csvs.values, edge_csvs.values[:, [1, 0]]]),
                                 columns=['src_id', 'dst_id'])

    edge_csvs['value'] = 1
    edge_csvs.to_csv(f'../embs/dataset_{dataset}_graph_src_dst_id.txt',
                     index=False,
                     header=False,
                     sep=' ')
