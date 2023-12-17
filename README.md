# CryptoBERT with FastAPI and Docker
In the volatile world of cryptocurrency trading, understanding market sentiment is crucial. CryptoBERT leverages the power of advanced NLP using BERT models to analyze and interpret sentiments from vast amounts of crypto-related text data. This solution provides traders, analysts, and enthusiasts with real-time insights, enabling informed decision-making in the fast-paced crypto market. Our integration with FastAPI and Docker ensures high performance, scalability, and ease of deployment, making CryptoBERT a state-of-the-art tool for sentiment analysis.

## NLP Sentiment Analysis for Cryptocurrency
This project is powered with CryptoBERT, an advanced NLP sentiment analysis service powered by BERT (Bidirectional Encoder Representations from Transformers) specifically tailored for cryptocurrency markets. This project combines a NLP model with the efficiency of FastAPI and the scalability of Docker to provide real-time sentiment analysis as a microservice.

## Features

* BERT for Sentiment Analysis: Utilizes a fine-tuned BERT model to analyze sentiment in cryptocurrency-related text, offering deep insights into market sentiment. 
* FastAPI Integration: Built on FastAPI, CryptoBERT ensures high performance, easy scalability, and quick responses, making it ideal for real-time applications. 
* Docker Support: Packaged as a Docker container, CryptoBERT is easy to deploy anywhere, ensuring consistency across different environments. 
* Microservice Architecture: Designed as a microservice, it seamlessly integrates with existing systems and allows for distributed deployment. 
* Comprehensive Sentiment Metrics: Provides detailed sentiment scores and distribution, giving a nuanced understanding of market sentiment. 
* Ready for Crypto Market Analysis: Tailored for cryptocurrency market data, it's a perfect tool for traders, analysts, and enthusiasts.

## Prerequisite
1. Python 3.11
2. Docker Engine (Docker CE)
3. Git
4. Git LFS (Large File Storage)
5. CryptoBERT pre-trained NLP model

## Quick Start

### Windows Specific Notes!

Windows users should use PowerShell or Git Bash for running the given shell commands.
Ensure `Docker Desktop for Windows` is set to use `Linux` containers.
For Windows systems, Python commands sometimes require using py instead of `python` or `python3`.


### Clone this repo
```commandline
git clone git@github.com:SMARTSHEEP-IO/crypto-bert-spike.git
```
### Clone the model repo
```commandline
git lfs install
git clone https://huggingface.co/kk08/CryptoBERT
```

### Install Locally
```commandline
pip3 install virtualenv
python3.11 -m venv crbtenv

source crbtenv/bin/activate
pip3 install -r requirements.txt
```
### Run from terminal (manually)

```commandline
uvicorn api:app --host 0.0.0.0 --port 8001 --reload
```

## Docker Deployment
Docker ensures that CryptoBERT can be easily set up and run in any environment. Instructions for building and running the Docker container are provided, making deployment a breeze.

### Build Docker Image (shell script)
```commandline
chmod +x build.sh
./builld.sh
```

### Run Docker image (shell script)
```commandline
chmod +x run.sh
./run.sh
```
    
## API Endpoints `http://localhost:8001/docs`

1. `/sentiment/:` Analyze sentiment for a given input text.
2. `/get_scores/:` Retrieve overall sentiment scores and distribution from the analyzed data.

```commandline
curl -X GET "http://localhost:8001/sentiment/?input=" -H "Accept: application/json"

curl -X GET http://localhost:8001/get_scores/ | json_pp
```

### Teardown the virtualenv
```commandline
deactivate
```

## Support and Subscribe to Our YouTube Channels

We are also active on YouTube, providing valuable content in both Farsi and English. If you find our project helpful, or are interested in more content related to cryptocurrency, blockchain technology, and various tech insights, we invite you to visit and subscribe to our YouTube channels. Your support helps us to continue producing high-quality, informative content.

- **Farsi Channel - [Dr. Samizadeh](https://www.youtube.com/@dr.samizadeh)**: Farsi channel (Persian), led by Dr. Samizadeh, offers a wealth of knowledge in cryptocurrency and blockchain technology. Subscribe for insightful content in Farsi.

- **English Channel - [Programming in 10 Minutes](https://www.youtube.com/channel/UCK-R2WyThSVk1i5Ac9PLtIA)**: Our English channel provides a global perspective on the latest developments in tech, focusing on blockchain and crypto-related topics. Join our community by subscribing for regular updates in English.

Your support on these channels is greatly appreciated as it enables us to continue sharing valuable knowledge and insights with a wider audience. Thank


## Credits and Acknowledgments

This project, CryptoBERT with FastAPI and Docker, stands on the shoulders of giants, incorporating significant contributions and resources from the wider open-source community. We would like to extend our heartfelt gratitude to the following:

- **[Hugging Face](https://huggingface.co/)**: For providing an incredible platform for machine learning models. Hugging Face has been instrumental in democratizing access to state-of-the-art NLP models.

- **[kk08's CryptoBERT](https://huggingface.co/kk08/CryptoBERT)**: A special thanks to the creators and maintainers of the CryptoBERT model. This model forms the backbone of our sentiment analysis service. The effort put into training and fine-tuning this model has been crucial in achieving high accuracy and relevancy in our sentiment analysis.

- **The Open Source Community**: For the various tools, libraries, and frameworks that have made this project possible. The collaborative nature of the open-source community continues to be a driving force in advancing technology and innovation.


## References
1. https://huggingface.co/kk08/CryptoBERT
2. https://git-lfs.com
3. https://git-scm.com/downloads
4. https://docs.docker.com/engine/install/
5. https://www.python.org/downloads/

## Citation

If you use CryptoBERT with FastAPI and Docker in your research or project, please cite it as follows:

```bibtex
@misc{CryptoBERT_FastAPI_Docker,
  author       = {Iman Samizadeh},
  title        = {CryptoBERT with FastAPI and Docker: NLP Sentiment Analysis for Cryptocurrency},
  year         = {2023},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  howpublished = {\url{https://github.com/SMARTSHEEP-IO/crypto-bert-spike}}
}
