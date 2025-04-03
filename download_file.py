import requests
import os
import time

def download_csv(url,save_path):
  response=requests.get(url)
  response.raise_for_status()

  with open(save_path, 'wb') as file:
    file.write(response.content)

if __name__=="__main__":
  file_url="https://sbi.co.in/documents/16012/1400784/FOREX_CARD_RATES.pdf"

save_dir=time.strftime("%Y")/time.strftime("%m")/time.strftime("%d")
os.makedirs(save_dir,exist_ok=True)
timestr = time.strftime("%Y%m%d-%H%M%S")
save_path=os.path.join(save_dir,"data" + timestr + ".pdf")

download_file(file_url,save_path)
print(f"Saved to {save_path}")
