# import streamlit as st
# import pickle
# import numpy as np
# from skimage.io import imread
# from skimage.transform import resize
# from sklearn.svm import SVC
# import os

# # Load the trained model
# model_path = "C:/College/Projects/CGminiproject/model.p"  # Corrected path separator for Windows
# if os.path.exists(model_path):
#     model = pickle.load(open(model_path, 'rb'))
# else:
#     st.error("Model file not found.")
#     st.stop()

# # Define the categories
# categories = ['Down Syndrome', 'Goldenhar Syndrome', 'Crouzon Syndrome', 'Pfeiffer Syndrome', 'Treacher Collins Syndrome']

# # Streamlit app
# st.title('Syndrome Classifier')

# # Upload image
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Read and process the image
#     image = imread(uploaded_file)
#     image_resized = resize(image, (15, 15))
#     image_flattened = image_resized.flatten().reshape(1, -1)

#     # Predict the class
#     prediction = model.predict(image_flattened)
#     predicted_category = categories[prediction[0]]

#     # Display the result
#     st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
#     st.write(f'Predicted Syndrome: {predicted_category}')

#     # Display description based on the predicted category
#     if predicted_category == 'Down Syndrome':
#         st.write(
#             "**Title:** Down Syndrome\n\n"
#             "**Description:** Down syndrome is a genetic disorder caused by the presence of an extra copy of chromosome 21, resulting in developmental and physical challenges. Individuals with Down syndrome often have distinct facial features, such as a flat facial profile, slanted eyes, and a protruding tongue. The condition can also lead to various health issues, including heart defects, gastrointestinal problems, and a higher susceptibility to infections.\n\n"
#             "**Suggested Treatments:**\n"
#             "- **Early Intervention:** Programs focusing on physical, occupational, and speech therapy to address developmental delays.\n"
#             "- **Medical Care:** Regular monitoring and treatment for associated health issues, such as heart defects or hearing problems.\n"
#             "- **Educational Support:** Tailored educational plans and resources to support learning and cognitive development.\n"
#             "- **Social and Emotional Support:** Counseling and support groups for individuals and families to enhance social skills and emotional well-being.\n"
#             "- **Regular Check-ups:** Routine health check-ups to manage and monitor ongoing health needs."
#         )
#     elif predicted_category == 'Goldenhar Syndrome':
#         st.write(
#             "**Title:** Goldenhar Syndrome\n\n"
#             "**Description:** Goldenhar syndrome is a congenital condition characterized by abnormalities on one side of the face, including malformed ears, eye abnormalities, and facial asymmetry. It may also involve vertebral anomalies and hearing loss.\n\n"
#             "**Suggested Treatments:**\n"
#             "- **Surgical Intervention:** To correct facial deformities and improve function.\n"
#             "- **Medical Management:** Regular monitoring and treatment for associated health issues.\n"
#             "- **Rehabilitation:** Physical therapy to address motor and developmental delays.\n"
#             "- **Hearing Support:** Hearing aids or other interventions if hearing loss is present."
#         )
#     elif predicted_category == 'Crouzon Syndrome':
#         st.write(
#             "**Title:** Crouzon Syndrome\n\n"
#             "**Description:** Crouzon syndrome is a genetic disorder resulting in early fusion of skull bones, leading to a protruding forehead, wide-set eyes, and a beak-like nose. It can also result in dental problems and hearing loss.\n\n"
#             "**Suggested Treatments:**\n"
#             "- **Surgical Correction:** To address skull and facial bone abnormalities.\n"
#             "- **Orthodontic Treatment:** To manage dental issues.\n"
#             "- **Hearing Support:** Regular hearing tests and management if hearing loss is present.\n"
#             "- **Ongoing Monitoring:** Regular follow-ups with a multidisciplinary team to manage symptoms."
#         )
#     elif predicted_category == 'Pfeiffer Syndrome':
#         st.write(
#             "**Title:** Pfeiffer Syndrome\n\n"
#             "**Description:** Pfeiffer syndrome is a genetic disorder characterized by early fusion of skull bones, leading to a broad, short head, high forehead, and other facial anomalies. It can also involve intellectual disability and other systemic issues.\n\n"
#             "**Suggested Treatments:**\n"
#             "- **Surgical Intervention:** To correct skull and facial deformities.\n"
#             "- **Developmental Support:** Early intervention programs to address developmental delays.\n"
#             "- **Medical Care:** Management of associated health problems and regular check-ups.\n"
#             "- **Supportive Therapies:** Occupational and physical therapy to support developmental progress."
#         )
#     elif predicted_category == 'Treacher Collins Syndrome':
#         st.write(
#             "**Title:** Treacher Collins Syndrome\n\n"
#             "**Description:** Treacher Collins syndrome is a genetic disorder that affects the development of facial bones and tissues, leading to underdeveloped cheekbones, a small jaw, and malformed ears. It may also involve hearing loss and other developmental challenges.\n\n"
#             "**Suggested Treatments:**\n"
#             "- **Surgical Reconstruction:** To address facial deformities and improve function.\n"
#             "- **Hearing Support:** Hearing aids or other interventions to manage hearing loss.\n"
#             "- **Early Intervention:** Programs to address developmental delays and support learning.\n"
#             "- **Regular Monitoring:** Ongoing care to manage health issues and developmental progress."
#         )

import streamlit as st
import pickle
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from sklearn.svm import SVC
import os

# Load the trained model
model_path = "C:/College/Projects/CGminiproject/model.p"  # Corrected path separator for Windows
if os.path.exists(model_path):
    model = pickle.load(open(model_path, 'rb'))
else:
    st.error("Model file not found.")
    st.stop()

