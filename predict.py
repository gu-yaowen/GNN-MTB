
import pandas as pd
import numpy as np
import torch
import torch.nn.functional as F
import dgl
from dgllife.utils import smiles_to_bigraph, CanonicalAtomFeaturizer, CanonicalBondFeaturizer


def read_smiles(file_dir: str):
    try:
        df = pd.read_csv(file_dir)
    except:
        df = pd.read_csv(file_dir, encoding='gbk')
    return df['SMILES'].values


def Predict_sample(smiles: str,
                   model: torch.nn):
    node_featurizer = CanonicalAtomFeaturizer(atom_data_field='h')
    edge_featurizer = CanonicalBondFeaturizer(bond_data_field='h')
    graph = smiles_to_bigraph(smiles=smiles,
                              node_featurizer=node_featurizer,
                              edge_featurizer=edge_featurizer)
    graph = dgl.add_self_loop(graph)
    if graph is None:
        return 'invalid'
    else:
        n_feat = graph.ndata['h']
        return F.sigmoid(model(graph, n_feat)).detach().numpy()[0][0]


def Predict(file_dir: str,
            save_dir: str):
    try:
        smiles_list = read_smiles(file_dir)
    except:
        return 'Load Failed!'
    model = torch.load('.\\model\\model.pkl', map_location='cpu')
    model.eval()
    pre_ = []
    for smiles in smiles_list:
        pre = Predict_sample(smiles, model)
        pre_.append(pre)
    df_out = pd.DataFrame(np.array(pre_).T, index=smiles_list, columns=['PREDICT'])
    df_out.to_csv(save_dir, float_format='%.3f')

    return df_out
