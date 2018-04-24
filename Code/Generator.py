import tensorflow as tf
import numpy as np
#z = tf.Variable(tf.random([5,1],2,14))

with tf.Session() as sess:
    
    z_1 = tf.Variable(np.random.randint(2,14,size=(5,1)))
    z_2 = tf.Variable(np.random.randint(0,3,size=(5,1)))
    
    tf.initialize_all_variables().run()
    print(z_1.eval(sess), z_2.eval(sess))
    