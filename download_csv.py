import requests
import os
import time

def download_csv(url,save_path):
  response=requests.get(url)
  response.raise_for_status()

  with open(save_path, 'wb') as file:
    file.write(response.content)

if __name__=="__main__":
  csv_url="https://cdn.wsform.com/wp-content/uploads/2020/06/industry.csv"

save_dir="data"
os.makedirs(save_dir,exist_ok=True)
timestr = time.strftime("%Y%m%d-%H%M%S")
save_path=os.path.join(save_dir,"data" + timestr + ".csv")

download_csv(csv_url,save_path)
print(f"Saved to {save_path}")
