import openai
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials



subscription_key = ""
endpoint = ""



api_key = ""
openai.api_key = api_key



#image
credentials=CognitiveServicesCredentials(subscription_key)
computervision_client=ComputerVisionClient(endpoint,credentials)
image_path="banana.jpg"

#vision
with open(image_path,"rb") as image_file:
    image_analysis=computervision_client.analyze_image_in_stream(
    image=image_file,
    visual_features=[VisualFeatureTypes.description]
    )


image_description=image_analysis.description.captions[0].text
custom_description=f"this image is about{image_description}."
#print("custome description",custom_description)



#generate
prompt=f"generate description for the givenn image:{custom_description}"

response=openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=200
)


description=response.choices[0].text.strip()
print(description)
