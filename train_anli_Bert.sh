gpus=2

CUDA_VISIBLE_DEVICES=$gpus python3 train.py --config config/anliPromptBert.config \
    --gpu $gpus
