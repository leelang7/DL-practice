import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.utils import to_categorical

import numpy as np
import matplotlib.pyplot as plt

def load_fashion_mnist():
    # Fashion MNIST 데이터셋을 불러옵니다.
    (train_X, train_y), (test_X, test_y) = fashion_mnist.load_data()

    # TODO: 이미지의 각 픽셀값을 0에서 1 사이로 정규화하세요.
    train_X = None
    test_X = None

    # TODO: 입력 데이터(trian_X, test_X)의 차원을 뒷쪽으로 하나 늘리세요.
    train_X = None
    test_X = None

    # TODO: 정수 형태로 이루어진 라벨 데이터를 one-hot encoding으로 바꾸세요.
    train_y = None
    test_y = None

    return train_X, train_y, test_X, test_y

def build_cnn_model(num_classes, input_shape):
    model = Sequential()

    # TODO: 지시사항 대로 CNN 모델을 만드세요.
    model.add(None)

    return model

def plot_loss(hist):
    # TODO: hist 객체에서 train loss와 valid loss를 불러오세요.
    train_loss = None
    val_loss = None
    epochs = np.arange(1, len(train_loss) + 1)

    fig, ax = plt.subplots()
    ax.set_xticks(list(epochs))
    # TODO: ax를 이용하여 train loss와 valid loss를 plot 하세요.
    None

    ax.legend(loc="upper right")
    ax.grid()
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")

    fig.savefig("loss.png")

def plot_accuracy(hist):
    # TODO: hist 객체에서 train accuracy와 valid accuracy를 불러오세요.
    train_acc = None
    val_acc = None
    epochs = np.arange(1, len(train_acc) + 1)

    fig, ax = plt.subplots()
    ax.set_xticks(list(epochs))
    # TODO: ax를 이용하여 train accuracy와와 valid accuracy와를 plot 하세요.
    None

    ax.legend(loc="lower right")
    ax.grid()
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Accuracy")

    fig.savefig("accuracy.png")

def main(cnn_model=None, epochs=5):
    # 랜덤 시드 고정을 위한 코드입니다. 수정하지 마세요!
    tf.random.set_seed(2021)

    train_X, train_y, test_X, test_y = load_fashion_mnist()
    if cnn_model is None:
        cnn_model = build_cnn_model(len(train_y[0]), train_X[0].shape)

    # TODO: 지시사항 대로 모델의 optimizer, loss, metrics을 설정하세요.
    None

    # TODO: 지시사항 대로 hyperparameter를 설정하여 모델을 학습하세요.
    None

    # TODO: Test loss와 test accuracy를 구하세요.
    None

    print(f"테스트 정확도: {test_accuracy * 100:.3f}%")

    plot_loss(hist)
    plot_accuracy(hist)

    return hist

if __name__ == '__main__':
    main()