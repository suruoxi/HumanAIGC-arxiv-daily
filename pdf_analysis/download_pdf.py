import os, json, pdb, requests

def download_pdf(save_path, pdf_name, pdf_url):
    if os.path.exists(f'{save_path}/{pdf_name}.pdf'):
        return 
    response = requests.get(pdf_url)
    with open(f'{save_path}/{pdf_name}.pdf', mode='wb') as f:
        f.write(response.content)
    print(f'{pdf_name}.PDF downloaded successfully!')


if __name__ == '__main__':
	json_path = '../docs/cv-arxiv-daily-web.json'

	with open(json_path, 'r') as f:
	    data = json.load(f)
	    for keyword in data.keys():
	    	for doc_id in data[keyword].keys():
	    		if '/' in doc_id: # skip too old papers
	    			continue
	    		print(doc_id)
	    		download_pdf('raw_pdfs', doc_id, f'https://arxiv.org/pdf/{doc_id}.pdf')
