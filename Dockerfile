FROM python:3.8

# Create a folder /app if it doesn't exist,
# the /app folder is the current working directory
WORKDIR /app

# Copy necessary files to our app
COPY ./main.py /app

COPY ./download_pretrained_model.py /app

COPY ./requirements.txt /app

COPY ./configs /app/configs

COPY ./src /app/src

# Port will be exposed, for documentation only
EXPOSE 30000

# Disable pip cache to shrink the image size a little bit,
# since it does not need to be re-installed

RUN pip install torch==2.0.1
RUN pip install transformers==4.36.2
RUN pip install -r requirements.txt --no-cache-dir

RUN python download_pretrained_model.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "30000"]
