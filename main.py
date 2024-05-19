from flask import Flask, request, jsonify
from transformers import pipeline



# Load the GPT-2 text generation model from the Hugging Face Transformers library
generator = pipeline('text-generation', model='gpt2')

app = Flask(__name__)

# Function to generate text using the loaded GPT-2 model
def generate_text(input, max_length=30, num_return_sequences=5):
    """
    Generate text based on the given input text using the GPT-2 model.

    Args:
        input (str): The input text to use as the starting point for generation.
        max_length (int, optional): The maximum length of the generated text. Default is 30.
        num_return_sequences (int, optional): The number of text sequences to generate. Default is 5.

    Returns:
        list: A list of generated text sequences.
    """
    return generator(input, max_length=max_length, num_return_sequences=num_return_sequences)

# Flask route to handle text generation requests
@app.route('/generate', methods=['POST'])
async def generate_text_fun():
    """
    API endpoint to generate text using the loaded GPT-2 model.

    Request format:
    {
        "input_text": "The input text to use as the starting point for generation."
    }

    Response format:
    {
        "generated_text": [
            "Generated text sequence 1",
            "Generated text sequence 2",
            ...
        ]
    }
    """
    input_text = request.json['input_text']
    generated_text = generate_text(input_text)
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(port=5000)


#<------------optimize gpu enable code--------------->
# from flask import Flask, request, jsonify
# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer

# # Load the GPT-2 model and tokenizer
# model_name = "gpt2"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name, load_in_8bit=True, device_map="auto")

# app = Flask(__name__)

# # Function to generate text using the loaded GPT-2 model
# def generate_text(input, max_length=30, num_return_sequences=5):
#     """
#     Generate text based on the given input text using the GPT-2 model.

#     Args:
#         input (str): The input text to use as the starting point for generation.
#         max_length (int, optional): The maximum length of the generated text. Default is 30.
#         num_return_sequences (int, optional): The number of text sequences to generate. Default is 5.

#     Returns:
#         list: A list of generated text sequences.
#     """
#     with torch.no_grad():
#         input_ids = tokenizer.encode(input, return_tensors="pt")
#         outputs = model.generate(input_ids, max_length=max_length, num_return_sequences=num_return_sequences)
#         generated_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)

#     # Move the model to CPU memory when not in use
#     model.to("cpu")

#     return generated_text

# # Flask route to handle text generation requests
# @app.route('/generate', methods=['POST'])
# async def generate_text_fun():
#     """
#     API endpoint to generate text using the loaded GPT-2 model.

#     Request format:
#     {
#         "input_text": "The input text to use as the starting point for generation."
#     }

#     Response format:
#     {
#         "generated_text": [
#             "Generated text sequence 1",
#             "Generated text sequence 2",
#             ...
#         ]
#     }
#     """
#     input_text = request.json['input_text']
#     generated_text = generate_text(input_text)
#     return jsonify({'generated_text': generated_text})

# if __name__ == '__main__':
#     app.run(port=5000)