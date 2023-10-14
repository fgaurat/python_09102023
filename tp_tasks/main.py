import threading



v = threading.Lock()


def traitement01():
    with v:
        for i in range(10):
            print(threading.current_thread().name,i)

def traitement02():
    with v:    
        for i in range(10):
            print(threading.current_thread().name,i)


def main():
    print(threading.current_thread().name,"start")
    th1 = threading.Thread(target=traitement01)
    th2 = threading.Thread(target=traitement02)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print("Après")

if __name__=='__main__':
    main()
