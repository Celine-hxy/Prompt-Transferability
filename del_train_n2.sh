gpus=2

CUDA_VISIBLE_DEVICES=$gpus python3 train.py --config config/recastfactualityPromptRoberta.config \
    --gpu $gpus


CUDA_VISIBLE_DEVICES=$gpus python3 train.py --config config/tweetevalsentimentPromptRoberta.config \
    --gpu $gpus