FROM nvidia/cuda:12.1.1-base-ubuntu22.04

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 python3-pip git curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install vllm

EXPOSE 8000

CMD ["vllm", "serve", "Qwen/Qwen2.5-1.5B-Instruct", "--port", "8000"]
