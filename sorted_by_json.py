import argparse

from resolve import sorted_categories


def sort_categories(filename):
    categories = sorted_categories(filename)
    for key, value in categories.items():
        for v in value:
            with open(fr'catalog/{v}.csv', 'a', encoding='utf-8') as data:
                data.write(f'{key}\n')


def pars():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', type=str)
    args = parser.parse_args()
    return sort_categories(args.filename)


if __name__ == '__main__':
    # sort_categories('test_task_python/user_support_letters.csv')
    pars()
