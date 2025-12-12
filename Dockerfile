

```dockerfile
FROM python:3.10-slim

RUN apt-get update && apt-get install -y wget gnupg2 unzip xvfb libnss3 libgconf-2-4 fonts-liberation libasound2 \
    && rm -rf /var/lib/apt/lists/*

# install chrome (example for Debian based)
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
 && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
 && apt-get update && apt-get install -y google-chrome-stable

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

ENV HEADLESS=true

CMD ["pytest", "-q", "--html=report.html", "--self-contained-html"]
