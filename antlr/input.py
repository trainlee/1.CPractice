{
    def a = 2, b = 3, c, d;
    c = a * b;
    {
        def a = 6;
        print a * b;
        d = a * b;
        print d;
    }
    print d;
    print a * b;
    print c;
}
