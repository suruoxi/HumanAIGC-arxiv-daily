from claude_api import Client
from random import randint
from time import sleep
import os, json
from tqdm import tqdm
import random

cookie = open('.cookie').read().replace("\n", "")
claude_api = Client(cookie)


if __name__ == '__main__':
	prompt_name = 'prompt1'
	prompt_content = "Please carefully review the following academic paper. After a thorough reading, summarize the essential elements by answering the following questions in a concise manner:\n \
				1.What is the primary research question or objective of the paper?\n\
				2.What is the hypothesis or theses put forward by the authors?\n\
				3.What methodology does the paper employ? Briefly describe the study design, data sources, and analysis techniques.\n\
				4.What are the key findings or results of the research?\n\
				5.How do the authors interpret these findings in the context of the existing literature on the topic?\n\
				6.What conclusions are drawn from the research?\n\
				7.Can you identify any limitations of the study mentioned by the authors?\n\
				8.What future research directions do the authors suggest?\n"

	paper_prefix = './raw_pdfs/'
	claude_results = './claude_results/'
	text_parsed_saved_prefix = './text_parsed/'
	parse_only = False

	open(os.path.join(claude_results, prompt_name+".txt"),'w').write(prompt_content)
	saved_prefix = os.path.join(claude_results, prompt_name)
	os.makedirs(saved_prefix, exist_ok=True)

	lists = list(os.listdir(paper_prefix))
	# random.shuffle(lists)
	lists.sort(reverse=True)

	for pdf_name in tqdm(lists):
		# print(pdf_name)
		if pdf_name == '.DS_Store':
			continue
		text_parsed_path = os.path.join(text_parsed_saved_prefix, pdf_name.replace(".pdf", ".json"))
		saved_json_path = os.path.join(saved_prefix, pdf_name.replace(".pdf", ".json"))
		if os.path.exists(saved_json_path) and not parse_only:
			continue

		if parse_only:
			conversation_id = ''
		else:
			conversation_id =  claude_api.create_new_chat()['uuid']
		
		response = claude_api.send_message(parse_only, text_parsed_path, prompt_content, conversation_id, attachment=os.path.join(paper_prefix, pdf_name))
		
		if response is None:
			continue
		if not parse_only:
			json_result = dict()
			json_result['conversation_id'] = conversation_id
			json_result['response'] = response.decode("utf-8")

			with open(saved_json_path, 'w') as f:
				json.dump(json_result, f)

