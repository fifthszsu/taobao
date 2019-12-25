from svm import *
from svmutil import *


def train_svm_model():
    """
    训练并生成model文件
    :return:
    """
    svm_root='E:/Python Project/Resource/svmdata'
    model_path=svm_root+'/model'
    y, x = svm_read_problem(svm_root + '/train_pix_feature_xy.txt')
    model = svm_train(y, x)
    svm_save_model(model_path, model)


def svm_model_test():
    """
    使用测试集测试模型
    :return:
    """
    svm_root='E:/Python Project/Resource/svmdata'
    model_path=svm_root+'/model'
    yt, xt = svm_read_problem(svm_root + '/last_test_pix_xy_8.txt')
    model = svm_load_model(model_path)
    p_label, p_acc, p_val = svm_predict(yt, xt, model)#p_label即为识别的结果
    cnt = 0
    for item in p_label:
        print('%d' % item, end=',')
        cnt += 1
        if cnt % 8 == 0:
            print('')    

if __name__ == '__main__':
#    train_svm_model()
    svm_model_test()