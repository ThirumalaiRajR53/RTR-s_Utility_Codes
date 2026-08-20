from rembg import remove
from PIL import Image
from datetime import datetime

input_path = 'test.png'

inp = Image.open(input_path)
output = remove(inp)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = f'op_{timestamp}.png'

output.save(output_path)

Image.open(output_path)
print(f"Saved to: {output_path}")