# Define the categories
categories = ['Down Syndrome', 'Goldenhar Syndrome', 'Crouzon Syndrome', 'Pfeiffer Syndrome', 'Treacher Collins Syndrome']

# Streamlit app
st.title('Syndrome Classifier')

# Introduction section
st.header('Introduction')
st.write(
    "Syndromes are a group of symptoms that collectively characterize a particular medical condition. They are often identified by a set of distinctive physical or behavioral traits that occur together."
)
st.write(
    "In this application, you can classify facial images to identify specific syndromes. The following syndromes can be classified here:"
)
st.write(
    "- **Down Syndrome:** A genetic disorder caused by an extra chromosome 21, leading to developmental and physical challenges.\n"
    "- **Goldenhar Syndrome:** A congenital condition characterized by abnormalities on one side of the face, including malformed ears and facial asymmetry.\n"
    "- **Crouzon Syndrome:** A genetic disorder resulting in early fusion of skull bones, leading to distinctive facial features such as a protruding forehead and wide-set eyes.\n"
    "- **Pfeiffer Syndrome:** A genetic disorder characterized by early fusion of skull bones, resulting in a broad, short head and other facial anomalies.\n"
    "- **Treacher Collins Syndrome:** A genetic disorder that affects facial bone and tissue development, leading to underdeveloped cheekbones, a small jaw, and malformed ears."
)

# Image upload section
st.header('Classify an Image')
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read and process the image
    image = imread(uploaded_file)
    image_resized = resize(image, (15, 15))
    image_flattened = image_resized.flatten().reshape(1, -1)

    # Predict the class
    prediction = model.predict(image_flattened)
    predicted_category = categories[prediction[0]]

    # Display the result
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write(f'Predicted Syndrome: {predicted_category}')

    # Display description based on the predicted category
    if predicted_category == 'Down Syndrome':
        st.write(
            "**Title:** Down Syndrome\n\n"
            "**Description:** Down syndrome is a genetic disorder caused by the presence of an extra copy of chromosome 21, resulting in developmental and physical challenges. Individuals with Down syndrome often have distinct facial features, such as a flat facial profile, slanted eyes, and a protruding tongue. The condition can also lead to various health issues, including heart defects, gastrointestinal problems, and a higher susceptibility to infections.\n\n"
            "**Suggested Treatments:**\n"
            "- **Early Intervention:** Programs focusing on physical, occupational, and speech therapy to address developmental delays.\n"
            "- **Medical Care:** Regular monitoring and treatment for associated health issues, such as heart defects or hearing problems.\n"
            "- **Educational Support:** Tailored educational plans and resources to support learning and cognitive development.\n"
            "- **Social and Emotional Support:** Counseling and support groups for individuals and families to enhance social skills and emotional well-being.\n"
            "- **Regular Check-ups:** Routine health check-ups to manage and monitor ongoing health needs."
        )
    elif predicted_category == 'Goldenhar Syndrome':
        st.write(
            "**Title:** Goldenhar Syndrome\n\n"
            "**Description:** Goldenhar syndrome is a congenital condition characterized by abnormalities on one side of the face, including malformed ears, eye abnormalities, and facial asymmetry. It may also involve vertebral anomalies and hearing loss.\n\n"
            "**Suggested Treatments:**\n"
            "- **Surgical Intervention:** To correct facial deformities and improve function.\n"
            "- **Medical Management:** Regular monitoring and treatment for associated health issues.\n"
            "- **Rehabilitation:** Physical therapy to address motor and developmental delays.\n"
            "- **Hearing Support:** Hearing aids or other interventions if hearing loss is present."
        )
    elif predicted_category == 'Crouzon Syndrome':
        st.write(
            "**Title:** Crouzon Syndrome\n\n"
            "**Description:** Crouzon syndrome is a genetic disorder resulting in early fusion of skull bones, leading to a protruding forehead, wide-set eyes, and a beak-like nose. It can also result in dental problems and hearing loss.\n\n"
            "**Suggested Treatments:**\n"
            "- **Surgical Correction:** To address skull and facial bone abnormalities.\n"
            "- **Orthodontic Treatment:** To manage dental issues.\n"
            "- **Hearing Support:** Regular hearing tests and management if hearing loss is present.\n"
            "- **Ongoing Monitoring:** Regular follow-ups with a multidisciplinary team to manage symptoms."
        )
    elif predicted_category == 'Pfeiffer Syndrome':
        st.write(
            "**Title:** Pfeiffer Syndrome\n\n"
            "**Description:** Pfeiffer syndrome is a genetic disorder characterized by early fusion of skull bones, leading to a broad, short head, high forehead, and other facial anomalies. It can also involve intellectual disability and other systemic issues.\n\n"
            "**Suggested Treatments:**\n"
            "- **Surgical Intervention:** To correct skull and facial deformities.\n"
            "- **Developmental Support:** Early intervention programs to address developmental delays.\n"
            "- **Medical Care:** Management of associated health problems and regular check-ups.\n"
            "- **Supportive Therapies:** Occupational and physical therapy to support developmental progress."
        )
    elif predicted_category == 'Treacher Collins Syndrome':
        st.write(
            "**Title:** Treacher Collins Syndrome\n\n"
            "**Description:** Treacher Collins syndrome is a genetic disorder that affects the development of facial bones and tissues, leading to underdeveloped cheekbones, a small jaw, and malformed ears. It may also involve hearing loss and other developmental challenges.\n\n"
            "**Suggested Treatments:**\n"
            "- **Surgical Reconstruction:** To address facial deformities and improve function.\n"
            "- **Hearing Support:** Hearing aids or other interventions to manage hearing loss.\n"
            "- **Early Intervention:** Programs to address developmental delays and support learning.\n"
            "- **Regular Monitoring:** Ongoing care to manage health issues and developmental progress."
        )
