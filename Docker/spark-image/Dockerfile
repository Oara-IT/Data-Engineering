FROM eclipse-temurin:17-jdk

RUN apt-get update && apt-get install -y wget python3 python3-pip && rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages pyspark google-cloud-storage google-auth google-cloud-bigquery requests

RUN wget -q https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar -O /opt/gcs-connector-hadoop3-latest.jar

ENV JAVA_HOME=/opt/java/openjdk

RUN ln -s /usr/bin/python3 /usr/bin/python