SRC_DIR=src
BIN_DIR=bin
DIST_DIR=dist
MAIN_CLASS=com.andre.Main
JAR_NAME=miapp.jar

SOURCES=$(shell find $(SRC_DIR) -name "*.java")

all: build

build:
	mkdir -p $(BIN_DIR)
	javac -d $(BIN_DIR) $(SOURCES)

run: build
	java -cp $(BIN_DIR) $(MAIN_CLASS)

jar: build
	mkdir -p $(DIST_DIR)
	jar cfe $(DIST_DIR)/$(JAR_NAME) $(MAIN_CLASS) -C $(BIN_DIR) .

clean:
	rm -rf $(BIN_DIR) $(DIST_DIR)

.PHONY: all build run jar clean
