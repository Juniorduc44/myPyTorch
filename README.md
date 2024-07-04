## first create python environment
    python -m venv venv
 ### On windows type the following in CMD
    .\venv\Scripts\activate
 ### On linux type the following
    source venv/bin/activate


## second load the environment with pip
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
    
    pip install git+https://github.com/huggingface/diffusers transformers accelerate

## Make sure torch is running along with cuda
- torch.cuda.is_available()

## Verify CUDA is installed
    sudo apt install nvidia-cuda-toolkit
 ### Then type "bash verifyCUDA.sh" in the terminal or command line