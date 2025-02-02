# pip install requests

# source TORCHANDFLASK/bin/activate

import requests

resp = requests.post("http://127.0.0.1:5000/predict",
                     files={"file": open('cat.jpg','rb')})
print(resp.json())

resp = requests.post("http://127.0.0.1:5000/predict",
                     files={"file": open('dog.jpg','rb')})
print(resp.json())

# $ python requuuuest.py 
# {'class_id': 'n02123394', 'class_name': 'Persian_cat'}
# {'class_id': 'n02099601', 'class_name': 'golden_retriever'}

'''
$ pip show Flask
Name: Flask
Version: 3.1.0
Summary: A simple framework for building complex web applications.
Home-page: 
Author: 
Author-email: 
License: 
Location: /home/torch_in_flask/TORCHANDFLASK/lib/python3.10/site-packages
Requires: blinker, click, itsdangerous, Jinja2, Werkzeug
Required-by: 

$ pip show torch
Name: torch
Version: 2.6.0
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org/
Author: PyTorch Team
Author-email: packages@pytorch.org
License: BSD-3-Clause
Location: /home/torch_in_flask/TORCHANDFLASK/lib/python3.10/site-packages
Requires: filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvtx-cu12, sympy, triton, typing-extensions
Required-by: torchvision
'''