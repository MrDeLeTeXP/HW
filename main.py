import logging
sumnumbers=0
try:
    nn = int(input('1 Число'))
    nn1 = int(input('2 Число'))
    nn2 = int(input('3 Число'))
    nn3 = int(input('4 Число'))
    nn4 = int(input('5 Число'))
    print((nn+nn1+nn2+nn3+nn4)/5)
except (ImportError,TypeError,NameError,ValueError):
    print('Тіки число 1|не текст')
infologging=input("Логін: ")
password=input("Пароль: ")
logging.basicConfig(
    level=logging.INFO,
    filename = 'logs.log',
    filemode='a',
    format=f'[%(asctime)s] %(message)s'
)
logging.info(infologging)
logging.info(password)
logging.debug("Антівірус!")
logging.warning("Попередження!")
logging.error("Актівовується антішвірус!")
logging.critical("Всьо окей віруса не найдено")