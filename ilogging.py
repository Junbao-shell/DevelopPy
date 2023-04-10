# ilogging.py

# 学习使用 logging lib
# date: 2023/04/10

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


if __name__ == "__main__":
    logging.debug('debug info')
    logging.info('info')
    logging.warning('warning info')
    logging.error('error info')
    logging.critical('caritical info')

