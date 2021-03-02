

import argparse
import os
import sys
import numpy as np
import random
import torch

from torch.backends import cudnn
from torch import nn
sys.path.append('.')
from config import cfg
import pdb
from data import make_data_loader
from engine.trainer import do_train
from modeling import build_model
from layers import make_loss
from solver import make_optimizer, WarmupMultiStepLR,WarmupStepLR

from utils.logger import setup_logger

def setup_seed(seed):
     torch.manual_seed(seed)
     torch.cuda.manual_seed(seed)
     torch.cuda.manual_seed_all(seed)
     np.random.seed(seed)
     random.seed(seed)




def train(cfg):
    # prepare dataset

    train_loader, val_loader, num_query, num_classes = make_data_loader(cfg)

    # prepare model
    model = build_model(cfg, num_classes)
    if cfg.SOLVER.FINETUNE:
        model.load_state_dict(torch.load(cfg.TEST.WEIGHT).module.state_dict())
    model = nn.DataParallel(model)


    optimizer = make_optimizer(cfg, model)
    scheduler = WarmupMultiStepLR(optimizer, cfg.SOLVER.STEPS, cfg.SOLVER.GAMMA, cfg.SOLVER.WARMUP_FACTOR,
                                  cfg.SOLVER.WARMUP_ITERS, cfg.SOLVER.WARMUP_METHOD)
    # scheduler = WarmupStepLR(optimizer,3, 9, cfg.SOLVER.WARMUP_FACTOR,
    #                               cfg.SOLVER.WARMUP_ITERS, cfg.SOLVER.WARMUP_METHOD)

    loss_func = make_loss(cfg)

    arguments = {}

    do_train(
        cfg,
        model,
        train_loader,
        val_loader,
        optimizer,
        scheduler,
        loss_func,
        num_query
    )


def main():
    setup_seed(1)
    parser = argparse.ArgumentParser(description="ReID Baseline Training")
    parser.add_argument(
        "--config_file", default="", help="path to config file", type=str
    )
    parser.add_argument("opts", help="Modify config options using the command-line", default=None,
                        nargs=argparse.REMAINDER)

    args = parser.parse_args()

    # num_gpus = int(os.environ["WORLD_SIZE"]) if "WORLD_SIZE" in os.environ else 1

    if args.config_file != "":
        cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.freeze()

    output_dir = cfg.OUTPUT_DIR
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    logger = setup_logger("reid_baseline", output_dir, 0)
    logger.info(args)

    if args.config_file != "":
        logger.info("Loaded configuration file {}".format(args.config_file))
        with open(args.config_file, 'r') as cf:
            config_str = "\n" + cf.read()
            logger.info(config_str)
    logger.info("Running with config:\n{}".format(cfg))

    cudnn.benchmark = True
    train(cfg)


if __name__ == '__main__':
    main()
