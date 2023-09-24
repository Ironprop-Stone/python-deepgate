from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import deepgate

if __name__ == '__main__':
    data_dir = './data/train'
    circuit_path = './data/train/graphs.npz'
    label_path = './data/train/labels.npz'
    num_epochs = 100
    
    print('[INFO] Parse Dataset')
    dataset = deepgate.NpzParser(data_dir, circuit_path, label_path)
    train_dataset, val_dataset = dataset.get_dataset()
    print('[INFO] Create Model and Trainer')
    model = deepgate.Model()
    
    print('[INFO] Stage 1 Training ...')
    trainer = deepgate.Trainer(model, prob_rc_func_weight=[1.0, 0.0, 0.0])
    trainer.train(num_epochs, train_dataset, val_dataset)
    
    print('[INFO] Stage 2 Training ...')
    trainer = deepgate.Trainer(model, prob_rc_func_weight=[3.0, 1.0, 2.0])
    trainer.train(num_epochs, train_dataset, val_dataset)
    