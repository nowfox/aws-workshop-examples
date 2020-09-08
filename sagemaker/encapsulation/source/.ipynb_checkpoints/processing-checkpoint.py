import os
import shutil
import numpy as np
import glob
import random
from shutil import copyfile
    
    
def processing_data(training_dir, validation_dir, testing_dir, validation_rate=0.1,  testing_rate=0.1):
    files = os.listdir(training_dir)
    for file in files :
        dir_path = os.path.join(os.path.join(input_dir, file))
        if os.path.isdir(dir_path):
            print('处理 ：', dir_path)
            get_filelist(dir_path, file, testing_rate, validation_rate, validation_dir, test_dir, train_dir)
            
            
    train_count = get_all_count(train_dir)
    validation_count = get_all_count(validation_dir)
    test_count = get_all_count(test_dir)  
    
    label_list = []
    for file_name in os.listdir(training_dir):
        if os.path.isdir(os.path.join(training_dir , file_name)):
            label_list.append(file_name)
    label_list.sort()
    
    
    print("==================================================")
    print('train count        : ', train_count)
    print('validation count   : ', validation_count)
    print('test count         : ', test_count)
    print("Label: ", label_list)
    print("==================================================")
    return label_list
    
    
def get_all_count(dir_path):
    files = os.listdir(dir_path)
    count = 0 
    for file in files :
        if os.path.isdir(dir_path):
            label_dir = os.path.join(dir_path, file)
            images = os.listdir(label_dir)
            tmp_count = len(images)
            #print('{}   {}'.format(label_dir, tmp_count))
            count += tmp_count
    return count


    
def copy_file(file_path, target_path, label_name, item ):
#     print('file: {} -> target_path {} '.format(file_path, target_path))
    target_dir = os.path.join(target_path, label_name)
    if not os.path.exists(target_dir): 
        os.mkdir(target_dir)
        #print(file_path, os.path.join(target_dir, item))

    copyfile(file_path, os.path.join(target_dir, item))

def get_filelist(dir_path, label_name, test_rate, val_rate, validation_dir, test_dir, train_dir):
    
    types = ('*.jpg', '*.png', '*.jpeg', '*.jpg', '*.PNG', '*.JPEG')
    files = []
    for file in types:
        files.extend(glob.glob(os.path.join(dir_path, file)))
    
    files = os.listdir(dir_path)
    #print("------------- file count: ", len(files))
    random.shuffle(files)
    count = len(files)
    
    val_count = int(count * val_rate)
    test_count = int(count * test_rate)
    #print('val count ', val_count)
    #print('test_count ', test_count)
    
    val_list = files[0:val_count]
    test_list = files[val_count: val_count + test_count]
    train_list = files[val_count + test_count: ]
    #print('train list len: ', len(train_list))
    
    for item in val_list:
        copy_file(os.path.join(os.path.join(dir_path, item)) , validation_dir, label_name, item ) 
    for item in test_list:
        copy_file(os.path.join(os.path.join(dir_path, item)) , test_dir,label_name, item)
    for item in train_list:
        copy_file(os.path.join(os.path.join(dir_path, item)) , train_dir, label_name, item) 
    
    
    
    
def main():
    processing_data(input_dir, training_data_dir)
    
    
if __name__ == '__main__':
    main()