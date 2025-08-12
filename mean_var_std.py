import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError(f"List must contain nine numbers.")
    mat = np.asarray(list, dtype=int).reshape(3, 3)
    flattened = np.asarray(list)
    calculations = {}
    calculations['mean'] = [mat.mean(axis=0).tolist(), mat.mean(axis=1).tolist(), flattened.mean().tolist()]
    calculations['variance'] = [mat.var(axis=0).tolist(), mat.var(axis=1).tolist(), flattened.var().tolist()]
    calculations['standard deviation'] = [mat.std(axis=0).tolist(), mat.std(axis=1).tolist(), flattened.std().tolist()]
    calculations['max'] = [mat.max(axis=0).tolist(), mat.max(axis=1).tolist(), flattened.max().tolist()]
    calculations['min'] = [mat.min(axis=0).tolist(), mat.min(axis=1).tolist(), flattened.min().tolist()]
    calculations['sum'] = [mat.sum(axis=0).tolist(), mat.sum(axis=1).tolist(), flattened.sum().tolist()]
    return calculations
