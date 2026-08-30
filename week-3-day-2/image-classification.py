from transformers import pipeline
from PIL import Image
import requests
from io import BytesIO


def load_image_from_url(url):
    response = requests.get(url, timeout=30)
    return Image.open(BytesIO(response.content)).convert("RGB")


def main():

    print("=" * 70)
    print("IMAGE CLASSIFICATION EXPERIMENT")
    print("=" * 70)

    classifier = pipeline(
        "image-classification",
        model="google/vit-base-patch16-224",
        device=0
    )

    # Replace these with your own image URLs or local images
    image_urls = {
        "Example Image 1": "https://images.unsplash.com/photo-1558788353-f76d92427f16",
        "Example Image 2": "https://images.unsplash.com/photo-1517849845537-4d257902454a",
    }

    for image_name, url in image_urls.items():

        print(f"\nImage: {image_name}")

        try:
            image = load_image_from_url(url)

            predictions = classifier(image, top_k=3)

            for rank, prediction in enumerate(predictions, start=1):
                print(
                    f"{rank}. {prediction['label']} "
                    f"({prediction['score']:.4f})"
                )

        except Exception as e:
            print(f"Error processing image: {e}")


if __name__ == "__main__":
    main()