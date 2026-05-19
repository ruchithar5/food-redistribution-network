from PIL import Image
import numpy as np
import random

def analyze_food_image(image_path):
    """
    Dummy AI food quality analysis
    """

    try:
        img = Image.open(image_path)

        # Resize image
        img = img.resize((224, 224))

        # Convert to numpy
        img_array = np.array(img)

        # Dummy AI logic
        quality_score = random.randint(70, 98)

        if quality_score >= 90:
            condition = "Excellent"
        elif quality_score >= 80:
            condition = "Fresh"
        elif quality_score >= 70:
            condition = "Average"
        else:
            condition = "Poor"

        return {
            "score": quality_score,
            "condition": condition
        }

    except Exception as e:
        return {
            "score": 50,
            "condition": "Unknown"
        }