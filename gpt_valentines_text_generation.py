"""
Use GPT-2 to complete paragraphs
=======================================================
Use GPT-2 to complete the sentence "I love you because"

Requires pytorch which can be installed with CPU only
from https://pytorch.org/

Requirements
:requires: pytorch
:requires: transformers
"""

# Install HuggingFace transformers by doing "pip install transformers"
# Then import the library
from transformers import pipeline

# Build text generation pipeline
text_generation = pipeline("text-generation")

# Define the text to start with
prefix_text = "I love you because"

# Start generating text
# If do_sample=False, the sentences remain the same when code is re-run
generated_text = text_generation(prefix_text, max_length=25, do_sample=True)[0]
print(generated_text["generated_text"])