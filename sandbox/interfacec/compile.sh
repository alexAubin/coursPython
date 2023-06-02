g++ -c -fPIC libalex.cpp -o libalex.o
g++ -shared -Wl,-soname,libalex.so -o libalex.so libalex.o
