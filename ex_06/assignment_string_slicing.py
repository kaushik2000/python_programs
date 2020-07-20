# Write code using find() and string slicing to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

# Finding the position ofthe required piece and extracting/slicing it
position = text.find(' ')
extracted_value = text[position:].strip()

# converting the extracted text
floating_value = float(extracted_value)
print(floating_value)