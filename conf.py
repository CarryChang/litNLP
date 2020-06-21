# -*- coding: utf-8 -*-
# @Time: 2020/6/20 0020 0:49
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
# sentence length
maxlen = 100
# 使用字符级大大减少了字典的长度
max_words = 1000
embedding_dim = 300
# tokenize path
model_path = 'sa_model'
tokenize_path = 'sa_model/tokenizer.pickle'
# sa model path
sa_model_path = 'sa_model/c_cnn.h5'
sa_model_path_m = 'sa_model/c_cnn_m.h5'
# 默认类别
num_classes = 2
