#CUDA_VISIBLE_DEVICES=$gpus

gpus=3

#MODEL_PROMPT="Roberta-base"
#MODEL_PROMPT="Bert-base"
#MODEL_PROMPT="Random"
#PROJECTOR="model/cross_Bert_to_Roberta_reconstructionLoss"
PROJECTOR="model/crossPromptRoberta"






############
#Sentiment
############
#restaurant
CUDA_VISIBLE_DEVICES=$gpus python3 valid.py --config config/restaurantPromptRobertaLarge.config \
    --gpu $gpus \
    --checkpoint model/restaurantPromptRobertaLarge \
    --replacing_prompt task_prompt_emb/restaurantPromptRoberta \
    --model_transfer_projector \
    --projector $PROJECTOR





'''
#laptop
CUDA_VISIBLE_DEVICES=$gpus python3 valid.py --config config/laptopPromptRobertaLarge.config \
    --gpu $gpus \
    --checkpoint model/laptopPromptRobertaLarge \
    --replacing_prompt task_prompt_emb/laptopPromptRoberta \
    --model_transfer_projector \
    --projector $PROJECTOR



#89%
#IMDB
CUDA_VISIBLE_DEVICES=$gpus python3 valid.py --config config/IMDBPromptRobertaLarge.config \
    --gpu $gpus \
    --checkpoint model/IMDBPromptRobertaLarge \
    --replacing_prompt task_prompt_emb/IMDBPromptRoberta \
    --model_transfer_projector \
    --projector $PROJECTOR
'''






#SST-2
CUDA_VISIBLE_DEVICES=$gpus python3 valid.py --config config/SST2PromptRobertaLarge.config \
    --gpu $gpus \
    --checkpoint model/SST2PromptRobertaLarge \
    --replacing_prompt task_prompt_emb/SST2PromptRoberta \
    --model_transfer_projector \
    --projector $PROJECTOR

exit


'''
############
#Paraphrase
############

#MRPC
CUDA_VISIBLE_DEVICES=$gpus python3 valid.py --config config/MRPCPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/MRPCPromptRoberta \
    --replacing_prompt task_prompt_emb/MRPCPromptBert \
    --model_transfer_projector \
    --projector $PROJECTOR

#QQP
CUDA_VISIBLE_DEVICES=$gpus python3 valid.py --config config/QQPPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/QQPPromptRoberta \
    --replacing_prompt task_prompt_emb/QQPPromptBert \
    --model_transfer_projector \
    --projector $PROJECTOR


############
#NLI
############

#RTE
#Remove prompts between two sentences
CUDA_VISIBLE_DEVICES=$gpus python3 valid.py --config config/RTEPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/RTEPromptRoberta \
    --replacing_prompt task_prompt_emb/RTEPromptBert \
    --model_transfer_projector \
    --projector $PROJECTOR

#MNLI
CUDA_VISIBLE_DEVICES=$gpus python3 valid.py --config config/MNLIPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/MNLIPromptRoberta \
    --replacing_prompt task_prompt_emb/MNLIPromptBert \
    --model_transfer_projector \
    --projector $PROJECTOR



#WNLI
CUDA_VISIBLE_DEVICES=$gpus python3 valid.py --config config/WNLIPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/WNLIPromptRoberta \
    --replacing_prompt task_prompt_emb/WNLIPromptBert \
    --model_transfer_projector \
    --projector $PROJECTOR



############
#RE
############
#RE
#CUDA_VISIBLE_DEVICES=$gpus python3 valid.py --config config/REPrompt.config \
#    --gpu $gpus \
#    --checkpoint model/REPrompt \
#    --replacing_prompt \
#    --task_transfer_projector \
###########
#Other
############


#QNLI
CUDA_VISIBLE_DEVICES=$gpus python3 valid.py --config config/QNLIPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/QNLIPromptRoberta \
    --replacing_prompt task_prompt_emb/QNLIPromptBert \
    --model_transfer_projector \
    --projector $PROJECTOR


CUDA_VISIBLE_DEVICES=$gpus python3 valid.py --config config/STSBPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/STSBPromptRoberta \
    --replacing_prompt task_prompt_emb/STSBPromptBert \
    --model_transfer_projector




'''

