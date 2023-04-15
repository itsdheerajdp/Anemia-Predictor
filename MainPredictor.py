import pickle
model=pickle.load(open("AnemiaPredictor.pkl", "rb"))
import numpy as np
import keras.utils as image
test_image=image.load_img('predict.png',target_size=(64,64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)
if result[0][0] == 1:
  prediction = 'Non Anemic'
else:
  prediction = 'Anemic'
print(prediction)