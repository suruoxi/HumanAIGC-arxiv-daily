from claude_api import Client
from random import randint
from time import sleep
import os, json
from tqdm import tqdm
import argparse


def analysis_papers(args):
    # Extract arguments
    prompt_name = args.prompt_name
    prompt_content = args.prompt_content
    paper_prefix = args.paper_prefix
    claude_results = args.claude_results
    text_parsed_saved_prefix = args.text_parsed_saved_prefix
    parse_only = args.parse_only
 
    # Initialize Claude API client
    claude_api = Client(open(args.cookie).read().replace("\n", ""))

    # Write prompt content to file
    open(os.path.join(claude_results, prompt_name+".txt"),'w').write(prompt_content)
    
    # Create directory for saving results
    saved_prefix = os.path.join(claude_results, prompt_name)
    os.makedirs(saved_prefix, exist_ok=True)

    # Get list of papers and sort in reverse order
    lists = list(os.listdir(paper_prefix))
    lists.sort(reverse=True)

    # Process each PDF
    for pdf_name in tqdm(lists):
        # Skip system files
        if pdf_name == '.DS_Store':
            continue
        
        # Define paths for parsed text and saved JSON
        text_parsed_path = os.path.join(text_parsed_saved_prefix, pdf_name.replace(".pdf", ".json"))
        saved_json_path = os.path.join(saved_prefix, pdf_name.replace(".pdf", ".json"))
        
        # Skip if JSON already exists and not in parse-only mode
        if os.path.exists(saved_json_path) and not parse_only:
            continue

        # Create new chat or use empty ID in parse-only mode
        conversation_id = '' if parse_only else claude_api.create_new_chat()['uuid']
        
        # Send message to Claude API
        response = claude_api.send_message(parse_only, text_parsed_path, prompt_content, conversation_id, attachment=os.path.join(paper_prefix, pdf_name))
        
        # Skip if no response received
        if response is None:
            continue
        
        # Save response to JSON file if not in parse-only mode
        if not parse_only:
            json_result = {'conversation_id': conversation_id, 'response': response.decode("utf-8")}
            with open(saved_json_path, 'w') as f:
                json.dump(json_result, f)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--prompt_name', type=str, default='prompt1')
	parser.add_argument('--prompt_content', type=str, default="Please carefully review the following academic paper. After a thorough reading, summarize the essential elements by answering the following questions in a concise manner:\n \
				1.What is the primary research question or objective of the paper?\n\
				2.What is the hypothesis or theses put forward by the authors?\n\
				3.What methodology does the paper employ? Briefly describe the study design, data sources, and analysis techniques.\n\
				4.What are the key findings or results of the research?\n\
				5.How do the authors interpret these findings in the context of the existing literature on the topic?\n\
				6.What conclusions are drawn from the research?\n\
				7.Can you identify any limitations of the study mentioned by the authors?\n\
				8.What future research directions do the authors suggest?\n")
	parser.add_argument('--paper_prefix', type=str, default='./raw_pdfs/')
	parser.add_argument('--claude_results', type=str, default='./claude_results/')
	parser.add_argument('--text_parsed_saved_prefix', type=str, default='./text_parsed/')
	parser.add_argument('--parse_only', type=bool, default=False)
	parser.add_argument('--cookie', type=str, default='.cookie')
 
	args = parser.parse_args()

	analysis_papers(args)



