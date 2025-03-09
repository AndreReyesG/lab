# gcc -I ../unity/ -I ./src ./src/car.c ./test/car_test.c ../unity/unity.c -o car_test

# Making paths
PATHU = ../unity/
PATHS = src/
PATHT = test/

CC = gcc
CFLAGS = -I $(PATHU) -I $(PATHS)
SRCS = $(PATHS)car.c $(PATHT)car_test.c $(PATHU)unity.c

TARGET = car_test

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) $(SRCS) -o $(TARGET)

clean:
	rm -f $(TARGET)
