import tensorflow as tf
import numpy as np
from visual import *

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

np.random.seed(100)
tf.random.set_seed(100)

def main():
    
    # 비선형 데이터 생성
    
    x_data = np.linspace(0, 10, 100)
    y_data = 1.5 * x_data**2 -12 * x_data + np.random.randn(*x_data.shape)*2 + 0.5
    
    '''
    1. 다층 퍼셉트론 모델을 만듭니다.
    '''
    
    model = tf.keras.models.Sequential([None])
    
    '''
    2. 모델 학습 방법을 설정합니다.
    '''
    
    model.compile(loss = None, optimizer = None)
    
    '''
    3. 모델을 학습시킵니다.
    ''' 
    
    history = None
    
    '''
    4. 학습된 모델을 사용하여 예측값 생성 및 저장
    '''
    
    predictions = None
    
    Visualize(x_data, y_data, predictions)
    
    return history, model

if __name__ == '__main__':
    main()
