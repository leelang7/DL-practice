import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

# 모델에 대한 어떠한 정보도 정의하지 않습니다
# 오직 저장된 모델로부터 다양한 정보를 불러와 출력합니다.

print("학습하던 모델을 불러옵니다.")
# TODO: 학습하던 모델 불러오세요 
loaded_model = tf.keras.models.load_model("./afterfit")
loaded_model.summary()

# TODO: 5번째 체크 포인트를 불러오세요
loaded_ckpt = tf.keras.models.load_model("./checkpoints/cp-0005.ckpt")
loaded_ckpt.summary()