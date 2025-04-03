import requests
import os
import time

def download_file(url,save_path):
  headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'accept-language': 'en,gu;q=0.9,hi;q=0.8'}
  sess = requests.Session()
  response = sess.get(url, headers=headers, timeout=5)
  with open(save_path, 'wb') as file:
    file.write(response.content)
    

if __name__=="__main__":
  file_url="https://sbi.co.in/documents/16012/1400784/FOREX_CARD_RATES.pdf"

save_dir=time.strftime("%Y") + '/' + time.strftime("%m") 
os.makedirs(save_dir,exist_ok=True)
timestr = time.strftime("%Y_%m_%d-%H:%M")
save_path=os.path.join(save_dir, "FOREX_CARD_RATES_" + timestr + ".pdf")

download_file(file_url,save_path)
print(f"Saved to {save_path}")
