# import os
import requests

tomcat_version = "8.5.91"
download_url = f"https://downloads.apache.org/tomcat/tomcat-8/v{tomcat_version}/bin/apache-tomcat-{tomcat_version}.tar.gz"
output_file = f"apache-tomcat-{tomcat_version}.tar.gz"

response = requests.get(download_url, stream=True)
if response.status_code == 200:
    with open(output_file, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Downloaded {output_file}")
else:
    print("Failed to download Tomcat.")
