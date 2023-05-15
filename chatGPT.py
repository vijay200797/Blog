import openai

openai.api_key = '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'
model_id = 'gpt-3.5-turbo'

def __ChatGPT(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    # api_usage = response['usage']
    # print('Total token consumed: {0}'.format(api_usage['total_tokens']))
    # stop means complete
    # print(response['choices'][0].finish_reason)
    # print(response['choices'][0].index)
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

def ChatGPT(textMessage):
    conversation = []
    conversation.append({'role': 'system', 'content': textMessage})
    conversation = __ChatGPT(conversation)
    # print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
    return conversation[-1]['content'].strip()
    

# while True:
#     prompt = input('User:')
#     conversation.append({'role': 'user', 'content': prompt})
#     conversation = ChatGPT_conversation(conversation)
#     print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))