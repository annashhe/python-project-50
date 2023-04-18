import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='Input first_file')
    parser.add_argument('second_file', type=str, help='Intput second_file')
    # args = parser.parse_args()
    # print(args.indir)


if __name__ == '__main__':
    main()
