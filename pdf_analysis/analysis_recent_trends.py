from claude_api import Client
from random import randint
from time import sleep
import os, json
from tqdm import tqdm
import random
import argparse

def analysis(paper_num,
			 cookie_path,
			 prompt_content,
			 paper_prefix,
			 claude_results,
			 text_parsed_saved_prefix,
			 saved_path):

	cookie = open(cookie_path).read().replace("\n", "")
	claude_api = Client(cookie)

	lists = list(os.listdir(paper_prefix))
	lists.sort(reverse=True)
	name_list = []
	for pdf_name in tqdm(lists[:paper_num]):
		if pdf_name == '.DS_Store':
			continue
		name_list.append(os.path.join(text_parsed_saved_prefix, pdf_name.replace(".pdf", ".json")))

	conversation_id = claude_api.create_new_chat()['uuid']

	response = claude_api.send_messages(prompt_content, conversation_id, name_list=name_list)

	open(saved_path, "w").write(response.decode("utf-8"))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--paper_num", type=int, default=10)
    parser.add_argument("--prompt_content", type=str, default="Based on the collection of academic papers provided as attachments, please summarize the most recent and notable trends that have emerged across the various studies. Focus on synthesizing key themes, methodologies, findings, and any shifts in perspective or new areas of inquiry that these papers collectively highlight. The summary should identify interconnectedness amongst the papers and indicate the direction in which the field of study is moving. This overview should serve as an insightful guide for researchers seeking to understand the cutting-edge developments and the future trajectory of research within this discipline.")
    parser.add_argument("--claude_results", type=str, default='./claude_results/')
    parser.add_argument("--paper_prefix", type=str, default='./raw_pdfs/')
    parser.add_argument("--text_parsed_saved_prefix", type=str, default='./text_parsed/')
    parser.add_argument("--cookie", type=str, default='.cookie')
    parser.add_argument("--saved_path", type=str, default='recent_trends.txt')

    args = parser.parse_args()

    analysis(args.paper_num,
    		 args.cookie,
			 args.prompt_content,
			 args.paper_prefix,
			 args.claude_results,
			 args.text_parsed_saved_prefix,
			 args.saved_path)

	