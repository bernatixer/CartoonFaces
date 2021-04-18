# Cartoon Faces

_Our project lies within the field of image-to-image translation, I2I: translate an image from a domain (e.g. a picture of a real person) to a different domain (e.g. a human cartoon face). We implement a GAN model for single domain generation of cartoon faces, and a XGAN model (from scratch) able to translate between multiple domains (from human to cartoon and vice-versa). Our implementation was informed by many experiments conducted during the execution of the proposal, regarding aspects such as data preprocessing, testing of various combinations of model parameters, and comparisons with other models in the state-of-the-art of the literature. We fully achieved the milestones that we committed in the pre-assessment of the project. The GitHub repository of the project contains the TensorFlow codes necessary to replicate our implementation regarding our main model, the XGAN. Additional experimental results are documented in this report. _

<p align="center">
  <img src="progression.gif" width="275" height="500"/>
</p>

## Implementation
Domain to domain translation using Generative Adversarial Networks (GANs)
### Installation
We recommend to use a virtual environment (venv). Steps to install the project:
```
# Create venv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install project requirements
pip3 install -r requirements.txt
```
### Train the model
```
# make sure your venv is activated
source venv/bin/activate

# start training the model
python3 training.py
```

### RESULTS
The results in the `RESULTS` folder and a new folder is also created on each execution. Please you should not push this results to the project (everyone has their own results)