####################
########Bert########
####################

############
#Sentiment
############
#restaurant
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/restaurantPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/restaurantPromptRoberta \
    --model_prompt $MODEL_PROMPT



#laptop
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/laptopPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/laptopPromptRoberta \
    --model_prompt $MODEL_PROMPT



#IMDB
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/IMDBPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/IMDBPromptRoberta \
    --model_prompt $MODEL_PROMPT


#SST-2
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/SST2PromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/SST2PromptRoberta \
    --model_prompt $MODEL_PROMPT


############
#Paraphrase
############

#MRPC
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/MRPCPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/MRPCPromptRoberta \
    --model_prompt $MODEL_PROMPT

#QQP
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/QQPPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/QQPPromptRoberta \
    --model_prompt $MODEL_PROMPT


############
#NLI
############

#RTE
#Remove prompts between two sentences
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/RTEPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/RTEPromptRoberta \
    --model_prompt $MODEL_PROMPT

#MNLI
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/MNLIPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/MNLIPromptRoberta \
    --model_prompt $MODEL_PROMPT



#WNLI
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/WNLIPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/WNLIPromptRoberta \
    --model_prompt $MODEL_PROMPT



############
#RE
############
#RE
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/REPrompt.config \
    --gpu $gpus \
    --checkpoint model/REPrompt \
    --model_prompt $MODEL_PROMPT


############
#Other
############


#QNLI
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/QNLIPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/QNLIPromptRoberta \
    --model_prompt $MODEL_PROMPT


CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/STSBPromptRoberta.config \
    --gpu $gpus \
    --checkpoint model/STSBPromptRoberta \
    --model_prompt $MODEL_PROMPT
'''


'''
################################
###########BERT#################
################################


############
#Sentiment
############
#restaurant
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/restaurantPromptBert.config \
    --gpu $gpus \
    --checkpoint model/restaurantPromptBert \
    --model_prompt $MODEL_PROMPT



#laptop
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/laptopPromptBert.config \
    --gpu $gpus \
    --checkpoint model/laptopPromptBert \
    --model_prompt $MODEL_PROMPT




#IMDB
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/IMDBPromptBert.config \
    --gpu $gpus \
    --checkpoint model/IMDBPromptBert \
    --model_prompt $MODEL_PROMPT




#SST-2
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/SST2PromptBert.config \
    --gpu $gpus \
    --checkpoint model/SST2PromptBert \
    --model_prompt $MODEL_PROMPT




############
#Paraphrase
############

#MRPC
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/MRPCPromptBert.config \
    --gpu $gpus \
    --checkpoint model/MRPCPromptBert \
    --model_prompt $MODEL_PROMPT


#QQP
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/QQPPromptBert.config \
    --gpu $gpus \
    --checkpoint model/QQPPromptBert \
    --model_prompt $MODEL_PROMPT


############
#NLI
############

#RTE
#Remove prompts between two sentences
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/RTEPromptBert.config \
    --gpu $gpus \
    --checkpoint model/RTEPromptBert \
    --model_prompt $MODEL_PROMPT


#MNLI
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/MNLIPromptBert.config \
    --gpu $gpus \
    --checkpoint model/MNLIPromptBert \
    --model_prompt $MODEL_PROMPT




#WNLI
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/WNLIPromptBert.config \
    --gpu $gpus \
    --checkpoint model/WNLIPromptBert \
    --model_prompt $MODEL_PROMPT




############
#RE
############
#RE
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/REPrompt.config \
    --gpu $gpus \
    --checkpoint model/REPrompt \


############
#Other
############


#QNLI
CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/QNLIPromptBert.config \
    --gpu $gpus \
    --checkpoint model/QNLIPromptBert \
    --model_prompt $MODEL_PROMPT



CUDA_VISIBLE_DEVICES=$gpus python3 valid_cross.py --config config/STSBPromptBert.config \
    --gpu $gpus \
    --checkpoint model/STSBPromptBert \
    --model_prompt $MODEL_PROMPT
'''



