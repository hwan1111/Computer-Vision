FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    git wget build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/pjreddie/darknet /darknet
WORKDIR /darknet

RUN sed -i 's/GPU=1/GPU=0/' Makefile && \
    sed -i 's/CUDNN=1/CUDNN=0/' Makefile && \
    sed -i 's/OPENCV=1/OPENCV=0/' Makefile

RUN make

RUN wget https://pjreddie.com/media/files/yolov3.weights -O yolov3.weights

ENTRYPOINT ["bash", "-c", "wget -O input.jpg \"$1\" && ./darknet detect cfg/yolov3.cfg yolov3.weights input.jpg", "--"]