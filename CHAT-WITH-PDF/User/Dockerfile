FROM python:3.12.3
EXPOSE 8084
WORKDIR /app
COPY requirements.txt ./
RUN pip install requirements.txt
COPY . ./
ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8084", "--server.address=127.0.0.1" ]