FROM python:3.9-slim

WORKDIR /project/app

COPY . .

# Install any needed packages specified in requirements.txt
# Uncomment the following line if you have a requirements.txt file:
# RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "hello.py"]
