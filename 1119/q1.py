import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.keras import layers, Sequential

# TODO: [지시사항 1번] 첫번째 모델을 완성하세요.
def build_model1():
    model = Sequential()
    
    model.add(layers.Embedding(None, None))
    model.add(layers.SimpleRNN(None))
    
    return model

# TODO: [지시사항 2번] 두번째 모델을 완성하세요.
def build_model2():
    model = Sequential()
    
    model.add(None)
    
    return model
    
def main():
    model1 = build_model1()
    print("=" * 20, "첫번째 모델", "=" * 20)
    model1.summary()
    
    print()
    
    model2 = build_model2()
    print("=" * 20, "두번째 모델", "=" * 20)
    model2.summary()

if __name__ == "__main__":
    main()