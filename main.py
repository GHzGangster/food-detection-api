import os

from common import predict, input_dir_path, output_dir_path

def main():
    input_path = os.path.join(input_dir_path, "test01.png")
    output_path = os.path.join(output_dir_path, "test01.jpg")
    predict(input_path, output_path)

if __name__ == '__main__':
    main()
