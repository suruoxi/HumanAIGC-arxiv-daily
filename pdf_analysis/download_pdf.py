import os
import json
import requests
from tqdm import tqdm

def download_pdf(save_path, pdf_name, pdf_url):
    pdf_file_path = os.path.join(save_path, f'{pdf_name}.pdf')
    if os.path.exists(pdf_file_path):
        return 
    response = requests.get(pdf_url)
    with open(pdf_file_path, mode='wb') as file:
        file.write(response.content)
    print(f'{pdf_name}.PDF downloaded successfully!')


if __name__ == '__main__':
    json_path = '../docs/cv-arxiv-daily-web.json'

    with open(json_path, 'r') as file:
        data = json.load(file)
        for keyword in data.keys():
            print(f'{keyword}:')
            for doc_id in tqdm(data[keyword].keys(), desc='Downloading PDFs'):
                if '/' in doc_id: # skip too old papers
                    continue
                # print(doc_id)
                download_pdf('raw_pdfs', doc_id, f'https://arxiv.org/pdf/{doc_id}.pdf')

