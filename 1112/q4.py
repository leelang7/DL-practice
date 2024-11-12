import tensorflow as tf
from tensorflow.keras import Sequential, layers

def build_vgg16():
    # Sequential 모델 선언
    model = Sequential()
    
    # TODO: [지시시항 1번] 첫번째 Block을 완성하세요.
    model.add(layers.Conv2D(None, input_shape=(224, 224, 3)))
    model.add(layers.Conv2D(None))
    model.add(layers.MaxPooling2D(None))
    
    # TODO: [지시시항 2번] 두번째 Block을 완성하세요.
    model.add(layers.Conv2D(None))
    model.add(layers.Conv2D(None))
    model.add(layers.MaxPooling2D(None))
    
    # TODO: [지시시항 3번] 세번째 Block을 완성하세요.
    model.add(layers.Conv2D(None))
    model.add(layers.Conv2D(None))
    model.add(layers.Conv2D(None))
    model.add(layers.MaxPooling2D(None))
    
    # TODO: [지시시항 4번] 네번째 Block을 완성하세요.
    model.add(layers.Conv2D(None))
    model.add(layers.Conv2D(None))
    model.add(layers.Conv2D(None))
    model.add(layers.MaxPooling2D(None))
    
    # TODO: [지시시항 5번] 다섯번째 Block을 완성하세요.
    None
    
    # Fully Connected Layer
    model.add(layers.Flatten())
    model.add(layers.Dense(4096, activation="relu"))
    model.add(layers.Dense(4096, activation="relu"))
    model.add(layers.Dense(1000, activation="softmax"))
    
    return model

def main():
    model = build_vgg16()
    model.summary()
    
if __name__ == "__main__":
    main()
