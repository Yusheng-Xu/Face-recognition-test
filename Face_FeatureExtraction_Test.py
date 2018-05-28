#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 19:53:28 2018

@author: Yusheng Xu
"""
import libface_image_to_feature
import libface_name_parse

# License path
str_license_pathname="cipher_license_180124.txt"

# Data path
str_data_paths = '/home/yushengxu/Documents/HeisAI_SDK_PY/Data/Aaron_Eckhart'

# Model path    
str_model_path = '/home/yushengxu/Documents/HeisAI_SDK_PY/Model'
    
# Image to Feature
output_features =libface_image_to_feature.face_image_to_feature(str_license_pathname,str_model_path,str_data_paths);

# Name of images
output_names =libface_name_parse.face_image_to_names(str_data_paths);

# Results
print(output_features)
print(output_names)
