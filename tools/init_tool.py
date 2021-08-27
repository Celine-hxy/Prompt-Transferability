import logging
import torch
from reader.reader import init_dataset, init_formatter, init_test_dataset
from model import get_model
from model.optimizer import init_optimizer
from .output_init import init_output_function
from torch import nn
from transformers import AutoTokenizer
import string
import os

logger = logging.getLogger(__name__)

def recover_model_transfer_prompt(prompt_emb,load_model):
    ##################
    #######AE trained#
    ##################
    if "Bert" in load_model:
        all_model_dir = os.listdir("model/crossPromptBert")
        path = "model/crossPromptBert/"
    elif "Roberta" in load_model:
        all_model_dir = os.listdir("model/crossPromptRoberta")
        path = "model/crossPromptRoberta/"
        print(all_model_dir)
    '''
    if "Bert" in load_model:
        #all_model_dir = os.listdir("model/cross_mlmPromptRoberta")
        all_model_dir = os.listdir("model/cross_mlmPromptBert")
        path = "model/cross_mlmPromptBert/"
        print(all_model_dir)
    elif "Roberta" in load_model:
        #all_model_dir = os.listdir("model/cross_mlmPromptBert")
        all_model_dir = os.listdir("model/cross_mlmPromptRoberta")
        path = "model/cross_mlmPromptRoberta/"
        print(all_model_dir)
    else:
        print("Error in init_tool.py/recover_model_transfer_prompt")
    '''


    max_epoch_model=0
    for model in all_model_dir:
        present_epoch_model = int(model.split("_")[0])
        if present_epoch_model > max_epoch_model:
            max_epoch_model = present_epoch_model
            PATH=path+str(model)
    print("Applied Model:",PATH)
    ###
    #PATH="model/projectPromptRoberta/99_model_AE.pkl"
    ###
    model = torch.load(PATH).to("cuda")
    model.eval()

    #load_task_prompt_dir = "task_prompt_emb/"+prompt_dir+"/task_prompt"
    prompt_emb_ = prompt_emb.reshape(int(prompt_emb.shape[0])*int(prompt_emb.shape[1]))
    prompt_emb_ = torch.nn.Parameter(prompt_emb_)
    prompt_emb_ = model(prompt_emb_.to("cuda"))
    prompt_emb_ = prompt_emb_.reshape(int(prompt_emb.shape[0]),int(prompt_emb.shape[1])).data

    return prompt_emb_





def recover_task_transfer_prompt(prompt_emb,load_model):
    ##################
    #######AE trained#
    ##################
    if "Bert" in load_model:
        all_model_dir = os.listdir("model/projectPromptBert")
        path = "model/projectPromptBert/"
        print(all_model_dir)
    elif "Roberta" in load_model:
        all_model_dir = os.listdir("model/projectPromptRoberta")
        path = "model/projectPromptRoberta/"
        print(all_model_dir)
    else:
        print("Error in init_tool.py/recover_task_transfer_prompt")

    #all_model_dir = os.listdir("model/projectPromptRoberta")
    #print(all_model_dir)

    max_epoch_model=0
    for model in all_model_dir:
        present_epoch_model = int(model.split("_")[0])
        if present_epoch_model > max_epoch_model:
            max_epoch_model = present_epoch_model
            PATH=path+str(model)
    print("Applied Model:",PATH)
    ###
    #PATH="model/projectPromptRoberta/99_model_AE.pkl"
    ###
    model = torch.load(PATH).to("cuda")
    model.eval()

    #load_task_prompt_dir = "task_prompt_emb/"+prompt_dir+"/task_prompt"
    prompt_emb_ = prompt_emb.reshape(int(prompt_emb.shape[0])*int(prompt_emb.shape[1]))
    prompt_emb_ = torch.nn.Parameter(prompt_emb_)
    prompt_emb_ = model(prompt_emb_.to("cuda"))
    prompt_emb_ = prompt_emb_.reshape(int(prompt_emb.shape[0]),int(prompt_emb.shape[1])).data

    return prompt_emb_




