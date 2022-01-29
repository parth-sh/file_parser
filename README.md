#  [![forthebadge](https://www.tradecred.com/image/logo/logo_white@3x.png)](https://forthebadge.com)
### Serverless Lambda functions
---
### Installation requirements
 1. [**AWS CLI**](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html)
 2. [**Serverless Framework**](https://www.serverless.com/framework/docs/providers/aws/guide/installation/)

 - DEMO
    --
    ```
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install
    aws configure


    npm install -g serverless
    npm install npm@latest -g
    npm update -g serverless

    serverless create --template aws-python3

    sls config credentials --provider aws --key YOUR-KEY --secret YOUR-SECRET -o
    
    sls plugin install -n serverless-python-requirements

    sls deploy --stage dev

    sls logs -f <func>

    sls remove
    ```
---
### Add Lambda Layers
#### For Dependencies of imported libraries
 -  [**Add Zip file created to Lambda function Layer**](https://www.youtube.com/watch?v=cz8QjmgfGHc&t=6s)

---
### ZipFile Creation `https://www.petewilcock.com/using-poppler-pdftotext-and-other-custom-binaries-on-aws-lambda/`
 
 - ```
    sudo snap install docker
    sudo groupadd docker
    sudo usermod -aG docker $USER
    ```
 -  Log out and log back in so that your group membership is re-evaluated.
 -  ```
    newgrp docker
    ```
 -  Add a Dockerfile `touch Dockerfile`
 -  ```
    # Dockerfile to extract Poppler binaries use by Pdf2Image
    FROM ubuntu:18.04

    RUN apt update
    RUN apt-get update
    RUN apt-get install -y locate \
                        libopenjp2-7 \
                        poppler-utils

    RUN rm -rf /poppler_binaries;  mkdir /poppler_binaries;
    RUN updatedb
    RUN cp $(locate libpoppler.so) /poppler_binaries/.
    RUN cp $(which pdftoppm) /poppler_binaries/.
    RUN cp $(which pdfinfo) /poppler_binaries/.
    RUN cp $(which pdftocairo) /poppler_binaries/.
    RUN cp $(locate libjpeg.so.8 ) /poppler_binaries/.
    RUN cp $(locate libopenjp2.so.7 ) /poppler_binaries/.
    RUN cp $(locate libpng16.so.16 ) /poppler_binaries/.
    RUN cp $(locate libz.so.1 ) /poppler_binaries/.
    RUN cp $(locate libfreetype.so.6 ) /poppler_binaries/.
    RUN cp $(locate libfontconfig.so.1 ) /poppler_binaries/.
    RUN cp $(locate libnss3.so ) /poppler_binaries/.
    RUN cp $(locate libsmime3.so ) /poppler_binaries/.
    RUN cp $(locate liblcms2.so.2 ) /poppler_binaries/.
    RUN cp $(locate libtiff.so.5 ) /poppler_binaries/.
    RUN cp $(locate libexpat.so.1 ) /poppler_binaries/.
    RUN cp $(locate libjbig.so.0 ) /poppler_binaries/.
    ```
 -  ```
    mkdir -p poppler_binaries
    docker build -t poppler-build .
    docker run -d --name poppler-build-cont poppler-build sleep 20 
    docker cp poppler-build-cont:/poppler_binaries .
    docker kill poppler-build-cont
    docker rm poppler-build-cont
    docker image rm poppler-build
    cd poppler_binaries
    zip -r9 poppler.zip .
    cd ..
    ```   

---
