def format_txtoutput():
    # Read the input text from a file
    with open("output.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # Find the indices of all "Task output:" occurrences
    start_indices = [i for i in range(len(text)) if text.startswith('Task output:', i)]
    start_indices = [idx for idx in start_indices if idx >= 0]
    start_indices.sort()

    # Extract the text after each "Task output:" up to the first [
    output_texts = []
    for start_index in start_indices:
        end_index = text.find("[", start_index)
        output_text = text[start_index:end_index].strip()
        output_texts.append(output_text)

    # Save the extracted text to a file
    with open("output_after_extraction.txt", "w", encoding="utf-8") as file:
        file.write("\n\n".join(output_texts))

    print("Text saved to 'output_after_extraction.txt' file.")