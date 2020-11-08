import os
import argparse

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def load():
    parser = argparse.ArgumentParser()

    # prediction task
    parser.add_argument('--task', default="next_activity")

    # feature
    parser.add_argument('--contextual_info', default=False, type=str2bool)
    parser.add_argument('--inter_case_level', default='Level1')

    # dnn
    parser.add_argument('--num_epochs', default=5, type=int)


    # all models
    parser.add_argument('--learning_rate', default=0.002, type=float)

    # evaluation
    parser.add_argument('--num_folds', default=10, type=int) # 10
    #parser.add_argument('--cross_validation', default=False, type=util.str2bool)
    parser.add_argument('--batch_size', default=256, type=int) #lstm 256 #dnc 1

    # data
    parser.add_argument('--data_set', default="modi_BPI_2012_dropna_filter_act.csv")
    parser.add_argument('--data_dir', default="../sample_data/")
    parser.add_argument('--checkpoint_dir', default="./checkpoints/")

    args = parser.parse_args()

    return args
