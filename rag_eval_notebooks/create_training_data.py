import json
import os

# Define the system message that will be added to each entry.
system_message = {
    "role": "system",
    "content": "You are a machine learning expert agent whose primary goal is to help users with questions with Azure Machine Learning. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Azure Machine Learning."
}


data_path = os.path.join('rag_eval_notebooks','data')



# Read the input file
with open(os.path.join(data_path,'aml_qa_pairs.json'), 'r') as file:
    data = json.load(file)

# Transform the data
transformed_data = []
for item in data:
    # Create a dictionary for the user and assistant messages based on the QA pair
    user_message = {
        "role": "user",
        "content": item["question"]
    }
    assistant_message = {
        "role": "assistant",
        "content": item["answer"]
    }
    # Combine the system message with the user and assistant messages
    message_set = {
        "messages": [system_message, user_message, assistant_message]
    }
    transformed_data.append(message_set)



# split the data into training and validation sets
split = int(0.8 * len(transformed_data))
training_data = transformed_data[:split]
validation_data = transformed_data[split:]

# Write the transformed data to an output file
with open(os.path.join(data_path,'training.jsonl'), 'w',) as outfile:
    for entry in training_data:
        json.dump(entry, outfile)
        outfile.write('\n')  # Write each entry on a new line

with open(os.path.join(data_path,'validation.jsonl'), 'w') as outfile:
    for entry in validation_data:
        json.dump(entry, outfile)
        outfile.write('\n')  # Write each entry on a new line
