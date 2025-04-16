from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# seed를 고정하는 코드입니다.
# 정확한 채점을 위하여 값을 변경하지 마세요!
np.random.seed(100)
tf.random.set_seed(100)

def MLP(x_train, y_train):
    # 1-1. 인공 신경망 분류 모델을 생성합니다.
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    # 1-2. 모델을 학습할 optimizer와 loss를 설정합니다.
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
                  
    # 1-3. 모델을 학습할 epochs 값을 설정합니다.
    
    model.fit(x_train, y_train, epochs=20)
    
    return model
'''
0 티셔츠/탑
1 바지
2 스웨터
3 드레스
4 코트
5 샌들
6 셔츠
7 스니커즈
8 가방
9 발목 부츠
'''    
def main():
    x_train = np.loadtxt('./data/train_images.csv', delimiter =',', dtype = np.float32)
    y_train = np.loadtxt('./data/train_labels.csv', delimiter =',', dtype = np.float32)
    x_test = np.loadtxt('./data/test_images.csv', delimiter =',', dtype = np.float32)
    y_test = np.loadtxt('./data/test_labels.csv', delimiter =',', dtype = np.float32)
    
    # 이미지 데이터를 0~1범위의 값으로 바꾸어 줍니다.
    
    x_train, x_test = x_train / 255.0, x_test / 255.0
    model = MLP(x_train,y_train)
    print(model.summary())
    
    # 학습한 모델을 test 데이터를 활용하여 평가합니다.
    
    loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
    
    print('\nTEST 정확도 :', test_acc)
    
    # 임의의 3가지 test data의 이미지와 레이블값을 출력하고 예측된 레이블값 출력
    
    predictions = model.predict(x_test)
    rand_n = np.random.randint(100, size=3)
    
    for i in rand_n:
        img = x_test[i].reshape(28,28) # 이미지로 보려고
        plt.imshow(img,cmap="gray")
        plt.show()
        plt.savefig("fashion_test.png")
        print("Label: ", y_test[i])
        print("Prediction: ", np.argmax(predictions[i]))
        
if __name__ == "__main__":
    main()