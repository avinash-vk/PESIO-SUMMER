import tensorflow as tf

#loading the datasets
mnist = tf.keras.datasets.fashion_mnist #predefined dataset to classify clothes/shoes etc
(train_x, train_y), (test_x, test_y) = mnist.load_data() 

#normalizing
train_x  = train_x / 255.0
test_x= test_x / 255.0 

#model design
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), tf.keras.layers.Dense(128, activation=tf.nn.relu),tf.keras.layers.Dense(10, activation=tf.nn.softmax)]) 

#training
model.compile(optimizer = tf.train.AdamOptimizer(),loss = 'sparse_categorical_crossentropy', metrics=['accuracy']) 
model.fit(train_x, train_y, epochs=5)  

#printing accuracy
print(model.evaluate(test_x, test_y)[1]) 
