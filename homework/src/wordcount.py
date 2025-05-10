from ._internals.parse_args import parse_args
from ._internals.read_all_lines import read_all_lines


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
