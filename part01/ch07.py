def main():
    a=2
    b=3
    c = a/b

    s = f"{a},{b} => c : {c:.3%}" # f-string
    print(s)
    s1 = "a ={0} ,b ={1} c ={2:.2f} ".format(a,b,c)
    s1 = "a ={} ,b ={} c ={:.2f} ".format(a,b,c)
    print(s1)
    
    l = [a,b,c]
    s1 = "a ={} ,b ={} c ={:.2f} ".format(l[0],l[1],l[2])
    s1 = "a ={} ,b ={} c ={:.2f} ".format(*l)
    print(s1)
    s1 = "a ={value_a} ,b ={value_b} c ={value_c:.2f} ".format(value_a=a,value_b=b,value_c=c)
    d= {
        "value_a":a,
        "value_b":b,
        "value_c":c
    }
    s1 = "a ={value_a} ,b ={value_b} c ={value_c:.2f} ".format(**d)


if __name__=='__main__':
    main()
