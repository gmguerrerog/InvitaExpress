import base64
import os
import re

html_path = 'index.html'

def get_base64_data_uri(filepath, content_type='image/jpeg'):
    with open(filepath, 'rb') as f:
        data = f.read()
    b64_str = base64.b64encode(data).decode('utf-8')
    return f"data:{content_type};base64,{b64_str}"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Logo
logo_uri = get_base64_data_uri('optimized_logo.jpg')
content = content.replace('Gemini_Generated_Image_3jqgby3jqgby3jqg.png', logo_uri)

# Replace Templates
for i in range(1, 11):
    old_str = f"plantillas/{i}.png"
    if old_str in content:
        b64_uri = get_base64_data_uri(f"optimized_plantillas/{i}.jpg")
        content = content.replace(old_str, b64_uri)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML inyectado correctamente.")
