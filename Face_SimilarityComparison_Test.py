#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:46:57 2018

@author: yushengxu
"""
import libface_image_to_feature
import libface_features_to_similarity
import libface_name_parse

# License path
str_license_pathname="cipher_license_180124.txt"

# Data path
str_data_refer_paths = '/home/yushengxu/Documents/HeisAI_SDK_PY/Data/Tom_Hanks_Target'
str_data_retrieve_paths = '/home/yushengxu/Documents/HeisAI_SDK_PY/Data/Tom_Hanks_Check'

# Model path    
str_model_path = '/home/yushengxu/Documents/HeisAI_SDK_PY/Model'

# Features of reference image
reference_features = libface_image_to_feature.face_image_to_feature(str_license_pathname,str_model_path,str_data_refer_paths);
# Name of ref image
reference_name =libface_name_parse.face_image_to_names(str_data_refer_paths);

# Features of retrieved images   
retrieved_features= libface_image_to_feature.face_image_to_feature(str_license_pathname,str_model_path,str_data_retrieve_paths);
# Name of retrieved images
retrieved_names =libface_name_parse.face_image_to_names(str_data_retrieve_paths);    

# Features to Similarity
output_similarities=libface_features_to_similarity.face_features_to_similarity(str_license_pathname,reference_features,retrieved_features);

#Results
print(reference_name)
print(retrieved_names)
print(output_similarities)