def init_all(config, gpu_list, checkpoint, mode, *args, **params):

    result = {}

    logger.info("Begin to initialize dataset and formatter...")
    if mode=="test":
        # init_formatter(config, ["test"], *args, **params)
        result["test_dataset"] = init_test_dataset(config, *args, **params)
    elif mode=="train" or mode=="valid":
        # init_formatter(config, ["train", "valid"], *args, **params)
        result["train_dataset"], result["valid_dataset"] = init_dataset(config, *args, **params)
        '''
        print("===================")
        print(result["train_dataset"])
        print(len(result["train_dataset"]))
        print("----")
        print(result["valid_dataset"])
        print(len(result["valid_dataset"]))
        print("===================")
        exit()
        '''
    else:
        print("Don't need to load data")

    logger.info("Begin to initialize models...")

    print(config.get("model", "model_name"))

    model = get_model(config.get("model", "model_name"))(config, gpu_list, *args, **params)
    #print(params) #{'local_rank': -1, 'prompt_emb_output': True}
    optimizer = init_optimizer(model, config, *args, **params)
    trained_epoch = 0
    global_step = 0


    '''
    if len(gpu_list) > 0:
        if params['local_rank'] < 0:
            model = model.cuda()
        else:
            ###
            #muti machines
            #model = model.to(gpu_list[params['local_rank']])

            #single machine
            model = model.to(params['local_rank'])
            ###

        try:
            ###
            #muti machines
            model = nn.parallel.DistributedDataParallel(model, device_ids=[params['local_rank']], output_device=params['local_rank'], find_unused_parameters = True)

            #single machine
            #model = nn.parallel.DistributedDataParallel(model, device_ids=gpu_list)
            #model = nn.parallel.DistributedDataParallel(model)
            ###
        except Exception as e:
            logger.warning("No init_multi_gpu implemented in the model, use single gpu instead.")
    '''




    #########
    #try:
    ##########
    #parameters = torch.load(checkpoint, map_location=lambda storage, loc: storage)
    if params["args"].checkpoint != None:
        parameters = torch.load(params["args"].checkpoint, map_location=lambda storage, loc: storage)

        if hasattr(model, 'module'):
            model.module.load_state_dict(parameters["model"])
        else:
            model.load_state_dict(parameters["model"])

        '''
        if torch.cuda.is_available() and mode=="train":
            model.cuda()
        else:
            pass
        '''

    else:
        pass


    ########################
    ########################
    ########################

    ########################
    ####Evalid will Open####
    ########################
    if mode=="valid" or mode=="Valid" or mode=="test" or mode=="Test":
        print("=========================")
        print(params)
        print("=========================")
        ###Replace or not
        if params["args"].replacing_prompt == None:
            print("=========================")
            print("Using original prompt emb")
            print("=========================")
            prompt_name = params["args"].config.split("/")[1].split(".")[0]
            #load_task_prompt_dir = "task_prompt_emb/"+prompt_name+"/task_prompt"
            #prompt_emb = torch.load(load_task_prompt_dir)
            if "Roberta" in prompt_name:
                prompt_emb = model.encoder.roberta.embeddings.prompt_embeddings.weight.data
            elif "Bert" in prompt_name:
                prompt_emb = model.encoder.bert.embeddings.prompt_embeddings.weight.data
            else:
                print("Warning: Use original prompt emb")

        elif params["args"].replacing_prompt == "Random" or params["args"].replacing_prompt == "random":
            print("=========================")
            print("Using random prompt emb")
            print("=========================")
            #prompt_emb = torch.nn.Parameter(torch.rand(100,768)).to("cuda")
            prompt_emb = torch.rand(100,768).to("cuda")
        else:
            print("=========================")
            print("Replace", params["args"].checkpoint.split("/")[1], "with", params["args"].replacing_prompt)
            print("=========================")
            load_task_prompt_dir = "task_prompt_emb/"+params["args"].replacing_prompt+"/task_prompt"
            prompt_emb = torch.load(load_task_prompt_dir)
        ###

        ###Using Project or not
        if params["args"].task_transfer_projector:
            load_model = params["args"].checkpoint.strip().split("/")[1]
            prompt_emb = recover_task_transfer_prompt(prompt_emb,load_model)
        elif params["args"].model_transfer_projector:
            load_model = params["args"].checkpoint.strip().split("/")[1]
            prompt_emb = recover_model_transfer_prompt(prompt_emb,load_model)
        elif params["args"].model_transfer_projector and params["args"].task_transfer_projector:
            print("init_tool.py: Cannot choose both task_project and model_project")
        else:
            print("No project")
            pass

        ##Put prompt emb back to model
        if prompt_emb != None:
            prompt_emb = torch.nn.Parameter(prompt_emb).to("cuda")

            ##Put prompt emb back to model
            if "Roberta" in params["args"].checkpoint:
                model.encoder.roberta.embeddings.prompt_embeddings.weight.data = prompt_emb
            elif "Bert" in params["args"].checkpoint:
                model.encoder.bert.embeddings.prompt_embeddings.weight.data = prompt_emb
            else:
                print("Wrong!!!")
                exit()
        else:
            print("=========================")
            print("Using original prompt emb")
            print("=========================")
            pass

    ########################
    #Return and Save prompt#
    ########################
    elif mode=="extract_prompt":
        print("=========================")
        print("Extract prompt emb")
        print("=========================")
        #mlm or not mlm
        save_name = params["args"].checkpoint.split("/")[1]

        if "Roberta" in save_name:
            prompt_emb = model.encoder.roberta.embeddings.prompt_embeddings.weight.data
        elif "Bert" in save_name:
            prompt_emb = model.encoder.bert.embeddings.prompt_embeddings.weight.data
        else:
            print("Wrong!!!")

        fp = str("task_prompt_emb/"+save_name)
        if os.path.exists(fp):
            print("Exist:",fp)
        else:
            os.mkdir(fp)
            print("Create:",fp)


        fp_dir = fp+"/task_prompt"
        print("save to:", fp_dir)
        torch.save(prompt_emb, fp_dir)
        print("!!!!!!!")
        print(prompt_emb.shape)
        print("!!!!!!!")
        print("Save prompt_emb_output")
        exit()


    ########################
    ####Train####
    ########################
    else:
        print("Mode: Train")
        pass
    ########################
    ########################
    ########################


    try:
        if mode == "train" or mode == "valid":
            trained_epoch = parameters["trained_epoch"]
            if config.get("train", "optimizer") == parameters["optimizer_name"]:
                optimizer.load_state_dict(parameters["optimizer"])
            else:
                logger.warning("Optimizer changed, do not load parameters of optimizer.")

            if "global_step" in parameters:
                global_step = parameters["global_step"]
    except:
        pass

    ###


    '''
    except Exception as e:

        information = "Cannot load checkpoint file with error %s" % str(e)
        if mode == "test":
            logger.error(information)
            raise e
        else:
            logger.warning(information)
    '''

    ############
    if len(gpu_list) > 0:
        if params['local_rank'] < 0:
            model = model.cuda()
        else:
            ###
            #muti machines
            model = model.to(gpu_list[params['local_rank']])

            #single machine
            #model = model.to(params['local_rank'])
            ###

        try:
            ###
            #muti machines
            model = nn.parallel.DistributedDataParallel(model, device_ids=[params['local_rank']], output_device=params['local_rank'], find_unused_parameters = True)

            #single machine
            #model = nn.parallel.DistributedDataParallel(model, device_ids=gpu_list)
            #model = nn.parallel.DistributedDataParallel(model)
            ###
        except Exception as e:
            logger.warning("No init_multi_gpu implemented in the model, use single gpu instead.")
    ############



    result["model"] = model
    if mode == "train" or mode == "valid":
        result["optimizer"] = optimizer
        result["trained_epoch"] = trained_epoch
        result["output_function"] = init_output_function(config)
        result["global_step"] = global_step

    logger.info("Initialize done.")


    return result
