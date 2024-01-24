from claude_api import Client
from random import randint
from time import sleep
import os, json
from tqdm import tqdm
import argparse

def convet_to_file_upload_format(text_path):
    file_name = os.path.basename(text_path)
    file_size = os.path.getsize(text_path)
    
    return {
        "file_name": file_name,
        "file_type": "text/plain",
        "file_size": file_size,
        "extracted_content": open(text_path).read()
    }

def analysis_papers(args):
    # Extract arguments
    prompt_name = args.prompt_name
    prompt_content = args.prompt_content
    claude_results = args.claude_results
    text_parsed_saved_path = args.text_parsed_saved_path
 
    # Initialize Claude API client
    claude_api = Client(open(args.cookie).read().replace("\n", ""))

    # Write prompt content to file
    os.makedirs(claude_results, exist_ok=True)
    open(os.path.join(claude_results, prompt_name+".txt"),'w').write(prompt_content)
    
    # Create directory for saving results
    saved_prefix = os.path.join(claude_results, prompt_name)
    os.makedirs(saved_prefix, exist_ok=True)

    # Get list of papers and sort in reverse order
    lists = [f for f in os.listdir(text_parsed_saved_path) if os.path.isfile(os.path.join(text_parsed_saved_path, f))]
    lists.sort(reverse=True)

    # Process each PDF
    for pdf_name in tqdm(lists):
        # Skip system files
        if pdf_name == '.DS_Store':
            continue
        pdf_name, _ = os.path.splitext(pdf_name)
        
        # Check if the text parsed file is in .txt or .md format
        text_parsed_path_txt = os.path.join(text_parsed_saved_path, pdf_name + ".txt")
        text_parsed_path_md = os.path.join(text_parsed_saved_path, pdf_name + ".md")
        text_parsed_path = text_parsed_path_md if os.path.exists(text_parsed_path_md) else text_parsed_path_txt
        saved_to_json_path = os.path.join(saved_prefix, pdf_name + ".json")
        if os.path.exists(saved_to_json_path):
            continue
        upload_file_format = convet_to_file_upload_format(text_parsed_path)
        
        # Send message to Claude API
        conversation_id = claude_api.create_new_chat()['uuid']
        response = claude_api.send_message(upload_file_format, prompt_content, conversation_id)
        
        # Skip if no response received
        if response is None:
            print(f'Error, checking {pdf_name}')
            continue
        
        # Save response to JSON file 
        json_result = {'conversation_id': conversation_id, 'response': response.decode("utf-8")}
        with open(saved_to_json_path, 'w') as f:
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
    
    parser.add_argument('--text_parsed_saved_path', type=str, default='./results/text_parsed/raw_text/')
    parser.add_argument('--claude_results', type=str, default='./results/claude_results/')
    parser.add_argument('--cookie', type=str, default='.cookie')
 
    args = parser.parse_args()

    analysis_papers(args)



