def invest(txt: str):
    num_txt = len(txt)
    final_text =''
    for i in range(0, num_txt):
        final_text += txt[num_txt - i - 1]
    print(final_text)
invest('ya no quiero estar en mi casa')