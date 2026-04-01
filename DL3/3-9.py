import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.keras import layers, Sequential, Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.utils import to_categorical

import numpy as np

def load_fashion_mnist():
    # Fashion MNIST 데이터셋을 불러옵니다.
    (X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

    # TODO: [지시사항 1번] 이미지의 각 픽셀값을 0에서 1 사이로 정규화하세요.
    X_train = None
    X_test = None

    # TODO: [지시사항 1번] 입력 데이터(trian_X, X_test)의 차원을 뒷쪽으로 하나 늘리세요.
    X_train = None
    X_test = None

    # TODO: [지시사항 1번] 정수 형태로 이루어진 라벨 데이터를 one-hot encoding으로 바꾸세요.
    y_train = None
    y_test = None

    return X_train, y_train, X_test, y_test
    
def build_vgg_model(num_classes, input_shape):
    model = Sequential()
    
    # TODO: [지시사항 2번] VGG-11 모델을 만드세요.
    model.add(None)
    
    return model
    
def main(model=None, epochs=2):
    tf.random.set_seed(2022)
    
    num_classes = 10
    X_train, y_train, X_test, y_test = load_fashion_mnist()
    input_shape = X_train[0].shape
    
    if model is None:
        model = build_vgg_model(num_classes, input_shape)
    
    # TODO: [지시사항 3번] Optimizer, 손실 함수, 평가 지표를 설정하세요.
    optimizer = None
    None
    
    # TODO: [지시사항 4번] 모델 학습을 위한 hyperparameter를 설정하세요.
    hist = None
    
    # TODO: [지시사항 5번] Test 정확도를 구하세요.
    _, test_accuracy = None
    
    print(f"테스트 정확도: {test_accuracy * 100:.3f}%")
    
    return optimizer, hist, test_accuracy

if __name__ == "__main__":
    main()