import argparse

from automate_projects_test_task.logging import configure_logging_basic
from .console import post_user_review


def get_args():
    parser = argparse.ArgumentParser(
        description='Post user review',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("nickname", help="Examples: Daniel88, Andrzej, Byłem tam, uciekaj.")
    parser.add_argument("review_datetime", metavar='review-datetime', help="Examples: 29.10.2020 13:10, 05.10.2020 15:29, 01.06.2020 20:37")
    parser.add_argument("--url", default='https://www.gowork.pl/opinie_czytaj,729637')
    parser.add_argument("--loading-timeout", type=float, default=20)

    return parser.parse_args()


def entry():
    configure_logging_basic()
    args = get_args()
    post_user_review(url=args.url, nickname=args.nickname, review_datetime=args.review_datetime,
                     loading_timeout=args.loading_timeout)


if __name__ == '__main__':
    entry()
