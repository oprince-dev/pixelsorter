import os
import args


def save(output):
    """Save pixel sorted image ('./images/export/')"""
    sub_path = './images/export/'
    if not os.path.exists(sub_path):
        os.makedirs(sub_path)

    base, file_extension = os.path.splitext(os.path.basename(args.input_image))
    output_base = base + '_' + str(args.mode) + str(args.direction) + str(args.threshold) + \
        str(args.reverse) + str(args.upper) + str(file_extension)
    output_path = ('/').join(args.input_image.split('/')[:-1])
    output_file = output_path + sub_path + output_base
    output.save(output_file)
