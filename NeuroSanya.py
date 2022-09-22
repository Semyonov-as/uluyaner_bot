import json
import markovify as mk
import matplotlib.pyplot as plt

chat_history = []

def chat_analysis(chat_history):
    lens =  [len(x) for x in chat_history]
    len_dict ={}
    for x in lens: 
        if x in len_dict: 
            len_dict[x] += 1 
        else:
            len_dict[x] = 1
    tmp = sorted(len_dict.items(), key=lambda x: x[1], reverse=True)
    X = [x[0] for x in tmp]
    H = [x[1] for x in tmp]
     
    plt.bar(X, H)
    plt.show()


with open("ChatExport_2022-09-22/result.json", 'r', encoding="utf8") as f:
    chat_history = json.load(f)

chat_history = [x['text'] for x in chat_history["messages"] if len(x['text']) > 0 and x["from_id"] == "user487029198" and type(x['text']) == str ]

size_merjed = 30
i = 0
merjed = ""

new_history = []

while i < len(chat_history):
    if len(chat_history[i]) < size_merjed:
        if merjed:
            merjed += f" {chat_history[i].lower()}"
        else:
             merjed = chat_history[i]

        if len(merjed) > size_merjed:
            new_history.append(merjed)
            merjed = ""
    else:
        new_history.append(chat_history[i])
    i += 1

print(f"Was {len(chat_history)} -- Now {len(new_history)}")
# chat_analysis(chat_history)
# chat_analysis(new_history)

text = ".\n".join([x for x in chat_history if type(x) == str])
new_text = ".\n".join([x for x in new_history if type(x) == str])

text_model = mk.Text(text, state_size=2)
new_text_model = mk.Text(new_text, state_size=2)

print(f"{'-'*100}\nold model output\n{'-'*100}")
i = 0
while i < 10:
    x = text_model.make_sentence()
    if x != None and len(x) > 50:
        i += 1
        print(f">>>>{x}")

print(f"{'+'*100}\nnew model output\n{'+'*100}")
i = 0
while i < 10:
    x = new_text_model.make_sentence()
    if x != None and len(x) > 50:
        i += 1
        print(f">>>>{x}")

