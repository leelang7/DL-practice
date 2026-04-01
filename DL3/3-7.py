import tensorflow as tf
from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dropout, Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.utils import to_categorical

import numpy as np
import matplotlib.pyplot as plt

def load_cifar10():
    # CIFAR-10 데이터셋을 불러옵니다.
    train_X = np.load("cifar10_train_X.npy")
    train_y = np.load("cifar10_train_y.npy")
    test_X = np.load("cifar10_test_X.npy")
    test_y = np.load("cifar10_test_y.npy")

    # TODO: 이미지의 각 픽셀값을 0에서 1 사이로 정규화하세요.
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

def plot_loss(hist, fig_name="loss"):
    # TODO: hist 객체에서 train loss와 valid loss를 불러오세요.
    train_loss = None
    val_loss = None
    epochs = np.arange(1, len(train_loss) + 1)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xticks(list(epochs))
    # TODO: ax를 이용하여 train loss와 valid loss를 plot 하세요.
    None

    ax.legend(loc="upper right")
    ax.grid()
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")

    fig.savefig(f"{fig_name}.png")

def plot_accuracy(hist, fig_name="accuracy"):
    # TODO: hist 객체에서 train accuracy와 valid accuracy를 불러오세요.
    train_acc = None
    val_acc = None
    epochs = np.arange(1, len(train_acc) + 1)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xticks(list(epochs))
    # TODO: ax를 이용하여 train accuracy와와 valid accuracy와를 plot 하세요.
    None

    ax.legend(loc="lower right")
    ax.grid()
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Accuracy")

    fig.savefig(f"{fig_name}.png")

def get_topk_accuracy(test_y, pred_y, k=1):
    # TODO: one-hot encoding으로 이루어진 test_y를 다시 정수 라벨 형식으로 바꾸세요.
    true_labels = None

    # TODO: pred_y를 확률값이 작은 것에서 큰 순서로 정렬하세요
    pred_labels = None

    correct = 0
    for true_label, pred_label in zip(true_labels, pred_labels):
        # TODO: 현재 pred_label에서 확률값이 가장 큰 라벨 k개를 가져오세요
        cur_preds = None

        if true_label in cur_preds:
            correct += 1

    # TODO: Top-k accuarcy를 구하세요.
    topk_accuracy = None

    return topk_accuracy

def main(model=None, epochs=30):
    # 랜덤 시드 고정을 위한 코드입니다. 수정하지 마세요!
    tf.random.set_seed(2021)

    train_X, train_y, test_X, test_y = load_cifar10()
    if model is None:
        model = build_cnn_model(len(train_y[0]), train_X[0].shape)
    model.summary()

    # TODO: 지시사항 대로 모델의 optimizer, loss, metrics을 설정하세요.
    optimizer = None
    None

    # TODO: 지시사항 대로 hyperparameter를 설정하여 모델을 학습하세요.
    hist = None

    # TODO: Test 데이터를 적용했을 때 예측 확률을 구합니다.
    pred_y = None
    top1_accuracy = get_topk_accuracy(test_y, pred_y)
    top3_accuracy = get_topk_accuracy(test_y, pred_y, k=3)
    
    print("Top-1 Accuracy: {:.3f}%".format(top1_accuracy * 100))
    print("Top-3 Accuracy: {:.3f}%".format(top3_accuracy * 100))

    # TODO: Test accuracy를 구하세요.
    _, test_accuracy = None

    # Tensorflow로 구한 test accuracy와 top1 accuracy는 같아야 합니다.
    # 다만 부동 소수점 처리 문제로 완전히 같은 값이 나오지 않는 경우도 있어서
    # 소수점 셋째 자리까지 반올림하여 비교합니다.
    assert round(test_accuracy, 3) == round(top1_accuracy, 3)

    plot_loss(hist)
    plot_accuracy(hist)

    return optimizer, hist, pred_y, test_accuracy

if __name__ == '__main__':
    main()