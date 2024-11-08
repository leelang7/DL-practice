import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def main():
    
    # XOR 문제를 위한 데이터 생성
    
    training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")
    target_data = np.array([[0],[1],[1],[0]], "float32")
    
    '''
    1. 다층 퍼셉트론 모델을 생성합니다.
    '''
    
    model = None
    model.add(None)
    
    '''
    2. 모델의 손실 함수, 최적화 방법, 평가 방법을 설정합니다.
    '''
    
    model.compile(None)
    
    '''
    3. 모델을 학습시킵니다. epochs를 자유롭게 설정해보세요.
    ''' 
    
    hist = None
    
    score = hist.history['binary_accuracy'][-1]
    
    print('최종 정확도: ', score*100, '%')
    
    return hist

if __name__ == "__main__":
    main()
