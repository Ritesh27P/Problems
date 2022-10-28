def designerPdfViewer(h, word):
    value = len(word)
    tall_value = 0
    for i in word:
        if tall_value < h[(ord(i) - 97)]:
            tall_value = h[(ord(i) - 97)]
    
    return (value * tall_value)
