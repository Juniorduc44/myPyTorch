## first create python environment
- python -m venv venv
- .\venv\Scripts\activate


## second load the environment with pip
- pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
- pip install git+https://github.com/huggingface/diffusers transformers accelerate

## Make sure torch is running along with cuda
- torch.cuda.is_available()