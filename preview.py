from PIL import Image
import args
import reader

def generate_preview(data, thresh_data):
    """Generate a preview of the pixels to be sorted.

    White -- Pixels to be sorted.
    Black -- Pixels that will be ignored.
    """
    user_preview_choice = False
    while not user_preview_choice:
        preview_img = Image.fromarray(thresh_data, mode='HSV')
        preview_img.show()
        choice = (input("Continue with this threshold map? Y/N: ")).lower()
        if choice == "y":
            user_preview_choice = True
            return thresh_data
        else:
            new_thresh_input = int(input("Enter a new threshold (0-255): "))
            thresh_data = reader.read_thresh(data, new_thresh_input)
