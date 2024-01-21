import os
import json
import argparse
from tqdm import tqdm
from claude_api import Client

def analysis(paper_num, cookie_path, prompt_content, paper_prefix, claude_results, text_parsed_saved_prefix, saved_path):
    # Read and clean cookie
    cookie = open(cookie_path).read().replace("\n", "")
    claude_api = Client(cookie)

    # Get list of papers and sort in reverse order
    paper_list = list(os.listdir(paper_prefix))
    paper_list.sort(reverse=True)

    # Prepare list of parsed text files
    parsed_text_files = []
    for pdf_name in tqdm(paper_list[:paper_num]):
        if pdf_name == '.DS_Store':
            continue
        parsed_text_files.append(os.path.join(text_parsed_saved_prefix, pdf_name.replace(".pdf", ".json")))

    # Create new chat
    conversation_id = claude_api.create_new_chat()['uuid']

    # Send messages and get response
    response = claude_api.send_messages(prompt_content, conversation_id, name_list=parsed_text_files)

    # Write response to file
    open(saved_path, "w").write(response.decode("utf-8"))

if __name__ == '__main__':
    # Initialize argument parser
    parser = argparse.ArgumentParser()

    # Define arguments
    parser.add_argument("--paper_num", type=int, default=10)
    parser.add_argument("--prompt_content", type=str, default="Based on the collection of academic papers provided as attachments, please summarize the most recent and notable trends that have emerged across the various studies. Focus on synthesizing key themes, methodologies, findings, and any shifts in perspective or new areas of inquiry that these papers collectively highlight. The summary should identify interconnectedness amongst the papers and indicate the direction in which the field of study is moving. This overview should serve as an insightful guide for researchers seeking to understand the cutting-edge developments and the future trajectory of research within this discipline.")
    parser.add_argument("--claude_results", type=str, default='./claude_results/')
    parser.add_argument("--paper_prefix", type=str, default='./raw_pdfs/')
    parser.add_argument("--text_parsed_saved_prefix", type=str, default='./text_parsed/')
    parser.add_argument("--cookie", type=str, default='.cookie')
    parser.add_argument("--saved_path", type=str, default='recent_trends.txt')

    # Parse arguments
    args = parser.parse_args()

    # Call analysis function
    analysis(args.paper_num, args.cookie, args.prompt_content, args.paper_prefix, args.claude_results, args.text_parsed_saved_prefix, args.saved_path)
