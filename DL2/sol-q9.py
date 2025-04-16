import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#1. 두 실수와 연산 종류를 입력받는 함수입니다. 코드를 살펴보세요.
def insert():
    x = float(input('정수 또는 실수를 입력하세요. x : '))
    y = float(input('정수 또는 실수를 입력하세요. y : '))
    cal = input('어떤 연산을 할것인지 입력하세요. (+, -, *, /)')
    return x, y, cal

# 사칙연산 함수를 구현해보세요.
def calcul(x,y,cal):
    # 더하기
    if cal == '+':
        result = tf.add(x,y)
    # 빼기
    elif cal == '-':
        result = tf.subtract(x,y)
    # 곱하기
    elif cal == '*':
        result = tf.multiply(x,y)
        # 나누기
    elif cal == '/':
        result = tf.truediv(x,y)
    return result.numpy()
    
def main():

    x, y, cal = insert()
    print(calcul(x,y,cal))
    
    
if __name__ == "__main__":
    main()
    
    