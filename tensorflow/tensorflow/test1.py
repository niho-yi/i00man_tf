import tensorflow as tf

# 변수와 상수를 이용한 연산
var1 = tf.Variable([5.0], dtype=tf.float32)
const1 = tf.constant([10.0], dtype=tf.float32)
session = tf.Session()
init = tf.global_variables_initializer()
# 변수는 반드시 초기화해서 사용한다
session.run(init)
print(session.run(var1 * const1))  # [50.]
print('-------------')
session.run(var1.assign([10.0]))
print(session.run(var1)) # [10.]

# 플레이스 홀더를 이용한 연산

p1 = tf.placeholder(dtype=tf.float32)
p2 =  tf.placeholder(dtype=tf.float32)

t1 = p1 * 3
t2 = p1 * p2
session = tf.Session()
print(session.run(t2, {p1 : 4.0, p2: [2.0,5.0]}))
# [ 8. 20.]