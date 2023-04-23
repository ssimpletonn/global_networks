from crc16 import crc16
from hamming import __hamming_common, decode, encode
from noize import noize4, noize


def main():
    msg = """Все эксперты по сетям знакомы с принципом end-to-end, когда специфичные для конкретной задачи фичи реализовываются на конечных нодах, а промежуточные ноды должны только передавать данные, не взаимодействуя с ними. 
          Но есть случаи, когда полезны вычисления внутри сети — с использованием устройств сети, занятых передачей трафика. Один из примеров таких задач — распределенный ML. 
          В докладе Дмитрий Афанасьев дал краткое введение в особенности вычислений для распределенного ML, паттерны обмена данными и коллективные операции. 
          Вторая половина доклада — о том, как редукция увеличивает производительность при обучении, и о некоторых реализациях. 
          — Меня зовут Дмитрий Афанасьев, я сетевой архитектор Яндекса. И я сегодня расскажу про достаточно экзотические — по крайней мере пока — технологии. 
          Но думаю, что они будут становиться менее экзотическими, и шансы с ними встретиться возрастают. Итак, распределенное обучение для machine learning и вычисления в сети. 
          Что я хочу рассказать? Сначала очень быстрое введение про то, что вообще такое нейросети, как они устроены, какие у них есть режимы функционирования и как они обучаются. 
          Дальше специфика распределенного обучения, как устроен трафик при распределенном обучении и как он может ложиться на топологию сети Compute Implementations. 
          И, наконец, расскажу про две реализации, где вычисление в сетях используется, чтобы оптимизировать распределенное обучение. 
          В пакетных и IP-сетях мы привыкли руководствоваться e2e-принципом. И говорим, что всю функциональность желательно реализовывать на endpoint, а сеть, которая посередине, должна быть быстрой, простой, дешевой и достаточно тупой, и заниматься только передачей данных, не вмешиваясь в процесс их обработки. 
          Но из любых хороших правил есть исключения. И есть приложения, у которых специфика, структура вычислений и структура обмена данными таковы, что, реализовав некоторые функции (вычисления) в сети, можно очень хорошо оптимизировать эти вычисления.
          Дальше мы посмотрим, как устроены сами задачи и что в них такое происходит с вычислениями, что можно внести много пользы, добавив вычисления в сети."""
    print("Первая отправка")
    first(msg)
    print("Вторая отправка")
    second(msg)
    print("Третья отправка")
    third(msg)


def first(msg):
    checksum = crc16(msg)
    enc_msg = encode(msg)
    print(f'Кодированное сообщение:\n{enc_msg}')
    dec_msg, err = decode(enc_msg)
    dec_msg = dec_msg[:-2:]
    print(f'Раскодированное сообщение:\n{dec_msg}')
    print(
        f'Контрольная сумма: {crc16(dec_msg)}, корректность: {crc16(dec_msg) == checksum}')
    print(f'MSG: {msg == dec_msg}')


def second(msg):
    enc_msg = encode(msg)
    checksum = crc16(msg)
    noize_msg = noize(enc_msg)
    print(f'Кодированное сообщение с ошибками:\n{noize_msg}')
    dec_msg, err = decode(noize_msg)
    dec_msg = dec_msg[:-2:]
    print(f'Раскодированное сообщение:\n{dec_msg}')
    print(
        f'Контрольная сумма: {crc16(dec_msg)}, корректность: {crc16(dec_msg) == checksum}')
    print(f'MSG: {msg == dec_msg}')


def third(msg):
    enc_msg = encode(msg)
    checksum = crc16(msg)
    noize_msg = noize4(enc_msg)
    print(f'Кодированное сообщение с ошибками:\n{noize_msg}')
    dec_msg, err = decode(noize_msg)
    dec_msg = dec_msg[:-2:]
    print(f'Раскодированное сообщение:\n{dec_msg}')
    print(
        f'Контрольная сумма: {crc16(dec_msg)}, корректность: {crc16(dec_msg) == checksum}, количество обнаруженных ошибок: {err}')


if __name__ == '__main__':
    main()
