import os

import django


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grail.settings')
    django.setup()
    from crawler.EastMoneyFundCrawler import EastMoneyFund
    eastmoneyfund = EastMoneyFund()


if __name__ == '__main__':
    main()