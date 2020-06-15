from tensorflow.keras.applications import vgg16
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.models import Model
from tensorflow.keras.applications.imagenet_utils import preprocess_input

from PIL import Image
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

imgs_path = "imgs/"
imgs_model_width, imgs_model_height = 224, 224

nb_closest_images = 5

files = [imgs_path + x for x in os.listdir(imgs_path) if "jpeg" in x]

#print("number of images:",len(files))


from tensorflow import keras
from tensorflow.keras.models import Model

vgg_model = keras.models.load_model('model')

feat_extractor = Model(inputs=vgg_model.input, outputs=vgg_model.get_layer("fc2").output)

# print the layers of the CNN
feat_extractor.summary()

#numpy_image = img_to_array(original)
# convert the image / images into batch format
# expand_dims will add an extra dimension to the data at a particular axis
# we want the input matrix to the network to be of the form (batchsize, height, width, channels)
# thus we add the extra dimension to the axis 0.
#image_batch = np.expand_dims(numpy_image, axis=0)
#print('image batch size', image_batch.shape)

# prepare the image for the VGG model
#processed_image = preprocess_input(image_batch.copy())


importedImages = []

for f in files:
    filename = f
    original = load_img(filename, target_size=(224, 224))
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    
    importedImages.append(image_batch)
    
images = np.vstack(importedImages)

processed_imgs = preprocess_input(images.copy())

imgs_features = feat_extractor.predict(processed_imgs)

print("features successfully extracted!")
print(imgs_features.shape)

cosSimilarities = cosine_similarity(imgs_features)

# store the results into a pandas dataframe

cos_similarities_df = pd.DataFrame(cosSimilarities, columns=files, index=files)
cos_similarities_df.head()

# function to retrieve the most similar products for a given one


def retrieve_most_similar_products(given_img):

    #print("-----------------------------------------------------------------------")
    #print("original product:")

    original = load_img(given_img, target_size=(imgs_model_width, imgs_model_height))
    #plt.imshow(original)
    #plt.show()

    #print("-----------------------------------------------------------------------")
    #print("most similar products:")

    closest_imgs = cos_similarities_df[given_img].sort_values(ascending=False)[1:nb_closest_images+1].index
    #print(closest_imgs)
    closest_imgs_scores = cos_similarities_df[given_img].sort_values(ascending=False)[1:nb_closest_images+1]
    closest_imgs=list(closest_imgs)
    #print(closest_imgs)
    for i in range(len(closest_imgs)):
        closest_imgs[i]=closest_imgs[i].replace("imgs/","https://github.com/niharika412/product_recommendations/blob/master/images/")
        closest_imgs[i]+='?raw=true'
		
    closest_imgs_scores=list(closest_imgs_scores)
    closest_imgs+=closest_imgs_scores
    return closest_imgs
   