import numpy as np
from PIL import Image

from tensorflow.keras.preprocessing import image

from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)

model = MobileNetV2(weights='imagenet')


def analyze_food_image(img_path):

    try:

        img = image.load_img(
            img_path,
            target_size=(224, 224)
        )

        x = image.img_to_array(img)

        x = np.expand_dims(x, axis=0)

        x = preprocess_input(x)

        preds = model.predict(x)

        decoded = decode_predictions(preds, top=5)[0]

        # GET LABELS
        labels = []

        for item in decoded:
            labels.append(item[1].lower())

        # TOP CONFIDENCE
        confidence = round(float(decoded[0][2]) * 100)

        print("AI LABELS:", labels)
        print("CONFIDENCE:", confidence)

        # STRICT FOOD KEYWORDS
        FOOD_KEYWORDS = [

            # meals
            "pizza",
            "burger",
            "hotdog",
            "sandwich",
            "spaghetti",
            "carbonara",
            "meatloaf",

            # fruits
            "banana",
            "apple",
            "orange",
            "lemon",
            "pineapple",

            # vegetables
            "broccoli",
            "cauliflower",
            "mushroom",
            "cucumber",

            # containers
            "plate",
            "bowl",

            # bakery
            "bagel",
            "pretzel",

            # food items
            "icecream",
            "guacamole",
            "consomme",
            "cheeseburger"
        ]

        # COUNT MATCHES
        food_matches = 0

        for label in labels:

            for keyword in FOOD_KEYWORDS:

                if keyword in label:
                    food_matches += 1

        # DETERMINE RESULT
        if food_matches >= 2 and confidence >= 40:

            if confidence >= 85:
                condition = "Fresh"

            elif confidence >= 65:
                condition = "Medium"

            else:
                condition = "Unsafe"

        else:

            condition = "Not Food"
            confidence = 10

        return {
            "condition": condition,
            "score": confidence,
            "labels": labels
        }

    except Exception as e:

        print("AI ERROR:", e)

        return {
            "condition": "Detection Failed",
            "score": 0,
            "labels": []
        }

