import argparse
import requests
import json
import sys
import os


def echo_message(message):
    print(message)


def main():
    parser = argparse.ArgumentParser(description='LVS Client CLI')
    parser.add_argument('-create', metavar='FILE', help='Criar business a partir de arquivo JSON')
    parser.add_argument('-echo', metavar='STRING', help='Exibe a string fornecida')

    args = parser.parse_args()

    if args.create:
        print(f"Create command received for file: {args.create}")
    elif args.echo:
        echo_message(args.echo)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()