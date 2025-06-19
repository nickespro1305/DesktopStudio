ARCHISO_DIR=archiso
WORK_DIR=work
OUTPUT_DIR=output

.PHONY: all clean build

all: build

build:
	python builder.py

clean:
	rm -rf $(WORK_DIR) $(OUTPUT_DIR) $(ARCHISO_DIR)