# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#     print(x)


# def my_function(food):
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)


# import time
#
# def do_something(second):
#     print(f'Sleeping in {second} second...')
#     time.sleep(second)
#     print('Done Sleeping')
#
# start = time.perf_counter()
#
# do_something(2)
#
# finish = time.perf_counter()
#
# print(f'Finished in total time{finish-start}')
# print(f'Finished in {round(finish-start, 2)} second(s)')



# import threading
# import time
#
# def do_something(second = 5):
#     print(f'Sleeping in {second} second...')
#     time.sleep(second)
#     print(f'Done Sleeping' + '\n')
#
# start = time.perf_counter()
#
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
#
# finish = time.perf_counter()
#
# print(f'Finished in total time{finish-start}')





# import threading
# import time
#
# def do_something(second = 5):
#     print(f'Sleeping in {second} second...')
#     time.sleep(second)
#     print(f'Done Sleeping')
#
# start = time.perf_counter()
#
# threads = []
#
# for _ in range(100):
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
#
#
# finish = time.perf_counter()
#
# print(f'Finished in total time{finish-start}')






# import threading
# import time
#
# def do_something(second):
#     print(f'Sleeping in {second} second...')
#     time.sleep(second)
#     print(f'Done Sleeping')
#
# start = time.perf_counter()
#
# threads = []
#
# for _ in range(100):
#     t = threading.Thread(target=do_something, args=[2])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
#
#
# finish = time.perf_counter()
#
# print(f'Finished in total time{finish-start}')


